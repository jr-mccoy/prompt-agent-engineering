---
title: "Services Pricing Model Selector"
category: client-services/pricing
description: "Choose the charging structure for a services engagement — hourly, day rate, fixed fee, retainer, value share, or milestone — from the engagement's risk profile, measurability, and scope stability, and state the conditions under which the chosen model fails"
techniques:
  - CM-02
  - RT-05
  - MP-04
  - OC-03
  - QA-08
difficulty: intermediate
tags:
  - consulting
  - freelance
  - pricing
  - day-rate
  - retainer
  - fixed-fee
  - value-pricing
  - solo-operator
updated: "2026-09-21"
---

# Services Pricing Model Selector

**Objective:** Select the **charging structure** for a services engagement — hourly,
day rate, fixed fee, milestone, retainer, or value share — by reasoning from the
engagement's scope stability, outcome measurability, and who carries the estimation
risk. Output the chosen model, the conditions under which it breaks, and the
structural protection that makes it safe to offer.

**When to Use:** Use after scope is defined and before a number is quoted. This
chooses the *shape* of the price. The amount comes from
`../../domain-finance/corporate-finance-fpa/finance_services_rate_floor_model.md`
(the floor) and `services_client_value_quantification.md` (the ceiling).

This is **distinct from** `../startup/monetization_model_selector.md`, which chooses
between freemium, subscription, in-app purchase and ads for an app, and from
`domain-agentic-resources/skills/marketing/pricing-strategy/`, which sets SaaS tiers
and runs willingness-to-pay research on a product. Neither addresses billing
structures for delivered human work, where the dominant variable is who bears the
risk of a bad estimate.

---

## Context Gathering

1. **Scope stability**
   - "Can you write the deliverable list today and expect it to hold?"
   - "How many times has a similar engagement changed shape mid-flight?"
   - "Is the client's problem diagnosed, or is diagnosis part of the work?"

2. **Measurability**
   - "Is there a number that moves if this works? Can you see it? Within what window?"
   - "Does the client already track it, or would you be creating the measurement?"
   - "Can you separate your contribution from everything else happening?"

3. **Your position**
   - "How many times have you delivered something close to this?"
   - "What is your estimate error on the last five engagements — actual over quoted?"
   - "Can you afford to be wrong by 50% on this one?"

4. **Client constraints**
   - "How does their procurement pay — PO, invoice, milestone, recurring?"
   - "Is there a budget cycle or approval threshold that shapes what is signable?"

The estimate-error question is the one people skip and the one that decides. Fixed
fee with unknown estimate error is gambling with a number you have not measured.

---

## Method

### Step 1 — Place the engagement on the two axes that matter

```
                 scope stable
                      |
   fixed fee /        |        value share /
   milestone          |        outcome fee
                      |
  --------------------+--------------------  outcome measurable
                      |
   day rate /         |        retainer /
   hourly             |        capped discovery
                      |
                 scope unstable
```

The diagonal is the trap. Unstable scope with measurable outcomes tempts people into
value pricing before they can define what they are delivering; stable scope with
unmeasurable outcomes tempts people into hourly when a fixed fee would pay better.

### Step 2 — Assign the estimation risk deliberately

Every model is an answer to one question: *who pays when the estimate is wrong?*

| Model | Risk holder | Right when | Fails when |
|---|---|---|---|
| **Hourly** | Client | Scope genuinely unknowable; short or advisory work | Client cannot forecast spend; you are penalised for being fast |
| **Day rate** | Client | Scope unstable but time-boxable; the client buys availability | Days drift into an open commitment; you become staff |
| **Fixed fee** | You | Scope stable, you have delivered it before, estimate error known | You have never done it; the client controls an input you need |
| **Milestone** | Shared | Long engagement, natural checkpoints, staged payment needed | Milestones are invented for billing rather than real acceptance |
| **Retainer** | Shared | Ongoing need, recurring cadence, value is access | No scope ceiling — see `services_retainer_design_and_ceiling.md` |
| **Value share** | You, heavily | Outcome measurable, attributable, and you influence it materially | Attribution is contested; the client can starve the input |

### Step 3 — Apply the four hard rules

These override preference:

1. **Never fixed-fee undiagnosed work.** If diagnosis is part of the engagement, sell
   diagnosis as its own paid phase and price the rest afterward. A paid discovery
   phase that ends in a fixed-fee proposal is the single highest-leverage structure
   available to a services practice.
2. **Never value-price without attribution.** If you cannot separate your effect from
   everything else the client is doing, you have built a dispute, not a fee.
3. **Never quote fixed fee with unmeasured estimate error.** Go day rate or milestone
   until you have five data points.
4. **Never leave a retainer uncapped.** A retainer without a scope ceiling converts
   into unpaid employment within two quarters.

### Step 4 — Name the structural protection

The model alone is not the decision. Each pairs with a protection that makes it safe:

- Fixed fee → written assumptions list, change-order trigger, client-input SLA
- Day rate → minimum block, cancellation notice, maximum days per month
- Milestone → acceptance criteria per milestone, payment on acceptance not delivery
- Retainer → scope ceiling, rollover rule, quarterly reset
- Value share → agreed baseline measured *before* start, agreed measurement source,
  floor fee regardless of outcome

### Step 5 — Offer two structures, not one

Where the analysis allows, present the client a choice between two shapes at
equivalent expected value — for example a lower fixed fee with tight scope versus a
day rate with flexibility. A choice between two shapes converts the conversation from
"is this too expensive" to "which of these suits us," and the answer tells you what
the client actually fears.

---

## Output Format

```markdown
## Pricing structure — [engagement]

**Scope stability:** [stable / unstable] — because [evidence]
**Outcome measurability:** [measurable / not] — [metric, source, window, attribution]
**Your estimate error (last 5):** [range] — [or: unmeasured]

### Recommended structure
**[Model]** — [one-line rationale]

**Required protections**
- [protection] — without this, [specific failure]

**Breaks when**
- [condition] → [what to switch to]

### Alternative to offer alongside
**[Model]** at [shape] — differs by [risk transfer]

### Rejected, and why
| Model | Rejected because |
|---|---|

### Hard-rule check
- [ ] Not fixed-fee on undiagnosed work
- [ ] Not value-priced without attribution
- [ ] Not fixed-fee without measured estimate error
- [ ] Retainer, if chosen, has a scope ceiling
```

---

## Verification

- [ ] The model follows from the two axes, not from what you charged last time.
- [ ] Every protection names the specific failure it prevents.
- [ ] The four hard rules are explicitly checked, not assumed.
- [ ] If value share is recommended, the baseline, source and attribution method are
      all named — and the baseline is measurable *before* work starts.
- [ ] The rejected-models table has real reasons, not "not applicable."

**False-positive prevention.** The dominant error is recommending value-based pricing
because it is the highest-status answer. Value pricing requires three things
simultaneously: a measurable outcome, defensible attribution, and material influence
by you. Missing any one makes it worse than a day rate, because you now carry the
risk *and* the argument. If the analysis cannot name the metric, its source, the
measurement window, and what else could move it, do not recommend it.

The mirror error is defaulting to hourly because it feels safe. Hourly transfers
estimate risk to the client but caps your upside at your speed and invites
line-by-line scrutiny of your time. It is the right answer less often than it is the
chosen one.

---

## Related

- `../../domain-finance/corporate-finance-fpa/finance_services_rate_floor_model.md` — the floor any structure must clear
- `services_client_value_quantification.md` — the ceiling, from the client's economics
- `services_retainer_design_and_ceiling.md` — if retainer is selected
- `../../domain-personal-development/prompts/solo-dev/solo_dev_pricing_value_confidence.md` — holding the number when you are asked to justify it
- `../../domain-negotiation/contexts/negotiation_freelance_rate_conversation.md` — the live conversation
