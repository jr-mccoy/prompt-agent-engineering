---
title: "Milestone & Checkpoint Architecture Designer"
category: education-teaching/curriculum-design
description: "Design a milestone or checkpoint architecture for a competency-based program — progression checkpoints, evidence requirements, decision rules, and the relationship between milestones and stackable credentials or graduation requirements."
techniques:
  - ST-02
  - ST-03
  - OC-03
  - DS-01
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - education
  - curriculum-design
  - milestones
  - checkpoints
  - competency-based-progression
  - acgme
  - apprenticeship
  - stackable-credentials
  - higher-ed
  - workforce
  - medical-education
updated: "2026-05-15"
related_prompts:
  - teaching_competency_framework_designer.md
  - teaching_progression_map_designer.md
  - ../program-outcomes-assessment/teaching_competency_assessment_evidence_design.md
  - teaching_competency_mapping_workforce.md
---

# Milestone & Checkpoint Architecture Designer

**Objective:** Design a milestone/checkpoint architecture for a competency-based program: a sequence of progression checkpoints with explicit evidence requirements at each, decision rules for advancement, and the relationship between milestones and stackable credentials, wage progressions, supervision levels, or graduation eligibility.

## When to Use
- ✅ ACGME milestone implementation for residency programs
- ✅ Apprenticeship wage-progression checkpoint design
- ✅ Stackable credential ladder design (each milestone awards a credential)
- ✅ Competency-based higher-ed program checkpoints
- ✅ Workforce career-lattice progression points
- ❌ Designing a single competency framework (use `teaching_competency_framework_designer.md`)
- ❌ Designing assessment evidence per competency (use `teaching_competency_assessment_evidence_design.md`)

## Inputs Required
- **Program identity and sector**
- **Competency framework** (with IDs)
- **Time horizon** for the program
- **Number of milestones desired** (typically 3-6 across the program)
- **What each milestone unlocks:** wage step, supervision-level change, credential award, graduation eligibility, ACGME level (1-5), promotion
- **Decision-making body:** CCC, CDC, supervisor sign-off, exam pass, committee
- **Regulatory constraints** (DOL apprenticeship, ACGME requirements, accreditor mandates)

## Constraints

**Must:**
- Each milestone has explicit evidence requirements drawn from the assessment plan
- Each milestone has explicit decision rule (what counts as meeting it)
- Each milestone has a remediation pathway for learners who don't meet it
- Each milestone has appeal/review procedure
- Relationship between milestones and what they unlock is explicit
- Honor regulatory frameworks (ACGME milestone language, DOL apprenticeship rules)

**Must Not:**
- Generate milestones with vague "demonstrates competence" language without evidence specification
- Set the same threshold for every milestone
- Skip the remediation pathway (this is where most architectures fail)
- Invent regulatory citations
- Generate so many milestones the system becomes administrative overhead

## Instructions

1. **Confirm inputs.** Echo program, framework, time horizon, milestone count, what each unlocks, decision body.

2. **Establish milestone sequence.**
   - Typical 3-6 milestones: Foundation / Developing / Competent / Proficient / Final / Expert (or sector-appropriate labels: PGY-1 Year-End, PGY-2 Mid-Year, PGY-3 Final for residency; Apprentice Y1Q4, Apprentice Y2Q2, Journey).
   - For each: position in time, what triggers review.

3. **For each milestone:**

   - **Competency expectations:** which competencies at what level (using framework's progression-level language)
   - **Evidence requirements:** what evidence must exist (observations, exams, work products, MSF, simulation, outcome data) and minimum counts
   - **Decision rule:** what counts as meeting milestone — proportion of evidence at target level, absence of red flags, committee judgment, threshold scores
   - **What it unlocks:** wage step, credential award, supervision change, advancement
   - **Remediation pathway:** if not met, what happens — extended time, additional learning, structured support, repeat attempt, alternative pathway, separation
   - **Appeal/review:** procedure for contested decisions

4. **Map dependencies.**
   - Which milestones must precede others?
   - Are there parallel tracks?

5. **Specify governance.**
   - Decision-making body composition
   - Cadence (semi-annual, annual)
   - Documentation requirements

6. **Audit for fairness and bias.**
   - Are decision rules transparent and consistent?
   - Are there safeguards for assessor bias?
   - Is remediation accessible to all learners?

7. **Verify regulatory compliance.**
   - For ACGME programs: milestone language and CCC governance per ACGME requirements
   - For DOL apprenticeship: wage-progression rules per registered apprenticeship standards
   - For accredited HE: progression rules per accreditor

## Output Format

### Section 1: Architecture Identity
- Program, framework, milestone count, time horizon, decision body, regulatory frame

### Section 2: Milestone Sequence Overview

| Milestone | Position in Time | Trigger for Review | What It Unlocks |
|---|---|---|---|

### Section 3: Per-Milestone Specification

For each milestone:

**Milestone [N]: [Name]**

| Element | Description |
|---|---|
| Competency expectations | [competencies × target levels] |
| Evidence requirements | [evidence types × minimum counts] |
| Decision rule | [explicit threshold or judgment criteria] |
| What it unlocks | [wage / credential / supervision / advancement] |
| Remediation pathway | [steps if not met] |
| Appeal/review procedure | |

### Section 4: Dependencies Map

| Predecessor | Successor | Type (gating / informational) |
|---|---|---|

### Section 5: Governance
- Decision body composition
- Cadence
- Documentation requirements
- Conflict-of-interest policies

### Section 6: Fairness & Bias Audit

| Question | Result | Notes |
|---|---|---|
| Decision rules transparent | Pass / Fail | |
| Consistent application across learners | Pass / Fail | |
| Assessor bias safeguards | Pass / Fail | |
| Remediation accessible | Pass / Fail | |
| Demographic pattern monitoring | Pass / Fail | |

### Section 7: Regulatory Compliance

| Regulation | Requirement | Compliance |
|---|---|---|

### Section 8: Architecture Audit

| Audit Question | Result |
|---|---|
| Every milestone has evidence specification | Pass / Fail |
| Every milestone has decision rule | Pass / Fail |
| Every milestone has remediation pathway | Pass / Fail |
| Dependencies mapped | Pass / Fail |
| Regulatory compliance confirmed | Pass / Fail |
| Fairness audit passed | Pass / Fail |

## False-Positive Prevention

| Common Mistake | Why It's Wrong | Correct Approach |
|---|---|---|
| "Demonstrates competence" as decision rule | Unscorable, unappealable | Specify evidence types, counts, thresholds |
| No remediation pathway | Architecture is punitive; learners have nowhere to go | Every milestone has explicit remediation |
| Identical thresholds across milestones | Progression isn't differentiated | Threshold should rise across milestones |
| Single-rater decisions for high-stakes | Bias concentrates | Multi-person decision body |
| Invented ACGME/DOL/accreditor rules | Architecture won't survive audit | Cite verified requirements; flag for verification |
| No appeal procedure | Legal and ethical exposure | Build explicit appeal/review |
| Demographic patterns unmonitored | Bias hidden | Build monitoring; surface patterns |

## Verification Checklist

- [ ] 3-6 milestones with explicit timing
- [ ] Each milestone has evidence requirements
- [ ] Each milestone has decision rule
- [ ] Each milestone has remediation pathway
- [ ] What each milestone unlocks is specified
- [ ] Dependencies mapped
- [ ] Governance defined
- [ ] Regulatory compliance addressed
- [ ] Fairness/bias audit passed
