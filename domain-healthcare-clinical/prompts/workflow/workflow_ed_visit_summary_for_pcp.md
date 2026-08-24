---
title: "ED Visit Summary for the PCP"
category: domain-healthcare-clinical/workflow
description: "Convert an emergency department encounter into a concise primary-care-facing handoff that closes the loop: what happened, what was ruled out, and what the PCP must own next."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: intermediate
tags:
  - workflow
  - care-transitions
  - emergency-medicine
  - handoff
updated: "2026-06-19"
---

## Objective

Produce a primary-care-facing summary of an ED visit that tells the PCP exactly what they need to act on, without making them read the full ED chart. The deliverable foregrounds the disposition decision, the actionable follow-up items, and the time-sensitive pending results — the three things that determine whether the loop closes safely.

## Inputs

- ED course: chief complaint, relevant history, vitals/exam highlights, workup performed and results, treatments given, ED diagnosis, disposition
- Pending-at-discharge items: cultures, final radiology reads, labs sent out, specialist callbacks
- Medications started, stopped, or changed in the ED
- Follow-up instructions given to the patient and any referrals placed
- Patient's baseline (from chart if available) so the PCP can judge what changed

## Role

Emergency medicine attending writing the courtesy note you would want to receive if this were your clinic patient.

## Reasoning Steps

1. **Lead with the disposition logic.** Why was this patient safe to discharge (or why admitted)? The PCP's first question is "should I be worried they went home?" Answer it: the dangerous diagnoses considered and how they were excluded.

2. **State the ED working diagnosis plainly,** and distinguish a confirmed diagnosis ("urine culture-confirmed cystitis") from a symptomatic discharge ("non-specific abdominal pain, serious causes excluded, no diagnosis established").

3. **Itemize the actionable follow-up,** ranked by time sensitivity. Separate "the PCP must do X" (recheck a potassium in 3 days, ensure the incidental nodule gets a CT in 6 months) from "already arranged" (cardiology referral placed) from "patient-dependent" (return if symptoms recur).

4. **Flag every pending result with an owner.** A blood culture pending at discharge is the classic dropped result. State what is pending, when it's expected, and who is responsible for acting on it — if that is the PCP, say so explicitly.

5. **List medication changes with reasons,** especially anything that interacts with the patient's chronic meds or requires monitoring (new anticoagulant, steroid burst, antibiotic with renal dosing).

6. **Surface incidental findings** discovered during the workup that have nothing to do with the presenting complaint but need longitudinal follow-up (pulmonary nodule on CT, elevated calcium, thyroid nodule). These are the highest-liability items because no one is assigned to them.

7. **Keep it short and skimmable.** A PCP triages dozens of these. The summary fails if it reproduces the ED note instead of distilling it. Do not fabricate results or follow-up not supported by the encounter.

## Output Format

```
PATIENT / DATE OF ED VISIT: [identifier, date]
CHIEF COMPLAINT: [one line]

WHY THEY CAME / WHY THEY WENT HOME (or were admitted):
- [disposition logic: dangerous dx considered + how excluded]

ED DIAGNOSIS: [confirmed dx vs. symptomatic discharge — be explicit]

WORKUP HIGHLIGHTS:
- [key positive and key negative results, not the full panel]

TREATMENTS GIVEN: [meds, procedures in ED]

MEDICATION CHANGES:
- [started/stopped/changed + reason + monitoring needed]

PENDING RESULTS (with owner):
- [test, expected back, who acts]

PCP ACTION ITEMS (ranked by time sensitivity):
1. [must-do + timeframe]
2. ...

ALREADY ARRANGED: [referrals/appointments placed in ED]

INCIDENTAL FINDINGS NEEDING FOLLOW-UP:
- [finding + recommended interval]

RETURN PRECAUTIONS GIVEN TO PATIENT: [brief]
```

## Worked Example

**Input:** 58 y/o F, ED visit for pleuritic chest pain and dyspnea. PERC-positive so D-dimer ordered → elevated → CTA chest. CTA negative for PE. Incidental 7 mm RUL pulmonary nodule noted. Troponin negative x2, ECG sinus. Discharged. History of HTN on amlodipine; 30-pack-year smoker.

**Output:**

```
PATIENT / DATE OF ED VISIT: 58 y/o F — ED visit 06/18/2026
CHIEF COMPLAINT: Pleuritic chest pain + dyspnea, 1 day.

WHY THEY WENT HOME:
- PE excluded by negative CTA chest. ACS excluded by two negative troponins and non-ischemic ECG. Hemodynamically stable, ambulated without desaturation. No effusion or pneumonia on imaging. Safe for outpatient management with the single open item below.

ED DIAGNOSIS: Pleuritic chest pain, likely musculoskeletal/viral — no PE, no ACS, no pneumonia. Symptomatic discharge; no confirmed diagnosis established.

WORKUP HIGHLIGHTS:
- CTA chest: NEGATIVE for PE. Incidental 7 mm solid nodule, right upper lobe.
- Troponin negative x2; ECG normal sinus, no ischemic changes.
- D-dimer elevated (the reason CTA was done).
- CBC/BMP unremarkable.

TREATMENTS GIVEN: NSAID in ED with symptom relief.

MEDICATION CHANGES: None to chronic meds. Advised PRN ibuprofen for pleuritic pain.

PENDING RESULTS (with owner): None pending — all studies finalized in ED.

PCP ACTION ITEMS (ranked):
1. **Pulmonary nodule follow-up (highest priority).** 7 mm solid nodule in a 58 y/o with 30-pack-year smoking history is intermediate risk. Per Fleischner, repeat low-dose chest CT at 6–12 months. PCP to order and track — no one else is assigned.
2. Address tobacco cessation; also confirm patient is enrolled in lung cancer screening (meets USPSTF criteria independent of this nodule).
3. Reassess chest pain at follow-up if persistent; consider MSK vs. other if not resolving.

ALREADY ARRANGED: None.

INCIDENTAL FINDINGS NEEDING FOLLOW-UP:
- 7 mm RUL solid pulmonary nodule → repeat CT 6–12 months (Fleischner, intermediate risk given smoking history).

RETURN PRECAUTIONS GIVEN TO PATIENT: Return for worsening dyspnea, syncope, unilateral leg swelling, or fever.
```
