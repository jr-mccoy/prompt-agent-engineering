---
title: "Account Closure Request — Close the Account and Confirm Nothing Is Left Open"
category: advocacy
description: "[SELF-SUBMIT] Help a person draft THEIR OWN written request to close an account entirely — final balance, return or transfer of funds or equipment, removal of stored payment methods, and written confirmation that the account is closed — distinguishing closure from cancelling a service and from deleting personal data. Does NOT cite account-closure or banking rules as authority, state what the provider must do with a balance or with retained records, predict compliance, or invent account details. Not legal advice."
techniques:
  - CM-01
  - DS-01
  - ST-02
  - ST-03
  - QA-01
difficulty: intermediate
intended_use: model-testing
tags:
  - written-advocacy
  - self-advocacy
  - consumer
  - account-closure
  - self-submit
  - documentation
updated: "2026-08-01"
related_prompts:
  - domain-written-advocacy/accounts-and-billing/advocacy_subscription_cancellation_request.md
  - domain-written-advocacy/privacy-and-data/advocacy_data_deletion_request.md
  - domain-written-advocacy/cross-cutting/advocacy_followup_and_deadline_tracker.md
  - domain-written-advocacy/accounts-and-billing/advocacy_recurring_charge_dispute.md
---

**Purpose:** Help you write **your own** dated request to close an account outright — a bank or brokerage account, a retailer or marketplace account, a utility account, an online service — and to get written confirmation that it is closed, that any balance has been settled or returned, that stored payment methods are removed, and that nothing remains that could generate a future charge or a credit-file entry.

**When to use:** You want the account itself gone rather than a single service stopped, and you want a record of the closure request and its confirmation.

**When NOT to use:** You only want to stop a recurring charge or subscription → `advocacy_subscription_cancellation_request.md`. You want your personal data erased, which is a different request with a different legal basis → `../privacy-and-data/advocacy_data_deletion_request.md` (often sent alongside this one). You are closing an account because of suspected fraud or identity theft → `domain-legal/personal-self-advocacy/identity-theft/` and the provider's fraud team first. The account is in dispute, in arrears, or with a collector → route to an attorney or legal aid.

---

## Boundary & Routing Block

Use a different pathway if:
- **The account is in arrears, in dispute, or has been referred to a debt collector** → closing it does not resolve the balance, and a closure request can be treated as an admission or ignored entirely. Route to an attorney or **legal aid**, and see `domain-legal/personal-self-advocacy/debt-collection/legalprep_debt_validation_dispute_letter_preparer.md`.
- **You suspect fraud or identity theft on the account** → contact the provider's fraud team through its official channel first; see `domain-legal/personal-self-advocacy/identity-theft/`. Closure comes after, not instead.
- **This is a financial account holding funds, securities, or a credit line** → how a balance must be returned, what happens to a credit line on closure, and any effect on your credit file are **not** questions this prompt answers. Route to the provider's written process and, for consequences, to an attorney or a nonprofit financial counsellor.
- **The account is held jointly, in trust, for a business, or for someone who has died** → closure typically requires specific authority and documentation. Route to the provider's designated process and to an attorney.
- **A claim or dispute deadline may be running** → route to an attorney or legal aid promptly.

This prompt is educational support for preparing your own correspondence. It is not a substitute for legal or financial services.

---

## Scope Boundary — Read First

This **drafts your own written account-closure request for you to send**. It is **not legal advice, legal strategy, financial advice, a legal filing, or a substitute for an attorney, a financial professional, or your jurisdiction's law.** It will **not** tell you what a provider is required to do with a balance, a deposit, a credit line, or retained records; state or cite an account-closure, banking, escheatment, or record-retention rule as authority; tell you how closure will affect your credit file; predict whether the provider will comply or how long it will take; assess how strong your position is; or invent an account number, balance, equipment identifier, or contract term. Closure and retention rules **vary by account type, state, and country and change over time.** Where such a concept appears it is flagged *verify for your jurisdiction*.

---

## Core Principles

1. **Closure, cancellation, and deletion are three different requests.** Cancelling stops a service. Closing ends the account relationship. Deleting removes personal data. Providers treat them separately, so ask for exactly the one you want — and send the data-deletion request as its own letter if you want that too.
2. **Settle the balance question explicitly, in both directions.** State what you believe is owed or owing, ask them to confirm it, and say where any credit balance should be sent. An unaddressed balance is the most common reason a "closed" account reappears months later.
3. **Name everything that could generate a future charge.** Stored payment methods, recurring authorizations, linked subscriptions, rented equipment, overdraft or credit facilities, auto-reload settings. Ask for each to be removed or returned, and ask them to confirm none remains.
4. **Ask what they need from you, before they ask you.** Equipment return, a final meter reading, a signed form, identity verification. Requesting the list up front prevents a closure stalling for weeks on a step nobody mentioned.
5. **Get the closure confirmed in writing with a date.** "Closed" without a date is not usable later. The confirmation, with its effective date, is the artifact that ends the relationship.
6. **Keep the record after closure.** Once an account is closed you often lose portal access to statements and correspondence. Download what you need *before* sending the request.
7. **You request and record; the professional handles consequences.** What closure does to a credit file, a balance, or retained records is for an attorney or a financial professional. Stop at the boundary.

---

## Your Input

- **Your jurisdiction (state/city/country):** [required]
- **Provider and account type:** [bank / retailer / utility / marketplace / online service]
- **Account identifiers:** [account #, username, registered email, name on account]
- **Designated closure channel:** [address / portal / form] or [NEED CHANNEL: locate it]
- **Current balance, as you understand it:** [owed to you / owed by you / zero / unknown]
- **Where any credit balance should go:** [payment method, bank details to be supplied securely]
- **Stored payment methods and recurring authorizations:** [list]
- **Linked services or subscriptions on the account:** [list]
- **Equipment or property held:** [routers, meters, cards, devices]
- **Effective date you want:** [immediately / after final billing on YYYY-MM-DD]
- **Statements or records you still need:** [what, and whether you have downloaded them]
- **Any arrears, dispute, fraud, joint holder, or deceased-holder dimension?:** [if yes → Boundary & Routing Block]

---

## Constraints

**Must:**
- Require the jurisdiction; use only the facts the user supplies.
- Distinguish closure from service cancellation and from data deletion, and point to the right sibling prompt for each.
- Direct the user to the provider's designated closure channel, flagging `[NEED CHANNEL:]` if unknown.
- Address the balance explicitly in both directions and state where a credit balance should be sent.
- Enumerate every stored payment method, recurring authorization, linked service, and item of equipment, and request removal or return of each.
- Ask the provider what steps it requires from the user to complete closure.
- Request written confirmation of closure with an effective date.
- Advise downloading statements and correspondence before sending.
- Include a Sending Log and label the output `MY OWN LETTER — NOT A LEGAL FILING`.

**Must Not:**
- State what the provider must do with a balance, deposit, credit line, or retained records.
- Cite or invent a banking, closure, escheatment, or record-retention rule or deadline.
- State or predict how closure will affect the user's credit file.
- Predict whether the provider will comply, or how long closure will take.
- Assess how strong the user's position is.
- Draft a legal threat or a damages claim.
- Include bank account or card numbers in the letter body, or advise sending full details insecurely.
- Invent an account number, balance figure, equipment identifier, or contract term.
- Present closure as a way to avoid a disputed balance.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for arrears, an active dispute, a collector, fraud, a financial account with funds or credit, a joint or deceased holder, or a running deadline → route per the Boundary & Routing Block. Restate the jurisdiction and the boundary: this requests closure; consequences are for an attorney or a financial professional.

### Stage 2 — Confirm It Is Closure the User Wants
Check the request against the three neighbouring actions — cancel a service, close the account, delete personal data. Confirm which the user wants, note that a data-deletion request is separate and can be sent alongside, and route to the sibling prompt for any part this letter will not cover.

### Stage 3 — Preserve the Record Before Closing
Instruct the user to download statements, invoices, correspondence, tax documents, and order history *before* sending, since portal access usually ends at closure. List what they still need as `[NEED DOCUMENT:]` items to retrieve first.

### Stage 4 — Inventory Everything Attached to the Account
Enumerate stored payment methods, recurring authorizations, linked subscriptions, credit or overdraft facilities, loyalty balances, and equipment held. Each becomes a line in the letter requesting removal, settlement, or return.

### Stage 5 — Settle the Balance and the Steps Required
State the balance as the user understands it, ask the provider to confirm it, and specify where a credit balance should be sent — without putting full financial details in the letter. Ask the provider to state every step it requires from the user to complete closure, and by when.

### Stage 6 — Draft the Letter and Close
Compose the user's own dated closure request, labeled as theirs to send, with the Sending Log. Advise checking for further charges or statements for at least two billing cycles after the confirmed closure date. Route consequences and disputes to an attorney or a financial professional.

---

## Output Format

```markdown
MY OWN ACCOUNT CLOSURE REQUEST — NOT A LEGAL FILING
From: [your name], [contact]. To: [provider, designated closures channel]. Date: [YYYY-MM-DD].
Delivery: [portal / designated email / certified mail]. Keep a copy.
This is my own closure request. It does NOT state what the provider is legally required to do
with any balance or record, cite any banking or retention rule, predict any outcome, or address
my credit file. Those questions are for an attorney or a financial professional.

Re: Request to close account [NEED ACCOUNT #: from your statement] — [account type]

## Account details
- Name on account: [name]  ·  Account number / username / registered email: [identifiers]
- Account type: [type]  ·  Opened: [YYYY-MM-DD, if known]

## What I am requesting
Please **close this account** effective [immediately / after final billing on YYYY-MM-DD].

This is a request to close the account. [If applicable:] I am separately sending a request
regarding my personal data.

## Balance
My understanding of the balance is: [owed to me $X / owed by me $X / zero / unknown].
Please confirm the final balance in writing.
[If a credit balance is due:] Please return any credit balance to [payment method / the account
on file]. I will supply payment details through your secure channel on request — I am not
including them in this letter.

## Please remove, settle, or arrange return of the following
| Item | Detail | What I am asking |
|---|---|---|
| Stored payment method | [card ending NNNN] | Remove from the account |
| Recurring authorization | [name] | Cancel; no further charges authorized |
| Linked subscription | [name] | Confirm cancelled or transferred |
| Credit / overdraft facility | [detail] | Confirm closed |
| Equipment held | [router / meter / card / device] | Tell me how and where to return it |
| Loyalty / stored balance | [amount] | Tell me how it is settled |
| [NEED DOCUMENT: ...] | | |

I do not authorize any further charges to any payment method associated with this account
after the effective date above.

## What I am asking you to send me
Please confirm in writing by [date]:
1. That the account is closed, and the effective closure date.
2. The final balance and how it has been settled.
3. That all stored payment methods and recurring authorizations have been removed.
4. Every step you still require from me to complete the closure, and by when.

[Your name], [YYYY-MM-DD]

---
## Sending Log (keep with your copy)
| Sent | Method | Sent to | Proof kept | Confirmation due | Confirmation received |
|---|---|---|---|---|---|
| [YYYY-MM-DD] | [method] | [channel] | [ticket # / receipt] | [YYYY-MM-DD] | [ ] |

Before sending, download and store: [statements / invoices / tax documents / order history /
correspondence] — portal access usually ends at closure.
After closure, check for further charges or statements on: [YYYY-MM-DD], [YYYY-MM-DD].

Note to self: this is my own letter, not legal or financial advice. What the provider must do
with a balance or retained records, and any effect on my credit file, are for an attorney or a
financial professional. Closing an account does not resolve a disputed balance.
*Verify for your jurisdiction — closure and retention rules vary by account type and country.*
```

---

## Verification

- [ ] Jurisdiction captured and consequences routed *verify with an attorney or financial professional*?
- [ ] Closure distinguished from service cancellation and data deletion, with siblings named?
- [ ] Designated closure channel identified, or flagged `[NEED CHANNEL:]`?
- [ ] Balance addressed in both directions, with confirmation requested?
- [ ] Credit-balance destination stated without full financial details in the letter body?
- [ ] Every stored payment method, authorization, linked service, and item of equipment listed?
- [ ] Provider asked to state the steps it still requires, and by when?
- [ ] Written confirmation of closure with an effective date requested?
- [ ] Record-preservation step included before sending?
- [ ] No claim about what the provider must do with a balance, deposit, or record?
- [ ] No banking, closure, escheatment, or retention rule cited or invented?
- [ ] No statement or prediction about credit-file effect, compliance, or timing?
- [ ] No invented account number, balance, or equipment identifier?
- [ ] Sending Log included with post-closure check dates?
- [ ] Arrears, dispute, fraud, joint-holder, or deceased-holder dimension screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "They must return your balance within 30 days" | Ask them to confirm the balance and how it will be settled; the rule is for an attorney |
| "Closing this will improve your credit score" | Say nothing about credit-file effects; route to a financial professional |
| "Close the account and the disputed charge goes away" | Closure does not resolve a disputed balance; route the dispute separately |
| "They're legally obliged to delete your data on closure" | Deletion is a separate request with its own basis — send the data-deletion prompt's letter |
| Put the user's full bank account and routing numbers in the letter | Offer to supply details through the provider's secure channel |
| Guess the balance so the letter reads as complete | Flag `[NEED AMOUNT: from your latest statement]` |
| "This will be processed within five working days" | Make no prediction about timing or compliance |
| Send the closure request before downloading statements | Preserve the record first — portal access usually ends at closure |
| Close an account that is with a collector to make it stop | Stop, use the Boundary & Routing Block, route to an attorney or legal aid |
| Treat a joint or deceased-holder account as a routine closure | Route to the provider's designated process and an attorney |

---

## Adaptations

**By account type:**
- **Bank, credit, or brokerage:** Ask specifically about pending transactions, scheduled payments, direct debits pointing at the account, and any credit line — and route consequences to a financial professional rather than assuming them.
- **Retailer or marketplace:** Ask about stored payment methods, saved addresses, open orders, returns in flight, and any seller balance; note that order history is usually lost at closure.
- **Utility or telecom:** Expect a final meter reading, equipment return, and a final bill — ask for the process and the return address in the same letter. See `advocacy_utility_telecom_service_dispute.md`.
- **Online service or platform:** Distinguish deactivation from deletion; ask which this is, and whether the account can be reinstated afterwards.

**By situation/profile:**
- **You also want data deleted:** Send both letters, reference each in the other, and track them separately — providers process them through different teams.
- **Provider offers deactivation instead:** Ask in writing what deactivation retains and whether it can generate charges; if the answer is unclear, restate the closure request.
- **Equipment to return:** Ask for a return label and address in writing, and keep the shipping receipt — unreturned equipment is a common source of later charges.
- **Arrears or dispute:** Boundary & Routing Block first; do not use closure to sidestep a balance.

---

## Related Prompts

- `advocacy_subscription_cancellation_request.md` — to stop a recurring service without closing the account.
- `../privacy-and-data/advocacy_data_deletion_request.md` — to have personal data erased, sent alongside this letter.
- `advocacy_recurring_charge_dispute.md` — if charges continue after the confirmed closure date.
- `../cross-cutting/advocacy_followup_and_deadline_tracker.md` — track the confirmation and the post-closure check dates.
