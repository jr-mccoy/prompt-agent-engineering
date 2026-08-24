---
title: "Telephone / Refill Encounter Note"
category: domain-healthcare-clinical/workflow
description: "Generate a concise but complete telephone or refill encounter note — reason, relevant data reviewed, the decision and its rationale, the action taken, and follow-up — for asynchronous care."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: intermediate
tags:
  - documentation
  - telephone-encounter
  - refill
  - clinical-notes
updated: "2026-06-19"
---

## Objective

Produce a telephone or refill encounter note that documents asynchronous care to the same standard as a visit: who/what prompted it, the relevant data the clinician reviewed, the clinical decision and the reasoning, the specific action taken (refill approved/denied, dose changed, advice given, escalation), and the follow-up plan. These encounters are high-volume and low-ceremony but carry real liability when the reasoning or the safety-netting isn't documented.

## Inputs

- Encounter type (refill request, symptom call, results call-back, medication question)
- The request or reason for the contact
- Who initiated it (patient, pharmacy, family) and who the clinician spoke with
- Relevant chart data reviewed (last visit, last relevant labs/vitals, current med list, monitoring status)
- The decision and its clinical basis
- The action taken (specific medication/dose/quantity/refills, or advice given)
- Follow-up and safety-netting

## Role

The clinician handling and documenting the asynchronous encounter.

## Reasoning Steps

1. **State the reason and the parties.** What was requested, who initiated it, and who the clinician communicated with. A refill from a pharmacy and a symptom call from the patient are documented differently.

2. **Document the relevant data reviewed.** For a chronic-med refill, this is the gate: when was the patient last seen, are required monitoring labs current (e.g., a statin refill with last lipids/LFTs, a lisinopril refill with last BP and K, a controlled substance with the PDMP/agreement status). Documenting that you checked is what makes the refill defensible.

3. **Make the clinical decision and state its basis.** Approve, deny, partial/bridge, or change — and why. "Patient overdue for labs; approving a 30-day bridge and requiring labs before further refills" is a complete decision; a bare "refilled" is not.

4. **For symptom calls, document the assessment and disposition** — the relevant history elicited, the working impression, and whether the issue was managed by advice, brought in for a visit, or escalated to urgent/ED care.

5. **Record the specific action** — exact drug, dose, quantity, number of refills, pharmacy; or the advice given verbatim enough to be clear. Ambiguity here causes errors downstream.

6. **Document the safety net and follow-up** — what the patient was told to watch for and when to follow up or seek urgent care, and any labs/appointments ordered.

7. **Flag when async is not appropriate.** If the request can't be safely handled by phone/refill (symptoms needing exam, monitoring overdue for a high-risk drug, controlled-substance early refill), document the conversion to a visit rather than forcing an async decision.

8. **Keep it concise but complete** — every element that makes the decision safe and auditable, nothing more.

## Output Format

```
TELEPHONE/REFILL ENCOUNTER NOTE
TYPE: [refill / symptom call / results call-back / med question]
INITIATED BY: [patient/pharmacy/family] | SPOKE WITH: [who]

REASON: [the request]

DATA REVIEWED:
- Last seen: [date] | Relevant labs/vitals: [+ dates] | Monitoring status: [current/overdue]
- Current relevant meds: [...]

ASSESSMENT/DECISION:
- [decision + clinical basis]

ACTION TAKEN:
- [exact medication, dose, quantity, refills, pharmacy] OR [advice given] OR [escalation]

FOLLOW-UP & SAFETY NET:
- [labs/appointments ordered, what to watch for, when to follow up / seek urgent care]
```

## Worked Example

**Input:** Pharmacy refill request for atorvastatin 40 mg and lisinopril 20 mg. Patient is a 61 y/o M with HTN and hyperlipidemia. Chart: last seen 14 months ago; last lipid panel and CMP 14 months ago; last BP at that visit 132/80. No labs since. Patient reached by phone, feeling well, no symptoms, checks home BP averaging 130s/80s.

**Output:**

```
TELEPHONE/REFILL ENCOUNTER NOTE
TYPE: Refill request.
INITIATED BY: Pharmacy | SPOKE WITH: Patient (by phone).

REASON: Refill requests for atorvastatin 40 mg daily and lisinopril 20 mg daily.

DATA REVIEWED:
- Last seen: 14 months ago. Last lipid panel and CMP (including K and Cr): 14 months ago. No labs since — monitoring overdue.
- Last office BP 132/80; patient reports home BP averaging 130s/80s, feeling well, no symptoms (no dizziness, cough, or edema).
- Current relevant meds: atorvastatin 40 mg, lisinopril 20 mg.

ASSESSMENT/DECISION:
- Patient stable and asymptomatic but overdue for an office visit and routine monitoring (lipids, CMP for K/Cr on an ACE inhibitor) by >12 months. Not appropriate to continue indefinite refills without monitoring, but a gap in therapy is also undesirable for BP and lipid control. Decision: approve a short bridge and require labs + visit before further refills.

ACTION TAKEN:
- Approved a 30-day supply of atorvastatin 40 mg and lisinopril 20 mg (no further refills) to [pharmacy].
- Ordered lipid panel and CMP to be completed before the visit.
- Scheduled office follow-up within 4 weeks.

FOLLOW-UP & SAFETY NET:
- Patient advised to complete labs and attend the follow-up visit to continue medications beyond the 30-day bridge.
- Advised to call sooner for dizziness, lightheadedness, new cough, leg swelling, or home BP readings persistently >150/90 or <100 systolic with symptoms.
```
