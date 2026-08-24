---
title: "Discharge Summary Drafter"
category: psychology/documentation
description: "Draft an outpatient or program discharge summary documenting course of treatment, gains, residual concerns, aftercare plan, and prognosis."
techniques:
  - ST-04
  - DT-02
  - DS-04
  - QA-04
  - CM-02
difficulty: intermediate
tags:
  - discharge-summary
  - episode-of-care-closeout
  - aftercare-plan
  - prognosis
intended_use: model-testing
updated: "2026-05-08"
related_prompts:
  - domain-psychology/documentation/psychology_termination_summary.md
  - domain-psychology/documentation/psychology_treatment_plan_update.md
  - domain-psychology/care-coordination
---

# Discharge Summary Drafter

## Objective

Produce a discharge summary that closes out an episode of care for an outpatient practice, IOP/PHP, residential, or inpatient setting. The summary must:

1. Document the full episode: dates, modalities, providers, diagnoses, interventions used, outcome-measure trajectories.
2. State the **reason for discharge** clearly: planned completion, mutual agreement, step-up or step-down, administrative discharge, AMA, no-show closeout, death.
3. Compare baseline and current status across symptoms, function, risk.
4. Specify the **aftercare plan** with named providers, scheduled appointments, medication continuity, crisis resources.
5. State **prognosis** with rationale.

## When to Use

- Closing an episode of care at any level.
- Required for any discharge from a program with a formal LOC.
- Required when transferring care to a new provider or stepping the client up/down.

## Inputs / Context

- Episode metadata: admission date, discharge date, primary clinician, prescriber, treatment-plan history.
- Final diagnoses (ICD-10) including any added or removed during the episode.
- Outcome-measure trajectory: intake, key review points, final.
- Attendance summary: scheduled, attended, no-show, late-cancel.
- Reason for discharge.
- Aftercare specifics: receiving provider, first appointment date, medication regimen at discharge, prescription continuity (last fill, next refill), crisis resources, ROI status with receiving provider.
- Prognostic indicators (treatment response, insight, supports, comorbidities).
- Final risk reassessment.
- Client's preferred language for the summary if shared with them.

## Constraints

### Must

- Output the following labeled sections in order: **Episode Metadata**, **Final Diagnoses**, **Reason for Discharge**, **Course of Treatment**, **Outcome Measure Trajectory**, **Attendance Summary**, **Functional Outcomes**, **Final Risk Reassessment**, **Medications at Discharge**, **Aftercare Plan**, **Crisis Resources**, **Prognosis**, **Outstanding Items / Recommendations**, **Signatures**.
- Reason for discharge uses one of the standard categories (Planned completion / Mutual agreement / Step up / Step down / Administrative / AMA / Lost to follow-up / Death / Transfer of care) plus a 1–2 sentence narrative.
- Outcome-measure trajectory presented as a table with intake, key intermediate points, and final scores; comment on clinically meaningful change per measure.
- Functional outcomes include change in work / school / relationships / self-care / ADLs / substance use as relevant.
- Medications at discharge include each agent, dose, frequency, last fill, next refill, prescriber, allergies confirmed.
- Aftercare plan includes named receiving provider, scheduled date/time of first appointment, contact info, ROI status, and contingency if appointment is missed.
- Crisis resources documented (988, local crisis line, walk-in clinic, ED).
- Prognosis is one of Excellent / Good / Fair / Guarded / Poor with rationale; do not declare prognosis without rationale.

### Must Not

- Do not write "client did well in treatment" without measurement and functional evidence.
- Do not omit reason for discharge or hide an AMA / lost-to-follow-up under "planned completion."
- Do not list aftercare without a named receiving provider and at least a tentative first-appointment date.
- Do not omit a final risk reassessment.
- Do not fabricate; flag missing inputs.

## Instructions

1. Compile episode metadata.
2. State final diagnoses (and changes from intake).
3. Categorize reason for discharge with brief narrative.
4. Summarize the course of treatment in 1–2 paragraphs: what was worked on, modalities used, key turning points.
5. Build outcome-measure trajectory table.
6. Compute attendance summary.
7. Document functional outcomes per domain.
8. Conduct final risk reassessment with explicit stratification.
9. List medications at discharge with refill / continuity details.
10. Specify aftercare plan with named provider and first appointment.
11. List crisis resources and confirm client has them in writing.
12. Assign and justify prognosis.
13. List outstanding items / recommendations for the receiving provider.
14. Run verification.

## Output Format

```
=== DISCHARGE SUMMARY ===

EPISODE METADATA
Client: [Initials/MRN]    DOB: [...]
Episode of care: [Admission YYYY-MM-DD] – [Discharge YYYY-MM-DD]    Total sessions: [N]
Level of care: [Outpatient / IOP / PHP / Residential / Inpatient]
Primary clinician: [name, credentials]    Prescriber: [name, credentials]
Other team members: [...]

FINAL DIAGNOSES
- [F##.##] [Descriptor] (active at discharge)
- [F##.##] [Descriptor] (in partial remission)
- [F##.##] [Descriptor] (resolved during episode)
- Z-codes: [...]

REASON FOR DISCHARGE
Category: [Planned completion / Mutual agreement / Step up / Step down / Administrative / AMA / Lost to follow-up / Death / Transfer of care]
Narrative: [1–2 sentences.]

COURSE OF TREATMENT
[1–2 paragraphs: what was worked on, modalities, key turning points, periods of plateau or regression and how they were addressed.]

OUTCOME MEASURE TRAJECTORY
| Measure | Intake | [Mid pt] | Final | Change | Clinically meaningful? |
|---------|--------|----------|-------|--------|------------------------|
| PHQ-9   | X      | X        | X     | ±X     | Yes / No |
| GAD-7   | X      | X        | X     | ±X     | Yes / No |
| [Other] | X      | X        | X     | ±X     | Yes / No |

ATTENDANCE SUMMARY
Scheduled: [N]    Attended: [N]    No-show: [N]    Late cancel: [N]    Rate: [%]

FUNCTIONAL OUTCOMES
- Work / school: [change]
- Relationships: [change]
- Self-care / ADLs: [change]
- Substance use: [change]
- Other relevant domains: [change]

FINAL RISK REASSESSMENT
SI: [denied / passive / active with-or-without plan/intent/means].
HI: [...]
NSSI: [...]
Substance: [last use, current pattern, risk].
Stratification: [Low / Moderate / High] with rationale.
Safety plan at discharge: [Stanley-Brown plan dated YYYY-MM-DD provided / declined].
Lethal-means status: [Firearms removed/secured | Medications secured | n/a].

MEDICATIONS AT DISCHARGE
| Medication | Dose | Frequency | Last fill | Next refill | Prescriber |
|------------|------|-----------|-----------|-------------|------------|
| [Name]     | [...] | [...]    | [Date]    | [Date]      | [Name]     |
Allergies confirmed: [...]
Medication reconciliation completed with client/family: [Yes / No, reason].

AFTERCARE PLAN
Receiving provider: [Name, role, agency, contact info]
First appointment: [Date / Time / Modality]
ROI in place: [Yes / No]
Records sent: [Date sent / Method]
Continuity of meds: [Plan for prescription continuity until first appointment]
Contingency: [What client / family does if first appointment is missed or cannot be scheduled.]

CRISIS RESOURCES
- 988 Suicide & Crisis Lifeline (call / text / chat)
- Local crisis line / mobile crisis team: [...]
- Walk-in crisis clinic: [...]
- Nearest ED: [...]
- Client confirmed receipt of resources in writing: [Yes / No]

PROGNOSIS
[Excellent / Good / Fair / Guarded / Poor]
Rationale: [Treatment response, insight, supports, comorbidities, adherence trajectory.]

OUTSTANDING ITEMS / RECOMMENDATIONS FOR RECEIVING PROVIDER
- [Specific items: e.g., "PCL-5 trended down but trauma processing not yet completed; recommend phase-2 trauma work after 4–6 sessions of stabilization with new provider."]
- [...]

SIGNATURES
Primary clinician: __________________  Date: ___________
Reviewer / Supervisor: ______________  Date: ___________
Client (acknowledgment of receipt): __  Date: ___________
```

## Verification

- [ ] All labeled sections present and in order.
- [ ] Reason for discharge categorized + narrative.
- [ ] Outcome-measure trajectory table with clinically-meaningful flags.
- [ ] Functional outcomes documented per relevant domain.
- [ ] Final risk reassessment with stratification + safety plan status + lethal-means status.
- [ ] Medications at discharge with refill / continuity plan.
- [ ] Aftercare plan names a receiving provider and first appointment date.
- [ ] Crisis resources documented + acknowledgment of receipt.
- [ ] Prognosis assigned with rationale.
- [ ] Outstanding items present for receiving provider.
- [ ] Gaps flagged; nothing fabricated.
