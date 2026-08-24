---
title: "Recurring Charge Dispute — Challenge a Charge After You Cancelled"
category: advocacy
description: "[SELF-SUBMIT] Help a person draft THEIR OWN written dispute of a recurring charge taken after a cancellation, at the end of a free trial, or after a plan changed without clear agreement — anchored to the cancellation evidence, the charge dates and amounts, and a specific refund request. Does NOT cite auto-renewal or unfair-practice law as authority, characterize the provider's conduct as a dark pattern or deceptive, predict refund success, or invent charge dates or confirmation numbers. Chargebacks and legal claims route elsewhere. Not legal advice."
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
  - consumer
  - billing-dispute
  - subscription
  - self-submit
updated: "2026-08-01"
related_prompts:
  - domain-written-advocacy/accounts-and-billing/advocacy_subscription_cancellation_request.md
  - domain-written-advocacy/cross-cutting/advocacy_escalation_ladder_designer.md
  - domain-legal/personal-self-advocacy/consumer-scams/legalprep_refund_chargeback_dispute_preparer.md
  - domain-legal/personal-self-advocacy/consumer-scams/legalprep_consumer_complaint_documentation_organizer.md
---

**Purpose:** Help you write **your own** dated dispute of a recurring charge you say should not have been taken — because you cancelled first, because a free trial converted, because a plan renewed at a different price, or because you never authorized the arrangement. It anchors the letter to the strongest thing you have: dated evidence of the cancellation or of what you agreed to, set against the dates and amounts actually charged.

**When to use:** A charge has appeared and you believe the authority for it had ended or never existed, and you want a written record of the dispute with the provider before or alongside any other step.

**When NOT to use:** You want to cancel going forward rather than dispute a past charge → `advocacy_subscription_cancellation_request.md`. You want to raise a chargeback with your card issuer or bank, or the merchant is unreachable → `domain-legal/personal-self-advocacy/consumer-scams/legalprep_refund_chargeback_dispute_preparer.md`. You did not recognize the charge at all and suspect fraud → `domain-legal/personal-self-advocacy/identity-theft/` and your card issuer's fraud process, first.

---

## Boundary & Routing Block

Use a different pathway if:
- **You do not recognize the merchant or the charge at all** → treat it as possible fraud, not a billing dispute. Contact your card issuer's or bank's fraud team through its official channel, and see `domain-legal/personal-self-advocacy/identity-theft/`.
- **You want to raise a chargeback or bank dispute** → that is a separate process with its own evidence requirements and time limits set by the card scheme or bank. See `domain-legal/personal-self-advocacy/consumer-scams/legalprep_refund_chargeback_dispute_preparer.md`, and **do not let a scheme time limit pass while corresponding with the merchant.** Whether any deadline applies is for your issuer's published process and, if it matters legally, an attorney.
- **The amount is large, or the arrangement involves a financed or fixed-term agreement** → route the contract question to an attorney, **legal aid**, or a consumer advice service.
- **The provider has referred the disputed amount to a collector or is reporting it adversely** → route to an attorney or legal aid and see `domain-legal/personal-self-advocacy/debt-collection/`.

This prompt is educational support for preparing your own correspondence. It is not a substitute for legal or financial services.

---

## Scope Boundary — Read First

This **drafts your own written dispute of a recurring charge for you to send to the provider**. It is **not legal advice, legal strategy, a legal filing, a chargeback submission, or a substitute for an attorney or your jurisdiction's law.** It will **not** tell you whether the charge was lawful or the authorization valid; state or cite an auto-renewal, negative-option, unfair-practice, or consumer-protection rule as authority; label the provider's interface or conduct deceptive, a dark pattern, or unlawful; tell you the time limit for a chargeback or a claim; predict whether you will be refunded; assess how strong your position is; or invent a charge date, amount, confirmation number, or cancellation reference. Auto-renewal and refund rules **vary by state and country and change over time.** Where such a concept appears it is flagged *verify for your jurisdiction*.

---

## Core Principles

1. **The cancellation evidence is the anchor.** The date you cancelled, the channel, the reference number, and the confirmation — set against the date charged. If you have that pairing, the letter almost writes itself; if you do not, say so plainly rather than implying evidence you lack.
2. **Charge dates and amounts, exactly as they appear.** Quote the statement descriptor verbatim, with the date and amount for each disputed charge. Providers match on descriptors, not on descriptions.
3. **State what you agreed to and when.** For a trial conversion or a price change, the question is what was presented at sign-up and what you accepted. Describe what you saw and when — without characterizing the design as deceptive.
4. **Describe the interface factually; do not label it.** "The cancellation option was under Account, then Billing, then Manage Plan" is a fact. "This is a deliberate dark pattern designed to trap users" is a conclusion that invites a defensive reply and is not yours to reach.
5. **Ask for one specific refund figure.** "Refund $X for the charges on [dates] to the original payment method." One number, one destination, one deadline.
6. **Say the authority ended, without saying they broke the law.** "I cancelled on [date]; I did not authorize the charge on [date]" states your position on the facts. Whether that makes the charge unlawful is for an attorney.
7. **Keep the merchant track and the bank track separate.** Both can run, but they are different processes with different evidence and different clocks. Do not conflate them in one letter.

---

## Your Input

- **Your jurisdiction (state/city/country):** [required]
- **Provider and service:** [name, plan]
- **Account identifiers:** [account #, registered email, payment method last 4]
- **Disputed charges:** [for each: date, amount, statement descriptor verbatim]
- **Basis of dispute:** [cancelled before the charge / free trial converted / price changed / never authorized]
- **Cancellation evidence, if any:** [date, channel, reference #, confirmation held] or ["none"]
- **What you were shown at sign-up, if relevant:** [what was presented about renewal, trial length, price]
- **Total refund you are requesting:** [$X]
- **Where the refund should go:** [original payment method]
- **Any prior contact on this charge:** [dates, channel, outcome, reference #]
- **Any fraud, collections, or chargeback dimension?:** [if yes → Boundary & Routing Block]

---

## Constraints

**Must:**
- Require the jurisdiction; use only the facts the user supplies.
- Anchor the letter to the cancellation or authorization evidence paired against the charge dates.
- List each disputed charge with date, amount, and the statement descriptor verbatim.
- State one total refund figure and the destination.
- Describe interfaces and sign-up flows factually, without labeling them.
- State plainly where the user has no cancellation evidence, rather than implying they do.
- Keep the merchant dispute separate from any chargeback, and route chargebacks to the sibling prompt with a note about scheme time limits.
- Flag missing dates, amounts, descriptors, and references as `[NEED …:]`.
- Include a Sending Log and label the output `MY OWN LETTER — NOT A LEGAL FILING`.

**Must Not:**
- State that the charge was unlawful, unauthorized as a legal conclusion, or in breach of any rule.
- Cite or invent an auto-renewal, negative-option, unfair-practice, or refund statute or deadline.
- Call an interface a dark pattern, deceptive, manipulative, or designed to trap users.
- State the time limit for a chargeback, claim, or dispute.
- Predict whether a refund will be issued, or assess how strong the position is.
- Characterize the provider or attribute intent to its design or staff.
- Invent a charge date, amount, statement descriptor, cancellation date, or reference number.
- Draft a legal threat, or instruct the user to threaten a chargeback as leverage.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for unrecognized charges suggesting fraud, a collections referral, or an intended chargeback with its own clock → route per the Boundary & Routing Block. Restate the jurisdiction and the boundary: this states the user's factual dispute; lawfulness and deadlines are for an attorney or the issuer's process.

### Stage 2 — Build the Charge Table
List every disputed charge with its date, amount, and verbatim statement descriptor, and total them. Flag anything the user cannot read off a statement as `[NEED DOCUMENT: statement showing the charge]` rather than approximating.

### Stage 3 — Establish the Authority Position
Pin down the basis: a cancellation before the charge date (with its evidence), a trial that converted, a price change, or an arrangement never authorized. Record the cancellation date, channel, reference, and confirmation if held — and record plainly if none exists. Where sign-up presentation matters, capture what the user recalls seeing and when, flagged `[UNCERTAIN WORDING:]` where recall is partial.

### Stage 4 — Pair the Evidence Against the Charges
Set the authority position against each charge date so the gap is visible: cancelled [date] → charged [date]. This pairing is the substance of the letter. Where evidence is missing, state what the user can and cannot show.

### Stage 5 — Set the Refund Request
State one total figure, the destination (original payment method), and a response date. Where only part of the total is disputed, say which charges and why, in factual terms.

### Stage 6 — Draft the Letter and Close
Compose the user's own dated dispute, labeled as theirs to send, with the Sending Log. Note that a chargeback is a separate track with its own time limits and point to the sibling prompt. Route lawfulness, collections, and deadline questions onward.

---

## Output Format

```markdown
MY OWN BILLING DISPUTE — NOT A LEGAL FILING
From: [your name], [contact]. To: [provider, billing disputes channel]. Date: [YYYY-MM-DD].
Delivery: [portal / designated email / certified mail]. Keep a copy.
This is my own factual dispute. It does NOT state that any law was broken, cite any auto-renewal
or refund rule, describe your interface as deceptive, state any deadline, or predict any outcome.
Legal questions are for an attorney; any chargeback is a separate process with its own time limits.

Re: Disputed charges on account [NEED ACCOUNT #:] — [service / plan]

## Account details
Name on account: [name] · Account / registered email: [identifiers]
Payment method charged: [card ending NNNN]

## The charges I am disputing
| Date | Amount | Statement descriptor (verbatim) |
|---|---|---|
| [YYYY-MM-DD] | [$X] | "[exact descriptor from my statement]" |
| [YYYY-MM-DD] | [$X] | "[exact descriptor]" |
| **Total disputed** | **[$X]** | |

## Why I say these were not authorized
[Choose the applicable basis, stated factually:]

**Cancelled before the charge:**
I cancelled this subscription on [YYYY-MM-DD] via [channel], reference [#].
[I hold: confirmation email dated [date] / portal screenshot / certified mail receipt [#].]
[or: I do not have written confirmation of that cancellation. What I can show is: [what].]
The charge above was taken on [YYYY-MM-DD], after that date.

**Free trial converted:**
I started a trial on [YYYY-MM-DD]. My understanding was that it ran until [date] and that
[what the user recalls being told about conversion — [UNCERTAIN WORDING:] where partial].
I was charged [$X] on [YYYY-MM-DD].

**Price changed:**
I agreed to [$X] per [period] on [YYYY-MM-DD]. I was charged [$Y] on [YYYY-MM-DD].
[Notice I received about the change, if any: [what and when] / "I did not receive notice."]

**Never authorized:**
I did not set up a recurring arrangement on this payment method. The first charge I can
identify is [YYYY-MM-DD].

## Prior contact on this
- [YYYY-MM-DD] — [channel], [what was said], reference [#]. [Outcome.]

## What I am requesting
Please refund **[$X]** to the original payment method, and confirm in writing by [date]:
1. That the refund has been issued, and the date it was issued.
2. That the recurring arrangement has been ended and the payment method removed.

## Documents I can provide on request
- [cancellation confirmation / statement pages / sign-up screenshots / prior correspondence]
- [NEED DOCUMENT: ...]

[Your name], [YYYY-MM-DD]

---
## Sending Log (keep with your copy)
| Sent | Method | Sent to | Proof kept | Response due | Response received |
|---|---|---|---|---|---|
| [YYYY-MM-DD] | [method] | [channel] | [ticket # / receipt] | [YYYY-MM-DD] | [ ] |

Note to self: this is my own letter, not legal advice or a filing. Whether the charge was lawful
is for an attorney. A chargeback through my card issuer is a **separate** process with its own
evidence requirements and time limits set by the issuer or card scheme — I will check those
directly and promptly rather than assuming this letter preserves them.
*Verify for your jurisdiction — auto-renewal and refund rules vary by state and country.*
```

---

## Verification

- [ ] Jurisdiction captured and lawfulness/deadline questions routed *verify with an attorney*?
- [ ] Fraud, collections, and chargeback dimensions screened and routed?
- [ ] Every disputed charge listed with date, amount, and verbatim statement descriptor?
- [ ] Authority position paired against charge dates so the gap is explicit?
- [ ] Where no cancellation evidence exists, stated plainly rather than implied?
- [ ] Sign-up or interface described factually, with no "dark pattern" or "deceptive" label?
- [ ] One total refund figure, destination, and response date stated?
- [ ] No claim that the charge was unlawful or in breach of any rule?
- [ ] No auto-renewal, negative-option, or refund statute cited or invented?
- [ ] No chargeback or claim time limit stated?
- [ ] No refund prediction, strength assessment, or intent attribution?
- [ ] No invented charge date, amount, descriptor, or reference number?
- [ ] Chargeback noted as a separate track with its own limits, and routed to the sibling prompt?
- [ ] Sending Log included and gaps flagged `[NEED …:]`?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "This violates auto-renewal law in your state" | State the dates factually; the legal question is for an attorney |
| "Their cancellation flow is a textbook dark pattern" | "The cancellation option was located under [path]" — describe, do not label |
| "You have 60 days to chargeback, so you're fine" | Do not state any time limit; check the issuer's published process promptly |
| "They'll refund this — they always do when challenged" | Make no prediction about the outcome |
| "Refund me or I'll chargeback and leave reviews everywhere" | State the refund request; a chargeback is a separate process, not leverage |
| Say the user has a cancellation confirmation they never mentioned | State plainly what they can and cannot show |
| Approximate the charge date from memory | Flag `[NEED DOCUMENT: statement showing the charge]` |
| Paraphrase the statement descriptor into something readable | Quote it verbatim — providers match on the descriptor |
| "They intentionally hid the cancel button to keep billing you" | Describe the interface; intent is not yours to assert |
| Handle an unrecognized merchant as a billing dispute | Stop, use the Boundary & Routing Block, treat as possible fraud |

---

## Adaptations

**By dispute basis:**
- **Cancelled and still charged:** Lead with the cancellation date, channel, and reference; this is the strongest version of the letter and needs least else.
- **Trial converted:** Anchor to the trial start date and what the user recalls about its length and conversion, flagged where recall is partial; ask what record the provider holds of what was presented.
- **Price increased:** Anchor to the agreed price and date, and ask what notice the provider says it gave and when — asking is factual, asserting they gave none may not be.
- **Never authorized:** Ask the provider to supply the record of how and when the arrangement was created; if it cannot, that is a fact for escalation. If the merchant is unfamiliar, treat as fraud first.

**By situation/profile:**
- **Charged repeatedly over months:** List every charge; the pattern and the total matter more than any single line.
- **Billed by an app store or platform rather than the provider:** Identify who actually took the payment and send the dispute there; the provider may have no ability to refund.
- **No cancellation evidence at all:** Say so, describe what you did and when, and ask the provider to produce its record of the account's cancellation status.
- **Fraud, collections, or chargeback dimension:** Boundary & Routing Block first; do not let another process's clock run out while corresponding.

---

## Related Prompts

- `advocacy_subscription_cancellation_request.md` — cancel properly going forward, with confirmation.
- `../cross-cutting/advocacy_escalation_ladder_designer.md` — if the dispute is refused or ignored.
- `../cross-cutting/advocacy_response_analyzer.md` — to read a partial-refund or refusal reply.
- `../../domain-legal/personal-self-advocacy/consumer-scams/legalprep_refund_chargeback_dispute_preparer.md` — the chargeback track with your card issuer.
- `../../domain-legal/personal-self-advocacy/consumer-scams/legalprep_consumer_complaint_documentation_organizer.md` — to build the wider record if this becomes a complaint.
