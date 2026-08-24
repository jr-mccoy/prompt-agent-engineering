---
title: "Referral Letter Generator (Specialist / Higher LOC)"
category: psychology/care-coordination
description: "Generate a scoped referral letter to a specialist (psychiatrist, neuropsychology, PCP, higher level of care) with a sharp referral question, ROI-bounded clinical summary, current meds/risk, and an explicit ask."
techniques:
  - ST-04
  - DT-01
  - DS-02
  - CM-02
  - QA-04
difficulty: intermediate
intended_use: model-testing
tags:
  - referral
  - care-coordination
  - specialist-referral
  - neuropsychology
  - psychiatry-referral
  - release-of-information
  - minimum-necessary
updated: "2026-06-08"
related_prompts:
  - domain-psychology/care-coordination/psychology_warm_handoff_narrative.md
  - domain-psychology/care-coordination/psychology_pcp_communication_note.md
  - domain-psychology/documentation/psychology_collateral_contact_note.md
  - domain-psychology/documentation/psychology_initial_treatment_plan.md
---

# Referral Letter Generator (Specialist / Higher LOC)

## Objective

Produce a referral letter from a treating behavioral-health clinician to a receiving provider — psychiatrist or psychiatric prescriber, neuropsychologist, primary care physician, or a higher level of care (IOP/PHP/residential/inpatient intake) — that leads with a **single, answerable referral question**, supplies only the clinical information the recipient needs to act on it, and states exactly what is being requested. The letter must respect the scope of the signed Release of Information (ROI), apply HIPAA minimum-necessary, and route an acutely-at-risk client to the correct urgent pathway rather than to a routine referral queue.

## When to Use

- Referring for a psychiatric evaluation or medication consultation.
- Referring for neuropsychological / psychoeducational testing (e.g., ADHD, dementia work-up, cognitive baseline).
- Referring back to or coordinating with a PCP for a medical work-up of psychiatric-presenting symptoms (thyroid, sleep apnea, medication interaction).
- Referring to a higher level of care when outpatient is no longer sufficient.
- Referring out for a modality the clinician does not provide (EMDR, specialized eating-disorder care, ABA).

## Inputs / Context Required

- **Recipient**: name, credentials, specialty, and clinic/setting of the receiving provider (or "intake department" if unnamed).
- **Referral type**: psychiatry / neuropsych / PCP / higher LOC / specialty modality.
- **The referral question**: the one clinical question the recipient is being asked to answer.
- **ROI status**: signed ROI on file? To whom? Scope (what may be shared)? Expiration date? `[clinician input required: ROI specifics if not provided]`.
- **Diagnoses** (DSM-5-TR / ICD-10-CM): active and relevant only.
- **Brief treatment summary**: presenting concern, course, what has been tried.
- **Current medications** (psychotropic and relevant medical) with prescriber.
- **Risk status**: current SI/HI/self-harm, recent attempts, current safety plan status.
- **SUD involvement**: is any substance-use information part of the record? (triggers 42 CFR Part 2 handling).
- **Urgency**: routine / urgent / emergent.
- `[clinician input required: any cultural, language, or accessibility needs of the client relevant to the receiving provider]`

## Constraints

### Must

- Open with **one referral question**, stated as a question the recipient can answer (e.g., "Is this presentation consistent with adult ADHD, and would stimulant treatment be appropriate?").
- Include only clinical content **within the signed ROI scope** and necessary to answer the referral question (minimum-necessary).
- State the ROI status explicitly: to whom information is authorized, the scope, and the expiration date.
- If any substance-use-disorder treatment information is included and the record is governed by **42 CFR Part 2**, mark it and require a Part 2–compliant authorization before that content is released; do not bundle Part 2 data under a general HIPAA ROI.
- List current medications with prescriber and the date of the medication list.
- Include a **risk/safety carve-out**: if the client has active risk, state current risk level, current safety plan status, and route to the appropriate urgency pathway (do not place an acutely suicidal client into a routine referral).
- State the explicit **ask** (evaluation, testing, medication consult, admission, takeover of care, co-management) and the requested timeframe.
- Where applicable, note the relevant interprofessional consultation code (99446–99449 for consultant-to-treating verbal/written report including review; 99451 written-report-only by consultant; 99452 for the treating clinician's referral time) so billing capture is possible.
- Flag missing data as `[clinician input required: ...]`; do not fabricate history, scores, or medication details.

### Must Not

- Do not include clinical content outside the ROI scope or beyond what the referral question requires.
- Do not disclose 42 CFR Part 2 SUD treatment detail under a general HIPAA authorization.
- Do not bury or omit active risk; do not route an emergent client through a routine referral.
- Do not fabricate diagnoses, scores, medication names/doses, or a prescriber if unknown.
- Do not write a vague, multi-question referral that gives the recipient no clear task.

## Instructions

1. Confirm the recipient and referral type; draft the single referral question first and keep the rest of the letter in service of it.
2. Verify ROI scope and expiration; restrict all clinical content to that scope and to minimum-necessary. Note Part 2 status if SUD content is present.
3. Run the safety screen: if active risk, set the urgency, document current risk and safety-plan status, and select the correct pathway before continuing.
4. Write a tight clinical summary (presenting concern, relevant course, what has been tried) — no exhaustive history dump.
5. Insert the current medication list with prescriber and list date.
6. State the explicit ask and requested timeframe; attach the interprofessional consult code where billing applies.
7. Add return-coordination instructions (how/where to send results, and who is the point of contact).
8. Run verification.

## Output Format

```
=== REFERRAL LETTER ===

DATE: [YYYY-MM-DD]
TO: [Recipient name, credentials, specialty / clinic]
FROM: [Referring clinician name, credentials, license #, practice, contact]
RE: [Client initials / MRN]  DOB: [YYYY-MM-DD]
URGENCY: [Routine / Urgent / Emergent]

REFERRAL QUESTION
[One answerable clinical question.]

REASON FOR REFERRAL
[2–4 sentences: presenting concern, why this specialist/LOC, what is needed.]

RELEVANT CLINICAL SUMMARY (ROI-scoped, minimum-necessary)
Diagnoses (active/relevant): [F##.## Descriptor; ...]
Course / what has been tried: [Brief — modality, duration, response.]
Relevant findings / scores: [Only those bearing on the referral question, e.g., PHQ-9 = [X].]

CURRENT MEDICATIONS (list date: [YYYY-MM-DD])
- [Medication, dose, frequency] — Prescriber: [Name]
- [...]

RISK / SAFETY STATUS
Current risk: [None active / Passive ideation / Active SI/HI — describe]
Safety plan: [On file dated [YYYY-MM-DD] / Updated / N/A]
Pathway: [Routine referral OK | Urgent — contact within [timeframe] | EMERGENT — emergency evaluation initiated; this is NOT a routine referral]

WHAT IS BEING REQUESTED
[Explicit ask: evaluation / testing battery / medication consult / admission / co-management.]
Requested timeframe: [...]

RELEASE OF INFORMATION
Signed ROI on file: [Yes/No]  To: [Recipient/entity]
Scope authorized: [What may be shared]  Expires: [YYYY-MM-DD]
42 CFR Part 2 (SUD) content: [None | Present — Part 2-compliant authorization required before release of that content]

RETURN COORDINATION
Send results / report to: [Name, secure fax / portal / address]
Point of contact: [Name, phone]
Billing note: [Interprofessional consult code if applicable, e.g., 99452 (referring) / 99446–99449 / 99451]

Signature: ____________________  [Clinician, credentials]  Date: __________
```

## Verification

- [ ] Exactly one answerable referral question stated up front.
- [ ] Clinical content limited to ROI scope and minimum-necessary.
- [ ] ROI status stated: recipient, scope, expiration.
- [ ] 42 CFR Part 2 SUD content flagged and gated behind a Part 2 authorization (not bundled under general HIPAA ROI).
- [ ] Current medications listed with prescriber and list date.
- [ ] Risk/safety status documented; acutely-at-risk client routed to correct urgency pathway (not routine).
- [ ] Explicit ask and requested timeframe present.
- [ ] Interprofessional consult code noted where billing applies.
- [ ] Return-coordination instructions and point of contact included.
- [ ] No fabricated diagnoses, scores, medications, or prescriber.
- [ ] Missing inputs flagged with `[clinician input required]`.
