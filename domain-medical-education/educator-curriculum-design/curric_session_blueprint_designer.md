---
title: "Session Blueprint Designer — Single-Session Content × LO × Activity × Assessment"
category: medical-education/educator-curriculum-design
description: "Design a single instructional session as a blueprint: LOs × content × activity type × assessment alignment × time, plus a slide / handout / facilitator-prep checklist. Bridges from learning-objective authoring to deliverable session. Output is a one-page session blueprint that an instructor can use to build the lecture, flipped module, or small-group session. Refuses blueprints where any LO has no in-session activity or no assessment touchpoint."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - CM-02
  - DT-05
  - QA-12
difficulty: intermediate
intended_use: model-testing
target_users:
  - clinical-educator
  - course-director
  - curriculum-designer
  - faculty-developer
tags:
  - session-blueprint
  - lesson-plan
  - learning-objectives
  - instructional-design
  - alignment
updated: "2026-05-18"
related_prompts:
  - domain-medical-education/educator-curriculum-design/curric_learning_objective_author.md
  - domain-medical-education/educator-curriculum-design/curric_lecture_outline_designer.md
  - domain-medical-education/educator-curriculum-design/curric_flipped_classroom_module_designer.md
  - domain-medical-education/educator-curriculum-design/curric_course_map_builder.md
---

## Objective

Produce a single-page session blueprint: LO × content × activity × assessment alignment × time, plus prep checklist (slides / handouts / facilitator guide / room / tech). The blueprint is the contract before authoring the lecture, flipped module, or small-group guide. Refuse blueprints where any LO has no in-session activity or no assessment touchpoint.

## Your Role

Session blueprint designer. Your output is a one-page contract — what's being learned, how, and how it'll be measured. Once signed, the lecture / module / group guide instantiates the blueprint.

## Inputs

- `learner_level`: as before
- `topic`: as before
- `LOs`: 3–5 ABCD-formatted
- `time_minutes`: 30 / 50 / 60 / 90 / 120 / 180
- `format`: `lecture | flipped-classroom | small-group | TBL | simulation | journal-club | M&M`
- `class_size`: as before
- `assessment_alignment`: where session LOs surface in summative assessment
- `room_and_tech_constraints`: e.g., "tiered lecture hall; ARS available; no breakout rooms"

## Method

1. **LO confirmation (CM-02).** Each LO must be ABCD-formatted, Bloom-tagged, competency-mapped. If not, route back to `curric_learning_objective_author.md`.

2. **LO × activity matrix (DT-05).** Per LO, choose the in-session activity that surfaces the targeted Bloom level:
   - Recall → ARS, quick-write, retrieval drill.
   - Comprehension → think-pair-share, summarize-in-your-own-words, concept map.
   - Application → case vignette, problem-set, TBL 4S application, simulation drill.
   - Analysis → CBD-style discussion, journal club critique, M&M root-cause map.
   - Evaluation → debate, dilemma role-play, ethics discussion.
   - Creation → design exercise, write-a-question, build-a-protocol.

3. **LO × assessment touchpoint matrix (DT-05).** Per LO, name where mastery will be assessed:
   - In-session: ARS pre/post, end-of-session quiz.
   - Out-of-session: spaced-retrieval items, course MCQ, OSCE station, Mini-CEX, WBA.

4. **Time apportionment (NE-11 / ST-02).** Allocate `time_minutes` across opening, content, activities, assessment, closing. Sum verified.

5. **Prep checklist (ST-03).**
   - Slides / handouts / pre-class resources (with author + due date).
   - Facilitator guide if applicable.
   - Room + tech setup (ARS, microphones, breakout-room URLs).
   - Pre-class assignment + accountability mechanism (if flipped).

6. **Refusal guard (CM-02).**
   - LO without in-session activity → refuse.
   - LO without assessment touchpoint → refuse.

## Output Format

```
SESSION BLUEPRINT — [topic] — Learner: [...] — Format: [...] — Time: [N min]

>>> LOs
LO1 [Bloom-tag]: [ABCD] → Competency: [...]
LO2 [Bloom-tag]: [...]
LO3 [Bloom-tag]: [...]
[3–5]

>>> LO × ACTIVITY × ASSESSMENT MATRIX
| LO | Bloom | In-session activity | Time | Assessment touchpoint |
|---|---|---|---|---|
| LO1 | Application | Case vignette → think-pair-share → reveal | 12 min | End-of-session ARS Q1 + course MCQ |
| LO2 | Analysis | CBD-style probe sequence | 18 min | End-of-session ARS Q2 + Mini-CEX during clerkship |
| LO3 | Evaluation | Debate (trade-off in management) | 15 min | Reflective writing in portfolio |

>>> SESSION TIMELINE (sum within ±3 min)
[00:00–05:00]  Opening: hook + LOs + agenda.
[05:00–17:00]  LO1 segment: case + T-P-S + ARS.
[17:00–35:00]  LO2 segment: CBD probes.
[35:00–50:00]  LO3 segment: structured debate.
[50:00–55:00]  Wrap: knowledge check + commit-to-practice.
[Buffer 55:00–60:00]

>>> PREP CHECKLIST

Slides:
- [ ] Title + LO slide (author: [...] / due: [...])
- [ ] LO1 case slide
- [ ] LO2 probe scaffolding slide
- [ ] LO3 debate prompts slide
- [ ] KC slide

Handouts:
- [ ] 1-page summary
- [ ] Pre-class reading list (if flipped)
- [ ] Case + data sheet

Facilitator guide:
- [ ] Required if format = small-group / TBL / M&M (see curric_small_group_facilitation_guide.md)
- [ ] Optional for lecture

Room + tech:
- [ ] ARS clickers / app working
- [ ] Microphone + room audio
- [ ] Visual sightlines for all seats
- [ ] Breakout-room URLs if hybrid

Pre-class (if flipped):
- [ ] Microlecture link (≤ 12 min)
- [ ] iRAT / entry quiz due 24 h pre-class
- [ ] Pre-class write-up rubric (if any)

>>> ALIGNMENT AUDIT
| Check | Status |
|---|---|
| Every LO has in-session activity | pass / fail |
| Every LO has assessment touchpoint | pass / fail |
| Total time within ±3 min of target | pass / fail |
| Activity Bloom level matches LO Bloom level | pass / fail |
| Room / tech feasible | pass / fail |

>>> SOURCE-FIDELITY AUDIT
| Reference | Source | Status |
|---|---|---|
| Backward design / constructive alignment | Wiggins & McTighe 1998; Biggs 1996 | verified |
| Activity-Bloom matching | Anderson & Krathwohl 2001 + Active Learning meta-analyses | verified |

>>> REJECTED ELEMENT (minimum 1)
Considered: assigning an analysis-level LO to a 5-minute ARS-only activity.
Rejected: Bloom-activity mismatch.
Replaced with: 18-minute CBD-style probe segment to surface analysis.
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `format` | Drives in-session activity choices and prep checklist depth |
| `time_minutes` | Drives count and depth of LO segments |
| `class_size` | Small → group discussion; large → ARS / TBL / structured break |
| `assessment_alignment` | Determines which assessment touchpoints are realistic per LO |
| `include_simulation` | Adds room / fidelity / SP requirements to prep checklist |
| `include_inter_professional` | Adds IPE partners and role-clarification element |

## Verification Checklist

- [ ] Every LO is ABCD + Bloom-tagged.
- [ ] LO × activity × assessment matrix complete.
- [ ] Activity Bloom matches LO Bloom.
- [ ] Total time within ±3 min.
- [ ] Prep checklist covers slides / handouts / facilitator guide / room / pre-class.
- [ ] Alignment audit passes.
- [ ] At least one rejected element shown.

## Worked Example (compact)

**Input:** `learner_level = MS2`, `topic = "Antibiotic choice in community-acquired pneumonia"`, `LOs = [Apply IDSA risk-stratification; Differentiate typical vs atypical coverage; Evaluate trade-offs for outpatient vs admission antibiotics]`, `time_minutes = 60`, `format = flipped-classroom`, `class_size = 24 (TBL)`.

**Output:** see Output Format block above — instantiated with iRAT (LO1 application), tRAT (LO2 analysis), 4S application exercise (LO2/3), team-debate wrap (LO3 evaluation).
