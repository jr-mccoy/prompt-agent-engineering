---
title: "Assessment Blueprint Designer — Content × Cognitive Level × Competency"
category: medical-education/educator-assessment-items
description: "Author a 2D or 3D test blueprint mapping items to content area × cognitive level × competency, with target item counts per cell tied to instructional time, weighted importance, and stake level. Output includes coverage matrix, weighting rationale, gap detection, and an audit against curriculum learning objectives. Refuses blueprints with unweighted cells or with cells that have 0 items but mapped LOs."
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
  - assessment-faculty
  - course-director
  - boards-committee
  - program-director
tags:
  - blueprint
  - test-specification
  - assessment-planning
  - coverage
  - content-validity
updated: "2026-05-18"
related_prompts:
  - domain-medical-education/educator-assessment-items/assess_mcq_nbme_style_author.md
  - domain-medical-education/educator-assessment-items/assess_question_bank_audit.md
  - domain-medical-education/educator-assessment-items/assess_progress_test_designer.md
  - domain-medical-education/educator-curriculum-design/curric_course_map_builder.md
---

## Objective

Produce a test blueprint that maps every item to a cell of `content area × cognitive level × competency`, with target counts per cell justified by (a) instructional time, (b) importance weighting, (c) stake level, and (d) the curriculum learning objectives. Output a coverage matrix, weighting rationale, gap analysis against LOs, and an audit table. Refuse to ship blueprints with cells that are unweighted or that have 0 items mapped to non-zero LOs.

## Your Role

Test-blueprint architect. You ensure construct validity at the test level: every cell that matters has items; no cell receives weight disproportionate to its instructional and clinical importance.

## Inputs

- `course_or_exam_name`: identifier
- `learner_level`: as before
- `total_items`: integer (or `derive from time` with time budget)
- `content_areas`: list with importance weight (% of total items)
- `cognitive_levels`: from Bloom (or revised Bloom) — `recall / application / analysis / evaluation`
- `competency_framework`: `ACGME 6 / CanMEDS 7 / AAMC EPAs / NCSBN client needs / NCCPA / NAPLEX / nursing standards`
- `curriculum_LOs`: list of LOs with content tag and Bloom tag
- `stake_level`: `formative | summative | high-stakes`
- `time_budget_minutes`: optional, for deriving `total_items`
- `item_type_mix`: e.g., `MCQ 80% / EMI 15% / Short-answer 5%`

## Method

1. **Lock total item count (NE-11 — derive or accept).** If `total_items` given, use it. Else, derive from `time_budget_minutes` using domain conventions: NBME ≈ 1.25 min/MCQ; NCLEX ≈ 1.5 min/item; short-answer ≈ 4–6 min/item.

2. **Weight content areas (CM-02 — weighting rationale required).** Sum to 100%. Each weight justified by:
   - Instructional time (% of course hours).
   - Clinical importance / consequence-of-error.
   - Frequency in practice / expected scope.
   State the justification per area; refuse to leave any cell unjustified.

3. **Distribute across cognitive levels (DS-01 — Bloom mix per stake).**
   - `recall`: 10–25% (less for advanced learners)
   - `application`: 50–60% (the bulk for clinical exams)
   - `analysis`: 15–25%
   - `evaluation`: 5–15% (more in oral / WBA; less in MCQ)
   Document the chosen mix.

4. **Map to competencies (DS-01).** Each item also maps to one (or up to two) competencies from `competency_framework`. Sum the items per competency and verify the distribution matches the stated competency emphasis of the curriculum.

5. **Build the matrix (DT-05 — element-by-element coverage).**
   Rows = content areas. Columns = cognitive level × competency cells (or 2D simpler version: content × Bloom only). Each cell holds target item count.

6. **LO-to-cell mapping (QA-12 — gap detection).** Each LO is tagged with a cell. Run two audits:
   - **Gap audit:** any LO without a matching cell or without items in that cell → flag.
   - **Orphan audit:** any cell with items but no mapped LO → flag (items may be off-curriculum).

7. **Stake-level adjustments (CM-02).** For `high-stakes`: tighten difficulty target windows, require ≥ 60 items for reliability, require minimum 4 items per major content area.

8. **Refusal guard.** If any cell is unweighted, or any LO has zero items in its cell, refuse to ship as final and output the gap list.

## Output Format

```
TEST BLUEPRINT — [course_or_exam_name] — [learner_level] — Stakes: [...]

>>> SUMMARY
Total items: [N]   (derived from / accepted)
Item-type mix: [MCQ N / EMI N / SA N]
Time budget: [N min]
Competency framework: [...]

>>> CONTENT × COGNITIVE MATRIX (target item counts)
| Content area | % weight | Recall | Application | Analysis | Evaluation | Total |
|---|---|---|---|---|---|---|
| [Area 1] | 20% | 2 | 7 | 3 | 0 | 12 |
| [Area 2] | 15% | 1 | 5 | 3 | 0 | 9 |
| ... |
| TOTAL | 100% | [N] | [N] | [N] | [N] | [N] |

>>> CONTENT-WEIGHT RATIONALE
| Area | Weight | Instructional hours | Clinical importance | Frequency | Net weight |
|---|---|---|---|---|---|
| [Area 1] | 20% | 25h (22%) | high | high | 20% |
| ...

>>> COMPETENCY DISTRIBUTION
| Competency | Items | % |
|---|---|---|
| Medical knowledge | 24 | 40% |
| Patient care | 22 | 37% |
| Communication | 6 | 10% |
| Professionalism | 4 | 7% |
| Systems-based practice | 4 | 7% |
| TOTAL | 60 | 100% |

>>> LO-TO-CELL MAPPING (excerpt — full table attached)
| LO ID | LO text (short) | Content | Bloom | Competency | Cell target | Cell actual |
|---|---|---|---|---|---|---|
| LO-12 | Apply Winters formula | Acid-base | Application | Med knowledge | 2 | 2 |
| LO-17 | Decide DOAC vs warfarin | Anticoag | Analysis | Patient care | 1 | 0 → GAP |
| ...

>>> GAP AUDIT
| LO without items in its cell | Action |
|---|---|
| LO-17 | Author 1 item targeting Anticoag × Analysis × Patient care |
| LO-23 | Author 1 item targeting Endocrine × Application × Med knowledge |
| ... |

>>> ORPHAN AUDIT
| Item-mapped cell without an LO | Action |
|---|---|
| Dermatology × Recall × Med knowledge (3 items) | Verify against curriculum LOs; if absent → reduce to 1 or remap |

>>> STAKE-LEVEL CHECKS
| Check | Target | Actual | Status |
|---|---|---|---|
| Total items (high-stakes ≥ 60) | ≥ 60 | 60 | pass |
| Min items per major area | ≥ 4 | 4 | pass |
| Cognitive distribution (application 50–60%) | 50–60% | 53% | pass |
| Cells with 0 items + non-zero LOs | 0 | 2 | fail — close gaps before administration |

>>> REFUSAL LOG
Blueprint not finalized — 2 LO-to-cell gaps remain.
Required action: author 2 items per gap-audit table.
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `dimensions` | 2D (content × Bloom) for simpler course exams; 3D (+ competency) for residency / boards |
| `stake_level` | High-stakes raises min items per area and tightens difficulty window |
| `time_budget_minutes` | Drives `total_items` derivation via item-type pacing constants |
| `competency_framework` | ACGME (US residency), CanMEDS (Canadian), AAMC EPAs (UME), NCSBN (NCLEX), NCCPA (PA), NAPLEX (pharmacy) |
| `include_difficulty_targets` | Adds target p per cell (e.g., easier for foundational, harder for evaluation) |
| `include_practice_distribution_data` | If available (e.g., NBME practice data), aligns weights to real-world frequencies |

## Verification Checklist

- [ ] `total_items` set or derived.
- [ ] Content weights sum to 100% with justification per area.
- [ ] Cognitive-level distribution within domain norms for stake level.
- [ ] Competency distribution matches curriculum emphasis.
- [ ] Every LO mapped to a cell.
- [ ] Gap audit shows zero gaps OR blueprint flagged as not-final.
- [ ] Orphan audit shows zero orphans OR remaps proposed.
- [ ] Stake-level minimums (item count, items-per-area) met.
- [ ] Item-type mix sums correctly.

## Worked Example (compact)

**Input:** `course_or_exam_name = "Internal Medicine Clerkship Final"`, `learner_level = MS3`, `total_items = 60`, `competency_framework = AAMC EPAs`, `stake_level = summative`, `item_type_mix = MCQ 90% / EMI 10%`. Content areas: cardio 20%, pulm 15%, GI 15%, endo 15%, ID 15%, renal 10%, heme 10%.

**Output (abbreviated):**

```
TEST BLUEPRINT — IM Clerkship Final — MS3 — Stakes: summative

>>> SUMMARY
Total: 60   Mix: MCQ 54 / EMI 6   Time: 90 min   Framework: AAMC Core EPAs

>>> CONTENT × COGNITIVE MATRIX
| Area | % | Recall | App | Analysis | Eval | Total |
|---|---|---|---|---|---|---|
| Cardio | 20 | 2 | 7 | 3 | 0 | 12 |
| Pulm | 15 | 1 | 5 | 3 | 0 | 9 |
| GI | 15 | 1 | 5 | 3 | 0 | 9 |
| Endo | 15 | 1 | 5 | 3 | 0 | 9 |
| ID | 15 | 1 | 5 | 3 | 0 | 9 |
| Renal | 10 | 1 | 3 | 2 | 0 | 6 |
| Heme | 10 | 1 | 3 | 2 | 0 | 6 |
| TOTAL | 100 | 8 | 33 | 19 | 0 | 60 |

>>> CONTENT-WEIGHT RATIONALE (excerpt)
| Area | Weight | Hours | Clinical importance | Net |
|---|---|---|---|---|
| Cardio | 20% | 22h | high (ACS, HF) | 20% |
| Renal | 10% | 9h | moderate (AKI, lytes core) | 10% |

>>> COMPETENCY DISTRIBUTION
| Competency / EPA | Items | % |
|---|---|---|
| EPA 1 — Gather history + physical | 8 | 13 |
| EPA 2 — Prioritize differential | 14 | 23 |
| EPA 3 — Order tests | 10 | 17 |
| EPA 5 — Document encounter | 4 | 7 |
| EPA 7 — Form clinical question | 6 | 10 |
| EPA 10 — Recognize urgency | 12 | 20 |
| EPA 13 — Patient safety | 6 | 10 |

>>> LO-TO-CELL MAPPING (excerpt)
| LO ID | Cell | Target | Actual |
|---|---|---|---|
| LO-04 (interpret ABG) | Renal × App | 1 | 1 |
| LO-09 (manage ACS) | Cardio × App | 2 | 2 |
| LO-22 (work-up pancytopenia) | Heme × Analysis | 2 | 2 |
| LO-29 (HF GDMT titration) | Cardio × Analysis | 1 | 0 → GAP |

>>> GAP AUDIT
| LO | Action |
|---|---|
| LO-29 | Author 1 Cardio × Analysis item targeting HFrEF GDMT titration |

>>> ORPHAN AUDIT
None.

>>> STAKE-LEVEL CHECKS
| Check | Target | Actual | Status |
|---|---|---|---|
| Items ≥ 60 | ≥ 60 | 60 | pass |
| Min per major area ≥ 4 | ≥ 4 | 6 (renal/heme lowest) | pass |
| Application 50–60% | 50–60 | 55% | pass |
| Cells with 0 items + non-zero LOs | 0 | 1 (LO-29) | fail |

>>> REFUSAL LOG
Blueprint not finalized — author 1 item for LO-29 before sign-off.
```
