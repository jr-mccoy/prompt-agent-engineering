---
title: "Student Loan Servicer Dispute — Correct a Balance, Payment, or Plan Error in Writing"
category: advocacy
description: "[SELF-SUBMIT] Help a borrower draft THEIR OWN written error notice to a student loan servicer — a misapplied or missing payment, a wrong balance or interest figure, an unprocessed repayment-plan or deferment request, a miscounted qualifying-payment tally, or a transfer-related error — with a reconciliation table from the borrower's own records, one correction per item, and a request for the account history the servicer relied on. Does NOT cite loan programme rules or statute as authority, state eligibility for any plan or forgiveness, compute what the balance should be, state response deadlines, name an ombudsman or agency, predict outcomes, or invent loan data. Distinct from advocacy_credit_report_dispute (the bureau entry) and advocacy_hardship_assistance_request (asking for relief rather than correcting an error). Not legal or financial advice."
techniques:
  - CM-01
  - RT-05
  - OC-03
  - ST-03
  - QA-01
difficulty: intermediate
intended_use: model-testing
tags:
  - written-advocacy
  - self-advocacy
  - student-loans
  - servicer-dispute
  - self-submit
  - consumer
updated: "2026-09-24"
related_prompts:
  - domain-written-advocacy/financial-hardship/advocacy_credit_report_dispute.md
  - domain-written-advocacy/financial-hardship/advocacy_hardship_assistance_request.md
  - domain-written-advocacy/cross-cutting/advocacy_response_analyzer.md
  - domain-written-advocacy/institutions-and-records/advocacy_regulator_complaint_drafter.md
---

**Purpose:** Help you write **your own** written error notice to the company that services your student loans when its records do not match yours — a payment applied to the wrong loan or not at all, a balance or interest figure you cannot reconcile, a plan or deferment request that was never processed, a count of qualifying payments that looks short, or something that went wrong when the loan was transferred. The letter puts your records beside theirs, line by line, and asks for one specific correction per item.

**When to use:** You have your own evidence — bank statements, confirmation emails, submitted forms — and the servicer's statement, portal, or phone answer disagrees with it.

**When NOT to use:** The problem is how the loan appears on your **credit report** → `advocacy_credit_report_dispute.md` (send both if both are wrong). You can't afford payments and want relief rather than a correction → `advocacy_hardship_assistance_request.md`. You don't recognize the loan at all → treat as possible identity theft: `domain-legal/personal-self-advocacy/identity-theft/`. The loan is in default, in collections, or wages or refunds are being taken → the Boundary & Routing Block, first.

---

## Boundary & Routing Block

Use a different pathway if:
- **The loan is in default, with a collector, or wages, tax refunds, or benefits are being taken** → contact **legal aid or a nonprofit student loan counselling service** now `[VERIFY: locate a free or nonprofit student loan assistance service from an official government source]`. The options in default are different and time-sensitive.
- **You are being sued or received court papers** → attorney or legal aid immediately.
- **You are deciding which repayment plan or forgiveness route to pursue** → that is a choice, not an error. Use the loan holder's own official information and a nonprofit counsellor; this prompt does not assess eligibility.
- **Someone contacts you offering to fix your loans for a fee** → do not share login details. Verify any company independently before engaging `[VERIFY: check against an official government source]`.
- **The servicer gives a response or appeal date** → act on it.

This prompt is educational support for preparing your own correspondence. It is not a substitute for legal or financial services.

---

## Scope Boundary — Read First

This **drafts your own written error notice for you to send**. It is **not legal advice, financial advice, a legal filing, or a substitute for an attorney, a nonprofit counsellor, or official programme guidance.** It will **not** cite a loan statute, regulation, or programme rule as authority; tell you whether you qualify for any repayment plan, deferment, forbearance, discharge, or forgiveness; state how interest accrues or capitalizes; compute what your balance or payment count should be; state how long the servicer has to respond; name a government ombudsman, agency, or complaint portal; predict the outcome; or invent a loan number, payment, date, or balance. Loan programmes **differ between government-held and private loans, by country, and by date, and change frequently.** Where such a concept appears it is flagged *verify with official programme guidance*.

---

## Core Principles

1. **Your records beside theirs.** The strength of an error notice is a table: date, what you paid or submitted, your proof, what their record shows. It turns an argument into a reconciliation.
2. **One item, one correction.** Each discrepancy gets its own row and its own requested correction. "Fix my account" gets a generic reply.
3. **Ask for their full history.** Request the complete payment and transaction history and the record of any plan or deferment requests received. You cannot find the error without their version.
4. **Label it as an error notice.** Use the words "written notice of error" and the account number at the top so it is routed to the team that investigates, not general correspondence.
5. **Keep paying what you can while it is resolved.** An error dispute does not by itself pause what is due — ask the servicer in writing what, if anything, you should pay while it investigates.
6. **Don't compute the answer.** Say what you paid and when; ask them to show how it was applied. Your own recalculation of interest is likely to be wrong in a way that distracts.

---

## Your Input

- **Your jurisdiction:** [required]
- **Loan type as you understand it:** [government-held / private / unsure — flag `[VERIFY]`]
- **Servicer and account number; loan IDs if shown:** [#]
- **Default, collections, wage or refund offset, or lawsuit?:** [if yes → Boundary & Routing Block]
- **Each discrepancy:** [date · what you did (paid $X / submitted form) · your proof · what their record shows]
- **Any transfer between servicers, with date:** [old servicer, new servicer, YYYY-MM-DD]
- **Prior contact:** [date, channel, reference, outcome]
- **Any response date the servicer gave:** [YYYY-MM-DD]

---

## Constraints

**Must:**
- Require the jurisdiction; use only records the user supplies.
- Screen for default, collections, offsets, and litigation first, and route.
- Label the letter "written notice of error" with the account number in the subject line.
- Build a reconciliation table, one row per discrepancy, each with proof or `[NEED DOCUMENT:]`.
- State one requested correction per row.
- Request the full payment and transaction history and the record of forms received.
- Ask what the borrower should pay while the investigation runs.
- Include a Sending Log and label the output `MY OWN NOTICE — NOT A LEGAL FILING`.

**Must Not:**
- Cite or invent a statute, regulation, or programme rule, or name a plan's conditions as rules.
- State that the borrower qualifies for any plan, deferment, discharge, or forgiveness.
- Compute a corrected balance, interest amount, or qualifying-payment count.
- State a servicer response period.
- Name an ombudsman, agency, or complaint portal, or supply contact details.
- Advise stopping payment.
- Predict the outcome.
- Invent loan numbers, payments, dates, or balances.

---

## Instructions

### Stage 1 — Screen and Frame
Screen default, collections, offsets, litigation, and fee-charging "relief" companies → route. Record any response date the servicer gave. Confirm the loan type or flag it `[VERIFY]`.

### Stage 2 — Build the Reconciliation
For each discrepancy, one row: date, what the borrower did, the proof, what the servicer shows, the gap. Where a transfer occurred, add the transfer date so the error can be located on one side of it.

### Stage 3 — Specify Corrections
For each row, the specific correction: apply payment of $X dated Y to loan Z; record form received on date Y; show the calculation of a figure. Where the user does not know the right answer, the correction is "explain how this was calculated."

### Stage 4 — Draft the Notice and Close
Compose the dated notice with the table, corrections, history request, and the interim-payment question. Add the Sending Log and a note on escalation via `[VERIFY:]`.

---

## Output Format

```markdown
MY OWN WRITTEN NOTICE OF ERROR — NOT A LEGAL FILING
From: [your name], [contact]. To: [servicer — the address it designates for error notices
or disputes, if any]. Date: [YYYY-MM-DD]. Delivery: [designated address / portal upload with
confirmation / certified mail]. Keep a copy.
This is my own notice. It does NOT cite law, claim eligibility for any programme, or calculate
what my balance should be.

Re: WRITTEN NOTICE OF ERROR — account [#], loan(s) [IDs]

## Discrepancies between my records and yours
| # | Date | What I did | My proof (enclosed) | What your record shows | Correction I am asking for |
|---|---|---|---|---|---|
| 1 | [YYYY-MM-DD] | Paid [$X] | [bank statement p.2] | [not shown / applied to loan B] | Apply to loan [A] as of [date] |
| 2 | [YYYY-MM-DD] | Submitted [form] | [upload confirmation #] | [no record] | Record as received [date]; process it |
| 3 | — | — | — | Balance [$Y] | Show how this figure was calculated |

## Also requested
1. My complete payment and transaction history for [period], showing how each payment was applied.
2. Your record of every form or request received from me since [date].
3. Written confirmation of what, if anything, I should pay while you investigate.

Please respond in writing by [date].
[Your name], account [#], [YYYY-MM-DD]

---
## Sending Log (keep with your copy)
| Sent | Method | Sent to | Reference # | Proof kept | Response due | Outcome |
|---|---|---|---|---|---|---|
| [YYYY-MM-DD] | [method] | [error-notice address] | [#] | [receipt] | [YYYY-MM-DD] | [ ] |

Note to self: I will keep paying what I can unless told otherwise in writing. Eligibility and
programme rules come from official guidance and a nonprofit counsellor —
`[VERIFY: identify official programme guidance and any complaint route from an official source]`.
*Verify with official programme guidance — loan rules change frequently.*
```

---

## Verification

- [ ] Default, collections, offsets, litigation, and fee-charging "relief" firms screened and routed?
- [ ] "Written notice of error" and account number in the subject line?
- [ ] One table row per discrepancy, each with proof or `[NEED DOCUMENT:]`?
- [ ] One specific correction per row?
- [ ] Full history and forms-received record requested?
- [ ] Interim-payment question asked; no advice to stop paying?
- [ ] No statute, programme rule, eligibility, interest method, or response period asserted?
- [ ] No computed balance or payment count?
- [ ] No ombudsman or agency named; `[VERIFY:]` used?
- [ ] Sending Log included; no invented loan data?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "You qualify for forgiveness after [n] payments" | State no eligibility; ask for their count and how it was reached |
| "Under [regulation] they must respond within [n] days" | Ask for a response by a date you set; cite nothing |
| "Your correct balance is $X after interest" | Ask them to show how their figure was calculated |
| "Stop paying until they fix it" | Ask in writing what to pay during the investigation |
| "File with the [named ombudsman]" | `[VERIFY: identify the route from an official source]` |
| "Please fix my account" | One row, one correction, per discrepancy |
| "I paid in March, I think" | Exact date and amount from the bank statement, or `[NEED DOCUMENT:]` |
| Draft a correction letter while wages are being garnished | Stop — legal aid or nonprofit counselling now |

---

## Adaptations

**By error type:**
- **Misapplied payment:** Ask how the payment was allocated across loans and between interest and principal, and ask for the allocation you want if the loan terms let you direct it — as a request, not a right.
- **Unprocessed plan or deferment request:** Submission date, channel, confirmation number; ask for it to be recorded as received on that date.
- **Qualifying-payment count:** List the months you believe were missed with proof of payment; ask for their month-by-month record rather than asserting the count.
- **Transfer error:** Send to the current servicer and ask it to obtain the prior servicer's history; keep both in the record.

**By loan type:**
- **Private loan:** Your promissory note and the lender's own terms are the reference points; quote them where you hold them.

---

## Related Prompts

- `advocacy_credit_report_dispute.md` — if the same error is showing on your credit report.
- `advocacy_hardship_assistance_request.md` — if the need is relief rather than correction.
- `../cross-cutting/advocacy_response_analyzer.md` — to read what the servicer actually corrected.
- `../institutions-and-records/advocacy_regulator_complaint_drafter.md` — once the correct body is verified.
