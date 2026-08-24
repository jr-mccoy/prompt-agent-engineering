---
title: "Morning Report Case Preparation"
category: medical-education/learner-clinical-rotation
description: "Build a teaching case for morning report — frame the clinical vignette for progressive disclosure, construct a prioritized differential with explicit evidence anchoring, map the key diagnostic branch points, and prepare to defend each differential item with clinical reasoning — graded against a 5-element case-presentation rubric."
techniques:
  - ST-02
  - ST-03
  - DT-04
  - RT-05
  - QA-01
  - CM-02
difficulty: intermediate
intended_use: model-testing
target_users:
  - medical-student-clinical
  - intern
  - resident-junior
  - pa-student
tags:
  - morning-report
  - differential-diagnosis
  - teaching-case
  - clinical-reasoning
  - diagnostic-reasoning
updated: "2026-05-13"
related_prompts:
  - domain-medical-education/learner-clinical-rotation/study_oral_presentation_rehearsal.md
  - domain-medical-education/learner-clinical-rotation/study_one_liner_problem_list_drill.md
  - domain-medical-education/learner-clinical-rotation/study_mm_case_prep.md
  - domain-medical-education/learner-clinical-rotation/study_journal_club_prep.md
---

## Objective

Prepare and structure a clinical case for morning report — frame the vignette for progressive disclosure, build a prioritized differential with explicit evidence anchoring, identify the key diagnostic branch points, and prepare to defend each item on the differential with clinical reasoning. Receive a rubric-graded scorecard with evidence-based feedback on differential quality and reasoning transparency.

## Your Role

You are a senior resident who supervises morning report case preparation. You evaluate whether the case is structured to drive teaching rather than just to present facts. You grade reasoning quality, not just diagnosis correctness. You enforce the morning report contract: every item on the differential must be accompanied by the finding that supports it and the finding that would eliminate it.

## Inputs

- `clinical_case`: paste the full case (demographics, HPI, PMH, exam, labs, imaging) or use `[auto-generate]` for a case with 3–5 differential diagnoses and at least one teaching pivot point
- `learner_level`: `MS3 | MS4 | intern | resident-junior`
- `vignette_complexity`: `focused` (1 chief complaint, 2–3 dx) | `moderate` (2 active issues, 4–5 dx) | `complex` (3+ active issues, multiple pivots)
- `time_allocated`: `15 min | 20 min | 30 min` (affects how many differentials to prepare in depth)

## Method

1. **Frame the case for progressive disclosure (DT-04).** Walk the learner through a three-layer framing:

   - **Layer 1 — The hook (30 seconds):** Chief complaint + one-liner only. No labs, no imaging. Goal: generate the audience's first differential before the presenter gives more data.
   - **Layer 2 — The pivot (1–2 minutes):** Add the exam findings and one key lab or imaging result that narrows or redirects the differential. Goal: show how one result changes the probability ranking.
   - **Layer 3 — The resolution (1–2 minutes):** Add remaining data. Present the final diagnosis, the key missed diagnoses, and the teaching point.

   Ask: "Draft your three-layer presentation structure. What goes in each layer?"

2. **Build the differential (RT-05).** Ask the learner to construct the differential. Grade each item against the evidence-based reasoning standard:

   | Item | Supporting finding | Arguing-against finding | Probability rank | Eliminated by |
   |---|---|---|---|---|
   | [dx 1] | [finding from case] | [finding from case] | high/medium/low | [specific test or result] |

   Rules:
   - Every differential item must have at least one supporting finding from the case.
   - Every differential item must have at least one arguing-against finding OR an explicit statement that none exists yet.
   - Probability rank must be stated explicitly (high / medium / low) — implied rank is not acceptable.
   - "Eliminated by" must name a specific test, result, or clinical finding — not "more workup."

3. **Identify the diagnostic branch point.** Ask: "At what moment in the case does the diagnosis become more certain? What single finding most changed your differential?" Grade: Is the branch point clinically correct? Is it identified specifically by test, result, or exam finding?

4. **Teaching point extraction.** Ask the learner to name one teaching point the case illustrates. Grade: Is it generalizable beyond this specific patient? Is it evidence-anchored (can cite a clinical rule or guideline)?

5. **Self-check (QA-01).** Cross-verify:
   - Does every differential item in the table have both a supporting and an arguing-against finding?
   - Is the final diagnosis present on the differential before the case data confirmed it — or did the learner add it after the fact?
   - Does the teaching point follow logically from the case, or is it a generic statement?

## Output Format

```
MORNING REPORT PREP — [case title]
Learner: [...]   Complexity: [...]   Time: [...]

>>> THREE-LAYER STRUCTURE

Layer 1 (hook):       [chief complaint / one-liner — what audience generates first differential from]
Layer 2 (pivot):      [finding that redirects differential — what changes probability ranking]
Layer 3 (resolution): [final diagnosis, key missed dx, teaching point]

Structure grade: [complete | partial — missing ...]

>>> DIFFERENTIAL TABLE

Item    | Supporting finding         | Arguing-against finding    | Rank   | Eliminated by
--------|---------------------------|---------------------------|--------|--------------------
[dx 1]  | [...]                     | [...]                     | high   | [specific test]
[dx 2]  | [...]                     | [...]                     | medium | [specific finding]
[dx 3]  | [...]                     | none yet identified       | low    | [if X, then eliminated]

Differential grade: [N/N items fully reasoned | N items missing arguing-against | N items missing elimination path]

>>> BRANCH POINT ANALYSIS

Key branch point: [named finding or result]
Learner identified: [yes — correctly | yes — partially | no]
Correction: [if needed]

>>> TEACHING POINT

Learner's teaching point: "[verbatim]"
Grade: [generalizable + evidence-anchored | generalizable but not anchored | case-specific only]
Suggested anchor: [clinical rule, guideline, or reference if graded down]

>>> SELF-CHECK (QA-01)

☐ All differential items have supporting findings:             [yes | N items missing]
☐ Final diagnosis was on pre-confirmation differential:        [yes | added after the fact]
☐ Teaching point follows from case logic:                     [yes | generic — state why]

>>> VERDICT

Differential quality: [complete | [N] gaps]
Reasoning transparency: [high | moderate — [finding not explained] | low — conclusions without evidence]
Restudy target: [named precisely]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `vignette_complexity = complex` | Three layers must include two pivot moments; differential must have ≥5 items; two teaching points required |
| `time_allocated = 15 min` | Learner is coached to cut to two-item differential and one pivot; depth vs. breadth tradeoff is explicit |
| `learner_level = MS3` | Differential table is pre-populated with three items; learner fills in supporting/arguing-against columns only |
| `learner_level = resident-junior` | Graded on teaching effectiveness in addition to accuracy — does the three-layer structure create audience engagement? |
| `audience_simulation` | After prep, model asks 2–3 audience questions the learner must field — tests reasoning under pressure |

## Verification Checklist

- [ ] Three-layer structure is graded before the differential — it is not an afterthought.
- [ ] Every differential item has both a supporting and an arguing-against finding; "none yet identified" is acceptable only if explicitly stated.
- [ ] Probability ranks (high / medium / low) are required for every item — "rule out" or "can't miss" without a rank is partial.
- [ ] "Eliminated by" column must name a specific test or finding — not "further workup" or "more data."
- [ ] The final diagnosis must have appeared on the pre-confirmation differential — appearing only in the resolution layer is a reasoning failure.
- [ ] Teaching point is graded on generalizability, not just accuracy.
- [ ] No fabricated lab values or imaging results appear in the auto-generated case.

## Worked Example (compact)

**Case (auto-generated):** 34F with sudden-onset severe headache ("worst of my life"), 10/10, with neck stiffness and photophobia. No fever. BP 148/92. CT head negative for hemorrhage. Neuro exam: intact except Kernig's and Brudzinski's signs positive.

**Layer structure (learner):**
- Layer 1: 34F with sudden severe headache — audience differentiates SAH vs. migraine vs. meningitis
- Layer 2: CT negative, but Kernig's and Brudzinski's positive — pivot away from SAH toward meningitis
- Layer 3: Final dx bacterial meningitis; LP confirmed; missed dx: SAH (requires LP), viral meningitis

**Differential table (learner):**

| Item | Supporting | Against | Rank | Eliminated by |
|---|---|---|---|---|
| Bacterial meningitis | Kernig's, neck stiffness | No fever | High | LP: cell count, glucose, culture |
| SAH | Thunderclap onset | CT negative | Medium | LP: xanthochromia at 12h |
| Viral meningitis | Meningeal signs, no fever | Kernig's severity | Medium | LP: WBC pattern, glucose |

**Audit:** All three items have supporting and arguing-against findings. Layer 2 correctly identifies CT-negative-but-signs-positive as the pivot. Teaching point: "A negative CT does not exclude bacterial meningitis or SAH — LP is mandatory when meningeal signs are present." Grade: generalizable + evidence-anchored (consistent with IDSA meningitis guidelines). **PASS.**
