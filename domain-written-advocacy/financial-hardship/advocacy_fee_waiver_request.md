---
title: "Fee Waiver Request — Ask for a Charge to Be Removed"
category: advocacy
description: "[SELF-SUBMIT] Help a person draft THEIR OWN written request to have a fee removed — overdraft, late, returned-payment, overlimit, service, or administrative — stating the fee and date precisely, the circumstances, and their account history, and asking whether the underlying trigger can be prevented from recurring. Does NOT cite fee or banking regulation as authority, state whether a fee was properly charged or lawful, promise a refund, predict the outcome, or invent fee amounts or account history. Not legal or financial advice."
techniques:
  - CM-01
  - DS-01
  - ST-02
  - ST-03
  - QA-01
difficulty: beginner
intended_use: model-testing
tags:
  - written-advocacy
  - self-advocacy
  - financial-hardship
  - fees
  - self-submit
  - consumer
updated: "2026-08-01"
related_prompts:
  - domain-written-advocacy/financial-hardship/advocacy_goodwill_adjustment_request.md
  - domain-written-advocacy/financial-hardship/advocacy_hardship_assistance_request.md
  - domain-written-advocacy/accounts-and-billing/advocacy_recurring_charge_dispute.md
  - domain-written-advocacy/cross-cutting/advocacy_escalation_ladder_designer.md
---

**Purpose:** Help you write **your own** short, dated request to have a fee removed — an overdraft or returned-payment charge, a late fee, an overlimit fee, a service or administrative charge. It states the fee and the date precisely, gives the circumstances briefly, sets them against your account history, and asks the question most people forget: what would stop this happening again.

**When to use:** A fee has been charged, you want it reversed, and you would rather ask in writing with the dates and history attached than argue about it on a call.

**When NOT to use:** You dispute the underlying transaction rather than the fee → `../accounts-and-billing/advocacy_recurring_charge_dispute.md`. You want a late payment removed from your credit file → `advocacy_goodwill_adjustment_request.md`. You are in ongoing financial difficulty and fees are compounding → `advocacy_hardship_assistance_request.md`, which reaches a different team with more to offer. You believe the fee was charged in breach of your agreement → that is a contract question; route to an attorney or a consumer advice service.

---

## Boundary & Routing Block

Use a different pathway if:
- **Fees are recurring because money is tight, rather than because of a one-off slip** → a waiver request treats the symptom. The account needs a hardship conversation, which reaches a different team with different options. Use `advocacy_hardship_assistance_request.md`, and for wider difficulty a **nonprofit credit counselling service** `[VERIFY: locate an accredited nonprofit service in your jurisdiction from an official or government source]`.
- **You believe the fee breaches your agreement, or was charged without the right to do so** → that is a contract question, not a goodwill request. Route to an attorney, **legal aid**, or a consumer advice service; asking for a waiver and asserting a breach are different letters and should not be combined.
- **The fee relates to a transaction you did not authorize** → treat it as possible fraud first. Contact the provider's fraud team through its official channel and see `domain-legal/personal-self-advocacy/identity-theft/`.
- **The account is in collections or subject to legal action** → route to an attorney or legal aid; a fee waiver does not address it.

This prompt is educational support for preparing your own correspondence. It is not a substitute for legal or financial services.

---

## Scope Boundary — Read First

This **drafts your own written fee waiver request for you to send**. It is **not legal advice, financial advice, a legal filing, a contract interpretation, or a substitute for an attorney or your jurisdiction's law.** It will **not** tell you whether a fee was properly charged, permitted under your agreement, or lawful; cite or quote a banking, fee, or consumer regulation as authority; tell you whether any cap, limit, or restriction applies to the charge; tell you what the provider is obliged to do; predict whether the fee will be reversed; assess how strong the request is; tell you how many waivers you can ask for; or invent a fee amount, charge date, or account history. Fee rules **vary by product, provider, state, and country and change over time.** Where such a concept appears it is flagged *verify for your jurisdiction*.

---

## Core Principles

1. **Name the fee exactly.** Date charged, amount, and the descriptor as it appears on the statement. A request that says "the charges last month" makes the reader do work they will not do.
2. **Keep it short.** A waiver request is one of the few letters where brevity helps. Fee, date, circumstance, history, ask. Anything longer reads as a case being built and tends to get a policy reply.
3. **Your history is the argument.** Length of relationship, payment record, and whether this has happened before. If it is a first occurrence in years, say so — that is the fact most likely to move the decision.
4. **Explain the circumstance without a plea.** "The payment was made on [date], one day after the due date, because [reason]" is enough. Extended hardship narratives belong in a hardship request, where they are actually assessed.
5. **Ask a real question about recurrence.** Whether a due-date change, a low-balance alert, an autopay setup, or a buffer would prevent it. This often produces more value than the waiver, and it changes the tone of the exchange.
6. **Ask, do not assert.** This is a goodwill request. Framing it as an entitlement invites a refusal quoting the terms, and if you believe there is an entitlement, that is a different letter routed to an attorney.
7. **If fees keep recurring, the request is the wrong tool.** Repeated fees are a signal, not a series of accidents. Route to hardship or counselling rather than sending a fourth waiver request.

---

## Your Input

- **Your jurisdiction (state/city/country):** [required]
- **Provider and product:** [bank / card / lender / service]
- **Account identifiers:** [account #, name on account]
- **The fee:** [date charged, amount, statement descriptor verbatim]
- **Fee type:** [overdraft / returned payment / late / overlimit / service / administrative]
- **What triggered it:** [factual circumstance]
- **Whether the underlying payment has since been made:** [date, amount]
- **Account history:** [customer since, payment record, prior fees of this type and when]
- **Any prior waiver on this account:** [when, what]
- **Are fees recurring due to ongoing difficulty?:** [if yes → Boundary & Routing Block]
- **Prior contact on this fee:** [date, channel, reference, outcome]

---

## Constraints

**Must:**
- Require the jurisdiction; use only the facts the user supplies.
- Screen for recurring fees caused by ongoing difficulty and route those to hardship rather than drafting a waiver.
- State the fee's date, amount, and statement descriptor verbatim.
- Keep the letter short and the circumstance brief and factual.
- Include account history — tenure, payment record, prior occurrences — where the user supplies it.
- Ask what would prevent recurrence, as a genuine question.
- Frame the request as a goodwill ask, not an entitlement.
- Keep a waiver request separate from any dispute over the underlying transaction or agreement.
- Include a Sending Log and label the output `MY OWN REQUEST — NOT A LEGAL FILING`.

**Must Not:**
- State whether the fee was properly charged, permitted, or lawful.
- Cite or invent a banking, fee, or consumer regulation, cap, or limit.
- State what the provider is obliged to do, or that the user is entitled to a waiver.
- Predict whether the fee will be reversed, or assess how strong the request is.
- Tell the user how many waivers they may request or that a first one is always granted.
- Combine a waiver request with an assertion that the fee breached the agreement.
- Invent a fee amount, charge date, descriptor, tenure, or payment history.
- Coach the user to overstate the circumstance or manufacture a reason.
- Advise repeated waiver requests where fees are recurring from ongoing difficulty.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for recurring fees driven by ongoing difficulty, a suspected breach of agreement, an unauthorized underlying transaction, or collections → route per the Boundary & Routing Block. Restate the jurisdiction and the boundary: this is a goodwill request; whether the fee was properly charged is for an attorney.

### Stage 2 — Pin the Fee Precisely
Record the charge date, the amount, and the statement descriptor verbatim, plus the fee type. Flag anything the user cannot read off a statement as `[NEED DOCUMENT: statement showing the charge]` rather than approximating.

### Stage 3 — State the Circumstance Briefly
Capture what happened in one or two factual sentences, and whether the underlying payment or balance has since been resolved and when. Resist expanding this into a narrative; where the circumstance genuinely is ongoing hardship, route instead.

### Stage 4 — Assemble the History
Record tenure, payment record, and whether this fee type has occurred before and when. Where this is a first occurrence, state that plainly. Where there have been previous waivers, record that too rather than omitting it.

### Stage 5 — Add the Recurrence Question
Add a genuine question about what would prevent this happening again — a due-date change, an alert, autopay, a buffer, or a different product. Frame it as wanting to fix the cause, not as a bargaining move.

### Stage 6 — Draft the Request and Close
Compose the user's own short dated request, labeled as theirs to send, with the Sending Log. Note that a refusal can be escalated once, and point to the escalation ladder. Route agreement, fraud, and hardship questions onward.

---

## Output Format

```markdown
MY OWN FEE WAIVER REQUEST — NOT A LEGAL FILING
From: [your name], [contact]. To: [provider, customer service channel]. Date: [YYYY-MM-DD].
Delivery: [portal / designated email / certified mail]. Keep a copy.
This is my own request. It does NOT state that the fee was improperly charged, cite any
regulation, claim an entitlement, or predict your decision. Whether the fee was permitted under
my agreement is a question for an attorney.

Re: Request to waive a fee — account [NEED ACCOUNT #: from your statement]

## The fee
| Item | Detail |
|---|---|
| Date charged | [YYYY-MM-DD] |
| Amount | [$X] |
| Statement descriptor | "[exact descriptor from my statement]" |
| Fee type | [overdraft / late / returned payment / overlimit / service] |

## What happened
[One or two factual sentences — e.g. "The payment was made on [date], one day after the due
date of [date]. The full balance has since been paid."]

## My account history
- Customer since: [YYYY-MM-DD]
- Payment record: [all payments on time before this / detail]
- Previous fees of this type: [none in [n] years / dates]
- Previous waiver on this account: [none / date and what]

## What I am asking
I am asking whether you would consider waiving this fee as a goodwill gesture.

## Preventing this happening again
I would also like to avoid this recurring. Could you tell me whether any of the following are
available on my account:
- Changing the payment due date to [preferred date]
- A low-balance or upcoming-payment alert
- Setting up automatic payment of [the minimum / the full balance]
- [any other option you offer]

Please respond in writing by [date].
[Your name], [YYYY-MM-DD]

---
## Sending Log (keep with your copy)
| Sent | Method | Sent to | Reference # | Proof kept | Response due | Outcome |
|---|---|---|---|---|---|---|
| [YYYY-MM-DD] | [method] | [channel] | [#] | [ticket # / receipt] | [YYYY-MM-DD] | [ ] |

Note to self: this is my own request, not legal or financial advice, and nobody is obliged to
agree to it. Whether the fee was properly charged under my agreement is a question for an
attorney or a consumer advice service. If fees keep recurring, the issue is not the individual
fee and I will use the hardship route instead.
*Verify for your jurisdiction — fee rules vary by product, provider, state, and country.*
```

---

## Verification

- [ ] Jurisdiction captured and agreement questions routed *verify with an attorney*?
- [ ] Recurring-fee-from-hardship dimension screened and routed to the hardship prompt?
- [ ] Fee date, amount, and verbatim statement descriptor recorded?
- [ ] Circumstance stated in one or two factual sentences, without a plea?
- [ ] Account history included — tenure, payment record, prior occurrences, prior waivers?
- [ ] Recurrence question included as a genuine question?
- [ ] Framed as a goodwill request rather than an entitlement?
- [ ] Kept separate from any dispute over the underlying transaction or the agreement?
- [ ] No statement on whether the fee was properly charged, permitted, or lawful?
- [ ] No banking, fee, or consumer regulation, cap, or limit cited or invented?
- [ ] No claim of obligation or entitlement?
- [ ] No outcome prediction or strength assessment?
- [ ] No claim about how many waivers may be requested?
- [ ] No invented amount, date, descriptor, tenure, or history?
- [ ] Sending Log included and gaps flagged `[NEED …:]`?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "This overdraft fee exceeds the regulatory cap" | Cite no rule or cap; ask for a waiver and route the question onward |
| "They're required to waive the first late fee" | State no obligation; this is a goodwill request |
| "Banks always reverse the first one — you'll get it" | Make no prediction about the outcome |
| "Waive this or I'll close my account and complain" | Ask plainly; threats belong in neither a goodwill request nor this domain |
| "The charges from last month" | Give the exact date, amount, and verbatim descriptor |
| Three paragraphs on how hard the month has been | Keep it to two factual sentences; genuine hardship routes to the hardship prompt |
| Omit the two previous waivers to look better | Record them; a discovered omission ends the goodwill framing |
| Combine "waive this" with "and it breached our agreement" | Keep them separate; the breach argument routes to an attorney |
| Send a fourth waiver request this year | Stop — recurring fees are a hardship signal, not a series of accidents |
| Guess the fee amount from the balance change | Flag `[NEED DOCUMENT: statement showing the charge]` |

---

## Adaptations

**By fee type:**
- **Overdraft or returned payment:** Note whether the account has since been brought positive and when; ask about buffer or alert options as the recurrence question.
- **Late fee:** State the payment date against the due date precisely, and ask whether the due date can be moved to align with when income arrives.
- **Overlimit fee:** Ask whether the limit or the overlimit setting can be adjusted, and what the consequence of each would be.
- **Service or administrative fee:** Ask what the fee covers and whether the account has a variant without it — this often produces a better result than the waiver.

**By situation/profile:**
- **First occurrence in a long relationship:** Lead with tenure and record; this is the strongest and shortest version of the letter.
- **Several fees from one event:** List each with its date and descriptor and ask about them together; a cascade from a single missed payment is a different conversation from four separate lapses.
- **Already refused once:** Escalate once, with the original request date and reference, rather than resending — see `../cross-cutting/advocacy_escalation_ladder_designer.md`.
- **Fees recurring:** Boundary & Routing Block — the hardship route reaches a team with more to offer.

---

## Related Prompts

- `advocacy_goodwill_adjustment_request.md` — to ask about a late mark already reported to credit bureaus.
- `advocacy_hardship_assistance_request.md` — when fees are recurring because of ongoing difficulty.
- `../accounts-and-billing/advocacy_recurring_charge_dispute.md` — where the underlying charge, not the fee, is disputed.
- `../cross-cutting/advocacy_escalation_ladder_designer.md` — if the request is refused.
