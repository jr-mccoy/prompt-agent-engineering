---
title: "Nursing Clinical Evaluation Tool — Bondy-Style Anchored Behavioral Rubric for Pre-Licensure Clinical Rotation"
category: medical-education/profession-specific/nursing
difficulty: advanced
intended_use: model-testing
description: "Author a clinical evaluation tool (CET) for a pre-licensure nursing rotation using the Bondy-derived 5-level rating scale (Independent / Supervised / Assisted / Marginal / Dependent) anchored with observable behaviors per QSEN competency domain (patient-centered care, teamwork, EBP, QI, safety, informatics) plus profession-specific domains (clinical judgment, professionalism, communication, technical skills). Output is a one-page tool with anchor descriptors per cell + scoring guide + faculty commentary blocks."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - DT-05
  - CM-02
  - QA-16
target_users:
  - clinical-educator
  - curriculum-designer
  - assessment-faculty
tags:
  - clinical-evaluation
  - bondy
  - qsen
  - rubric
  - pre-licensure
  - educator-tool
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/profession-specific/nursing/prof_rn_concept_map_designer.md
  - domain-medical-education/profession-specific/nursing/prof_rn_preceptor_orientation_plan.md
---

## Objective

Build a single-rotation clinical evaluation tool (CET) that an instructor can use mid-rotation and end-of-rotation. Anchored 5-level rating scale per competency domain, with observable behavior descriptors at each level. Output is a faculty-usable one-page tool — not a vague global rating scale.

## Your Role

Nursing assessment-faculty / curriculum designer. You write the CET to NLN-style accreditation expectations and Bondy-derived anchor logic (1955 Bondy scale carried forward in modern pre-licensure tools). You produce instructor-facing language, not learner-facing language.

## Inputs

- `program_type`: `ADN | BSN-traditional | BSN-accelerated | LPN/LVN | direct-entry-MSN`
- `rotation`: free text (e.g., "med-surg I — fundamentals," "med-surg II — adult acute care," "OB," "peds," "psych," "community health," "leadership/capstone preceptored," "critical care elective")
- `weeks_in_rotation`: integer
- `learner_level`: `nursing-student-2nd-semester | nursing-student-3rd-semester | nursing-student-final-semester`
- `framework_overlay`: `QSEN | AACN-essentials-2021 | NLN-competencies | program-specific` — drives the named domain set
- `competency_count`: integer 6–10 (number of distinct competency rows)
- `time_in_rotation`: `midpoint | end-of-rotation` (changes the expected level on the scale; final week should expect closer to Independent for supervised tasks)
- `failing_anchor_required`: boolean (default true — surface what triggers a failing rating with due-process implications)

## Method

1. **Lock the framework (CM-02).** Pick the domain set from `framework_overlay`. Examples:
   - QSEN: Patient-Centered Care, Teamwork & Collaboration, EBP, QI, Safety, Informatics.
   - AACN Essentials 2021: 10 domains — choose the 6–8 most observable in this rotation.
   - Program-specific: instructor pastes domain list.

2. **Define the rating scale (DS-01 Bondy-derived):**
   - **5 — Independent:** safe, accurate, proficient. No prompting. Time-efficient. Affect appropriate.
   - **4 — Supervised:** safe, accurate, proficient. Occasional prompting. Some inefficiency. Sound judgment.
   - **3 — Assisted:** safe, accurate, mostly skilled. Frequent prompting. Some inefficiency. Sound judgment.
   - **2 — Marginal:** safe only with continuous supervision. Skill is unrefined. Affect/judgment may be inconsistent. Cannot meet competency for level.
   - **1 — Dependent:** unsafe. Cannot perform without complete direction. Lacks insight or judgment. Triggers remediation pathway.
   - **N/O — Not Observed:** competency not demonstrated this rotation.

3. **For each competency row, write level-anchored behavioral descriptors (DT-05).** Each cell of the matrix gets a 1–2 sentence observable behavior. *Behavioral, not affective.* Bad: "shows compassion." Good: "introduces self by name and role; explains procedure before touching the patient; checks understanding by asking patient to teach back."

4. **Add critical-element columns (QA-16).** For each row, also flag:
   - `Critical safety element` — one specific behavior that, if absent, drops the rating to 2 or below regardless of other strengths (e.g., for medication administration: independent verification of patient identifiers; for sterile technique: not breaking field).
   - `Required artifact` — what the learner must submit/demonstrate to be rated (concept map, dosage calc sheet, observed med pass, narrative documentation sample).

5. **Add evaluator commentary blocks.** Three free-text blocks at end:
   - Strengths (specific behaviors observed, with date if possible).
   - Areas for growth (specific behaviors to develop, framed as next-rotation goal).
   - Plan for improvement (only completed if any rating is 2 or below — names due-process steps).

6. **Failing anchor (DS-01).** If `failing_anchor_required = true`, name the rating threshold for course failure (e.g., "Any '1' on a critical safety element OR any 'N/O' on a required artifact OR ≥ 2 ratings of '2' constitutes failure of the clinical rotation").

## Output Format

```
CLINICAL EVALUATION TOOL
Program: [...]   Rotation: [...]   Weeks: [...]
Framework: [...]   Time point: [midpoint | end-of-rotation]

>>> RATING SCALE

5 = Independent: [...]
4 = Supervised: [...]
3 = Assisted: [...]
2 = Marginal: [...]
1 = Dependent (unsafe): [...]
N/O = Not Observed

>>> COMPETENCY MATRIX

═══ Domain 1: [name]
  Critical safety element: [...]
  Required artifact: [...]
  
  Level descriptors:
    5: [observable behavior]
    4: [...]
    3: [...]
    2: [...]
    1: [...]
  
  Mid-rotation expected: [level]    End-of-rotation expected: [level]
  Rating: ☐5  ☐4  ☐3  ☐2  ☐1  ☐N/O
  Evidence (cite specific behavior + date): __________

═══ Domain 2: [name]
  [same structure]

[repeat for competency_count rows]

>>> EVALUATOR COMMENTARY

Strengths (specific behaviors observed):
  • [...]
  • [...]

Areas for growth (specific next-rotation behaviors):
  • [...]
  • [...]

Plan for improvement (REQUIRED if any rating is 2 or below):
  Behavior of concern: [...]
  Specific objectives for next rotation week: [...]
  Resources / faculty support: [...]
  Due-process notification: ☐ Verbal ☐ Written warning ☐ Learning contract

>>> FAILING THRESHOLD

[Named threshold per inputs]

>>> SIGNATURES

Learner: __________ Date: ____
Clinical instructor: __________ Date: ____
Course coordinator (if rating < 3): __________ Date: ____
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `program_type` | Different programs have different end-of-rotation expectations |
| `rotation` | Drives which competencies are observable |
| `time_in_rotation` | Midpoint vs end raises the expected level on the scale |
| `framework_overlay` | QSEN vs AACN-2021 vs NLN |
| `competency_count` | Density (6 = focused; 10 = comprehensive) |
| `failing_anchor_required` | Surfaces the due-process line |
| `population_overlay` | Adds population-specific competency rows (peds: weight-based dosing; OB: maternal-fetal monitoring; psych: therapeutic communication + safety) |

## Verification Checklist

- [ ] Rating scale has 5 anchor levels + N/O, each with one-line definition.
- [ ] Every competency row has a critical safety element named.
- [ ] Every competency row has a required artifact named.
- [ ] Every level descriptor is *behavioral and observable*, not affective ("shows initiative" is too vague; "volunteers to take primary patient assignment without prompting" is observable).
- [ ] Mid-rotation expected level differs from end-of-rotation expected level (otherwise the tool is time-blind).
- [ ] Evidence field requires specific behavior + date, not "see narrative."
- [ ] Plan for improvement section is conditionally required (only if rating < 3) and names due-process steps.
- [ ] Failing threshold is numeric / criterion-referenced, not "instructor judgment."
- [ ] No vague competencies ("demonstrates professionalism" without anchored behaviors).
- [ ] No invented program policies; named accreditation framework cited (QSEN / AACN / NLN).

## Worked Example (compact)

**Input:** program_type = `BSN-traditional`, rotation = `med-surg II — adult acute care`, weeks_in_rotation = 7, learner_level = `nursing-student-3rd-semester`, framework_overlay = `QSEN`, competency_count = 6, time_in_rotation = `end-of-rotation`, failing_anchor_required = true.

**Output (excerpt):**

```
═══ Domain 1: Safety — Medication Administration

Critical safety element: Independent verification of two patient identifiers AND independent calculation of high-alert medication doses (insulin, anticoagulants, opioids, IV potassium) before administration.
Required artifact: Three faculty-observed medication passes with calculation sheet attached.

Level descriptors:
  5 — Independent: Performs full 6 rights independently; identifies medication errors before administration; recalculates high-alert meds independently; teaches patient about new meds in plain language without prompting.
  4 — Supervised: Performs 6 rights with occasional faculty cue; correctly identifies meds requiring independent dual verification; calculates doses correctly; provides patient education with minimal prompting.
  3 — Assisted: Performs 6 rights with frequent faculty prompting; needs cue to perform independent dose calculation; can verbalize rationale but does not initiate teaching.
  2 — Marginal: Misses one of the 6 rights without faculty intervention; relies on faculty for dose calculation; cannot identify high-alert medications without prompting.
  1 — Dependent (unsafe): Attempts administration without verification; calculation errors not self-caught; would administer wrong dose without faculty intercept.

Mid-rotation expected: 3    End-of-rotation expected: 4
Rating: ☐5  ☐4  ☐3  ☐2  ☐1  ☐N/O
Evidence: __________

═══ Domain 2: Patient-Centered Care — Communication
[etc.]

>>> FAILING THRESHOLD

Course failure occurs if ANY of the following:
  • Any '1' rating on a critical safety element (single occurrence)
  • Any 'N/O' on a required artifact at end of rotation
  • ≥ 2 ratings of '2' across domains at end of rotation
  • Documented unsafe practice incident regardless of subsequent improvement (per program safety policy)
```
