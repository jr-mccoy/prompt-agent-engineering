---
title: "Prior Authorization Status Request — Move a Pending Approval Before Care Is Denied"
category: advocacy
description: "[SELF-SUBMIT] Help a patient draft THEIR OWN pair of short written requests while a prior authorization (pre-approval) is pending or stalled — one to the insurer asking for the request's status, the criteria it is being reviewed against, and what documentation is missing; one to the treating clinician's office asking it to submit or complete the request and whether it will seek an expedited review. Screens urgent care first. Does NOT argue medical necessity, cite insurance regulation, state review timeframes, interpret coverage, name a regulator, predict approval, or invent codes or reference numbers. Distinct from medicine_prior_authorization_letter (the clinician's medical-necessity letter) and advocacy_insurance_claim_denial_appeal (after a denial). Not legal or medical advice."
techniques:
  - CM-01
  - CM-03
  - DS-21
  - ST-03
  - QA-01
difficulty: beginner
intended_use: model-testing
tags:
  - written-advocacy
  - self-advocacy
  - insurance
  - prior-authorization
  - self-submit
  - patient
  - waiting-on-approval
updated: "2026-09-24"
related_prompts:
  - domain-written-advocacy/insurance-and-medical/advocacy_insurance_claim_denial_appeal.md
  - domain-healthcare-clinical/prompts/workflow/medicine_prior_authorization_letter.md
  - domain-written-advocacy/insurance-and-medical/advocacy_medical_records_request.md
  - domain-written-advocacy/cross-cutting/advocacy_channel_and_record_strategy.md
---

**Purpose:** Help you write **your own** short written requests while a prior authorization — the insurer's pre-approval for a test, treatment, drug, or procedure — is pending, stalled, or bouncing between your clinician's office and your insurer. The patient's lever at this stage is not arguing the medicine; it is **making both parties state in writing where the request is, what it is being judged against, and who is doing what next.**

**When to use:** Your clinician has ordered something that needs pre-approval, and you have heard "it's with the insurer" from the office and "we haven't received it" or "it's under review" from the insurer, with no date.

**When NOT to use:** The request has been **denied** in writing → `advocacy_insurance_claim_denial_appeal.md`. You are the clinician writing the medical-necessity justification → `domain-healthcare-clinical/prompts/workflow/medicine_prior_authorization_letter.md`. You already received the care and the **claim** was denied → the denial appeal. Care is urgent → the Boundary & Routing Block, first.

---

## Boundary & Routing Block

Use a different pathway if:
- **The care is urgent, your condition is worsening, or a delay could cause harm** → do not wait on a letter. Ask your clinician to request an **expedited or urgent review** by phone today, and call the insurer yourself to ask the same. `[VERIFY: the insurer's expedited process from your plan documents or member services.]` If your condition is deteriorating, seek medical care — coverage is a separate problem from treatment.
- **You are told to go ahead without approval** → ask who told you, and get it in writing before relying on it; the financial consequences of proceeding without approval are a question for the insurer, in writing.
- **An appeal or response date appears in anything you receive** → act on that date.
- **A pharmacy says a drug needs approval** → the same letters apply, but address the pharmacy-benefit side of your plan if it is separate; your insurance card or plan documents say which.

This prompt is educational support for preparing your own correspondence. It is not a substitute for legal, medical, or insurance-professional services.

---

## Scope Boundary — Read First

This **drafts your own status and support requests for you to send**. It is **not legal advice, medical advice, a prior authorization submission, or a substitute for your clinician, your insurer, or your jurisdiction's law.** It will **not** argue or assess medical necessity; cite an insurance statute or regulation; state how long the insurer has to decide or what counts as urgent; state whether your plan covers the service; tell you whether the criteria being applied are appropriate; name an insurance regulator; predict approval; or invent a procedure code, drug name, reference number, or date. Prior-authorization rules **vary by plan, state, and country.** Where such a concept appears it is flagged *verify in your plan documents*.

---

## Core Principles

1. **Two letters, two jobs.** The insurer letter asks *where is it, and what is it being judged against*. The clinician letter asks *has it been sent, and is it complete*. Most stalls are a gap between the two.
2. **Get the reference number.** Every prior authorization has a case or reference number once received. If the insurer cannot give one, it may not have the request — which is itself the answer.
3. **Ask for the criteria, not a verdict.** Ask which clinical policy or criteria the request is being reviewed against, and what documentation is missing. That is what the clinician needs to complete it.
4. **The clinician argues the medicine.** You do not write about medical necessity; you make sure the person who can has what they need.
5. **Ask about expedited review explicitly.** Whether a request is urgent is the clinician's call — ask whether they will request it.

---

## Your Input

- **Your jurisdiction:** [required]
- **Is the care urgent or your condition worsening?:** [if yes → Boundary & Routing Block, first]
- **Insurer, plan, member ID:** [#]
- **Ordering clinician and practice:** [name]
- **The service, test, or drug as the clinician's office names it:** [description; code only if shown to you]
- **Date the office says it submitted, and how:** [YYYY-MM-DD / unknown]
- **Any reference number from either side:** [# or none]
- **What each side has told you, with dates:** [office said… / insurer said…]
- **Scheduled date of care, if any:** [YYYY-MM-DD]

---

## Constraints

**Must:**
- Require the jurisdiction; use only facts the user supplies.
- Screen urgency first and route to expedited review and the clinician.
- Produce two separate short letters: insurer status request and clinician-office support request.
- Ask the insurer for status, reference number, the criteria or policy being applied, missing documentation, and expected decision date.
- Ask the clinician's office whether it submitted, when, the reference number, whether anything was requested back, and whether it will seek expedited review.
- Record what each side has said, with dates.
- Include a Sending Log and label the output `MY OWN REQUEST — NOT A LEGAL FILING`.

**Must Not:**
- Argue or assess medical necessity.
- Cite an insurance statute or regulation, or state a decision timeframe or urgency definition.
- State whether the plan covers the service.
- Advise proceeding without approval.
- Name a regulator.
- Predict approval.
- Invent codes, drug names, reference numbers, or dates.

---

## Instructions

### Stage 1 — Screen for Urgency
Urgent or worsening → expedited review by phone today via the clinician and the insurer; letters afterwards as the record.

### Stage 2 — Reconstruct Who Said What
List every statement from the office and the insurer with its date. Identify the gap: not submitted, submitted but not received, received and pending, or information requested and not returned.

### Stage 3 — Draft the Insurer Letter
Status, reference number, criteria or policy applied, missing documentation, expected decision date, and a request to copy any information request to the patient as well as the clinician.

### Stage 4 — Draft the Clinician-Office Letter
Submission date and method, reference number, anything the insurer asked for, whether the office will seek expedited review, and who in the office is handling it.

### Stage 5 — Close
Add Sending Logs, and point to the denial appeal if a written denial arrives.

---

## Output Format

```markdown
MY OWN STATUS REQUEST TO MY INSURER — NOT A LEGAL FILING
From: [name], member ID [#], [contact]. To: [insurer], [member services / utilization
management channel]. Date: [YYYY-MM-DD]. Delivery: [portal message / designated address].
This is my own request. It does NOT argue medical necessity or cite regulation.

Re: Prior authorization for [service as named by my clinician], ordered by [clinician]
Care scheduled for: [YYYY-MM-DD / not yet scheduled]

My clinician's office tells me the request was submitted on [date / NEED DATE:].
Please tell me in writing:
1. Whether you have received it, and its reference number.
2. Its current status and the date you expect to decide.
3. Which clinical policy or criteria it is being reviewed against.
4. Whether you have asked my clinician for anything further, and what — please copy me.
[Your name], [YYYY-MM-DD]

---
MY OWN REQUEST TO MY CLINICIAN'S OFFICE
To: [practice], attention [prior-authorization / referrals staff]. Date: [YYYY-MM-DD].
Re: Prior authorization for [service], ordered [date]
The insurer [has told me on [date] that it has no record / that it is pending — reference #].
Could you please tell me:
1. When and how the request was submitted, and the reference number.
2. Whether the insurer has asked for anything further, and whether it has been sent.
3. Whether you will ask the insurer for an expedited review.
4. Who in your office is handling it, so I can follow up without taking your clinical time.
[Your name], DOB [YYYY-MM-DD], [YYYY-MM-DD]

---
## Sending Log (keep with your copy)
| Sent | Method | Sent to | Reference # | Proof kept | Response due | Outcome |
|---|---|---|---|---|---|---|
| [YYYY-MM-DD] | [portal] | [insurer] | [#] | [screenshot] | [YYYY-MM-DD] | [ ] |
| [YYYY-MM-DD] | [portal] | [clinic] | [#] | [screenshot] | [YYYY-MM-DD] | [ ] |

Note to self: if a written denial arrives, I will act on the date in it and use the appeal prompt.
*Verify in your plan documents — prior-authorization rules vary by plan and state.*
```

---

## Verification

- [ ] Urgency screened first and routed to expedited review?
- [ ] Two separate letters, insurer and clinician office?
- [ ] Insurer asked for receipt, reference, status, criteria, missing items, and decision date?
- [ ] Office asked for submission date, reference, outstanding requests, expedited review, and contact?
- [ ] Who-said-what recorded with dates?
- [ ] No medical-necessity argument, regulation, timeframe, coverage view, or prediction?
- [ ] No regulator named; no invented codes or reference numbers; Sending Log included?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "This MRI is medically necessary because…" | Leave necessity to the clinician; ask for the criteria being applied |
| "You must decide within [n] days" | Ask for the expected decision date |
| "This is covered under my plan" | Ask status; coverage is decided in the determination |
| "Go ahead with the procedure; it'll be approved" | Advise nothing; ask the insurer in writing |
| One combined letter to both parties | Two letters; each party answers its own questions |
| Invent a CPT code to look precise | Describe the service as the clinic names it |
| Write a status letter while the patient is deteriorating | Expedited review by phone today; seek care |

---

## Adaptations

- **Drug requiring approval at the pharmacy:** Address the pharmacy-benefit side of the plan if separate, and ask the prescriber's office whether a different formulary option exists — a clinical question for them to answer.
- **"No record of the request":** Send the office letter first; ask for the submission confirmation to forward to the insurer.
- **Information requested and not returned:** Ask the office for the date they expect to send it, and ask the insurer to confirm when it arrives.
- **Scheduled date approaching:** State the date in both letters and ask each party what happens if no decision is made by then.

---

## Related Prompts

- `advocacy_insurance_claim_denial_appeal.md` — once a written denial arrives.
- `domain-healthcare-clinical/prompts/workflow/medicine_prior_authorization_letter.md` — what the clinician's side of the request looks like.
- `advocacy_medical_records_request.md` — if records supporting the request need to move between providers.
- `../cross-cutting/advocacy_channel_and_record_strategy.md` — confirming phone calls with the insurer in writing.
