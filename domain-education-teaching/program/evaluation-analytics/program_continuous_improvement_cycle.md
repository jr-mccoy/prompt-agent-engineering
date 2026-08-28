---
title: "Continuous Improvement Cycle Designer (PDSA / Improvement Science)"
category: education-teaching/program/evaluation-analytics
description: "Design a Plan-Do-Study-Act (PDSA) or improvement-science cycle for an educational program — specifying the change idea, measures (outcome / process / balancing), test scale, data plan, and decision rules for scaling, adapting, or abandoning."
techniques:
  - ST-02
  - ST-03
  - OC-03
  - DS-01
  - QA-01
difficulty: intermediate
tags:
  - education
  - continuous-improvement
  - pdsa
  - improvement-science
  - higher-ed
  - k12
  - workforce
  - medical-education
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/program/evaluation-analytics/program_program_evaluation_framework.md
  - domain-education-teaching/program/evaluation-analytics/program_logic_model_designer.md
  - ../accreditation-program-review/teaching_program_review_cycle_designer.md
---

# Continuous Improvement Cycle Designer

**Objective:** Design a Plan-Do-Study-Act (PDSA) or improvement-science cycle for an educational change idea — clear change theory, test scale, measures (outcome / process / balancing), data collection plan, decision rules for adopt-adapt-abandon — that produces evidence-based iteration rather than indefinite implementation.

## When to Use
- ✅ Testing an instructional change before full adoption
- ✅ Iterating program design based on early results
- ✅ Implementing improvement-science work in K-12 networks (NIC, BTEN, IHI)
- ✅ ACGME-style continuous improvement loops
- ❌ Annual program review (use `teaching_program_review_cycle_designer.md`)
- ❌ Full program evaluation framework (use `teaching_program_evaluation_framework.md`)

## Inputs Required
- **Change idea** to test
- **Problem the change addresses** (with baseline data)
- **Change theory:** why this change should produce the desired effect
- **Test scale:** how big to start (one classroom, one cohort, one site)
- **Resources for testing**

## Constraints

**Must:**
- State the change theory explicitly (why this change → expected outcome)
- Specify three measure types: outcome (primary signal), process (was it implemented), balancing (unintended effects)
- Start small (PDSA principle: test before scaling)
- Specify data collection plan (frequency, instruments)
- Specify decision rules (adopt as is / adapt / abandon)
- Build a multi-cycle plan (PDSAs rarely succeed first time)

**Must Not:**
- Skip balancing measures (changes have side effects)
- Test at full scale before small-scale evidence
- Generate cycles without explicit decision rules
- Treat single-cycle success as proof
- Skip process measures (if implementation drifted, outcome findings are confounded)

## Instructions

1. **Confirm change idea, problem, change theory.**

2. **Specify the test cycle.**

   **Plan:**
   - Change idea
   - Change theory (causal logic)
   - Predictions
   - Who, what, when, where
   - Data plan (measures, collection)

   **Do:**
   - Implement at small scale
   - Document what happened (including deviations from plan)

   **Study:**
   - Compare results to predictions
   - Examine outcome, process, balancing measures
   - Identify what worked, what didn't, why

   **Act:**
   - Decision: Adopt / Adapt / Abandon
   - Next cycle plan if adapting

3. **Specify measures.**

   **Outcome measure:** the primary signal of whether the change produced the intended effect.

   **Process measure:** whether the change was implemented as designed.

   **Balancing measure:** whether the change produced unintended negative consequences elsewhere.

4. **Build multi-cycle plan.**

   - Cycle 1: smallest scale (one classroom, one week, one cohort sub-group)
   - Cycle 2: expand if Cycle 1 promising; adapt if mixed
   - Cycle 3+: progressively expand
   - Scale-up plan if multi-cycle evidence supports

5. **Specify decision rules.**

   - Adopt: outcome measure improved meaningfully; process implemented; balancing measures acceptable
   - Adapt: partial success; refine and re-test
   - Abandon: no improvement / unintended harm; revise change idea

6. **Build the data infrastructure.**
   - Who collects what
   - Frequency
   - Format (real-time, periodic)
   - Where stored
   - Who analyzes
   - When reviewed

## Output Format

### Section 1: Cycle Identity
- Change idea, problem, change theory, scale

### Section 2: PDSA Plan

| Element | Specification |
|---|---|
| Change idea | |
| Change theory | |
| Prediction | |
| Who/what/when/where | |
| Data plan | |

### Section 3: Measures

| Measure Type | Measure | Source | Frequency | Decision Threshold |
|---|---|---|---|---|
| Outcome | | | | |
| Process | | | | |
| Balancing | | | | |

### Section 4: Multi-Cycle Plan

| Cycle | Scale | Duration | Expected Decision Point |
|---|---|---|---|

### Section 5: Decision Rules

| Decision | Conditions | Next Step |
|---|---|---|
| Adopt | | |
| Adapt | | |
| Abandon | | |

### Section 6: Data Infrastructure
- Collectors
- Frequency
- Format
- Storage
- Analysis owner
- Review cadence

### Section 7: Scale-Up Plan
- Conditions for moving from PDSA to broader implementation
- Spread plan

### Section 8: Cycle Audit

| Audit Question | Result |
|---|---|
| Change theory stated | Pass / Fail |
| Three measure types specified | Pass / Fail |
| Test scale appropriately small | Pass / Fail |
| Decision rules explicit | Pass / Fail |
| Multi-cycle plan | Pass / Fail |
| Data infrastructure realistic | Pass / Fail |

## False-Positive Prevention

| Common Mistake | Why It's Wrong | Correct Approach |
|---|---|---|
| Skipping balancing measures | Side effects unknown | Always specify what could go wrong |
| Testing at full scale | High-risk; no easy reversal | Start small; expand based on evidence |
| Single cycle "proves" the change | Statistical noise + Hawthorne effect | Multi-cycle confirmation required |
| No process measures | Can't distinguish implementation failure from concept failure | Process measure required |
| Vague decision rules | Drift continues regardless of evidence | Explicit conditions for each decision |
| No change theory | Test becomes blind | State why the change should work |
| No data infrastructure | Measures aren't collected | Specify infrastructure before launching |

## Verification Checklist

- [ ] Change theory explicit
- [ ] Three measure types specified
- [ ] Multi-cycle plan with scaling logic
- [ ] Decision rules for adopt/adapt/abandon
- [ ] Data infrastructure realistic
- [ ] Test starts small
- [ ] Scale-up plan conditional on evidence
