---
title: "Outcomes-to-Assessment Mapper (Program Evidence Plan)"
category: education-teaching/program/outcomes-assessment
description: "Map every program outcome (PSLO / competency / graduate-profile element) to the assessment evidence that produces signal for it — direct measures, indirect measures, single-source vs. triangulated — and audit the resulting evidence plan for sufficiency, alignment, and feasibility."
techniques:
  - ST-02
  - ST-03
  - OC-03
  - DS-02
  - QA-01
  - QA-02
difficulty: intermediate
tags:
  - education
  - program-outcomes
  - assessment
  - evidence-plan
  - direct-measures
  - indirect-measures
  - higher-ed
  - workforce
  - medical-education
  - accreditation
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/program/outcomes-assessment/program_program_outcomes_framework.md
  - domain-education-teaching/program/outcomes-assessment/program_assessment_blueprint_builder.md
  - domain-education-teaching/program/curriculum-design/program_curriculum_map_builder.md
  - domain-education-teaching/program/outcomes-assessment/program_competency_assessment_evidence_design.md
---

# Outcomes-to-Assessment Mapper

**Objective:** Produce a complete program assessment evidence plan: every program outcome (PSLO / competency / graduate-profile element) mapped to ≥2 evidence sources (≥1 direct measure), with assessment timing, sample/coverage population, scoring rubric pointer, and a sufficiency audit per outcome.

## When to Use
- ✅ Building an assessment plan for a program (annual or multi-year cycle)
- ✅ Preparing accreditation evidence (program-level student learning data)
- ✅ Auditing whether existing assessments produce sufficient signal for each outcome
- ✅ Closing the loop after a program review identified outcome-data gaps
- ❌ Designing individual assessment items (use blueprint builder or rubric builder)
- ❌ Defining outcomes (use `teaching_program_outcomes_framework.md`)

## Inputs Required
- **Program identity**
- **Program outcomes / PSLOs** with IDs and text
- **Existing assessment inventory:** assessments currently in use across courses + program (e.g., capstone, portfolio, licensure exam, employer survey)
- **Accreditor requirements** (optional): specific evidence types or volumes required
- **Sampling/census preferences:** whether outcomes are assessed for all students or sampled
- **Assessment cycle:** annual / multi-year rotating

## Constraints

**Must:**
- Every outcome has ≥2 evidence sources
- Every outcome has ≥1 direct measure (student performance evidence — not perception)
- Distinguish direct measures (capstone artifact, performance task, licensure exam, portfolio defense) from indirect (alumni surveys, employer satisfaction, course evaluations)
- Specify sampling/census for each measure
- Tie each measure to a scoring rubric or scoring protocol
- Identify the responsible party (faculty committee, assessment office, external evaluator)

**Must Not:**
- Rely solely on indirect measures
- Treat course grades as direct evidence of outcome attainment (grades roll up too many things)
- Treat student self-report as direct measure
- Invent assessments not in the existing inventory; flag "proposed" if recommending additions
- Overload one assessment to measure too many outcomes (signal degrades)

## Instructions

1. **Confirm inputs.** Echo outcomes, assessment inventory, accreditor requirements, cycle.

2. **Categorize existing assessments.** For each, tag: Direct or Indirect, format, current use, courses involved.

3. **Build outcome × assessment matrix.** Mark which assessments produce signal for which outcomes.

4. **Audit sufficiency per outcome.**
   - ≥2 sources? ≥1 direct? Triangulation?
   - If gap: identify proposed addition.

5. **Audit assessment design.**
   - Does the assessment actually produce signal at the outcome's cognitive level?
   - Is the rubric/scoring protocol aligned to the outcome?
   - Is sampling adequate?

6. **Build the timing plan.**
   - Annual cycle: which outcomes assessed which year?
   - For each assessment: when administered, when scored, when reported.

7. **Produce remediation plan.**
   - Outcomes with insufficient evidence: proposed additions
   - Assessments overloaded with too many outcomes: redesign or split
   - Rubrics that don't align to outcomes: revise

## Output Format

### Section 1: Plan Identity
- Program, outcomes count, cycle, sampling approach, accreditor

### Section 2: Assessment Inventory

| Assessment | Format | Direct/Indirect | Courses Involved | Current Use |
|---|---|---|---|---|

### Section 3: Outcome × Assessment Matrix

|  | Assess-A | Assess-B | Assess-C | Assess-D | … |
|---|---|---|---|---|---|
| Outcome 1 | Direct | | Indirect | Direct | |

### Section 4: Sufficiency Audit per Outcome

| Outcome | # Direct | # Indirect | Total | Triangulated? | Gap | Proposed Addition |
|---|---|---|---|---|---|---|

### Section 5: Assessment-Design Audit

| Assessment | Cognitive Level Match | Rubric Alignment | Sampling Adequacy | Notes |
|---|---|---|---|---|

### Section 6: Timing Plan

| Year/Cycle | Outcomes Assessed | Assessments Run | Reporting Due |
|---|---|---|---|

### Section 7: Remediation Plan

| Action | Outcome / Assessment | Specifics |
|---|---|---|

## False-Positive Prevention

| Common Mistake | Why It's Wrong | Correct Approach |
|---|---|---|
| Course grades as direct evidence | Grades aggregate too many factors; outcome signal is lost | Use specific assignment-level evidence with outcome-aligned rubric |
| Student self-report as direct | Self-report is perception, not performance | Direct measures observe or score student work product |
| Only indirect measures | Alumni surveys don't show what students could do | Every outcome needs ≥1 direct measure |
| Overloading one capstone with all outcomes | Signal degrades; rubric becomes unscorable | Spread evidence; capstone covers some outcomes, embedded assessments cover others |
| Inventing assessments | Plan becomes aspirational, not operational | Distinguish existing from proposed; mark proposed clearly |
| No sampling specification | Implementers don't know who to assess | Specify census or sample (with sample size and selection method) |
| No scoring rubric pointer | Different scorers produce inconsistent data | Every measure has named rubric or scoring protocol |

## Verification Checklist

- [ ] Every outcome has ≥2 evidence sources
- [ ] Every outcome has ≥1 direct measure
- [ ] Direct vs. indirect distinction maintained
- [ ] Sampling/census specified per measure
- [ ] Rubric/scoring protocol pointer for every measure
- [ ] Timing plan covers the assessment cycle
- [ ] Proposed assessments distinguished from existing
- [ ] Remediation plan addresses every gap
