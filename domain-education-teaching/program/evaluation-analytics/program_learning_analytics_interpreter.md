---
title: "Learning Analytics Interpreter (LMS, Formative Data, Dashboards)"
category: education-teaching/program/evaluation-analytics
description: "Interpret learning-analytics data — LMS engagement, formative assessment results, completion/grade dashboards — producing structured analysis: pattern detection, equity audit, plausible-cause hypotheses, and instructional/program action plan."
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
  - learning-analytics
  - lms-data
  - formative-data
  - dashboards
  - higher-ed
  - k12
  - workforce
  - medical-education
  - equity
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/program/evaluation-analytics/program_early_warning_system_designer.md
  - domain-education-teaching/program/evaluation-analytics/program_continuous_improvement_cycle.md
  - ../program-outcomes-assessment/teaching_program_gap_analysis.md
---

# Learning Analytics Interpreter

**Objective:** Interpret supplied learning-analytics data (LMS engagement, formative assessment results, completion/grade dashboards, performance trends) producing structured analysis: pattern detection, equity audit (disaggregated subgroup performance), plausible-cause hypotheses, and an action plan tied to instructional or program decisions.

## When to Use
- ✅ Mid-term or end-of-term data review for a course or program
- ✅ Equity-focused audit of grade or completion data
- ✅ Diagnostic review when a course has elevated DFW or attrition
- ✅ Program-level cohort analysis
- ❌ Designing the analytics system (use `teaching_early_warning_system_designer.md`)
- ❌ Building the evaluation framework (use `teaching_program_evaluation_framework.md`)

## Inputs Required
- **Data supplied:** what data tables, time period, granularity
- **Course / program context:** what's being measured, intended uses
- **Comparison baselines:** prior cohorts, program averages, benchmarks
- **Subgroups for disaggregation:** demographics, prep level, enrollment status
- **Decision context:** what action might follow the interpretation

## Constraints

**Must:**
- Distinguish description, pattern detection, hypothesis, and recommendation
- Always disaggregate by relevant subgroups (equity audit is not optional)
- Surface alternative explanations for observed patterns (not just one cause)
- Flag data-quality issues (missing, biased, low-N)
- Pair findings with action recommendations
- Note correlations are not causes

**Must Not:**
- Claim causal mechanism from observational data alone
- Skip equity disaggregation
- Treat low-N subgroups as if reliable (flag and aggregate where needed)
- Generate recommendations not supported by the data
- Use only aggregate measures

## Instructions

1. **Confirm data and context.** Echo what data, period, subgroups, decision.

2. **Describe the data.**
   - Summary statistics
   - Distributions
   - Trends across time

3. **Detect patterns.**
   - Where are concentrations of low/high performance?
   - When do patterns emerge (early, mid, late)?
   - What's correlated with what?

4. **Equity audit.**
   - Disaggregate by relevant subgroups
   - Compare subgroup distributions to overall
   - Flag disparities
   - Note where N is too low for reliable subgroup analysis

5. **Hypothesize causes.**
   - Generate 3-5 plausible explanations
   - Note which are testable from supplied data
   - Note which require additional data

6. **Data-quality audit.**
   - Missing data
   - Sampling bias
   - Measurement validity
   - Confound risks

7. **Action recommendations.**
   - Short-term (within current term)
   - Medium-term (next term)
   - Long-term (program revision)
   - Each tied to evidence

8. **Communication plan.**
   - Who gets what
   - Format
   - Framing (asset-based, not deficit-based about students)

## Output Format

### Section 1: Interpretation Identity
- Data supplied, period, context, decision

### Section 2: Descriptive Summary

| Metric | Overall | Comparison Baseline | Direction |
|---|---|---|---|

### Section 3: Patterns Detected

| Pattern | Where / When | Evidence |
|---|---|---|

### Section 4: Equity Audit (Disaggregation)

| Subgroup | Metric | Overall | Subgroup Value | Gap | N (reliability flag) |
|---|---|---|---|---|---|

### Section 5: Plausible-Cause Hypotheses

| Hypothesis | Evidence in Supplied Data | Testable From Supplied? | Additional Data Needed |
|---|---|---|---|

### Section 6: Data Quality Audit

| Issue | Affected Data | Implication |
|---|---|---|

### Section 7: Action Recommendations

| Time Horizon | Action | Evidence Linked | Owner | Measure |
|---|---|---|---|---|

### Section 8: Communication Plan

| Audience | Findings to Share | Format | Framing Considerations |
|---|---|---|---|

### Section 9: Interpretation Audit

| Audit Question | Result |
|---|---|
| Description before hypothesis | Pass / Fail |
| Equity disaggregation included | Pass / Fail |
| Alternative explanations considered | Pass / Fail |
| Data quality assessed | Pass / Fail |
| Recommendations evidence-linked | Pass / Fail |
| No causal claims from observational data alone | Pass / Fail |
| Low-N subgroups flagged | Pass / Fail |

## False-Positive Prevention

| Common Mistake | Why It's Wrong | Correct Approach |
|---|---|---|
| Causal claims from observational data | Misleads decisions | "Associated with" / "correlated with" — not "caused by" |
| Skipping equity disaggregation | Hides disparate outcomes | Always disaggregate by relevant subgroups |
| Treating low-N as reliable | Statistical noise misread as signal | Flag low-N; aggregate or use cautious language |
| Single-cause hypotheses | Reality is multi-causal | Generate alternative explanations |
| Recommendations beyond data | Damages credibility | Tie each recommendation to specific evidence |
| Deficit-framed communication about students | Damages morale; reinforces bias | Asset-based framing; focus on systems |
| Skipping data-quality audit | Builds on shaky foundation | Audit before interpreting |
| LMS engagement = learning | Engagement is proxy at best | Triangulate with performance data |

## Verification Checklist

- [ ] Description before pattern before hypothesis
- [ ] Equity disaggregation
- [ ] Alternative explanations
- [ ] Data quality audited
- [ ] Low-N flagged
- [ ] Recommendations evidence-linked
- [ ] No unwarranted causal claims
- [ ] Communication plan honors framing
