---
title: "Travel Disruption Refund Request — Cancelled, Delayed, or Changed Trips in Writing"
category: advocacy
description: "[SELF-SUBMIT] Help a person draft THEIR OWN written refund and expense request to an airline, rail or coach operator, cruise line, tour operator, or booking platform after a cancellation, long delay, schedule change, downgrade, or denied boarding — building a timestamped disruption timeline, separating the fare refund from out-of-pocket expenses and any separate compensation question, and asking the carrier to state its own policy in writing. Does NOT cite passenger-rights regulation or any compensation scheme as authority, state an eligibility rule, amount, or deadline, name an enforcement body, predict the outcome, or invent booking details. Distinct from legalprep_refund_chargeback_dispute_preparer (card-issuer chargeback) and advocacy_recurring_charge_dispute (subscriptions). Not legal advice."
techniques:
  - CM-01
  - RT-05
  - ST-02
  - ST-03
  - QA-01
difficulty: beginner
intended_use: model-testing
tags:
  - written-advocacy
  - self-advocacy
  - travel
  - refund
  - self-submit
  - consumer
  - flight-cancelled
updated: "2026-09-24"
related_prompts:
  - domain-legal/personal-self-advocacy/consumer-scams/legalprep_refund_chargeback_dispute_preparer.md
  - domain-written-advocacy/cross-cutting/advocacy_escalation_ladder_designer.md
  - domain-written-advocacy/cross-cutting/advocacy_response_analyzer.md
  - domain-written-advocacy/institutions-and-records/advocacy_regulator_complaint_drafter.md
---

**Purpose:** Help you write **your own** dated request to a carrier or travel seller after a trip went wrong — a cancelled or heavily delayed flight, a schedule change you did not accept, a downgrade, denied boarding, or a missed connection. It builds a timestamped timeline of what happened, separates **three different asks** that usually get blurred together (the fare refund, the expenses you paid out of pocket, and any separate compensation question), and asks the carrier to state in writing which of its own policies it applied.

**When to use:** The disruption has happened, you are home or at least safe, you have your booking and receipts, and the carrier's chat or phone line gave you a voucher, a vague answer, or nothing.

**When NOT to use:** You are still stranded and need to get somewhere → deal with rebooking and safety first; this letter can wait. You want your card issuer to reverse the charge → `domain-legal/personal-self-advocacy/consumer-scams/legalprep_refund_chargeback_dispute_preparer.md`. Your claim is against your **travel insurer** rather than the carrier → `../insurance-and-medical/advocacy_insurance_claim_denial_appeal.md` once a decision exists. You were injured, or baggage loss involves significant value → route to an attorney before corresponding.

---

## Boundary & Routing Block

Use a different pathway if:
- **You are stranded, unwell, travelling with a dependent who needs care, or without accommodation** → safety and rebooking come first. Ask the carrier at the desk or by chat what it will provide now, keep every receipt, and write the letter afterwards.
- **Anyone was injured, or there was an incident on board or in transit** → route to an attorney or **legal aid** before writing; what you say in a refund letter can matter later.
- **You booked through an agent, platform, or package operator** → the seller and the carrier may each point at the other. Ask the seller in writing who is handling the refund, and send to that party; keep both in the record.
- **You want a chargeback** → the card issuer has its own process and time limit; see the chargeback preparer above and **act on the issuer's stated deadline**, not an assumed one.
- **You believe a statutory compensation scheme applies** → such schemes exist in some jurisdictions and routes, and their conditions are specific. Do **not** rely on this prompt to say whether one applies. `[VERIFY: identify from an official government source whether any passenger-rights scheme covers your journey, and what it requires.]` If you verify one yourself, it can appear in the letter as **your own stated basis, in your own words**.

This prompt is educational support for preparing your own correspondence. It is not a substitute for legal services.

---

## Scope Boundary — Read First

This **drafts your own written refund and expense request for you to send**. It is **not legal advice, a legal filing, or a substitute for an attorney or your jurisdiction's law.** It will **not** tell you whether you are entitled to a refund or compensation; cite a passenger-rights regulation, convention, or consumer statute as authority; state a compensation amount, a delay threshold, an extraordinary-circumstances rule, or a claim deadline; name an aviation, transport, or consumer enforcement body or supply its address; tell you whether the carrier's stated reason for the disruption is true; predict whether you will be paid; or invent a booking reference, flight number, time, or receipt. Passenger rules **vary by country, route, carrier, ticket type, and date, and change over time.** Where such a concept appears it is flagged *verify for your journey*.

---

## Core Principles

1. **The timeline is the letter.** Scheduled time, actual time, when you were told, what you were told, and by whom — each with a timestamp. A disruption claim is decided on those facts, and memory degrades fast.
2. **Three asks, kept separate.** (a) Refund of the fare for the part not flown or not accepted; (b) reimbursement of out-of-pocket expenses caused by the disruption, each with a receipt; (c) any compensation question, asked as a question. Combined into one lump, they get answered with the smallest.
3. **Cash or voucher is your decision to state.** If you want the refund to your original payment method, say so explicitly. Accepting a voucher by clicking a link can close the question — decide before you click.
4. **Ask them to name their policy.** The carrier's own conditions of carriage and customer commitments are the authority in this exchange. Ask which provision they applied, and quote it back if you have it.
5. **Quote their stated reason; do not argue it.** Record the reason they gave for the disruption verbatim. Whether it was genuinely outside their control is not something you can establish from a letter.
6. **Receipts, not estimates.** Every expense line has a receipt or is flagged `[NEED DOCUMENT:]`. A reasonable-looking estimate invites a request for proof and delays everything.

---

## Your Input

- **Your jurisdiction and the journey's origin and destination countries:** [required — rules depend on both]
- **Are you still travelling or stranded?:** [if yes → Boundary & Routing Block, first]
- **Who you booked with and who operated the service:** [seller / carrier — may differ]
- **Booking reference, ticket number, passengers:** [#, #, names]
- **Scheduled and actual times for each leg:** [YYYY-MM-DD HH:MM, local time]
- **What happened:** [cancelled / delayed / schedule change / downgrade / denied boarding / missed connection]
- **When and how you were told, and the reason given, verbatim:** [timestamp, channel, exact words]
- **What was offered at the time, and what you accepted or declined:** [rebooking, voucher, meals, hotel]
- **Out-of-pocket expenses:** [item, date, amount, currency, receipt held yes/no]
- **Any prior contact:** [date, channel, reference, outcome]
- **Any statutory basis you have personally verified:** [your own words, or none]
- **Injury, incident, or high-value loss?:** [if yes → Boundary & Routing Block]

---

## Constraints

**Must:**
- Require the jurisdiction and journey countries; use only the facts and documents the user supplies.
- Screen for being stranded or unsafe first, then injury or incident, and route those before drafting.
- Build a timestamped timeline in local time, noting the time zone.
- Separate fare refund, expense reimbursement, and any compensation question into distinct numbered asks.
- State the user's preferred refund method explicitly and flag the voucher-acceptance risk.
- Record the carrier's stated disruption reason verbatim, without characterizing it.
- Ask the carrier to identify the policy provision it applied.
- Include a Sending Log and label the output `MY OWN REQUEST — NOT A LEGAL FILING`.

**Must Not:**
- Cite or invent a passenger-rights regulation, convention, scheme, threshold, compensation amount, or claim deadline.
- State that the user is entitled to a refund or compensation.
- State whether the carrier's reason qualifies as outside its control.
- Name an enforcement body, ombudsman, or dispute scheme, or supply its contact details.
- Predict the outcome or assess the claim's strength.
- Invent a booking reference, flight or service number, time, receipt, or amount.
- Threaten legal action, a chargeback, or public complaints as leverage.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for stranded, unwell, or unaccommodated travellers → rebooking and safety first. Screen for injury, incident, or high-value loss → attorney. Capture the jurisdiction and journey countries. Restate the boundary: this drafts a request; entitlement questions route elsewhere.

### Stage 2 — Build the Timeline
For each affected leg, record scheduled versus actual departure and arrival, in local time with the zone. Add each notification — when, channel, what was said, the reason given verbatim. Flag unknown times `[NEED DATE:]` rather than estimating.

### Stage 3 — Separate the Three Asks
Classify each thing the user wants: fare refund (which segments, which amount), expenses (itemized with receipts), or a compensation question. Compensation is phrased as a question about the carrier's own policy and any scheme the user has personally verified — never as an asserted entitlement.

### Stage 4 — Resolve Seller versus Carrier
Where the booking and the operator differ, draft a one-line request asking which party handles the refund, and address the main letter to that party with the other copied.

### Stage 5 — Draft the Request and Close
Compose the user's dated letter with the timeline, the three asks, the refund method, the request to identify the policy applied, and a response window. Add the Sending Log. Point to the escalation ladder and to the `[VERIFY:]` route for any external body.

---

## Output Format

```markdown
MY OWN TRAVEL REFUND REQUEST — NOT A LEGAL FILING
From: [your name], [contact]. To: [carrier or seller, customer relations]. Date: [YYYY-MM-DD].
Delivery: [claims form / designated email / post]. Keep a copy and any form confirmation number.
This is my own request. It does NOT cite passenger-rights law, claim a legal entitlement, or
characterize the reason you gave for the disruption.

Re: Booking [#], [service #] on [YYYY-MM-DD], [origin] to [destination], passengers [names]

## What happened (times local, zone noted)
| Leg | Scheduled | Actual | Notified (when / how) | Reason given, verbatim |
|---|---|---|---|---|
| [origin–dest] | [YYYY-MM-DD HH:MM] | [HH:MM / cancelled] | [timestamp, app/desk] | "[exact words]" |

At the time I was offered [rebooking / voucher / meals]. I [accepted / declined] [what].

## What I am asking
1. **Fare refund:** a refund of [$X] for [segments not flown / the change I did not accept],
   to my original payment method. I am not asking for a voucher.
2. **Expenses caused by the disruption** (receipts enclosed):
   | Date | Item | Amount | Receipt |
   |---|---|---|---|
   | [YYYY-MM-DD] | [hotel] | [$X] | [enclosed / NEED DOCUMENT:] |
3. **Compensation question:** please tell me whether your policy provides compensation for this
   disruption and, if not, which provision you are applying.
   [If personally verified: "My own understanding is that [your own words]."]

Please also tell me which provision of your conditions of carriage you applied, and respond in
writing by [date].
[Your name], [YYYY-MM-DD]

---
## Sending Log (keep with your copy)
| Sent | Method | Sent to | Reference # | Proof kept | Response due | Outcome |
|---|---|---|---|---|---|---|
| [YYYY-MM-DD] | [method] | [channel] | [#] | [confirmation] | [YYYY-MM-DD] | [ ] |

Note to self: I will not accept a voucher by clicking a link unless I have decided to. Whether I
am entitled to anything is for an attorney or an official source —
`[VERIFY: identify any passenger-rights scheme and the correct body for my journey from an
official government source]`. *Verify for your journey — rules vary by route, carrier, and date.*
```

---

## Verification

- [ ] Stranded/unsafe and injury/incident screened first and routed?
- [ ] Jurisdiction and journey countries captured?
- [ ] Timeline in local time, zone noted, gaps flagged `[NEED DATE:]`?
- [ ] Refund, expenses, and compensation question kept as three separate asks?
- [ ] Refund method stated and the voucher-acceptance risk flagged?
- [ ] Carrier's reason quoted verbatim and not characterized?
- [ ] Carrier asked to identify the policy provision applied?
- [ ] No regulation, scheme, threshold, amount, or deadline cited or invented?
- [ ] No enforcement body named; `[VERIFY:]` used instead?
- [ ] No entitlement claim, outcome prediction, or threat?
- [ ] Every expense backed by a receipt or flagged `[NEED DOCUMENT:]`?
- [ ] Sending Log included?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "Under [regulation] you owe me [amount] for a 3-hour delay" | Ask whether their policy provides compensation; cite no scheme or amount |
| "Weather isn't a valid excuse — that was your fault" | Quote the reason they gave; do not characterize it |
| "Refund me or I'll file a chargeback and post reviews" | Ask plainly; a chargeback is a separate process with its own deadline |
| "Complain to [named aviation authority] at [address]" | `[VERIFY: identify the correct body from an official source]` |
| One total: "I want $1,400 for everything" | Three numbered asks, each itemized |
| "Hotel about $200" with no receipt | Receipt enclosed, or `[NEED DOCUMENT: hotel receipt]` |
| "Departed around 6pm" | Exact local time from the app or boarding pass, or `[NEED DATE:]` |
| Draft while the user is still stranded at the gate | Rebooking and safety first; letter afterwards |

---

## Adaptations

**By disruption type:**
- **Cancellation:** Record when you were told relative to departure, and whether a rebooking was offered, accepted, or declined — both matter to how the carrier reads the request.
- **Schedule change before travel:** State the original and new times and whether you accepted the change. If you did not travel, the refund ask is for the whole booking.
- **Downgrade:** Record the class booked and the class flown, and ask for the fare difference as the carrier calculates it; do not compute it yourself.
- **Denied boarding:** Record whether you were asked for volunteers, what you were offered, and whether you signed anything.

**By seller:**
- **Package or tour operator:** Address the operator, not each component supplier, and ask which parts of the package it will refund.
- **Online platform:** Ask in writing whether the platform or the carrier holds your money now; send to whoever answers.

---

## Related Prompts

- `domain-legal/personal-self-advocacy/consumer-scams/legalprep_refund_chargeback_dispute_preparer.md` — if you decide to go to your card issuer.
- `../cross-cutting/advocacy_escalation_ladder_designer.md` — if customer relations refuses or stalls.
- `../cross-cutting/advocacy_response_analyzer.md` — to read a partial refund or voucher offer.
- `../institutions-and-records/advocacy_regulator_complaint_drafter.md` — once the correct body is verified.
