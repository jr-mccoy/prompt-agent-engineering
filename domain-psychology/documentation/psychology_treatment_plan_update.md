---
title: "Treatment Plan Update / 90-Day Review Drafter"
category: psychology/documentation
description: "Generate a treatment-plan update or 90-day review documenting progress on each objective, justifying continued care, and modifying the plan with audit-grade rationale."
techniques:
  - ST-04
  - DT-02
  - DS-02
  - DS-04
  - QA-04
  - CM-02
difficulty: advanced
tags:
  - treatment-plan-review
  - 90-day-review
  - utilization-review
  - medical-necessity
  - measurement-based-care
intended_use: model-testing
updated: "2026-05-08"
related_prompts:
  - domain-psychology/documentation/psychology_initial_treatment_plan.md
  - domain-psychology/documentation/psychology_discharge_summary.md
  - domain-psychology/measurement-based-care
---

# Treatment Plan Update / 90-Day Review Drafter

## Objective

Produce a structured treatment-plan update that:

1. Reports progress on every active objective with measurement evidence (outcome-measure trajectories, behavioral counts, attendance, observable change).
2. Justifies continued care with explicit medical-necessity reasoning per active diagnosis.
3. Modifies the plan: closes met objectives, reformulates partial-progress objectives, retires objectives that aren't working, and adds new objectives only when warranted by current data.
4. Documents level-of-care decision (continue / step up / step down / discharge) with rationale.

## When to Use

- Standard 90-day plan review interval.
- Shorter intervals when level-of-care change is contemplated or when a payer requires quarterly utilization review.
- Whenever a clinically significant event (ED visit, medication change, life event, plateau, regression) prompts a plan revision.

## Inputs / Context

- Original treatment plan with verbatim objectives and interventions.
- Outcome-measure data: scores at intake, mid-treatment, and current.
- Attendance, no-show, cancellation pattern.
- Risk events during the review period (ED visits, hospitalizations, NSSI, suicidal crises, substance relapses).
- Coordination updates (PCP, prescriber, school, family).
- Clinician's qualitative observations of progress.
- Client's self-reported sense of progress and goals for next interval.
- Medication changes during the review period.
- Reviewer / supervisor for sign-off.

## Constraints

### Must

- Output the following labeled sections in order: **Review Period**, **Outcome Measure Trajectories**, **Attendance & Engagement**, **Risk Events**, **Per-Objective Progress**, **Coordination Updates**, **Plan Modifications**, **Updated Problem / Goal / Objective List**, **Continued-Care Justification**, **Level-of-Care Decision**, **Plan Review Schedule**, **Signatures**.
- For every objective, classify status as **Met / Partial Progress / No Progress / Worsening / Modified / Discontinued**, with measurement evidence supporting the classification.
- Outcome-measure trajectories include intake, prior-review, and current scores in a table; comment on clinically meaningful change (e.g., PHQ-9 change ≥ 5 = clinically meaningful improvement; reliable change index where applicable).
- Continued-care justification is per active diagnosis, citing current symptoms, functional impairment, and the specific interventions still required.
- Plan modifications are explicitly listed (removed / added / revised) so the change history is traceable.
- Level-of-care decision uses LOCUS / CALOCUS / ASAM (for SUD) or comparable framework with rationale.
- Reviewer / supervisor signature line.

### Must Not

- Do not mark objectives "Met" without measurement evidence; "Met by clinical impression" is insufficient.
- Do not silently rewrite goals from the prior plan; if you change a goal, list it under Plan Modifications with rationale.
- Do not justify continued care with diagnosis alone; current functional impairment must be documented.
- Do not conceal regression or risk events; document them and adjust the plan.
- Do not fabricate scores or attendance data; flag missing inputs.

## Instructions

1. Compile outcome-measure trajectory across intake → review points → current.
2. Compile attendance: scheduled, attended, no-show, late-cancelled, with rate.
3. List any risk events with dates, level of care touched, outcome.
4. For each objective in the original plan: state verbatim text, current status, measurement evidence, recommendation (close / continue / modify / discontinue).
5. Document coordination updates per external party.
6. Compile Plan Modifications: explicitly list closed objectives, added objectives, revised objectives with old vs new wording.
7. Restate the Updated Problem / Goal / Objective list (same structure as initial plan) so progress notes can quote it forward.
8. Write Continued-Care Justification per active diagnosis.
9. Make Level-of-Care Decision with framework name and rationale.
10. Schedule next plan review.
11. Run verification.

## Output Format

```
=== TREATMENT PLAN UPDATE / 90-DAY REVIEW ===

Client: [Initials/MRN]
Review period: [YYYY-MM-DD] to [YYYY-MM-DD]    Sessions in period: [N]
Plan effective date: [YYYY-MM-DD]    Prior review: [YYYY-MM-DD]    This review: [YYYY-MM-DD]
Next review: [YYYY-MM-DD]

OUTCOME MEASURE TRAJECTORIES
| Measure | Intake | Prior review | Current | Change | Clinically meaningful? |
|---------|--------|--------------|---------|--------|------------------------|
| PHQ-9   | X      | X            | X       | ±X     | Yes / No |
| GAD-7   | X      | X            | X       | ±X     | Yes / No |
| PCL-5   | X      | X            | X       | ±X     | Yes / No |
| C-SSRS  | [endorsements] | [endorsements] | [endorsements] | [direction] | [Yes/No] |
| [Other] | X      | X            | X       | ±X     | Yes / No |

ATTENDANCE & ENGAGEMENT
Scheduled: [N]    Attended: [N]    No-show: [N]    Late cancel: [N]    Attendance rate: [%]
Engagement notes: [Homework completion %, in-session participation, openness to feedback.]

RISK EVENTS DURING PERIOD
- [Date — event — level of care touched — outcome — plan implications]
- [If none: "No risk events during review period; SI/HI/NSSI screened each session, denied throughout."]

PER-OBJECTIVE PROGRESS
Objective #[ID] (verbatim): "[...]"
   Status: [Met / Partial / None / Worsening / Modified / Discontinued]
   Evidence: [Specific measurement data — score change, behavior count, observation.]
   Recommendation: [Close / Continue / Modify / Discontinue].
   Rationale: [...]

[Repeat for every objective.]

COORDINATION UPDATES
- PCP: [Last contact date, content, next contact plan.]
- Prescriber: [Med changes during period; current regimen; next visit.]
- School / Case manager / Family: [...]

PLAN MODIFICATIONS
Closed (objectives met):
- [ID + verbatim text + close date]
Added (new objectives):
- [New objective with SMART criteria + tied to which problem + start date + target date.]
Revised:
- [ID — Old wording → New wording — Rationale.]
Discontinued (without meeting):
- [ID — Reason for discontinuation.]

UPDATED PROBLEM / GOAL / OBJECTIVE LIST
[Restate the post-modification plan in the same structured form as the initial plan, so subsequent progress notes can quote forward.]

CONTINUED-CARE JUSTIFICATION
Per active diagnosis:
- [F##.## Descriptor]: Current symptoms include [specifics]; functional impairment in [domains]; interventions still required: [named techniques]; expected duration: [interval]; reason care cannot be discontinued: [...].
- [Repeat per active dx.]

LEVEL-OF-CARE DECISION
Framework: [LOCUS / CALOCUS / ASAM / clinical].
Decision: [Continue current LOC / Step up / Step down / Discharge].
Rationale: [Specific data supporting the LOC decision.]

PLAN REVIEW SCHEDULE
Next review: [YYYY-MM-DD]    Reviewer: [Supervisor name, credentials]

SIGNATURES
Client: ____________________________  Date: ___________
Guardian (if applicable): __________  Date: ___________
Primary clinician: __________________  Date: ___________
Reviewer / Supervisor: ______________  Date: ___________
```

## Verification

- [ ] All labeled sections present in order.
- [ ] Outcome-measure trajectory table includes intake, prior, current, change, clinically-meaningful flag.
- [ ] Attendance rate computed and engagement noted.
- [ ] Risk events documented (or explicit "none + how risk was screened").
- [ ] Every objective from the prior plan has a status, evidence, recommendation, rationale.
- [ ] Plan Modifications list closed / added / revised / discontinued objectives.
- [ ] Updated Problem/Goal/Objective list restated for forward reference.
- [ ] Continued-care justification present per active diagnosis with current functional impairment.
- [ ] LOC decision uses a named framework with rationale.
- [ ] Reviewer / supervisor signature line present.
- [ ] Gaps flagged; nothing fabricated.
