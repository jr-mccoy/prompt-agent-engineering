---
title: "High-School Graduation Tracker & Intervention Planner"
category: education-teaching/instructor/student-support
description: "Track a high-school student's progress toward graduation requirements, surface gaps, and design specific interventions — anchored on the user's jurisdiction's requirements (which the user supplies)."
techniques:
  - ST-02
  - CM-02
  - DS-01
  - OC-01
  - QA-01
difficulty: intermediate
tags:
  - school-counseling
  - advising
  - graduation
  - high-school
  - intervention
  - student-support
updated: "2026-05-09"
related_prompts:
  - domain-education-teaching/instructor/student-support/teaching_course_selection_advising.md
  - domain-education-teaching/instructor/student-support/teaching_iep_goal_writer.md
  - domain-education-teaching/instructor/response-cycle/teaching_reteach_intervention_planner.md
---

# High-School Graduation Tracker & Intervention Planner

## Objective

Track an individual high-school student's progress toward graduation, surface what's done / in progress / not yet attempted / off track, and design specific interventions per gap. The prompt anchors on the user's jurisdiction's graduation requirements — which the user must supply, since requirements vary by state, province, country, district, and year of enrollment.

> **Important:** This prompt does not assert specific graduation requirements for any specific jurisdiction. Requirements differ by state/province, district, year of enrollment, diploma type (standard / honors / IB / CTE / alternative), and pathway. The user must supply the controlling requirements list before tracking begins.

## When to Use

- Counselor / advisor running graduation audits each semester or quarter
- Student-and-family meeting to plan remaining time
- Off-track student needing intervention plan
- Transfer student whose prior credits must be evaluated
- Senior-year final audit before commencement

## When NOT to Use

- Course selection for a single term — use `advising_course_selection_advisor.md`
- College / post-secondary planning — different scope
- Special-education IEP-driven graduation — incorporate IEP team; this prompt covers academic progress only

---

## Inputs Needed

- **Student identifier (de-identified for testing):** [...]
- **Grade level & expected graduation year:** [...]
- **Diploma type / pathway:** [Standard / honors / IB / CTE / alternative — as defined in jurisdiction]
- **Authoritative graduation requirements (user-supplied):** [Paste or summarize: required credits per subject, required courses, exit exams, service hours, capstone, etc.]
- **Transcript data:** [Courses taken, credits earned, grades, in-progress, planned]
- **Other requirements progress:** [Exit exams, service hours, capstone, financial-aid forms if required for diploma]
- **Special considerations:** [504 / IEP, ELL, recent transfer, credit recovery history, attendance flags]
- **Available intervention resources:** [Credit recovery, summer school, tutoring, dual enrollment, alternative path]
- **Student & family preferences:** [Path priorities — diploma type, post-secondary, employment]

---

## Instructions

### Step 1: Confirm Authoritative Requirements

Before audit:
- [ ] User has supplied the controlling graduation requirements
- [ ] User has confirmed which year-of-enrollment cohort the student belongs to (requirements often change by cohort)
- [ ] User has confirmed diploma pathway

If any element is uncertain, **stop and request it**. The prompt does not generate jurisdiction-specific requirements from training data.

### Step 2: Build the Requirements Checklist

From the authoritative source, create a structured table:

| Requirement category | Required (per source) | Earned | In progress | Planned | Gap |
|----------------------|------------------------|--------|--------------|---------|-----|
| English / Language Arts | [n credits] | | | | |
| Math | [n credits, specified courses] | | | | |
| Science | [n credits, specified labs] | | | | |
| Social Studies | [n credits, specified courses] | | | | |
| World Language | [n credits / requirement] | | | | |
| Physical Education / Health | [n credits] | | | | |
| Fine / Performing Arts | [n credits] | | | | |
| Electives | [n credits] | | | | |
| **Total credits** | [n] | | | | |
| Exit / state exams | [list] | | | | |
| Service hours | [n hours, if required] | | | | |
| Capstone / senior project | [if required] | | | | |
| Financial-aid completion | [if required] | | | | |
| Other (per source) | [...] | | | | |

### Step 3: Categorize Each Gap

For each gap, classify:

| Classification | Meaning | Default response |
|----------------|---------|-------------------|
| **On track** | Will be addressed by current/planned schedule | Monitor |
| **At risk** | Possible to address, but tight | Plan ahead |
| **Off track** | Will not be addressed without intervention | Intervene now |
| **Critical** | Will block graduation absent immediate action | Escalate now |

### Step 4: Per-Gap Intervention Design

For each off-track or critical gap, design:

```
GAP: [Specific requirement not on track]
SEVERITY: [At risk / Off track / Critical]
WHY: [Cause — failed course, attendance, transfer credit not posted, exam not taken, etc.]
OPTIONS:
  Option A: [E.g., credit recovery summer]
    Cost: [Time / money / opportunity cost]
    Fit: [How well it works for this student]
    Timeline: [When it must start, when it completes]
  Option B: [E.g., online dual-enrollment course]
    Cost / Fit / Timeline
  Option C: [E.g., schedule change next term]
RECOMMENDATION: [Top option + why]
DECISION OWNER: [Student, family, counselor — who decides]
NEXT ACTION: [Concrete next step + by when]
```

### Step 5: Path Comparison Across Diploma Types

If the student is at risk of one diploma type, compare alternates from the user-supplied requirements:

| Diploma type | Status | Pros for this student | Cons | Decision impact |
|--------------|--------|------------------------|------|-----------------|
| Current target | [On / off track] | | | |
| Alternative path | [Status if shifted] | | | |
| Minimum path | [Status if shifted] | | | |

This is a counseling conversation, not a downgrade. Surface options; the family decides.

### Step 6: Time-to-Graduation Math

Confirm:
- Credits remaining
- Terms remaining at expected pace
- Average credits earned per term (historical)
- Required credits per term to finish on time
- If gap exceeds terms remaining: how many extra terms or what acceleration is needed

Show the math, not just the conclusion.

### Step 7: Risk-Factor Audit

Beyond credits, scan:

- Attendance (chronic absenteeism is graduation's strongest predictor)
- GPA trend (declining vs. recovering)
- Course failure pattern (subject-specific or general)
- Disengagement signals (clubs dropped, schedule churn)
- Life-event flags (housing instability, caregiving, work hours, mental health)

Each elevates intervention priority and may shift options.

### Step 8: Family Conversation Plan

Surface in the meeting:
- Current status (specific, not vague)
- Concrete options (with tradeoffs, not opinions)
- Decisions needed and by when
- What student commits to do
- What family supports
- What school provides

Output a one-page summary the family can take home.

### Step 9: Coordination Plan

Most interventions touch multiple staff:

| Action | Owner | Coordination needed |
|--------|-------|---------------------|
| Schedule change | Counselor | Registrar |
| Credit recovery enrollment | Counselor + student | Online program provider, parent signature |
| Tutoring | Teacher / center | Counselor referral |
| 504 / IEP review | Case manager | IEP team, parent |
| Truancy intervention | Attendance team | Parent, teacher, possibly community partner |

### Step 10: Documentation & Privacy

- Document audit findings in the SIS or counseling notes per district policy
- Share only what's necessary with each staff member
- FERPA / equivalent privacy compliance
- De-identify any examples used in training contexts

### Step 11: Follow-Up Cadence

- Next audit date
- Mid-term check on each intervention's progress
- Trigger criteria to escalate (e.g., another course fail, attendance below threshold)
- End-of-year wrap

---

## Output Format

1. Authoritative-requirements confirmation note
2. Requirements checklist with earned/in-progress/planned/gap
3. Gap classification per requirement
4. Per-gap intervention design block
5. Path comparison (if alternates relevant)
6. Time-to-graduation math
7. Risk-factor audit
8. One-page family conversation summary
9. Coordination plan
10. Documentation & privacy notes
11. Follow-up cadence

---

## False-Positive Prevention

❌ **DON'T:**
- Cite credit requirements the user didn't provide — invented requirements harm students
- Reduce a student to a credit balance — risk factors and life context matter
- Recommend diploma downgrade without family choice
- Skip attendance and engagement signals
- Assume one-size intervention works for all gaps
- Document beyond what's necessary or share beyond need-to-know

✅ **DO:**
- Anchor on user-supplied requirements
- Classify gaps by severity
- Design per-gap interventions with options
- Show time-to-graduation math
- Audit risk factors beyond credits
- Coordinate with named owners
- Plan follow-up

---

## Quality Indicators

- [ ] Authoritative source confirmed
- [ ] Full requirements checklist completed
- [ ] Each gap classified
- [ ] Each off-track/critical gap has intervention design
- [ ] Time-to-graduation math shown
- [ ] Risk-factor audit completed
- [ ] Family conversation summary ready
- [ ] Follow-up scheduled

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **ST-02** | Source → checklist → classify → intervene → coordinate → follow-up pipeline. |
| **CM-02** | Constrains content to user-supplied requirements; refuses to invent jurisdictional rules. |
| **DS-01** | Counselor-frame (gap classification, intervention design with options) drives output. |
| **OC-01** | Per-gap block template enforces actionable, paste-ready output. |
| **QA-01** | Risk audit, time math, and follow-up cadence verify the plan against reality. |
