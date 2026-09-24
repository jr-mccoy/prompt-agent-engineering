---
title: "Game HUD, UI and Game-Feel Review"
category: game-development/design
description: "Review a game's HUD and menus for information hierarchy, readability at play distance and accessibility, then review the feel of core actions frame by frame — input latency, anticipation, hitstop, shake, sound and particles — flagging both missing feedback and over-juiced noise; distinct from web/app heuristic evaluation and WCAG audits."
techniques:
  - RT-02
  - QA-18
  - DS-06
  - QA-04
difficulty: intermediate
tags:
  - game-ui
  - hud
  - game-feel
  - juice
  - accessibility
  - ux-review
updated: "2026-09-24"
related_prompts:
  - domain-frontend-development/ux-research/frontend_ux_heuristic_evaluation.md
  - domain-frontend-development/accessibility/frontend_accessibility_wcag_audit.md
  - domain-game-development/design/design_mechanics_design.md
---

# Game HUD, UI and Game-Feel Review

**Objective:** Tell the team which HUD elements the player cannot read or does
not need in the moment, and which core actions feel unresponsive, weightless or
noisy — each finding tied to evidence (a frame count, a size, a screenshot
location) and marked where only a playtest can confirm it.

**When to Use:**
- A vertical slice or milestone build needs a UI and feel pass before playtest.
- Players say combat "feels floaty" or "I didn't see that coming".
- The HUD has grown by accretion and nobody has asked what each element is for.

**When NOT to use:**
- Web or app interfaces — `domain-frontend-development/ux-research/frontend_ux_heuristic_evaluation.md`.
  This review is distinct because games put information under time pressure and
  treat feedback intensity as a design material.
- Formal WCAG conformance — `domain-frontend-development/accessibility/frontend_accessibility_wcag_audit.md`.
  Game accessibility here follows game-specific guidance.
- Rendering cost of UI and VFX — `performance/performance_rendering_optimization.md`.

## Inputs

1. **Captures**: screenshots at native resolution of HUD in normal, busy and
   low-health states; menus; video of core actions (60 fps or higher).
2. **Platform and viewing distance**: TV at couch distance, monitor, handheld, phone.
3. **Core actions** to review for feel: e.g. jump, attack, hit received, dodge.
4. **Frame data** if available: startup, active, recovery, hitstop per action.
5. **Measured input latency** if available (high-speed camera or tool).
6. **Accessibility options** already present.

## Method

1. **Inventory HUD elements (RT-02).** For each: what decision it supports, how
   often the player needs it, screen position, size at target resolution,
   contrast, and whether it could be diegetic or contextual (shown only when relevant).
2. **Rank information hierarchy.** What must be readable in peripheral vision in
   under a second (health, ammo, threat direction) vs on demand (map, quest log).
   Elements that compete with the centre of action are findings.
3. **Check readability and accessibility against game guidance (QA-18).** Text
   size at the viewing distance per the platform's current accessibility guidance
   (record the value and its source), colour not the only channel, subtitle size
   and background, remapping, HUD scale, motion-reduction for shake and flashes.
4. **Break down each core action's feel.** Frame timeline: input → anticipation
   → active → hitstop → recovery; input latency end to end; and the feedback
   layers at impact — animation, sound, particles, screen shake, controller
   rumble, camera. Name the missing layer or the one that drowns the others.
5. **Run the game-feel smell tests (QA-18).**
   - Input to first visible response over ~100 ms reads as sluggish for action games.
   - Every hit identical in intensity → nothing reads as big.
   - Shake on every event → shake stops meaning anything and causes discomfort.
   - Feedback on the attacker but not the target → hits feel like they missed.
6. **Prioritise (DS-06).** Severity: blocks a decision / slows a decision /
   polish. Mark confidence and which findings need a playtest (QA-04).

## Output Format

```
## HUD inventory   — element | supports decision | frequency | size/contrast | verdict
## Hierarchy       — at-a-glance vs on-demand; conflicts with centre of action
## Accessibility   — option | present? | guidance value applied (source)
## Feel breakdown  — per action: frame timeline, latency, feedback layers, finding
## Findings        — severity | finding | evidence | fix | confidence | playtest?
```

## Verification

- [ ] Every HUD element names the decision it supports, or is flagged as decoration.
- [ ] Every size or contrast finding cites a measured value and the guidance used.
- [ ] Frame timelines sum to the stated total and use one stated frame rate.
- [ ] Feel findings name the specific missing or excessive feedback layer.
- [ ] Subjective findings are marked Medium/Low confidence with a playtest flag.

## False-Positive Prevention

1. **Minimal HUD is not missing HUD.** A deliberately sparse or diegetic design
   is a choice; flag it only where a needed decision has no information.
2. **More juice is not better feel.** Recommend removing feedback as often as
   adding it; noise hides the hits that matter.
3. **Do not quote accessibility numbers from memory.** Use the platform's current
   guidance and record which document you used, or mark `[verify]`.
4. **Heavy is not sluggish.** Long anticipation on a heavy attack can be correct
   if input is acknowledged immediately (a sound or flash on frame 1).
5. **Screenshots are not play distance.** Judge size at the stated viewing distance.
6. **Latency needs a measurement.** "Feels laggy" without a number is a playtest
   question, not a finding.

## Example

**Input:** Console action game, TV at couch distance, 1080p/60 fps capture.
Action reviewed: light attack hitting an enemy. Measured input latency 83 ms.

```markdown
## HUD inventory (excerpt)
| Element | Supports | Frequency | Size / contrast | Verdict |
|---|---|---|---|---|
| Health bar (top-left) | retreat / heal | constant | 18 px tall, good | OK |
| Combo counter (centre-right) | none mid-fight | constant | 64 px, pulsing | Move / contextual |
| Objective text (top-centre) | navigation | on demand | 20 px, no backing | Too small [verify guidance] |
| Off-screen threat arrows | dodge | in combat | red only | Colour-only channel |

## Hierarchy
At a glance: health, stamina, threat direction. The combo counter sits 120 px from
the crosshair and pulses every hit — it competes with the centre of action.

## Accessibility
| Option | Present? | Value applied |
|---|---|---|
| Subtitle size / background | size only | add background; size per platform guidance [verify] |
| HUD scale | No | add 80–150% slider |
| Screen-shake toggle | No | add; see feel finding 2 |
| Threat-arrow colour | red only | add shape (chevron) |

## Feel breakdown — light attack (60 fps, 1 frame = 16.7 ms)
| Phase | Frames | ms |
|---|---|---|
| Anticipation | 4 | 67 |
| Active | 3 | 50 |
| Hitstop | 5 | 83 |
| Recovery | 12 | 200 |
| **Total** | **24** | **400** |
Input latency 83 ms (5 frames) before anticipation begins → first visible response
at 83 ms, within the ~100 ms threshold.
Feedback at impact: attacker anim ✓, hit sound ✓, spark particle ✓, screen shake ✓
(same amplitude as heavy attack), target flinch ✗ (plays on 2nd hit only), rumble ✓.

## Findings
| Sev | Finding | Evidence | Fix | Conf. | Playtest? |
|---|---|---|---|---|---|
| High | Threat arrows colour-only | red on red-lit arena | add chevron shape | High | No |
| Med | First light hit feels like a miss | target flinch absent on hit 1 | flinch on every hit (3-frame) | Medium | Yes |
| Med | Light and heavy shake identical | same amplitude in capture | scale shake by damage; light = none | Medium | Yes |
| Med | Combo counter pulls eyes to centre | 120 px from crosshair, pulsing | fade out after 1 s idle; move to edge | Medium | Yes |
| Low | Objective text small at TV distance | 20 px | resize per guidance [verify] | Low | No |
```

## Techniques Used

- **RT-02 (Multi-Dimensional Analysis Framework):** each HUD element scored on decision, frequency, size and contrast.
- **QA-18 (Domain-Specific Smell Tests):** game-feel smell tests for latency, uniform juice and one-sided feedback.
- **DS-06 (Prioritization and Severity Guidance):** severity by effect on the player's decision.
- **QA-04 (Uncertainty Acknowledgment):** confidence and playtest flags on subjective findings.

## Related Prompts

- `domain-frontend-development/ux-research/frontend_ux_heuristic_evaluation.md` — heuristic review for app UIs.
- `domain-frontend-development/accessibility/frontend_accessibility_wcag_audit.md` — WCAG conformance.
- `domain-game-development/design/design_mechanics_design.md` — the actions whose feel is reviewed.
