---
title: "Price Increase & Retention Request — Ask for a Better Rate in Writing"
category: advocacy
description: "[SELF-SUBMIT] Help a person draft THEIR OWN written request for a lower rate, a reversal of a price increase, a downgrade, or a retention offer — anchored to their account history, the increase itself, and comparable options they have actually seen. Does NOT cite pricing or notice regulation as authority, state what the provider must offer or whether an increase is permitted, invent competitor prices or offers, predict what will be granted, or bluff a departure the user has not decided on. Not legal advice."
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
  - pricing
  - retention
  - self-submit
updated: "2026-08-01"
related_prompts:
  - domain-written-advocacy/accounts-and-billing/advocacy_subscription_cancellation_request.md
  - domain-written-advocacy/financial-hardship/advocacy_interest_rate_reduction_request.md
  - domain-negotiation/channels/negotiation_written_async_message.md
  - domain-written-advocacy/cross-cutting/advocacy_response_analyzer.md
---

**Purpose:** Help you write **your own** dated request for a better rate — after a price increase, at the end of an introductory period, or simply because you have been paying a long-standing customer premium. It anchors the request to your actual account history, the increase as billed, and any comparable option you have genuinely seen, and asks for one specific outcome.

**When to use:** A price has gone up, an introductory rate has ended, or you believe you are paying more than the current rate for your service, and you want the request and any offer in writing rather than negotiated verbally with a retention agent.

**When NOT to use:** You cannot afford the payment and need hardship help → `../financial-hardship/advocacy_hardship_assistance_request.md`. You want a lower interest rate on a credit product → `../financial-hardship/advocacy_interest_rate_reduction_request.md`. You have decided to leave → `advocacy_subscription_cancellation_request.md`. You want to challenge whether the increase was correctly applied or notified → that is a billing dispute; use `advocacy_recurring_charge_dispute.md` or `advocacy_utility_telecom_service_dispute.md`.

---

## Boundary & Routing Block

Use a different pathway if:
- **You cannot afford the current or increased payment** → this is a hardship conversation, not a retention one, and the two get routed to different teams with different options. Use `../financial-hardship/advocacy_hardship_assistance_request.md`, and for genuine financial difficulty consider a **nonprofit credit counselling service** `[VERIFY: locate an accredited nonprofit service in your jurisdiction from an official or government source — do not rely on a name from memory]`.
- **You are in a fixed term and want to know whether the provider may raise the price at all, or whether you can exit** → that is contract analysis. Route to an attorney, **legal aid**, or a consumer advice service.
- **You believe the increase was applied without proper notice or contrary to what you agreed** → that is a billing dispute rather than a rate request; use the dispute prompts and keep the two letters separate.
- **The account is in arrears or with a collector** → route to `domain-legal/personal-self-advocacy/debt-collection/` and an attorney or legal aid; a retention request will not address it.

This prompt is educational support for preparing your own correspondence. It is not a substitute for legal or financial services.

---

## Scope Boundary — Read First

This **drafts your own written rate or retention request for you to send**. It is **not legal advice, legal strategy, financial advice, a legal filing, a contract interpretation, or a substitute for an attorney or your jurisdiction's law.** It will **not** tell you whether a price increase was permitted, properly notified, or lawful; state or cite a pricing, notice-period, or consumer-protection rule as authority; tell you what the provider is obliged to offer; supply competitor prices, current promotional rates, or market comparisons from memory; predict whether a discount will be granted or how much; assess how strong your negotiating position is; or invent an account tenure, prior rate, offer, or amount. Pricing and notice rules **vary by sector, state, and country and change over time.** Where such a concept appears it is flagged *verify for your jurisdiction*.

---

## Core Principles

1. **Anchor to your own verifiable history.** Tenure, what you have actually paid, on-time payment record, products held. These are facts the provider can check in seconds, and they are the whole basis of the request.
2. **State the increase precisely.** Old rate, new rate, the date it took effect, and the difference — in figures, from the bill. A request that says "my bill went up a lot" gives them nothing to act on.
3. **Only cite a comparable you have actually seen.** If you have a specific quote or advertised price, name it with its source and the date you saw it. If you have not, say you are asking for their best available rate rather than inventing a competitor's number you may be asked to produce.
4. **Ask for one specific outcome.** A named target rate, a reversal to the prior rate, a specific downgrade, or their best available rate for your usage. "Something better" is not actionable.
5. **Do not bluff a departure you have not decided on.** Threatening to leave when you will not is a tactic that can be accepted — some providers simply process the cancellation. State your position honestly: exploring options, or genuinely deciding, whichever is true.
6. **Get any offer in writing before accepting.** Retention offers frequently carry a new minimum term, a reverting rate after a promotional period, or a changed service level. Ask for the full terms in writing before agreeing to anything.
7. **You ask and record; nobody is obliged to agree.** A rate request has no entitlement behind it. What the provider must do is a contract question for an attorney. Stop at the boundary.

---

## Your Input

- **Your jurisdiction (state/city/country):** [required]
- **Provider and service:** [name, plan or tariff]
- **Account identifiers:** [account #, registered email, service address]
- **How long you have held the account:** [since YYYY-MM-DD]
- **Payment record:** [on time / any missed payments and when]
- **The increase:** [old rate, new rate, effective date, difference] or ["no increase — long-standing rate"]
- **Other products held with them:** [list — bundling is often relevant]
- **Comparable you have actually seen:** [provider, rate, source, date seen] or ["none — asking for their best rate"]
- **What you are asking for:** [target rate / reversal to prior rate / named downgrade / best available rate]
- **Your actual position:** [exploring / seriously considering leaving / will stay either way]
- **Contract status:** [rolling / fixed term ending YYYY-MM-DD]
- **Any affordability, arrears, or contract-term question?:** [if yes → Boundary & Routing Block]

---

## Constraints

**Must:**
- Require the jurisdiction; use only the facts the user supplies.
- Screen affordability first and route genuine hardship to the hardship prompts rather than a retention letter.
- Anchor the request to verifiable account facts: tenure, payment record, products held, rate history.
- State the increase in figures with its effective date, where there is one.
- Include a comparable **only** where the user has actually seen it, with source and date; otherwise ask for the provider's best available rate.
- State one specific requested outcome.
- Represent the user's actual position honestly, without manufacturing a departure threat.
- Ask for any offer's full terms in writing — including minimum term, promotional period, reverting rate, and any service change — before acceptance.
- Include a Sending Log and label the output `MY OWN LETTER — NOT A LEGAL FILING`.

**Must Not:**
- State whether a price increase was permitted, properly notified, or lawful.
- Cite or invent a pricing, notice-period, or consumer-protection rule.
- Supply competitor prices, promotional rates, or market comparisons from memory.
- Invent an offer, quote, tenure, prior rate, or amount the user did not supply.
- Tell the user what the provider is obliged to offer, or that they are entitled to a discount.
- Predict whether a discount will be granted, or how large it will be.
- Assess how strong the user's negotiating position is.
- Coach the user to bluff cancellation, imply a competitor offer they lack, or manufacture urgency.
- Draft a legal threat, or conflate the rate request with a billing dispute in the same letter.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for affordability difficulty, arrears, a collections referral, or a fixed-term contract question → route per the Boundary & Routing Block. A hardship matter must not be sent as a retention letter. Restate the jurisdiction and the boundary: this is a request, not an entitlement.

### Stage 2 — Assemble the Account Facts
Capture tenure, payment record, products held, and the rate history. These are the checkable facts the request rests on. Flag anything the user cannot confirm from a statement as `[NEED DOCUMENT:]`.

### Stage 3 — State the Increase Precisely
Record the old rate, new rate, effective date, and the difference in both absolute and percentage terms where the user can compute them from their bills. Where there was no increase, frame the request instead around tenure and the current rate paid versus the plan's current advertised rate — only if the user has seen it.

### Stage 4 — Handle Comparables Honestly
If the user has a genuine quote or advertised price, record it with provider, rate, source, and the date seen, and note they may be asked to produce it. If not, drop the comparison entirely and ask for the provider's best available rate for the user's usage. Never supply a market rate.

### Stage 5 — Fix the Ask and the User's Real Position
Set one specific requested outcome. Establish the user's actual position — exploring, seriously deciding, or staying regardless — and represent it truthfully. Where the user is genuinely considering leaving, say so plainly; where not, the letter asks on the strength of the account history alone.

### Stage 6 — Draft the Letter and Close
Compose the user's own dated request, labeled as theirs to send, with the Sending Log. Include the request for full written terms of any offer. Point to the response analyzer for reading the reply. Route affordability, contract, and dispute questions onward.

---

## Output Format

```markdown
MY OWN RATE REQUEST — NOT A LEGAL FILING
From: [your name], [contact]. To: [provider, account or retentions channel]. Date: [YYYY-MM-DD].
Delivery: [portal / designated email / certified mail]. Keep a copy.
This is my own request. It does NOT state that any increase was unlawful or improperly notified,
cite any pricing rule, claim any entitlement to a discount, or predict any outcome. Contract
questions are for an attorney.

Re: Request to review my rate — account [NEED ACCOUNT #:]

## My account
- Name on account: [name] · Account: [#] · Service address: [address]
- Customer since: [YYYY-MM-DD] ([n] years)
- Plan / tariff: [name] · Contract status: [rolling / fixed term ending YYYY-MM-DD]
- Payment record: [all payments on time / detail]
- Other products held with you: [list]

## The change in my rate
| Item | Detail |
|---|---|
| Rate I was paying | [$X per period] until [YYYY-MM-DD] |
| Rate now billed | [$Y per period] from [YYYY-MM-DD] |
| Difference | [$Y − $X] per period ([n]% where I can compute it from my bills) |

[If no increase:]
I have held this plan at [$X] since [YYYY-MM-DD] and would like it reviewed.

## Comparable I have seen
[Only if genuinely seen:]
On [YYYY-MM-DD] I saw [provider] advertising [service] at [$Z per period] at [source].
I can provide what I saw on request.

[If none:]
I am not citing a competitor's price. I am asking what your best available rate is for my
usage and account.

## What I am asking for
[One specific ask — e.g. "Please reduce my rate to [$X per period], the rate I paid before
[date]" / "Please move me to [named plan] at its current rate" / "Please tell me the best
available rate for my usage on this account."]

## My position
[Honest statement — e.g. "I am reviewing my options before my renewal on [date]" /
"I would prefer to stay and am asking before I look elsewhere" / "I am seriously considering
moving providers and wanted to ask you first."]

## If you can offer something
Please set out in writing, before I agree to anything:
1. The rate offered and the period it applies for.
2. Any minimum term or early-termination charge it creates.
3. The rate it reverts to, and on what date.
4. Any change to the service, allowance, or equipment.

Please respond in writing by [date].
[Your name], [YYYY-MM-DD]

---
## Sending Log (keep with your copy)
| Sent | Method | Sent to | Proof kept | Response due | Response received | Offer terms in writing? |
|---|---|---|---|---|---|---|
| [YYYY-MM-DD] | [method] | [channel] | [ticket # / receipt] | [YYYY-MM-DD] | [ ] | [ ] |

Note to self: this is my own request, not legal or financial advice, and nobody is obliged to
agree to it. Whether the increase was permitted or properly notified is a contract question for
an attorney. I will not accept any offer before I have its full terms in writing, including any
new minimum term and the rate it reverts to.
*Verify for your jurisdiction — pricing and notice rules vary by sector and country.*
```

---

## Verification

- [ ] Jurisdiction captured and contract questions routed *verify with an attorney*?
- [ ] Affordability screened first, with genuine hardship routed to the hardship prompts?
- [ ] Request anchored to verifiable account facts: tenure, payment record, products, rate history?
- [ ] Increase stated in figures with its effective date, where one exists?
- [ ] Comparable included **only** where the user actually saw it, with source and date?
- [ ] No competitor price, promotional rate, or market comparison supplied from memory?
- [ ] One specific requested outcome stated?
- [ ] User's real position represented honestly, with no manufactured departure threat?
- [ ] Full written terms of any offer requested — period, minimum term, reverting rate, service change?
- [ ] No statement that an increase was permitted, notified properly, or lawful?
- [ ] No pricing or notice rule cited or invented?
- [ ] No claim of entitlement to a discount, and no prediction of what will be granted?
- [ ] No strength assessment or legal threat?
- [ ] Rate request kept separate from any billing dispute?
- [ ] Sending Log included and gaps flagged `[NEED …:]`?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "They can't raise your price mid-contract" | Do not interpret the contract; route to an attorney or an advice service |
| "Competitors are offering this at $40 right now" | Only cite a comparable the user actually saw, with source and date |
| "Tell them you have a better offer — they always match" | Represent the user's real position; do not coach a bluff |
| "Say you're cancelling; they'll transfer you to retentions" | Some providers simply process it; state the true position instead |
| "You're entitled to the new-customer rate" | No entitlement exists; this is a request |
| "They'll almost certainly give you 20% off" | Make no prediction about what will be offered |
| Accept the offer as described on the phone | Get full written terms first — minimum term, reverting rate, service change |
| Guess the old rate to make the increase look larger | Flag `[NEED DOCUMENT: prior bill showing the old rate]` |
| Combine "your increase was improperly notified" with the rate request | Keep dispute and request in separate letters |
| Send a retention letter when the user cannot afford the bill | Stop, use the Boundary & Routing Block, route to hardship |

---

## Adaptations

**By situation:**
- **Introductory rate ended:** Anchor to the introductory rate, its end date, and the standard rate now applied; ask what current offers apply to existing customers.
- **Annual increase applied:** State the increase in figures and ask what options exist to offset it — a different plan, a longer term, or a bundle — rather than asserting it should not have happened.
- **Long tenure, never renegotiated:** Tenure and payment record are the whole basis; ask directly what the best available rate is for the user's usage.
- **Bundle or multi-product:** List all products held and their total monthly value; ask for the review across the bundle rather than one line.

**By posture/profile:**
- **Genuinely willing to leave:** Say so plainly and name the renewal or decision date; an honest, dated decision point is more credible than a threat.
- **Will stay regardless:** Ask on the strength of tenure and payment record alone; do not manufacture leverage that does not exist.
- **Provider offers a call instead:** Take the call if you wish, then send a same-day written confirmation of what was offered — see `../cross-cutting/advocacy_channel_and_record_strategy.md`.
- **Affordability, not value:** Boundary & Routing Block first; a hardship request reaches a different team with different options.

---

## Related Prompts

- `advocacy_subscription_cancellation_request.md` — if you decide to leave after all.
- `../financial-hardship/advocacy_interest_rate_reduction_request.md` — the credit-product equivalent.
- `../financial-hardship/advocacy_hardship_assistance_request.md` — when the issue is affordability rather than value.
- `../cross-cutting/advocacy_response_analyzer.md` — to read the offer and see what it actually commits to.
- `../../domain-negotiation/channels/negotiation_written_async_message.md` — general craft for negotiating in writing.
