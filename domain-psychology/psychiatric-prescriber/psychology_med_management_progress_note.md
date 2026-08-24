---
title: "Medication Management Progress Note (E&M + Psychotherapy Add-On)"
category: psychology/psychiatric-prescriber
description: "Draft an E&M-style medication management follow-up note (99213/99214, with optional 90833 psychotherapy add-on) with interval history, target-symptom and side-effect tracking, focused MSE, MDM justification of the E&M level, and medication decisions."
techniques:
  - DS-02
  - DT-01
  - CM-01
  - QA-04
  - ST-04
difficulty: intermediate
intended_use: model-testing
tags:
  - medication-management
  - E&M
  - 99214
  - 90833
  - progress-note
  - side-effects
  - AIMS
updated: "2026-06-08"
related_prompts:
  - domain-psychology/psychiatric-prescriber/psychology_initial_psych_eval_drafter.md
  - domain-psychology/psychiatric-prescriber/psychology_psychotropic_taper_plan.md
  - domain-psychology/treatment-planning/psychology_measurement_based_care_plan.md
  - domain-psychology/risk-crisis/psychology_columbia_suicide_risk_assessment.md
---

# Medication Management Progress Note (E&M + Psychotherapy Add-On)

## Objective

Generate a medication management follow-up note authored by a prescriber, structured to support an **evaluation & management (E&M)** code (99212–99215) selected by **medical decision-making (MDM)** under the 2021+ E&M guidelines, with an optional psychotherapy **add-on** (90833 for ≥ 16 min, 90836 for ≥ 38 min, 90838 for ≥ 53 min) when time-separable psychotherapy is provided. The note must document interval history, target-symptom tracking against measures, side-effect and abnormal-movement screening, adherence, labs, a focused MSE, the MDM elements that justify the chosen E&M level, and the medication decision with rationale.

## When to Use

- Routine return visits for ongoing pharmacologic management.
- Visits where both medication management and a discrete psychotherapy service are rendered (split E&M + add-on).
- Any follow-up where the E&M level must be defensible under audit by MDM.

## Inputs / Context Required

- **Interval since last visit** and current medication regimen (agent, dose, schedule, last change date).
- **Target symptoms** and current measure scores (PHQ-9, GAD-7, PCL-5, etc.) vs. prior/baseline.
- **Side effects reported** and any new somatic complaints; **adherence** (self-report, pill count, refill data, blood levels).
- **Abnormal-movement screen** (AIMS) status for patients on antipsychotics.
- **Labs/levels** drawn since last visit (e.g., lithium level, valproate level, metabolic panel, lipids, HbA1c, TSH, prolactin, EKG/QTc).
- **Risk update**: current SI/HI/self-harm.
- **Whether discrete psychotherapy was provided** and its minutes (separate from E&M time).
- `[clinician input required: which problems were addressed today and their status (stable/worsening/improving)]`
- `[clinician input required: total E&M time if time-based coding is used instead of MDM]`

## Constraints

### Must

- Output sections in order: **Visit Header**, **Interval History**, **Target-Symptom & Measure Tracking**, **Side Effects / Tolerability**, **Abnormal-Movement (AIMS) Screen**, **Adherence**, **Labs / Levels**, **Focused MSE**, **Risk Update**, **Assessment (problems + status)**, **Medication Decision & Plan**, **Psychotherapy Add-On (if provided)**, **MDM / E&M Level Justification**, **Billing**, **Follow-Up**, **Signature**.
- Justify the E&M level by the three MDM elements: (1) number/complexity of problems addressed, (2) amount/complexity of data reviewed (labs, levels, collateral, prior records), (3) risk of complications/morbidity (medication management with monitoring counts as moderate risk; controlled substances, suicidality, or hospitalization decision can raise it).
- For every medication decision: name agent (generic), dose change with direction and amount, and rationale (efficacy, tolerability, level, target-symptom trajectory).
- Document an AIMS screen when any antipsychotic is on board; state cadence (baseline, then per local protocol, e.g., every 3–6 months).
- If a psychotherapy add-on is billed, document that the psychotherapy time is **separate** from E&M time and meets the add-on's minute threshold.
- Update risk every visit; do not carry forward "no SI" without a current statement.
- Reference monitoring tied to the agent class (e.g., metabolic monitoring for second-generation antipsychotics; level + renal/thyroid for lithium).

### Must Not

- Do not bill 99214 by default; the level must follow from documented MDM (or total time).
- Do not bill a psychotherapy add-on without separately documented psychotherapy minutes and content.
- Do not record a dose change without direction, amount, and rationale.
- Do not omit the AIMS screen for antipsychotic-treated patients.
- Do not fabricate labs or levels; flag pending/needed labs as `[clinician input required: ...]`.

## Instructions

1. Build the **Visit Header** (date, regimen, last change date, visit purpose).
2. Write the **Interval History**: changes since last visit, stressors, response.
3. Complete **Target-Symptom & Measure Tracking**: cite measure scores vs. prior; note MCID-level change if relevant.
4. Document **Side Effects / Tolerability** and any new somatic symptoms.
5. Complete the **AIMS Screen** if an antipsychotic is on board (movements rated; positive findings → action).
6. Document **Adherence** and **Labs/Levels** (interpret levels against therapeutic range).
7. Record a **Focused MSE** (appearance, mood/affect, thought process/content, SI/HI, cognition, insight/judgment).
8. Write a **Risk Update**.
9. Write the **Assessment**: list problems addressed and status (stable/improving/worsening) — this feeds MDM problem count.
10. State the **Medication Decision & Plan**: continue/increase/decrease/switch/augment/taper, with agent, dose, and rationale; note monitoring.
11. If psychotherapy was provided, complete the **Add-On** block with minutes and modality.
12. Complete the **MDM/E&M Level Justification** mapping the three elements to a level; or document total time if time-based.
13. Complete **Billing**, **Follow-Up**, **Signature**. Run verification.

## Output Format

```
=== MEDICATION MANAGEMENT PROGRESS NOTE ===

VISIT HEADER
Patient: [Initials/MRN]   Date: [YYYY-MM-DD]   Interval since last visit: [..]
Current regimen: [agent(s), dose, schedule]   Last change: [date/what]
Place of service: [11 | 02/10 telehealth]   Prescriber: [Name, credentials]

INTERVAL HISTORY
[Changes, stressors, adherence narrative, response since last visit.]

TARGET-SYMPTOM & MEASURE TRACKING
| Measure | Today | Last visit | Baseline | Trajectory |
|---------|-------|------------|----------|------------|
| PHQ-9   | [..]  | [..]       | [..]     | [improving/plateau/worsening] |
| GAD-7   | [..]  | [..]       | [..]     | [..] |
Target symptoms: [sleep, energy, panic frequency, etc. — quantified where possible]

SIDE EFFECTS / TOLERABILITY
[Reported side effects; new somatic complaints; severity; action.]

ABNORMAL-MOVEMENT (AIMS) SCREEN  [if antipsychotic on board]
AIMS performed: [Yes/No]   Findings: [none / describe]   Cadence: [baseline then q3–6 mo]
Action if positive: [reduce/switch/consider VMAT2 inhibitor; document]

ADHERENCE
[Self-report / pill count / refill data / blood level corroboration.]

LABS / LEVELS
[Lithium level X (therapeutic 0.6–1.2 mEq/L) | valproate level X (50–125 µg/mL) |
metabolic/lipids/HbA1c | TSH | prolactin | QTc — interpret each vs. reference.]
Pending/needed: [clinician input required if applicable]

FOCUSED MSE
Appearance/behavior: [..] | Mood: "[..]" | Affect: [..] | Thought process/content: [SI/HI] |
Cognition: [..] | Insight/Judgment: [..]

RISK UPDATE
SI: [none/passive/active] | HI: [..] | Self-harm: [..] | Means access: [..] | Risk level: [..]

ASSESSMENT (problems addressed + status)
1. [Dx — status: stable/improving/worsening]
2. [Dx — status: ...]

MEDICATION DECISION & PLAN
Decision: [Continue / Increase / Decrease / Switch / Augment / Taper]
Agent (generic): [..]   Dose change: [from → to, direction + amount]
Rationale: [efficacy/tolerability/level/trajectory]
Monitoring ordered: [labs/EKG/weight/AIMS schedule]
Other: [taper logic if applicable — see psychology_psychotropic_taper_plan.md]

PSYCHOTHERAPY ADD-ON  [if provided]
Modality: [supportive / CBT / IPT element]   Psychotherapy minutes (separate from E&M): [≥16/≥38/≥53]
Add-on code: [90833 / 90836 / 90838]   Content: [brief summary]

MDM / E&M LEVEL JUSTIFICATION
Problems addressed: [count + complexity → e.g., "2 chronic illnesses, 1 worsening"]
Data reviewed: [labs/levels/collateral/records → element met]
Risk: [moderate: prescription drug management | higher: controlled substance / suicidality / hospitalization]
Selected level: [99212 / 99213 / 99214 / 99215]  — by [MDM | total time = __ min]

BILLING
E&M: [99213/99214/...]   Psychotherapy add-on: [90833/90836/90838 if applicable]
Pharmacologic management captured within E&M (90863 not separately billed with E&M).
ICD-10: [codes]

FOLLOW-UP
Next visit: [interval]   Labs to recheck: [..]   Risk-reassessment hook: [re-screen at next visit / on dose change]

SIGNATURE
Prescriber: __________________  Date: ________
Supervising / collaborating prescriber co-sign (if applicable): __________  Date: ________
```

## Verification

- [ ] All sections present in order.
- [ ] Target symptoms tracked against measure scores with trajectory.
- [ ] Side-effect/tolerability review documented.
- [ ] AIMS screen documented if any antipsychotic is on board.
- [ ] Adherence and labs/levels interpreted against reference ranges.
- [ ] Risk updated with a current statement (not carried forward).
- [ ] Each medication decision states agent, dose direction/amount, and rationale.
- [ ] Monitoring tied to the agent class.
- [ ] E&M level justified by the three MDM elements (or total time).
- [ ] Psychotherapy add-on, if billed, has separate documented minutes and content.
- [ ] Billing block correct; 90863 not double-billed with E&M.
- [ ] Follow-up + risk-reassessment hook present; co-sign where applicable.
- [ ] Nothing fabricated; pending labs flagged with `[clinician input required]`.
