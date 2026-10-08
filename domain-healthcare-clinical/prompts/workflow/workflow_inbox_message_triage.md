---
title: "Clinical Inbox Message Triage"
category: domain-healthcare-clinical/workflow
description: "Triage a batch of EHR inbox items — patient messages, results, refills, staff requests — into an urgency-ranked, routed action queue with drafted next steps."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - workflow
  - inbox
  - triage
  - ehr
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

Take an unsorted batch of clinical inbox messages and convert it into a triaged work queue: each item assigned an urgency tier, a route (who handles it), and a drafted action. The point is to surface the one message in forty that is a clinical emergency hiding among refill requests, and to clear the routine volume efficiently. The hard requirement is that no time-critical item gets buried.

## Inputs

- The inbox batch: patient portal messages, lab/imaging results released to the provider, refill requests, pharmacy queries, nursing/staff messages, results-callback requests, prior-auth notices
- Provider scope: what this clinician owns vs. what routes to nursing, pharmacy, scheduling, or a covering colleague
- Available patient context for each item (relevant problems, meds, recent visits) where supplied
- Coverage status: is the responsible provider in clinic today, out, or is this a covering inbox?

## Role

Attending clearing your inbox at end of clinic, with a low threshold for escalating anything that smells time-critical.

## Reasoning Steps

1. **First pass: scan every item for red flags before sorting anything.** A patient-portal message reading "I've had chest pain since this morning" or a critical lab (K 6.8, INR 9, new blast count) is an emergency regardless of how it arrived. Pull these out first. Err toward over-triage — the cost of escalating a benign message is minutes; the cost of burying a real one is a sentinel event.

2. **Assign each item an urgency tier:**
   - **EMERGENT** — needs action within minutes to hours; may require calling the patient or 911-level instruction. Critical results, acute symptom messages.
   - **URGENT** — same-day action. Abnormal-but-not-critical results needing intervention, symptomatic patients who can wait hours, medication problems.
   - **ROUTINE** — handle within days. Stable refills, normal results to release, administrative.
   - **FYI/DELEGATE** — no provider decision required; route to staff (scheduling, forms, normal-result letters).

3. **Route, don't hoard.** Anything within nursing protocol, pharmacy scope, or scheduling should be delegated with a clear instruction, not done by the provider. State the route for each item.

4. **For results, decide the action, not just the read.** A result is not triaged until you've decided: release with reassurance, release with a plan change, call the patient, or order a next step. Tie the action to the result.

5. **For symptomatic patient messages, decide the disposition:** self-care advice, same-day visit, ED referral, or call-back. When a message describes a potential emergency, the correct output is a directive to contact the patient immediately / advise ED — not an async portal reply.

6. **Draft the action for each item** so it's executable: the refill approved or denied with reason, the result letter, the nurse instruction, the call-back script. A triage that doesn't reduce downstream work is incomplete.

7. **Verification pass.** Re-scan the EMERGENT and URGENT tiers: is anything misclassified down? Confirm no critical result was sorted as routine. State explicitly if any item is ambiguous and needs human eyes on the full chart.

## False-Positive Prevention

❌ **DON'T:**
- Draft a renal-dose, hold or resume instruction (gabapentin, K-retaining agents, anticoagulants) from a recalled number; use the label or formulary value or write `[VERIFY: label renal dosing at this CrCl]` — label renal tables are keyed to CrCl, not the eGFR the result shows.
- Treat a single critical value as confirmed without checking the input for a spurious cause (hemolyzed or delayed specimen), or dismiss it as artifact without ordering the repeat.
- Approve an item in ROUTINE while another item in the batch may be the same patient and changes the decision; resolve identity by MRN/DOB, never by name or drug.
- Fill TRIAGE VERIFICATION with "re-scanned, no misclassification" as boilerplate.

✅ **DO:**
- Count items in versus items out: the total across EMERGENT, URGENT, ROUTINE, FYI/DELEGATE and AMBIGUOUS equals the batch size, or a message has been dropped.
- For each EMERGENT and URGENT line, name the trigger that put it there — the value with units and the reporting lab's critical flag, or the symptom phrase quoted from the message.
- Label a result with no prior value supplied "single value — no trend available" instead of "improved" or "stable".

## Output Format

```
=== EMERGENT (act now) ===
- [item] | ROUTE: [provider call / ED advice / RN now] | ACTION: [drafted directive]

=== URGENT (same day) ===
- [item] | ROUTE: [who] | ACTION: [drafted next step]

=== ROUTINE (days) ===
- [item] | ROUTE: [who] | ACTION: [drafted reply/order]

=== FYI / DELEGATE (no provider decision) ===
- [item] | ROUTE: [staff] | ACTION: [instruction]

AMBIGUOUS — NEEDS FULL CHART REVIEW:
- [item + what's unclear]

TRIAGE VERIFICATION: [confirmation that emergent/urgent tiers were re-scanned; any item escalated on second pass]
```

## Worked Example

**Input:** Batch of 6 inbox items for a family medicine provider in clinic today:
1. Portal message: "My blood sugar has been 350-400 for three days and now I'm nauseous and breathing hard." (T2DM patient on metformin)
2. Lab result: Potassium 6.5 on a CKD patient on lisinopril + spironolactone.
3. Refill request: lisinopril 20 mg, patient stable, last BP 126/78.
4. Portal message: "Can you fill out my gym membership medical form?"
5. Lab result: A1c 6.8, down from 7.5, patient on metformin.
6. Pharmacy query: requesting renal dose clarification on gabapentin for a patient with eGFR 25.

**Output:**

```
=== EMERGENT (act now) ===
- Item 1 (sugar 350-400, nausea, dyspnea, T2DM): Picture concerning for DKA/HHS — hyperglycemia + nausea + tachypnea. ROUTE: Provider/RN to CALL PATIENT NOW. ACTION: Directive — "Do not reply by portal. Call patient immediately; if confirmed nausea + labored breathing with these glucoses, advise ED now for ketone/anion-gap evaluation. Do not manage async."
- Item 2 (K 6.5, CKD on lisinopril + spironolactone): Critical hyperkalemia. ROUTE: Provider call. ACTION: Call patient now, hold lisinopril AND spironolactone, and advise ED now for ECG and repeat potassium — a critical value is not deferred to an outpatient recheck or made conditional on symptoms [VERIFY: local critical-potassium protocol]. Flag both K-retaining agents for discontinuation pending recheck.

=== URGENT (same day) ===
- Item 6 (gabapentin renal dosing, eGFR 25): ROUTE: Provider answer to pharmacy. ACTION: Renal dose reduction required — calculate CrCl (label renal tables are keyed to CrCl, not eGFR) and give the label's dose range for that CrCl [VERIFY: gabapentin product label renal dosing at this CrCl]. Confirm indication and current dose before finalizing.

=== ROUTINE (days) ===
- Item 3 (lisinopril refill, stable, BP 126/78): ROUTE: Provider approve. ACTION: Approve 90-day refill only after confirming by MRN/DOB that this is not the Item 2 patient; if it is the same patient, do not refill — lisinopril is on hold per Item 2. Document last BP.
- Item 5 (A1c 6.8, improved): ROUTE: RN result letter. ACTION: Release with reassurance — "A1c improved to 6.8, continue current plan, recheck in 6 months."

=== FYI / DELEGATE ===
- Item 4 (gym form): ROUTE: Front desk / forms queue. ACTION: Forward for standard form-completion workflow; no clinical decision.

AMBIGUOUS — NEEDS FULL CHART REVIEW: None beyond the Item 2/3 identity check — the batch does not state whether they are the same patient; confirm by MRN/DOB before acting on the lisinopril refill.

TRIAGE VERIFICATION: Re-scanned emergent/urgent tiers. Two emergent items (DKA-concern message, critical K) both involve symptoms or critical values requiring a phone call, not an async reply — correctly escalated. No critical result was sorted as routine.
```
