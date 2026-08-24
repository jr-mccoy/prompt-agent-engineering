---
title: "Set a Defensible Price Anchored to Value, Not Self-Doubt"
category: personal-development/solo-dev
description: "Diagnose whether a solo dev's price is set from delivered-value evidence or from low confidence, then produce one defensible number, the evidence behind it, and a pre-committed raise trigger."
techniques:
  - ST-01
  - ST-02
  - RT-09
  - DS-06
  - QA-12
difficulty: intermediate
tags:
  - solo-developer
  - pricing
  - value-based-pricing
  - confidence
  - revenue
updated: "2026-07-23"
related_prompts:
  - domain-personal-development/prompts/solo-dev/solo_dev_deciding_alone.md
  - domain-personal-development/prompts/resilience/resilience_motivation_diagnosis.md
  - domain-personal-development/prompts/identity/identity_confidence_calibration.md
  - domain-finance/corporate-finance-fpa/finance_breakeven_operating_leverage.md
  - domain-personal-development/prompts/agency/agency_weekly_review.md
---

# Set a Defensible Price Anchored to Value, Not Self-Doubt

**Objective:** Separate the part of the user's price that is set by delivered-value evidence from the part set by low confidence, then output one defensible number, the evidence line behind it, and a pre-committed trigger for the next raise.

**When to use:** The user suspects they undercharge, keeps discounting before being asked, freezes when quoting, or hasn't raised prices in a long time despite better results. Also useful before sending a proposal or publishing a pricing page. Not for building a full monetization or pricing-model strategy across tiers — that's a market/finance task; this fixes the *number* and the *fear behind it*.

**Audience:** An individual pricing their own solo product or service. Not for advising someone else on their pricing, and not clinical. If pricing anxiety generalizes into persistent, overwhelming dread about money or worth, that is not a pricing problem — see `domain-psychology/` and a licensed professional.

---

## Inputs Required

1. **Current price(s).** The exact number(s) charged now, and the unit (per month, per project, per seat, one-time).
2. **Delivered-value evidence.** 3–8 concrete outcomes the product/service produced for real customers: time saved, money made or saved, problem removed, before/after. Each with a number or a specific customer quote if available. "Customers seem happy" does not count.
3. **Cost floor.** Rough monthly cost to keep the thing running plus the hours/month it takes — enough to know the number below which the user is paying to work.
4. **Pricing history.** When the price was last set or raised, and what happened (churn, silence, complaints, nothing).
5. **The self-talk.** In the user's own words, the sentence that runs when they consider charging more (e.g., "no one will pay that," "I'm not senior enough," "they'll leave").
6. **Comparable prices, if known.** What 2–4 alternatives (competitors, adjacent tools, doing-it-manually) cost the customer. Label as estimates if unverified.

If there is no delivered-value evidence (input 2 is empty or all vibes), refuse to set a higher number. Say so: a value-anchored price cannot be built without value evidence. Route to gathering it first.

---

## Instructions

### Step 1 — Locate the current price's true anchor

Classify what today's price is actually anchored to, using this fixed taxonomy. Pick the dominant one:

| Anchor | Tell | Confidence-driven? |
|---|---|---|
| **Cost-plus** | Price ≈ costs + a modest margin | Partly — safe, leaves value on table |
| **Competitor-matching** | Price copied from a rival | Partly — assumes rival priced well |
| **Round-number comfort** | Price is whatever felt "not greedy" | Yes — fear-set |
| **Fear-of-loss** | Price kept low to avoid churn/rejection | Yes — fear-set |
| **Value-anchored** | Price is a fraction of proven customer gain | No — evidence-set |

Name the anchor and cite the input that reveals it (usually input 5 plus input 4).

### Step 2 — Build the value line

From input 2, construct the single strongest value statement in the form: *"For [customer type], this produces [quantified outcome] worth roughly [$X or X hours] per [period]."* Use the most-supported outcome, not the most flattering. If outcomes vary by customer, pick the median case, not the best one.

A defensible value-based price typically captures **5–20%** of the value delivered. Compute that band from the value line. This band, not the user's nerves, sets the ceiling and floor.

### Step 3 — Separate the number from the doubt

Put three numbers side by side:
- **Fear number:** today's price (from Step 1, if fear-set).
- **Cost floor:** from input 3 — below this the user loses money.
- **Value band:** the 5–20% range from Step 2.

State plainly where the current price sits relative to the value band. The gap between the fear number and the bottom of the value band is the confidence tax — quantify it in dollars per month/year.

### Step 4 — Set one defensible number

Pick **one** new price. Not a range to "test your comfort with," not three tiers. It must sit inside the value band and above the cost floor, and it must be justifiable in one sentence using input 2 evidence. If the honest evidence only supports a small raise, set a small raise — do not inflate to make a point.

State the exact sentence the user will say when asked "why this price?" — grounded in the delivered outcome, never in the user's seniority, effort, or feelings.

### Step 5 — Set the raise trigger

Because confidence lags evidence, pre-commit the *next* raise to an observable event, so it isn't re-litigated by nerves each time. Use one concrete trigger: e.g., "raise to $Y when 3 more customers report [outcome]," or "raise 15% at 20 paying customers," or "on every renewal after a documented win." Put a date or a count on it.

### Step 6 — Name the rollout move

One physical action this week: update the pricing page, send the new quote on the next proposal, or email existing customers about the change (new customers only vs. grandfathering is the user's call — state the tradeoff in one line, don't decide it for them). Include what to watch after: silence and paying is the signal, not immediate complaints.

---

## Constraints

### Must
- Anchor the recommended price to input-2 evidence, computing the 5–20% value-capture band.
- Quantify the confidence tax in real money.
- Output exactly one new number and one raise trigger.
- Keep the new price above the cost floor from input 3.
- Refuse to raise if no value evidence exists.

### Must Not
- Justify a price by the user's effort, hours, credentials, or how they feel about themselves.
- Produce a multi-tier pricing architecture or a "test 3 prices" plan — one number.
- Cheerlead ("you're worth it!") or shame the user for undercharging.
- Invent competitor prices, market rates, or customer outcomes not supplied by the user.
- Recommend a discount, coupon, or "founder's pricing" as the safe default.

---

## False-Positive Prevention

1. **Low price is not always low confidence.** A deliberate land-and-expand or genuinely commodity offering can be correctly cheap. Only call it fear-set when input 5 self-talk or input 4 history confirms it — don't diagnose underpricing from the number alone.
2. **Don't confuse a raise the market rejected with a confidence problem.** If input 4 shows a prior raise caused real churn at a price still inside the value band, that's market data, not doubt — respect it.
3. **Best-case outcome is not the value line.** Pricing off the single happiest customer manufactures a number the median customer won't validate. Use the median case in Step 2.
4. **Above cost floor is not the same as defensible.** Clearing costs proves survival, not value. The band, not the floor, sets the price.
5. **Comfort with the new number is not the goal.** A correctly set value-based price usually feels slightly uncomfortable to quote. Don't lower it until it feels safe.
6. **Silence after a raise is success, not rejection.** Warn against reading normal quiet as proof the price was too high.

---

## Output Format

```
## Your current price's real anchor
[Anchor from taxonomy] — evidence: [input 4/5 citation]. Fear-set: [yes/no].

## The value line
For [customer], this produces [quantified outcome] worth ~[$X]/[period].
Value-capture band (5–20%): [$low]–[$high].

## Number vs. doubt
- Fear number (now): [$]
- Cost floor: [$]
- Value band: [$low]–[$high]
- Confidence tax: [$/month] = [$/year] left on the table.

## Your defensible number
New price: [$ exact], per [unit].
One-sentence justification: "[grounded in delivered outcome]."

## Raise trigger (pre-committed)
Raise to [$ next] when [observable event / count / date].

## Rollout (this week)
[Physical action]. New vs. existing customers: [one-line tradeoff, user decides].
Predicted check: after the change, expect [silence + payment], not immediate complaints.
```

---

## Verification

- [ ] The new price sits inside the computed 5–20% value band and above the cost floor.
- [ ] The recommended number is justified only by delivered-value evidence, never effort or credentials.
- [ ] The confidence tax is quantified in dollars.
- [ ] Exactly one new number and one observable raise trigger are produced.
- [ ] If input 2 had no value evidence, the prompt refused to raise and routed to gathering it.
- [ ] No competitor prices or customer outcomes were fabricated.
- [ ] No cheerleading, shaming, discount-defaults, or multi-tier sprawl.
