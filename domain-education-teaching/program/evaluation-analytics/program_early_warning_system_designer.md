---
title: "Early Warning System Designer (Indicator-Threshold-Intervention)"
category: education-teaching/program/evaluation-analytics
description: "Design an early-warning system for learner risk — indicator selection, threshold setting, intervention triggers, owner assignment, and feedback loops — for K-12 dropout prevention, HE retention, or workforce attrition mitigation."
techniques:
  - ST-02
  - ST-03
  - OC-03
  - DS-02
  - QA-01
  - QA-02
difficulty: advanced
tags:
  - education
  - early-warning
  - learning-analytics
  - retention
  - dropout-prevention
  - k12
  - higher-ed
  - workforce
  - equity
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/program/evaluation-analytics/program_learning_analytics_interpreter.md
  - domain-education-teaching/program/curriculum-design/program_remediation_pathway_designer.md
  - domain-education-teaching/program/evaluation-analytics/program_continuous_improvement_cycle.md
---

# Early Warning System Designer

**Objective:** Design an early-warning system (EWS) for identifying at-risk learners — indicator selection, threshold setting, intervention triggers, owner assignment, feedback loops to validate accuracy, and equity safeguards — for K-12 dropout prevention, HE retention, or workforce attrition mitigation.

## When to Use
- ✅ K-12 designing or improving a dropout-prevention EWS
- ✅ HE designing a retention/persistence EWS
- ✅ Workforce training designing an attrition-prevention EWS
- ✅ Auditing an existing EWS for accuracy, equity, and impact
- ❌ Designing remediation pathway (use `teaching_remediation_pathway_designer.md`)
- ❌ Interpreting existing analytics data (use `teaching_learning_analytics_interpreter.md`)

## Inputs Required
- **Sector:** K-12 / HE / workforce
- **Population at risk:** what risk (dropout, course failure, attrition, milestone failure)
- **Available data sources:** SIS, LMS, attendance, assessment, behavioral incidents, financial aid status
- **Existing indicators in use** (if any)
- **Intervention resources:** what supports can be deployed
- **Equity commitments and accreditor/regulatory frame**

## Constraints

**Must:**
- Select indicators based on research evidence (well-known predictors: attendance, course failure in core subjects, behavior incidents for K-12; midterm grades, financial aid, advising attendance for HE)
- Set thresholds with evidence (predictive validity, sensitivity/specificity)
- Pair every indicator-threshold combination with an intervention trigger and owner
- Build feedback loop (does the EWS actually predict; do interventions actually work)
- Address equity (does EWS over-flag or under-flag specific subgroups; bias audit)
- Honor data-privacy regulations (FERPA, GDPR where applicable)
- Avoid surveillance creep

**Must Not:**
- Treat correlation as causation
- Use proxy indicators that encode bias (zip code, school of origin without examination)
- Generate intervention triggers with no resourced response
- Skip equity audit
- Build systems that stigmatize learners without supportive response

## Instructions

1. **Confirm sector, risk, data sources, resources.**

2. **Select indicators.**
   - For K-12 dropout: attendance, course failure in core subjects, behavior referrals (ABC: Attendance, Behavior, Course performance)
   - For HE retention: midterm grades, course attendance/engagement, financial aid hold status, advising attendance, first-generation status flag
   - For workforce: training session attendance, performance metrics, supervisor feedback, employer-stability factors
   - Add other research-supported indicators relevant to the context

3. **Set thresholds.**
   - For each indicator, what value triggers attention
   - Multi-indicator combinations (e.g., "≥2 indicators in red")
   - Severity tiers (yellow, orange, red)

4. **Tie to interventions.**
   - For each threshold tier, the intervention that triggers
   - Who owns the response
   - Time window for action
   - Documentation requirements

5. **Build feedback loops.**
   - Predictive validity: do indicators actually predict the outcome?
   - Intervention effectiveness: do interventions reduce the predicted outcome?
   - Calibration: re-tune thresholds based on data

6. **Equity audit.**
   - Are flagging rates disproportionate by subgroup?
   - Are intervention outcomes equitable?
   - Are indicators encoding bias (e.g., "behavior incidents" reflect discipline disparities)?
   - Monitor and report patterns

7. **Address governance and privacy.**
   - Who sees indicator flags
   - Data-handling rules
   - Learner / family notification policy
   - Right to know / appeal

8. **Avoid surveillance creep.**
   - Indicators serve support, not punishment
   - Data shared only with those needing it for action
   - No use in disciplinary decisions

## Output Format

### Section 1: System Identity
- Sector, risk targeted, population, data sources, intervention resources

### Section 2: Indicator Inventory

| Indicator | Data Source | Research-Evidence Citation | Notes |
|---|---|---|---|

### Section 3: Threshold and Tier Structure

| Indicator | Yellow | Orange | Red | Predictive Validity |
|---|---|---|---|---|

### Section 4: Multi-Indicator Combinations

| Combination | Tier | Action |
|---|---|---|

### Section 5: Intervention Triggers

| Tier | Intervention | Owner | Time Window | Documentation |
|---|---|---|---|---|

### Section 6: Feedback Loops
- Predictive validity monitoring
- Intervention effectiveness monitoring
- Threshold recalibration cadence

### Section 7: Equity Audit

| Subgroup | Flagging Rate | Compared to Population | Intervention Outcomes | Bias Hypothesis |
|---|---|---|---|---|

### Section 8: Governance & Privacy
- Data access controls
- Notification policy
- Right to know / appeal
- Non-disciplinary use

### Section 9: Surveillance-Creep Safeguards
- Use restrictions
- Audit trail
- Sunset reviews

### Section 10: System Audit

| Audit Question | Result |
|---|---|
| Indicators research-supported | Pass / Fail |
| Thresholds evidence-based | Pass / Fail |
| Every trigger has owner + intervention | Pass / Fail |
| Feedback loops built | Pass / Fail |
| Equity audit | Pass / Fail |
| Privacy honored | Pass / Fail |
| Anti-surveillance safeguards | Pass / Fail |

## False-Positive Prevention

| Common Mistake | Why It's Wrong | Correct Approach |
|---|---|---|
| Indicators without evidence | Predict noise, not risk | Use research-supported indicators |
| Thresholds set by intuition | Poor sensitivity/specificity | Set based on predictive validity data |
| Triggers without resourced intervention | Identification without response | Every trigger has owner + intervention + time window |
| No equity audit | Reproduces disparate impact | Disaggregate; bias-check indicators |
| Indicators encoding bias | E.g., behavior referrals reflect discipline disparities | Examine indicator-level bias; consider alternatives |
| No feedback loop | System drifts; never improves | Monitor predictive validity + intervention effectiveness |
| Privacy negligence | Legal and ethical exposure | Honor FERPA/GDPR; access controls |
| Surveillance creep | Damages trust; punitive shift | Hard restrictions on disciplinary use |

## Verification Checklist

- [ ] Indicators research-supported with citations
- [ ] Thresholds evidence-based with predictive validity
- [ ] Every threshold-tier paired with intervention + owner + time
- [ ] Feedback loops for validity and effectiveness
- [ ] Equity audit
- [ ] Privacy and governance
- [ ] Surveillance-creep safeguards
- [ ] Asset-based framing (support, not punishment)
