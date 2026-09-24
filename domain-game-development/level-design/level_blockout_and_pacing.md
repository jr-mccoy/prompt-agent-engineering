---
title: "Handcrafted Level Blockout and Pacing Review"
category: game-development/level-design
description: "Plan or review a handcrafted level at blockout (greybox) stage: player metrics that fix dimensions, a beat chart with intensity and minutes, critical path and optional space, landmarks and sightlines, gating and teaching, and a pacing audit before art is committed — distinct from procedural generation systems and from prose pacing."
techniques:
  - DT-01
  - DS-02
  - OC-03
  - QA-01
difficulty: intermediate
tags:
  - level-design
  - blockout
  - greybox
  - pacing
  - beat-chart
  - player-metrics
updated: "2026-09-24"
related_prompts:
  - domain-game-development/level-design/level_procedural_generation.md
  - domain-game-development/design/design_core_loop_analysis.md
  - domain-creative-writing/fiction/writing_pacing_and_tension_management.md
---

# Handcrafted Level Blockout and Pacing Review

**Objective:** Produce (or audit) the greybox plan for a handcrafted level so its
dimensions follow from player metrics, its pacing is charted beat by beat, and
the obvious problems — flat intensity, no rest, lost players, untaught mechanics
— are caught while geometry is still cheap to move.

**When to Use:**
- A level is going from paper map to greybox, or a greybox is about to go to art.
- Playtests show players lost, bored in the middle, or exhausted before the end.
- A new mechanic must be taught in this level and nobody has written how.

**When NOT to use:**
- Rule-based or algorithmic level generation — `level_procedural_generation.md`.
  This prompt is distinct because every space here is placed by hand and paced
  deliberately.
- Pacing a manuscript — `domain-creative-writing/fiction/writing_pacing_and_tension_management.md`.
  The tension-curve idea transfers; player-controlled time does not.
- Engine streaming and load boundaries — `architecture/architecture_scene_management.md`.

## Inputs

1. **Player metrics**: run/walk speed, jump height and distance, crouch height,
   character width, camera type and default distance.
2. **Level brief**: purpose in the campaign, target play time, mechanics
   introduced or tested, narrative beat.
3. **Map**: sketch, greybox screenshots, or a list of spaces with rough sizes.
4. **Prior-level state**: what the player can already do.
5. **Playtest data**, if any: times per section, deaths, where players got lost.

## Method

1. **Fix the metrics first (DS-02).** Derive standard dimensions: door width,
   corridor width, jump gaps that must succeed (≤ 80% of max jump) and must fail
   (≥ 120%), cover height, ceiling height. Anything built off-metric is a finding.
2. **Break the level into beats (DT-01).** Each beat: purpose (teach, test, rest,
   reward, spectacle), intensity 1–5, target minutes, the mechanic in play, and
   entry/exit points.
3. **Chart the beats (OC-03).** Table plus a text intensity curve. Totals must
   match the target play time.
4. **Check pacing rules.**
   - Rest after every peak (intensity ≥ 4) before the next peak.
   - No more than ~25% of play time at intensity ≥ 4 unless the brief asks for it.
   - Teach → test → twist for any new mechanic, in that order, in safe space first.
   - Opening and closing beats orient and reward.
5. **Map navigation.** Critical path length and traversal time at run speed;
   landmarks visible from each decision point; sightlines that preview the goal;
   one-way gates and how the player knows they are one-way.
6. **Audit (QA-01).** Re-check every finding against the metrics and brief; mark
   which need a playtest to confirm rather than a designer's judgement.

## Output Format

```
## Metrics        — table: element | value | derived from
## Beat chart     — table: beat | purpose | intensity | minutes | mechanic
## Intensity curve — one line per beat, bar of # per intensity point
## Navigation     — critical path length/time, landmarks, gates
## Findings       — severity | issue | evidence | fix | needs playtest?
## Confidence     — per section
```

## Verification

- [ ] Beat minutes sum to the target play time (±10%).
- [ ] Every dimension cited in a finding is checked against the metrics table.
- [ ] Every new mechanic has teach, test and twist beats in that order.
- [ ] Every peak is followed by a lower-intensity beat, or the exception is justified.
- [ ] Traversal time at run speed is less than total time, and the gap is accounted for.

## False-Positive Prevention

1. **Flat is not always wrong.** Exploration or cosy levels may hold intensity 1–2
   by design; judge against the brief, not an action-game curve.
2. **Back-to-back peaks can be the point.** A finale chase after a boss is a
   choice; flag it only if nothing in the brief asks for it.
3. **Do not critique art at greybox.** Lighting and texture are not in scope;
   readability of shape and landmark silhouette is.
4. **Minutes are estimates until played.** Mark them `[estimate]`; real times
   from a playtest override your chart.
5. **Off-metric is not a finding if it is intentional.** An impossible jump that
   teaches "you need the grapple" is correct; say so.
6. **"Players got lost" needs a location.** Name the decision point and what is
   visible from it, or do not report it.

## Example

**Input:** "Flooded Cannery", linear third-person action level, target 22 minutes.
Metrics: run 6 m/s, max jump 3.0 m horizontal, 1.2 m vertical. Introduces the
valve-draining mechanic.

```markdown
## Metrics
| Element | Value | Derived from |
|---|---|---|
| Safe jump gap | ≤ 2.4 m | 80% of 3.0 m max |
| Must-fail gap | ≥ 3.6 m | 120% of 3.0 m |
| Corridor width | 3 m | 2 × camera collision radius + character |
| Low cover | 1.0 m | crouched eye line 1.1 m |

## Beat chart
| # | Beat | Purpose | Int. | Min | Mechanic |
|---|---|---|---|---|---|
| B1 | Dockside arrival, chimney landmark | orient | 1 | 2 | — |
| B2 | Conveyor traversal | teach jumps | 2 | 3 | jump |
| B3 | Loading bay skirmish | test combat | 3 | 3 | combat |
| B4 | Foreman's office, lore | rest | 1 | 2 | — |
| B5 | Valve room (drain one tank) | teach valve | 2 | 4 | valve |
| B6 | Canning floor arena, valve drains cover | test + twist | 4 | 4 | valve + combat |
| B7 | Collapse chase | spectacle | 5 | 2 | traversal |
| B8 | Roof exit, reward chest | reward | 1 | 2 | — |
| | **Total** | | | **22** | |

## Intensity curve
B1 #  B2 ##  B3 ###  B4 #  B5 ##  B6 ####  B7 #####  B8 #

## Navigation
Critical path 1,450 m → 242 s (≈4 min) at run speed. Remaining ≈18 min is combat,
puzzle and optional space — consistent with the chart. Chimney landmark visible
from B1, B3, B6 exits; not visible from B5 (interior).

## Findings
| Sev | Issue | Evidence | Fix | Playtest? |
|---|---|---|---|---|
| High | B6→B7 is 6 min at intensity ≥ 4 with no rest (27% of level) | beats B6+B7 = 6 of 22 min | 30 s breather: short safe catwalk between arena and chase | Yes |
| Med | Valve twist (B6) arrives before valve is tested alone | B5 teaches, B6 tests + twists at once | Add second, combat-free valve in B5 | Yes |
| Med | B2 gap at conveyor end is 2.8 m, over safe 2.4 m | metrics table | Shorten to 2.3 m | No |
| Low | No landmark cue at B5 exit door | chimney not visible | Light shaft or signage toward stairwell | Yes |

## Confidence
Metrics: High. Beat minutes: Medium [estimate]. Findings 1, 2, 4: Medium until
playtested; finding 3: High (metric violation).
```

## Techniques Used

- **DT-01 (Hierarchical Task Breakdown):** level → beats → spaces.
- **DS-02 (Metric Specification):** player metrics drive every dimension check.
- **OC-03 (Markdown Table Specification):** beat chart and findings tables.
- **QA-01 (Self-Verification):** findings re-checked against metrics and brief.

## Related Prompts

- `domain-game-development/level-design/level_procedural_generation.md` — algorithmic levels.
- `domain-game-development/design/design_core_loop_analysis.md` — the loop each beat exercises.
- `domain-creative-writing/fiction/writing_pacing_and_tension_management.md` — tension-curve craft.
