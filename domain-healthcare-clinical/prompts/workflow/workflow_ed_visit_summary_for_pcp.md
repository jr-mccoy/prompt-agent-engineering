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
updated: "2026-10-06"
---

> **Medical disclaimer — read before use.** This prompt is a decision-support and
> teaching aid for **licensed clinicians**. It is **not medical advice** and is not for
> patients to diagnose or treat themselves. Drug doses, thresholds and guideline
> references in it and in its worked example may be incomplete, outdated or wrong:
> verify each one against the current guideline, the product label and your local
> formulary, and follow your institution's protocols. It does not replace examination
> or clinical judgment. **Medical emergency: call your local emergency number (911 in
> the US).**
>
> **Review status:** AI-assisted content, reviewed by AI only (2026-10-06);
> **not yet reviewed by a licensed clinician.**

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

## False-Positive Prevention

❌ **DON'T:**
- Pad WHY THEY WENT HOME with reassuring negatives the ED course never recorded ("ambulated without desaturation", "no effusion", "CBC/BMP unremarkable") — a disposition rationale assembled from plausible exclusions reads as safe and is unsupported.
- Write "None pending — all studies finalized in ED" because no pending list was supplied; a missing list is not an empty one (blood cultures, radiology over-reads and send-out labs are the usual stragglers).
- Attach a surveillance interval or risk category to an incidental finding from memory; if the radiology report gives no recommendation, write the interval as `[VERIFY: current Fleischner / ACR incidental-findings guidance]`.
- Promote a symptomatic discharge to a named diagnosis in the ED DIAGNOSIS line because every test came back negative.

✅ **DO:**
- Trace every entry in WORKUP HIGHLIGHTS, TREATMENTS GIVEN and RETURN PRECAUTIONS to a line of the ED input; anything without a source is deleted or tagged `[not in ED record]`.
- Recount pending items against the ED orders: each culture, send-out and preliminary read appears in PENDING RESULTS with an expected date and a named owner, or the line reads "pending status not supplied — confirm with ED".
- Say whether each incidental-finding interval is the radiologist's own recommendation or guideline-derived, so the PCP knows which one to reconcile.

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

**Input:** 58 y/o F, ED visit 06/18/2026 for 1 day of pleuritic chest pain and dyspnea. PERC-positive so D-dimer ordered → elevated → CTA chest. CTA negative for PE. Incidental 7 mm solid RUL pulmonary nodule noted; the radiology report gives no follow-up recommendation. Troponin negative x2, ECG sinus without ischemic changes. NSAID given in ED with symptom relief. Discharged on PRN ibuprofen; return precautions given for worsening dyspnea, syncope, unilateral leg swelling, or fever. No pending-results list supplied. History of HTN on amlodipine; 30-pack-year current smoker.

**Output:**

```
PATIENT / DATE OF ED VISIT: 58 y/o F — ED visit 06/18/2026
CHIEF COMPLAINT: Pleuritic chest pain + dyspnea, 1 day.

WHY THEY WENT HOME:
- PE excluded by negative CTA chest. ACS excluded by two negative troponins and non-ischemic ECG. Discharged for outpatient management with the open items below.

ED DIAGNOSIS: Pleuritic chest pain — no PE, no ACS. Symptomatic discharge; no confirmed diagnosis established.

WORKUP HIGHLIGHTS:
- CTA chest: NEGATIVE for PE. Incidental 7 mm solid nodule, right upper lobe.
- Troponin negative x2; ECG normal sinus, no ischemic changes.
- D-dimer elevated (the reason CTA was done).

TREATMENTS GIVEN: NSAID in ED with symptom relief.

MEDICATION CHANGES: None to chronic meds. Advised PRN ibuprofen for pleuritic pain.

PENDING RESULTS (with owner): Pending status not supplied — confirm with ED (final radiology read and any send-outs).

PCP ACTION ITEMS (ranked):
1. **Pulmonary nodule follow-up (highest priority).** 7 mm solid nodule in a 58 y/o with 30-pack-year smoking history; the radiology report gives no recommendation, so risk category and CT interval(s) are guideline-derived: `[VERIFY: current Fleischner / ACR incidental-findings guidance]`. PCP to order and track — no one else is assigned.
2. Address tobacco cessation; also confirm patient is enrolled in lung cancer screening (meets USPSTF criteria independent of this nodule).
3. Reassess chest pain at follow-up if persistent; consider MSK vs. other if not resolving.

ALREADY ARRANGED: None.

INCIDENTAL FINDINGS NEEDING FOLLOW-UP:
- 7 mm RUL solid pulmonary nodule → interval `[VERIFY: current Fleischner / ACR incidental-findings guidance]` (guideline-derived; no radiologist recommendation in report).

RETURN PRECAUTIONS GIVEN TO PATIENT: Return for worsening dyspnea, syncope, unilateral leg swelling, or fever.
```
