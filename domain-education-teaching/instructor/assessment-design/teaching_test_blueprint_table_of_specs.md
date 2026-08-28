---
title: "Test Blueprint / Table of Specifications"
category: education-teaching/assessment
description: "Build a test blueprint mapping items to objectives, DOK levels, and weights — producing a defensible content-validity matrix and an item-write order with target counts per cell."
techniques:
  - CM-01
  - ST-02
  - DS-01
  - OC-01
  - QA-01
difficulty: advanced
tags:
  - assessment
  - test-blueprint
  - table-of-specifications
  - content-validity
  - dok
  - blueprint
  - psychometrics
updated: "2026-05-09"
related_prompts:
  - domain-education-teaching/assessment/assessment_mc_item_writer_with_distractors.md
  - domain-education-teaching/assessment/assessment_performance_task_designer.md
  - domain-education-teaching/teaching_standards_alignment_mapper.md
---

# Test Blueprint / Table of Specifications

## Objective

Produce a complete table of specifications (test blueprint) that a teacher or assessment writer can use to build a content-valid test. Output assigns target item counts and points to each (objective × DOK × item-type) cell, justifies weights from instructional emphasis, and yields an item-write order.

## When to Use

- Building unit tests, midterms, finals, common assessments
- Auditing an existing test for content validity
- PLCs designing common formative assessments
- Replacing tests that drift from what was actually taught

## When NOT to Use

- Single-objective quiz — go straight to `assessment_mc_item_writer_with_distractors.md`
- Performance task — use `assessment_performance_task_designer.md`
- Standards alignment for a whole curriculum — use `teaching_standards_alignment_mapper.md`

---

## Inputs Needed

- **Subject and grade:** [e.g., 8th grade life science]
- **Unit / scope:** [What the assessment covers]
- **Objectives or standards (with codes):** [Numbered list]
- **Total testing time:** [Minutes]
- **Total points:** [If known]
- **Item types allowed:** [MC / SR (short response) / ER (extended response) / performance]
- **Instructional time per objective:** [If you have it — drives weighting]
- **Use case:** [Formative / summative / high-stakes / district common]

---

## Instructions

### Step 1: Confirm and Number the Objectives

List the objectives. For each, capture:
- Objective ID and verb
- Bloom's / DOK ceiling (highest level taught and assessable in time)
- Estimated instructional time spent (% of unit)

If instructional time wasn't provided, mark as "needs input" and propose defaults.

### Step 2: Allocate Weight by Objective

Convert instructional emphasis to assessment weight. Default rule: weight ≈ instructional time, but constrained:

| Adjustment | Rule |
|-----------|------|
| Cap any single objective at 35% | Prevents overweighting one strand |
| Floor at 5% if assessed at all | Items below floor signal blueprint cleanup |
| Boost foundational prerequisites by ≤5% | If next unit depends on mastery |
| Reduce easily-tested vocabulary by ≤5% | Prevent recall-trivia bias |

Output a weights table:

| Objective | Instructional time % | Assessment weight % | Justification |
|-----------|---------------------|---------------------|---------------|

Weights must sum to 100%.

### Step 3: Build the Specifications Matrix

Build the (objective × DOK × item-type) matrix:

|              | DOK 1 (Recall) | DOK 2 (Skill/Concept) | DOK 3 (Strategic) | DOK 4 (Extended) | TOTAL items | TOTAL pts |
|--------------|----------------|------------------------|--------------------|--------------------|-------------|-----------|
| **Obj 1**    | __ MC (__pts)  | __ MC + __ SR          | __ ER              | —                  | __          | __        |
| **Obj 2**    |                |                        |                    |                    |             |           |
| ...          |                |                        |                    |                    |             |           |
| **TOTAL**    |                |                        |                    |                    |             |           |
| **% by DOK** |                |                        |                    |                    |             |           |

Apply these defaults if not specified:

| DOK distribution defaults by use case | DOK 1 | DOK 2 | DOK 3 | DOK 4 |
|--------------------------------------|-------|-------|-------|-------|
| Formative check | 30% | 50% | 20% | — |
| Unit summative | 20% | 50% | 25% | 5% |
| Final / high-stakes | 15% | 50% | 30% | 5% |
| Test prep (mirror exam) | (match the exam) | | | |

### Step 4: Time Budget

Apply per-item-type time estimates (default):

| Item type | Minutes per item |
|-----------|------------------|
| MC | 1.0–1.5 |
| Short response | 3–5 |
| Extended response | 10–20 |
| Performance | 15+ |

Total time = Σ(items × time). Compare to allotted testing time. If over budget, propose cuts (lowest-leverage cells). If under by >15%, flag opportunity to add depth.

### Step 5: Point Allocation

Distribute total points to match weights:

| Objective | Weight % | Items | Suggested point distribution |
|-----------|----------|-------|------------------------------|

Rule: points should track weight, not item count alone. A single ER item can equal 10 MC items.

### Step 6: Item-Write Order

Produce a worklist for the item writer in order of priority:

1. **Anchor items first:** highest-weight × highest-DOK cells
2. **Then fill volume cells:** DOK 1–2 across all objectives
3. **Last:** stretch items (DOK 4) and reserve / pilot items

For each cell, link to the appropriate item-writer prompt:
- MC items → `assessment_mc_item_writer_with_distractors.md`
- Performance items → `assessment_performance_task_designer.md`
- Constructed response → `teaching_assessment_rubric_builder.md`

### Step 7: Validity & Audit Checklist

- [ ] Every objective is represented; no orphans
- [ ] No objective taught is omitted from assessment unless intentionally
- [ ] DOK ceiling matches what was actually taught (no surprise rigor)
- [ ] Weights sum to 100% and approximately match instructional time
- [ ] Time budget fits the window
- [ ] Item types align with the construct (don't MC a writing standard)
- [ ] No single-item objectives carry >15% of total points (single point of failure)

### Step 8: Optional — Equating to Prior Forms

If this test must be comparable to a prior version, output a side-by-side blueprint comparison and flag cells that differ.

---

## Output Format

1. Objectives table with weights and DOK ceilings
2. Specifications matrix (objective × DOK × item-type)
3. Time budget reconciliation
4. Point allocation table
5. Item-write worklist in priority order
6. Validity audit checklist
7. Optional: equating comparison

---

## False-Positive Prevention

❌ **DON'T:**
- Distribute items evenly when instructional time wasn't even
- Skip DOK targets — recall-only tests under-measure target objectives
- Exceed the testing window — students perform worse on rushed tests
- Single-item an objective — one bad item destroys validity for that objective
- Use MC for writing or speaking standards — wrong construct

✅ **DO:**
- Tie weights to taught time, with adjustments for foundational vs. enrichment
- Set a DOK ceiling per objective and assess up to it
- Provide multiple items per high-weight objective
- Match item type to construct
- Audit before writing — fix the blueprint, not the items

---

## Quality Indicators

- [ ] Weights sum to 100% and trace to instructional time
- [ ] DOK distribution matches use case
- [ ] Time budget fits window
- [ ] No orphan objectives, no single-item high-weight objectives
- [ ] Item-write worklist is ordered by priority
- [ ] Audit checklist completed

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **CM-01** | Use case, time, point cap, and instructional emphasis anchor weights and counts. |
| **ST-02** | Eight-step build moves from objectives → matrix → time → audit. |
| **DS-01** | DOK and Bloom's frameworks structure rigor; weighted-coverage is the validity model. |
| **OC-01** | Specifications matrix template enforces consistent structure. |
| **QA-01** | Validity audit and time-budget reconciliation verify before items are written. |
