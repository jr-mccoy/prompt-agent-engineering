---
title: "Medical Bill Dispute — Get an Itemized Bill and Challenge What Is Wrong"
category: advocacy
description: "[SELF-SUBMIT] Help a person dispute a medical bill in writing — requesting a fully itemized bill first, reconciling it against the insurer's explanation of benefits, identifying duplicate, never-received, or miscoded charges, and asking for a hold on collection while it is reviewed. Does NOT cite billing or surprise-billing law as authority, state what a provider may charge or whether a code was correct, interpret an EOB as a legal position, predict adjustment, or invent codes or amounts. Not legal, financial, or medical advice."
techniques:
  - CM-01
  - DS-01
  - DS-21
  - ST-03
  - QA-01
difficulty: intermediate
intended_use: model-testing
tags:
  - written-advocacy
  - self-advocacy
  - medical-billing
  - dispute
  - self-submit
  - consumer
updated: "2026-08-01"
related_prompts:
  - domain-written-advocacy/insurance-and-medical/advocacy_financial_assistance_charity_care_request.md
  - domain-written-advocacy/insurance-and-medical/advocacy_insurance_claim_denial_appeal.md
  - domain-written-advocacy/financial-hardship/advocacy_payment_arrangement_proposal.md
  - domain-legal/personal-self-advocacy/debt-collection/legalprep_debt_validation_dispute_letter_preparer.md
---

**Purpose:** Help you dispute a medical bill in writing — starting with the step that resolves a surprising share of these disputes on its own: getting a fully itemized bill. It then reconciles the itemization against your insurer's explanation of benefits, identifies duplicates, services never received, and coding that does not match what happened, and asks for collection to be held while the review runs.

**When to use:** A medical bill looks wrong, is larger than expected, or you cannot tell what it is for, and you want a documented dispute rather than a phone conversation you cannot later evidence.

**When NOT to use:** The bill is correct and you cannot afford it → `advocacy_financial_assistance_charity_care_request.md` **first**, then `../financial-hardship/advocacy_payment_arrangement_proposal.md`; paying or arranging instalments on a bill that should have been reduced is a common and expensive mistake. The insurer denied coverage → `advocacy_insurance_claim_denial_appeal.md`. The bill is with a collector and you do not recognize it → `domain-legal/personal-self-advocacy/debt-collection/legalprep_debt_validation_dispute_letter_preparer.md` first.

---

## Boundary & Routing Block

Use a different pathway if:
- **You cannot afford the bill even if it is correct** → ask about financial assistance or charity care **before** agreeing to pay or to instalments. Many facilities have programmes that are not offered unless asked, and an instalment arrangement on a bill that qualified for reduction is difficult to undo. Use `advocacy_financial_assistance_charity_care_request.md` first.
- **The account has been sent to collections** → validate the debt before disputing or paying anything. See `domain-legal/personal-self-advocacy/debt-collection/legalprep_debt_validation_dispute_letter_preparer.md`, and route to an attorney or **legal aid** if it is being reported adversely or legal action is mentioned.
- **The bill relates to an injury where someone else may be responsible, or to a workplace injury** → do not correspond about payment before speaking to an attorney; how these bills are handled can affect a claim.
- **You believe you were billed for care you did not receive at all, or under someone else's identity** → treat it as possible medical identity theft. See `domain-legal/personal-self-advocacy/identity-theft/`.
- **The care is ongoing and you are worried a dispute will affect it** → disputing a bill and receiving care are separate; say so to the provider, and do not defer needed care over a billing dispute. If a condition is deteriorating, seek care.

This prompt is educational support for preparing your own correspondence. It is not a substitute for legal, financial, or medical services.

---

## Scope Boundary — Read First

This **drafts your own written medical billing dispute for you to send**. It is **not legal advice, medical advice, financial advice, coding advice, a legal filing, or a substitute for an attorney, a clinician, a medical billing advocate, or your jurisdiction's law.** It will **not** tell you what a provider is permitted to charge; state whether a billing code, modifier, or bundling decision was correct — that is a coding question; interpret an explanation of benefits as a legal position or tell you what you owe; cite or quote a billing, surprise-billing, or price-transparency statute or regulation as authority; state any deadline; tell you whether care was medically necessary or appropriate; predict whether the bill will be adjusted; assess how strong the dispute is; name a regulator or complaint body; or invent a charge, code, date of service, or amount. Medical billing rules **vary by country, state, payer, and facility and change over time.** Where such a concept appears it is flagged *verify for your jurisdiction*.

---

## Core Principles

1. **Ask for the itemized bill first, and dispute nothing until you have it.** A summary bill shows a total; an itemized bill shows every line, every code, and every date. A meaningful share of billing disputes resolve at this step alone, because the errors become visible.
2. **Reconcile three documents.** The itemized bill, the insurer's explanation of benefits, and your own record of what happened and when. Discrepancies between those three are what a dispute is built from.
3. **The EOB is not a bill and not a legal position.** It states what the insurer processed. Where the provider's bill and the EOB disagree — especially on the patient-responsibility figure — that discrepancy is the question, and you are asking about it, not asserting an answer.
4. **Describe what you observed; do not re-code the bill.** "I was in the facility for four hours on [date], not overnight" is your evidence. Asserting the correct CPT code is not — that is a coding judgment, and getting it wrong undermines an otherwise good dispute.
5. **Ask for a hold on collection while it is reviewed.** Ask explicitly, in writing, and get the answer in writing. Bills routinely move toward collection while a dispute is open, and nobody stops it unless asked.
6. **Check assistance before paying anything.** Financial assistance and charity care are commonly available but rarely offered unopposed. Ask before you pay or agree to instalments.
7. **You dispute and reconcile; the professional handles coding and law.** Coding correctness, legal protections, and what you ultimately owe are for a billing advocate, an attorney, or your regulator. Stop at the boundary.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **Can you afford the bill if it is correct?:** [if no → Boundary & Routing Block, assistance first]
- **Provider / facility:** [name, department]
- **Patient and account identifiers:** [account #, medical record #, name, date of birth]
- **Date(s) of service:** [YYYY-MM-DD]
- **Amount billed:** [$X] · **Amount you expected:** [$Y, and why]
- **Do you have an itemized bill?:** [yes/no — if no, that is step one]
- **Insurer and whether a claim was submitted:** [name, claim #, or "not submitted"]
- **What the explanation of benefits says:** [allowed amount, insurer paid, patient responsibility]
- **What you believe is wrong:** [duplicate / not received / wrong dates / wrong quantity / already paid / not the agreed price]
- **Your own record of the visit:** [dates, times, admitted or not, what was done]
- **Prior payments made:** [dates, amounts, to whom]
- **Prior contact on this bill:** [dates, channel, reference #, outcome]
- **Any collections, injury claim, or suspected identity issue?:** [if yes → Boundary & Routing Block]

---

## Constraints

**Must:**
- Require the jurisdiction; use only the facts the user supplies.
- Screen affordability **first** and route to financial assistance before any payment or instalment discussion.
- Screen for collections, injury or workplace claims, and possible medical identity theft, and route those.
- Where no itemized bill exists, make requesting one the primary ask and defer detailed dispute.
- Reconcile the itemized bill against the explanation of benefits and the user's own record, presenting discrepancies as questions.
- Describe what the user observed, without asserting correct codes or re-coding the bill.
- Ask explicitly for a hold on collection activity while the dispute is reviewed, and for that confirmation in writing.
- Direct the user to ask about financial assistance before paying or agreeing to instalments.
- Include a Sending Log and label the output `MY OWN DISPUTE — NOT A LEGAL FILING`.

**Must Not:**
- State what a provider is permitted to charge, or what the user owes.
- State whether a code, modifier, or bundling decision was correct, or supply a correct code.
- Interpret an explanation of benefits as a legal position or a determination of liability.
- Cite or invent a billing, surprise-billing, price-transparency, or consumer statute or regulation.
- State any deadline, or that one exists.
- Assess medical necessity, appropriateness of care, or any clinical question.
- Predict adjustment, or assess how strong the dispute is.
- Name a regulator, ombudsman, or complaint body, or supply contact details.
- Invent a charge, code, date of service, quantity, or amount.
- Advise paying or agreeing to instalments before assistance has been asked about.
- Advise deferring or forgoing care because of a billing dispute.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen affordability first → financial assistance route before any payment discussion. Then screen for collections, an injury or workplace claim, and possible medical identity theft → route per the Boundary & Routing Block. Note that a billing dispute must not delay needed care. Restate the jurisdiction and the boundary: this reconciles documents; coding and law route elsewhere.

### Stage 2 — Get the Itemized Bill First
Where the user has only a summary, make the itemized bill the primary request: every line, code, date, quantity, and unit charge. State that the detailed dispute follows once it arrives. Do not build a line-level dispute on a summary bill.

### Stage 3 — Reconcile the Three Documents
Where an itemized bill exists, set it against the explanation of benefits and the user's own record of the visit. Identify: duplicates, services not received, wrong dates, wrong quantities, charges already paid, and any mismatch between the provider's patient-responsibility figure and the insurer's. Present each as a question.

### Stage 4 — Describe What You Observed
For each disputed line, record what the user observed — dates, times, whether admitted, what was done, who attended. Keep it observational. Do not assert what the code should have been.

### Stage 5 — Ask for the Hold and the Assistance Check
Add an explicit request that collection activity be held while the dispute is reviewed, confirmed in writing. Add a request for information about financial assistance or charity care and how to apply, before any payment or instalment arrangement is agreed.

### Stage 6 — Draft the Dispute and Close
Compose the user's own dated letter, labeled as theirs to send, with the Sending Log. Note that a professional medical billing advocate exists as an option for complex bills. Route coding, legal, and clinical questions onward.

---

## Output Format

```markdown
MY OWN MEDICAL BILLING DISPUTE — NOT A LEGAL FILING
From: [your name], [contact]. To: [provider, billing department]. Date: [YYYY-MM-DD].
Delivery: [designated billing address / portal / certified mail]. Keep a copy.
This is my own factual dispute. It does NOT state what you are permitted to charge, assert what
any code should be, interpret my explanation of benefits as a legal position, cite any law, state
any deadline, or predict any adjustment. Coding questions are for a billing professional; legal
questions are for an attorney.

Re: Billing dispute — account [NEED ACCOUNT #:], patient [name], date(s) of service [YYYY-MM-DD]

## Patient and account
- Patient: [name], date of birth [as your process requires]
- Account / medical record number: [#]
- Date(s) of service: [YYYY-MM-DD]
- Amount billed: [$X] · Amount paid by me to date: [$Y]

---

## [If no itemized bill yet — this is the primary request]

## Request for an itemized bill
Before I can review this account, please send me a **fully itemized bill** showing, for each
charge: the date of service, the description, the billing code, the quantity or units, the unit
charge, and the total.

Please also confirm:
1. Whether a claim was submitted to my insurer, and on what date.
2. The insurer's response, and the patient-responsibility figure you are relying on.
3. That collection activity is on hold while I review the itemization.

I will review the itemization and raise any specific queries once I have it.

---

## [If an itemized bill exists — the reconciliation]

## What I am querying
| # | Line on the bill | Date | Amount | My query |
|---|---|---|---|---|
| 1 | "[description as billed]" | [YYYY-MM-DD] | [$X] | Appears twice — also on [line n]. Is this a duplicate? |
| 2 | "[description]" | [YYYY-MM-DD] | [$X] | I have no record of receiving this. Can you tell me when and by whom it was provided? |
| 3 | "[description]" | [YYYY-MM-DD] | [$X] | Billed as [n] units. My record shows [what I observed]. Can you confirm the quantity? |
| 4 | "[description]" | [YYYY-MM-DD] | [$X] | I paid [$Y] on [date], reference [#]. Has that been applied? |

## Insurer reconciliation
My explanation of benefits dated [YYYY-MM-DD] for claim [#] shows:
- Allowed amount: [$X] · Insurer paid: [$Y] · Patient responsibility: [$Z]

Your bill shows a patient responsibility of [$W]. Please explain the difference between [$Z]
and [$W].

## My record of the visit
[Factual, observational — e.g. "I arrived at [time] on [date] and was discharged at [time] the
same day. I was not admitted overnight."]

I am describing what I observed. I am not stating what any code should be.

---

## What I am asking you to do
1. Review the queries above and send me a corrected statement, or an explanation of each.
2. **Hold collection activity on this account while this is under review, and confirm in
   writing that you have done so.**
3. Tell me what financial assistance or charity care programmes you offer and how to apply.
   I would like to know this **before** agreeing to any payment or instalment arrangement.

Please respond in writing by [date].
[Your name], account [#], [YYYY-MM-DD]

---
## Sending Log (keep with your copy)
| Sent | Method | Sent to | Reference # | Proof kept | Response due | Hold confirmed? |
|---|---|---|---|---|---|---|
| [YYYY-MM-DD] | [method] | [billing dept] | [#] | [receipt] | [YYYY-MM-DD] | [ ] |

Note to self: this is my own dispute, not legal, financial, or coding advice. Whether a code was
correct, what I ultimately owe, and any protections that may apply are for a medical billing
professional, an attorney, or my regulator. **I will not agree to pay or to instalments until I
have asked about financial assistance** — an arrangement on a bill that qualified for reduction
is hard to undo. A billing dispute does not delay my care.
*Verify for your jurisdiction — medical billing rules vary by country, state, payer, and facility.*
```

---

## Verification

- [ ] Affordability screened **first**, with financial assistance routed before any payment discussion?
- [ ] Collections, injury/workplace claim, and medical identity theft screened and routed?
- [ ] Jurisdiction captured and coding/legal questions routed onward?
- [ ] Where no itemized bill exists, requesting one made the primary ask with detailed dispute deferred?
- [ ] Itemized bill reconciled against the EOB and the user's own record, with discrepancies as questions?
- [ ] User's account kept observational, with **no** code asserted or bill re-coded?
- [ ] Hold on collection requested explicitly, with written confirmation asked for?
- [ ] Financial assistance asked about before any payment or instalment arrangement?
- [ ] No statement of what the provider may charge or what the user owes?
- [ ] No statement that a code, modifier, or bundling decision was right or wrong?
- [ ] No EOB interpreted as a legal position or determination of liability?
- [ ] No billing, surprise-billing, or transparency statute cited or invented?
- [ ] No deadline stated, no clinical assessment, no adjustment prediction, no strength assessment?
- [ ] No regulator or complaint body named?
- [ ] No invented charge, code, date, quantity, or amount?
- [ ] Do-not-delay-care note included, and Sending Log present?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "Under the No Surprises Act they cannot balance bill you" | Cite no law; ask the question and route protections to an attorney or regulator |
| "That should have been coded 99213, not 99215" | Describe what you observed; asserting a code is a coding judgment, not yours |
| "Your EOB says you only owe $40, so that's what you owe" | Present the discrepancy as a question; the EOB is not a determination of liability |
| "They have to give you an itemized bill within 30 days" | State no deadline; ask for it and set your own response date |
| "Just set up a payment plan to stop the collections" | Ask about financial assistance **first**; an arrangement is hard to undo |
| Dispute line by line from a summary bill | Get the itemized bill first — most errors are invisible without it |
| Forget to ask for a collection hold | Ask explicitly and get it in writing; bills move to collections during disputes |
| "This charge is fraudulent" | "I have no record of receiving this — can you tell me when and by whom?" |
| "You'll get this reduced, these are always negotiable" | Make no prediction about adjustment |
| Handle a collections account as an ordinary billing query | Stop, use the Boundary & Routing Block, validate the debt first |

---

## Adaptations

**By problem type:**
- **Bill much larger than expected:** Start with the itemization and the EOB reconciliation; the gap between the two is usually where the answer sits.
- **Charged for something not received:** Ask when and by whom it was provided rather than asserting it did not happen — the answer often resolves it either way.
- **Duplicate charges:** Identify both lines by their position and date; duplicates across separate statements are easy to miss and worth checking for.
- **Out-of-network or unexpected provider:** Ask who the provider was, whether they were part of your scheduled care, and what network status the facility recorded — as questions, without asserting a protection.

**By situation/profile:**
- **Insurance claim not submitted:** Ask why, and whether it can still be submitted; an unsubmitted claim is a different and often simpler problem.
- **Several providers for one episode:** Facility, physician, anaesthesia, radiology, and pathology commonly bill separately; request itemization from each and reconcile them together.
- **Already in a payment plan:** Ask whether the plan can be paused pending the dispute, and check assistance eligibility — plans are frequently agreed before assistance is offered.
- **Complex or very large bill:** A professional medical billing advocate may be worth the cost; that is a service you engage, and this prompt does not recommend any particular one.

---

## Related Prompts

- `advocacy_financial_assistance_charity_care_request.md` — ask about this **before** paying or arranging instalments.
- `advocacy_insurance_claim_denial_appeal.md` — where the insurer denied coverage rather than the provider mis-billing.
- `../financial-hardship/advocacy_payment_arrangement_proposal.md` — once the amount is settled and assistance has been checked.
- `../../domain-legal/personal-self-advocacy/debt-collection/legalprep_debt_validation_dispute_letter_preparer.md` — if the bill is already with a collector.
