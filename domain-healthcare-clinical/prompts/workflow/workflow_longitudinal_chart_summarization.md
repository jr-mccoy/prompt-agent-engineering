---
title: "Longitudinal Chart Summarization"
category: domain-healthcare-clinical/workflow
description: "Condense a multi-year, multi-encounter chart into a prioritized clinical synopsis a clinician can read in two minutes before seeing the patient."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - DS-02
difficulty: advanced
tags:
  - workflow
  - chart-summarization
  - ehr
  - handoff
updated: "2026-06-19"
---

## Objective

Take a sprawling longitudinal record — years of notes, labs, imaging, medication changes, hospitalizations, specialist input — and produce a single prioritized synopsis that lets a clinician who has never met the patient understand who they are, what is driving their care, and what is currently unresolved. Output is a structured summary that foregrounds active problems and decision-relevant history and suppresses noise.

## Inputs

- The chart material: progress notes, discharge summaries, consult notes, problem list, medication list, lab and imaging history, procedure history (paste or reference what is available)
- Reason the summary is needed: new-patient handoff, transfer of care, inpatient admission of an outside patient, pre-op review, prior-auth/appeal, second opinion
- Time horizon of interest: entire record vs. last N years vs. since a specific event
- Audience: PCP, hospitalist, specialist, covering clinician — calibrates what counts as relevant

## Role

Senior attending picking up an unfamiliar complex patient, building the mental model you would want signed out to you.

## Reasoning Steps

1. **Establish the one-line identity.** Age, sex, dominant chronic conditions, functional/social baseline (lives alone, dialysis-dependent, etc.). This is the anchor every downstream reader needs first.

2. **Separate active from resolved/historical.** An active problem changes current decisions (CKD stage 4 on the verge of dialysis); a historical one is context (appendectomy 1998, fully resolved). Do not let resolved items dilute the active picture. Anything resolved but recurrence-relevant (prior PE, prior cancer in surveillance) stays active.

3. **For each active problem, reconstruct the trajectory, not just the label.** "Heart failure" is useless; "HFrEF, EF 25%→35% on GDMT since 2024, one admission for decompensation 6 months ago, currently NYHA II" is decision-relevant. Pull the arc: when diagnosed, how it has moved, what's controlling it, last objective data point.

4. **Reconcile the medication story.** Note current meds tied to their indication, recent changes (started, stopped, dose-changed and why), and any drug the chart suggests was stopped for intolerance or adverse effect — that prevents a re-prescribe error.

5. **Surface the load-bearing results.** Most recent and most extreme values for the conditions in play (last A1c, last EF, last GFR trend, last relevant imaging). Include the date — a normal value from 3 years ago is not reassurance.

6. **Flag the unresolved threads.** Pending workups, recommended-but-not-done studies, abnormal results without documented follow-up, specialist recommendations not yet acted on. These are where care falls through cracks; they are the highest-value output.

7. **Capture goals/code status/advance directives** if documented — especially for inpatient or transfer summaries.

8. **Note data quality caveats.** If the record is internally contradictory (two different EFs, conflicting allergy lists) or has gaps (no notes for a 2-year window), say so rather than papering over it. Do not invent continuity that the record does not support.

## Output Format

```
ONE-LINER: [age, sex, dominant problems, baseline]

ACTIVE PROBLEMS (prioritized by current clinical weight):
1. [Problem] — [trajectory: dx date, course, current control, last objective data + date]
2. ...

MEDICATIONS (current, by indication):
- [drug, dose] — [indication]
- Recent changes: [started/stopped/changed + reason]
- Intolerances/ADRs on record: [drug → reaction]

KEY RESULTS (most recent / most relevant, with dates):
- [labs, imaging, EF, GFR trend, etc.]

UNRESOLVED / OPEN LOOPS:
- [pending studies, un-acted recommendations, abnormal results w/o follow-up]

HISTORICAL CONTEXT (not currently active but relevant):
- [prior cancer in surveillance, prior PE, surgeries]

GOALS / CODE STATUS: [if documented]

DATA CAVEATS: [contradictions, gaps, low-confidence items]
```

## Worked Example

**Input:** New-patient handoff. 71 y/o M transferring care; ~6 years of records available. Reason: establishing with new PCP.

**Output:**

```
ONE-LINER: 71 y/o M with HFrEF, CKD stage 3b, T2DM, and prior NSTEMI; community-dwelling, independent in ADLs, drives.

ACTIVE PROBLEMS (prioritized):
1. HFrEF — dx 2021 after NSTEMI; EF 30% (2021) → 40% (echo 03/2026) on GDMT. NYHA II. No admissions in >18 mo. On quadruple therapy.
2. CAD s/p NSTEMI 2021 with DES to LAD — on DAPT through 2022, now ASA monotherapy. No recurrent angina documented.
3. CKD stage 3b — baseline Cr ~1.7, eGFR 38 (04/2026), stable x2 yr. Proteinuria present; on ACEi/ARB-class agent (see meds).
4. T2DM — A1c 7.4% (04/2026), trending down from 8.9% (2023). No documented retinopathy screen since 2023 (OPEN LOOP).
5. HTN — controlled, last clinic BP 128/74.

MEDICATIONS (current, by indication):
- Sacubitril/valsartan 49/51 mg BID — HFrEF (note: counts as the ACEi/ARB; do not co-prescribe an ACEi)
- Metoprolol succinate 50 mg daily — HFrEF/CAD
- Dapagliflozin 10 mg daily — HFrEF + T2DM + CKD
- Spironolactone 25 mg daily — HFrEF
- Atorvastatin 80 mg daily — CAD secondary prevention
- Aspirin 81 mg daily — CAD
- Metformin 1000 mg BID — T2DM
- Recent changes: dapagliflozin added 2024; ARB switched to sacubitril/valsartan 2024.
- Intolerances/ADRs on record: lisinopril → cough (2021), discontinued.

KEY RESULTS (with dates):
- Echo 03/2026: EF 40%, mild MR, no significant valve disease.
- eGFR 38, Cr 1.7, K 4.6 (04/2026).
- A1c 7.4% (04/2026).
- Lipids 04/2026: LDL 62.
- K trend stable on spironolactone + sacubitril/valsartan.

UNRESOLVED / OPEN LOOPS:
- Diabetic retinopathy screening overdue (last 2023).
- Pneumococcal and RSV vaccination status not documented.
- 2024 cardiology note recommended consideration of ICD evaluation given EF 30% at that time — EF has since improved to 40%; reassess whether ICD indication still applies at current EF.

HISTORICAL CONTEXT:
- NSTEMI 2021 (the index event for CAD/HFrEF).
- Cholecystectomy 2015, resolved.

GOALS / CODE STATUS: Full code per 2025 note; no advance directive on file.

DATA CAVEATS: No records for a ~14-month gap (2022–2023) when patient was out of state; medication reconciliation at first visit advised. Allergy list consistent across notes.
```
