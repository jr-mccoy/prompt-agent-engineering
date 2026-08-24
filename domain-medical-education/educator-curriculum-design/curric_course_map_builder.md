---
title: "Course Map Builder — Course-Long LO × Session × Assessment × Resource Map"
category: medical-education/educator-curriculum-design
description: "Build a complete course map: course-level LOs → session-level LOs → sessions (date / format / time) → resources → assessments → competency / EPA mapping → progression check. Audits for coverage gaps, redundancy, Bloom skew, and assessment-alignment failures. Refuses to ship maps where a course LO has no covering session, or where any assessment is not tied to a course LO."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - CM-02
  - DT-05
  - QA-12
difficulty: advanced
intended_use: model-testing
target_users:
  - course-director
  - curriculum-designer
  - faculty-developer
  - associate-dean
tags:
  - course-map
  - curriculum-map
  - blueprint
  - alignment
  - constructive-alignment
updated: "2026-05-18"
related_prompts:
  - domain-medical-education/educator-curriculum-design/curric_learning_objective_author.md
  - domain-medical-education/educator-curriculum-design/curric_session_blueprint_designer.md
  - domain-medical-education/educator-curriculum-design/curric_vertical_horizontal_integration_audit.md
  - domain-medical-education/educator-assessment-items/assess_blueprint_designer.md
---

## Objective

Produce a course-long map linking: course-level LOs → session-level LOs → sessions (date / format / time) → resources → assessments → competency / EPA mapping. Run audits for coverage gaps, redundancy, Bloom-level skew, and assessment alignment. Refuse to ship maps where any course LO has no covering session or any assessment is not tied to a course LO.

## Your Role

Course map architect. You enforce constructive alignment: what's taught is what's practiced is what's assessed.

## Inputs

- `course_name`: identifier
- `learner_level`: as before
- `total_weeks`: course duration
- `total_hours`: total contact hours
- `course_LOs`: 4–10 course-level LOs (ABCD)
- `competency_framework`: as before
- `assessment_plan`: list of formative + summative assessments
- `session_inventory`: list of sessions with date / time / format
- `pre_existing_resources`: microlectures / cases / readings already in inventory

## Method

1. **Lock course LOs (CM-02 — coverage requirement).** 4–10 ABCD LOs at the course level. Each must trace to ≥ 1 session AND ≥ 1 assessment.

2. **Build session-LO mapping (DS-01).** For each session, identify session-level LOs (3–5) that decompose toward course LOs. Tag each session-LO to ≥ 1 course-LO.

3. **Build session × resource × assessment matrix (DT-05).** Per session: format, time, resources, in-session activities, formative + summative assessment touchpoints. Tag everything to LOs.

4. **Coverage audit (QA-12).** Run:
   - **Coverage gap:** any course LO without ≥ 1 session AND ≥ 1 assessment touchpoint → flag.
   - **Orphan session:** session whose LOs don't trace to any course LO → flag.
   - **Bloom skew:** if course LOs require analysis/evaluation but sessions are 90% application, flag.
   - **Assessment-alignment failure:** any assessment item not tied to a course LO → flag.
   - **Redundancy:** ≥ 2 sessions covering the same LO at the same Bloom level → flag.

5. **Progression check (DS-01 — Bloom progression across course).** Across the course timeline, ensure LOs at higher Bloom levels appear later (when foundation is built). Flag if evaluation-level LOs assessed before scaffold-building sessions.

6. **Refusal guard.** Any course LO without coverage in session AND assessment → refuse to ship.

7. **Source-fidelity audit (QA-12).** Constructive-alignment reference (Biggs); curriculum-mapping references (Harden 2001).

## Output Format

```
COURSE MAP — [course_name] — Learner: [...] — Weeks: [N] — Hours: [N]

>>> COURSE-LEVEL LOs
CLO1 [Bloom]: [ABCD] → Competency: [...]
CLO2 [...]
[...]
CLO N [...]

>>> SESSION INVENTORY × LO MAPPING
| Session # | Date / Wk | Format | Hours | Session LOs | Covers CLO(s) |
|---|---|---|---|---|---|
| S1 | Wk 1 | Lecture | 1.0 | SLO1.1–1.3 | CLO1, CLO2 |
| S2 | Wk 1 | Small group | 1.5 | SLO2.1–2.3 | CLO1, CLO3 |
| S3 | Wk 2 | Flipped TBL | 2.5 | SLO3.1–3.4 | CLO2, CLO3 |
| ... |

>>> COURSE LO × SESSION COVERAGE MATRIX
| CLO | Sessions covering | # sessions | Bloom levels covered |
|---|---|---|---|
| CLO1 | S1, S2, S4, S9 | 4 | App, App, Analysis, Analysis |
| CLO2 | S1, S3, S7 | 3 | App, App, Eval |
| CLO3 | S2, S3, S6, S10 | 4 | App, Analysis, Analysis, Eval |
| CLO4 | (none) | 0 | GAP — needs ≥ 1 session |

>>> ASSESSMENT PLAN × LO ALIGNMENT
| Assessment | Type | Items | LO coverage |
|---|---|---|---|
| Midterm MCQ | Summative | 50 | CLO1 ×15, CLO2 ×12, CLO3 ×15, CLO4 ×0 — GAP |
| Final MCQ | Summative | 80 | CLO1 ×20, CLO2 ×20, CLO3 ×20, CLO4 ×0 — GAP |
| OSCE station 3 | Summative | 1 station | CLO3 |
| Reflective essay | Formative | 1 essay | CLO5 (evaluation) |
| Progress test | Formative | 60 | longitudinal |
| Mini-CEX (clerkship-integrated) | Formative | 4 forms | CLO1, CLO3 |

>>> COVERAGE AUDIT
| Audit | Status | Action |
|---|---|---|
| Every CLO has ≥ 1 session | fail | Add ≥ 1 session for CLO4 |
| Every CLO has ≥ 1 assessment touchpoint | fail | Add 5 items to final MCQ targeting CLO4 |
| No orphan sessions | pass | — |
| Bloom progression appropriate | pass | — |
| No redundant Bloom × LO combos | pass | (mild redundancy CLO2 × Application acceptable as deliberate practice) |
| Assessment items all tied to CLOs | fail | "case-presentation rating" not tied to any CLO — drop or remap |

>>> COVERAGE GAP RESOLUTION
| Gap | Resolution |
|---|---|
| CLO4 has 0 sessions | Author 1 session in Wk 5 (format: flipped TBL, 2 h) targeting CLO4 — see curric_session_blueprint_designer.md |
| CLO4 has 0 assessment items | Author 5 MCQs at analysis level for final exam |
| Orphan rating "case presentation rating" | Either remap to CLO1 (communication subdomain) or remove from grade |

>>> PROGRESSION CHECK
| CLO | Bloom | First appearance (week) | Final appearance | OK? |
|---|---|---|---|---|
| CLO1 | Application | Wk 1 | Wk 9 | yes |
| CLO2 | Application + Eval | Wk 1 (App), Wk 7 (Eval) | Wk 10 | yes (scaffold) |
| CLO3 | Analysis + Eval | Wk 2 (Analysis), Wk 8 (Eval) | Wk 11 | yes |
| CLO4 | Analysis | (none yet) | — | gap |

>>> ASSESSMENT-LO BLUEPRINT (see assess_blueprint_designer.md)
Total items per assessment × LO computed and exported to blueprint designer.

>>> SOURCE-FIDELITY AUDIT
| Reference | Source | Status |
|---|---|---|
| Constructive alignment | Biggs 1996 Higher Educ; Biggs & Tang 2011 | verified |
| Curriculum mapping | Harden 2001 Med Teach | verified |
| Outcome-based education | Spady 1994; Harden 1999 Med Teach | verified |

>>> REJECTED ELEMENT (minimum 1)
Considered: shipping the map with CLO4 uncovered "because we'll add it later."
Rejected: violates coverage requirement.
Replaced with: explicit Wk-5 session author task + final-exam item-author task before sign-off.
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `total_weeks` | Drives session inventory; longer courses tolerate Bloom progression across more time |
| `competency_framework` | Maps CLOs to ACGME / CanMEDS / EPAs / NCSBN |
| `assessment_plan` | Drives assessment-LO alignment matrix and blueprint hand-off |
| `pre_existing_resources` | Identifies which sessions inherit existing materials vs need new authoring |
| `include_integration_audit` | Adds vertical / horizontal integration check (see curric_vertical_horizontal_integration_audit.md) |
| `include_progression_pacing` | Adds week-by-week pacing report |

## Verification Checklist

- [ ] 4–10 course LOs in ABCD format.
- [ ] Session inventory complete (date / time / format / LOs).
- [ ] Every CLO covered by ≥ 1 session AND ≥ 1 assessment touchpoint.
- [ ] No orphan sessions or orphan assessment items.
- [ ] Bloom progression appropriate across the course timeline.
- [ ] Coverage-gap resolutions named with concrete actions.
- [ ] Source-fidelity audit populated.
- [ ] At least one rejected element shown.

## Worked Example (compact)

**Input:** `course_name = "MS2 Cardiology Block"`, `total_weeks = 4`, `total_hours = 40`, `course_LOs = 6 CLOs (CLO1 ABG/acid-base inappropriate for cardio; replaced with 6 cardio-specific)`, `competency_framework = AAMC Core EPAs`, sessions: 8 lectures + 4 flipped TBL + 2 small groups + 1 simulation + 1 SP encounter + assessments: midterm MCQ + final MCQ + OSCE.

**Output:** see Output Format block above — instantiated with the cardio-block map, coverage audit revealing CLO4 (arrhythmia interpretation) gap, and explicit fill-in action.
