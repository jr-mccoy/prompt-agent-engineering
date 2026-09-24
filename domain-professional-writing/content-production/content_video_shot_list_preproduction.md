---
title: "Video Shot List and Pre-Production Plan — From Approved Script to a Shootable Day"
category: professional-writing/content-production
description: "Convert an approved script or outline for a live-action video into a numbered shot list (scene, shot size, angle, movement, subject, audio, lens or coverage notes, script line covered), a shooting order grouped by location and setup rather than story order, and a pre-production checklist (locations, releases, props, crew, gear, schedule) — distinct from the storyboard workflow (AI-generated storyboard images) and the video skill (AI or programmatic video generation)."
techniques:
  - DT-01
  - ST-03
  - OC-03
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - video-production
  - shot-list
  - pre-production
  - filmmaking
  - scheduling
  - content-production
  - plan-a-shoot
  - brand-video
  - one-day-shoot
updated: "2026-09-24"
related_prompts:
  - domain-image-generation/STORYBOARD_WORKFLOW.md
  - domain-agentic-resources/skills/marketing/video/SKILL.md
  - domain-professional-writing/content-production/content_long_form_script.md
---

# Video Shot List and Pre-Production Plan

**Objective:** Make sure every line of the approved script is covered by a
planned shot, that the day is scheduled by setup rather than story order, and
that nothing needed on set (a release, a prop, a battery) is discovered missing
on the day.

**When to Use:**
- A camera crew (even a crew of one) will shoot live action: explainer, brand
  film, interview-plus-B-roll, short narrative, event recap.
- The script is approved and the shoot date is set.
- A previous shoot ran over because shots were planned in story order.

**Not this prompt if:**
- You are generating storyboard frames with image models →
  `domain-image-generation/STORYBOARD_WORKFLOW.md`. A storyboard can feed this
  shot list; this prompt does not make images.
- The video will be generated with AI or code (avatars, Remotion, text-to-video) →
  `domain-agentic-resources/skills/marketing/video/`.
- The script is not written yet → `domain-professional-writing/content-production/content_long_form_script.md`.
- You need a documentary treatment for unscripted work →
  `domain-creative-writing/script-stage/writing_documentary_treatment.md`.

## Inputs

1. **Approved script or outline**, with scene or section numbers.
2. **Deliverables**: aspect ratios (16:9, 9:16), lengths, cut-downs.
3. **Locations** and their constraints (access hours, light, noise).
4. **Talent and crew** available, with call times.
5. **Gear list** available (camera bodies, lenses, audio, lighting, gimbal).
6. **Budget constraints** and the number of shoot days.

## Method

1. **Break the script down (DT-01).** Script → scenes → beats → required
   shots. For every script line, name the shot(s) that cover it, including
   B-roll for voiceover passages.
2. **Specify each shot (ST-03).** Number (scene.shot, e.g. 3.2), shot size
   (WS, MS, MCU, CU, ECU, insert), angle, movement (static, pan, tilt, push,
   handheld, gimbal), subject/action, audio (sync, wild, none), and notes
   (lens, frame rate, 9:16 safe area).
3. **Plan coverage, not just the "hero" shot.** For dialogue or interview:
   wide, two mid-shots or singles, cutaways. For every scene, at least one
   cutaway to fix edits.
4. **Tabulate (OC-03)** and mark priority: A (must have — the edit fails
   without it), B (should have), C (nice to have — shoot if ahead).
5. **Sequence by setup, not by story.** Group shots by location, then by
   camera direction and lighting setup; schedule exteriors against the light;
   put A-priority shots early in each setup.
6. **Apply constraints (CM-02).** Every identifiable person on camera needs a
   release; every location needs permission; music on set is avoided (it
   blocks editing and raises licensing issues); 9:16 deliverables need
   centre-safe framing noted per shot.
7. **Build the pre-production checklist** and the day schedule with call
   times, setups, meal break, and wrap.
8. **Self-check (QA-01):** every script line covered; setup count realistic
   for the hours.

## Output Format

```
# Shot list — [project], shoot [date(s)]
Deliverables: [...]   Locations: [...]   Crew: [...]

## Coverage map
| Script line / section | Shot numbers |

## Shot list
| # | Scene | Size | Angle | Movement | Subject / action | Audio | Notes | Priority |

## Shooting order (by setup)
| Setup | Location | Shots | Est. time | Light / notes |

## Day schedule
## Pre-production checklist
Releases · location permits · props · wardrobe · gear & batteries · data/cards · backup plan
## Risks and fallbacks
```

## Verification

- [ ] Every script line maps to at least one shot.
- [ ] Every scene has at least one cutaway or insert.
- [ ] Shooting order is grouped by location and setup, not script order.
- [ ] A-priority shots fit in the scheduled time with ≥15% slack.
- [ ] Every person on camera and every location has a release/permission line.
- [ ] 9:16 framing notes exist where vertical deliverables are required.

## False-Positive Prevention

1. **Story order is not shooting order.** Planning in script sequence
   multiplies setups and company moves.
2. **A shot list is not a storyboard.** Words are enough; do not delay the
   shoot for images unless the client requires them.
3. **Over-specifying lenses for a one-person crew wastes the plan.** Match
   detail to crew size.
4. **"Get B-roll" is not a shot.** Name the subject and action.
5. **Do not assume permissions.** Public space, private premises, and people
   in frame each have their own rules; mark `[CONFIRM PERMISSION]`.
6. **More shots is not more coverage.** Coverage means the editor has options
   at every cut point; forty inserts of the same object do not help.

## Example Output

```
# Shot list — "How We Roast" brand film (90 s + 30 s 9:16 cut-down), shoot 2026-10-12
Locations: roastery floor (07:00–13:00 access), front café. Crew: director/DP,
sound, producer. Talent: head roaster (Maya), café barista.

## Coverage map
| Script | Shots |
|---|---|
| VO "It starts before sunrise" | 1.1, 1.2 |
| Maya on camera: "We roast in small batches…" | 2.1–2.4 |
| VO "Every batch gets tasted" | 3.1–3.3 |
| End card in café | 4.1, 4.2 |

## Shot list
| # | Scene | Size | Angle | Move | Subject / action | Audio | Notes | Pri |
|---|---|---|---|---|---|---|---|---|
| 1.1 | Arrival | WS | Eye | Static | Maya unlocks roastery door, dark street | Wild | Pre-dawn exterior, 9:16 centre-safe | A |
| 1.2 | Arrival | CU | Low | Push | Hand flips main switch, lights stutter on | Wild | Insert | B |
| 2.1 | Interview | MS | Eye, 30° off lens | Static | Maya at roaster, speaking | Sync lav + boom | Roaster off during takes | A |
| 2.2 | Interview | MCU | Same | Static | Same, tighter | Sync | Second camera or repeat take | A |
| 2.3 | Interview | ECU | — | Handheld | Beans tumbling in drum | Wild | Cutaway | A |
| 2.4 | Interview | CU | High | Static | Maya checks temperature dial | Wild | Cutaway | B |
| 3.1 | Cupping | MS | Eye | Gimbal | Maya slurps from spoon | Wild | Humour beat | A |
| 3.2 | Cupping | CU | Top-down | Static | Row of cups, steam | None | 9:16 friendly | B |
| 3.3 | Cupping | CU | Eye | Rack focus | Notes card → Maya | Wild | — | C |
| 4.1 | Café | MS | Eye | Static | Barista hands cup across counter | Wild | No music playing in café | A |
| 4.2 | Café | Insert | Top | Static | Latte art, logo cup | None | End card background | A |

## Shooting order
| Setup | Location | Shots | Time | Notes |
|---|---|---|---|---|
| S1 | Street exterior | 1.1 | 06:45–07:15 | Pre-dawn light window |
| S2 | Roastery, door side | 1.2 | 07:15–07:35 | |
| S3 | Roastery, roaster (interview lighting) | 2.1, 2.2, 2.4 | 07:45–09:15 | Roaster off for sync |
| S4 | Roastery, roaster running | 2.3 | 09:15–09:45 | Wild sound only |
| S5 | Cupping table | 3.1–3.3 | 10:00–11:00 | |
| S6 | Café | 4.1, 4.2 | 11:30–12:30 | Before lunch rush |

## Day schedule
06:15 call · 06:45 S1 · 11:00 break · 11:30 S6 · 12:30 wrap-out · 13:00 off premises.

## Pre-production checklist
Releases: Maya ✔, barista [CONFIRM], café customers in frame [CONFIRM
PERMISSION or keep out of frame] · Location: roastery access letter ✔ ·
Props: logo cups ×6 · Gear: 2 lavs, boom, 4 batteries per body, 2× cards ·
Backup: if pre-dawn is missed, 1.1 becomes interior of door opening.

## Risks and fallbacks
Roaster noise ruins sync → interview only with roaster off (built into S3/S4).
```

## Techniques Used

- **DT-01 Hierarchical Task Breakdown** — script → scenes → beats → shots.
- **ST-03 Output Format Specification** — the standard shot-list fields.
- **OC-03 Markdown Table Specification** — shot list, shooting order, coverage map.
- **CM-02 Constraint Specification** — releases, permissions, no music on set, 9:16 safety.
- **QA-01 Self-Verification** — coverage and schedule checks.

## Related Prompts

- `domain-image-generation/STORYBOARD_WORKFLOW.md` — AI storyboard frames.
- `domain-agentic-resources/skills/marketing/video/SKILL.md` — AI and programmatic video.
- `content_long_form_script.md` — writing the script this list covers.
