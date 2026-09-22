---
title: "Productized Offer Designer"
category: client-services/offer
description: "Convert a bespoke service into a fixed-scope, fixed-price, fixed-duration package — identifying the repeatable core, standardising the process, setting the input contract, and testing whether the variance across past engagements is low enough for a fixed price to be safe"
techniques:
  - CM-03
  - NE-09
  - QA-08
  - OC-03
  - RT-05
difficulty: advanced
tags:
  - consulting
  - freelance
  - productized-service
  - fixed-price
  - packaging
  - repeatability
  - solo-operator
updated: "2026-09-21"
---

# Productized Offer Designer

**Objective:** Convert a bespoke service into a **fixed-scope, fixed-price,
fixed-duration** package: the repeatable core extracted from past engagements, a
standardised process, an input contract the client must satisfy, and an evidence-based
verdict on whether variance is low enough for a fixed price to be safe.

**When to Use:** Use when you have delivered a similar engagement at least five times,
proposals are consuming disproportionate effort, or you want an offer that can be
sold without a bespoke scoping call each time. Nothing in this repository covers
productized services; the adjacent monetization prompts address app revenue.

This is **distinct from** `services_offer_definition_and_boundary.md`, which defines
what an offer *is* and can apply to bespoke work. This one tests whether an offer is
**repeatable enough to fix a price to**, and its central output is the variance
analysis that answers that.

---

## Context Gathering

The evidence must come from delivered work. A productized offer designed from
imagination prices the version you imagine, not the version you deliver.

1. **The history** — for the last five to ten similar engagements:
   - "Effort actually spent, per engagement."
   - "What varied most between them?"
   - "Which steps did you perform every single time, without exception?"
   - "Which steps appeared in some and not others, and what predicted that?"

2. **The inputs**
   - "What did you need from the client each time?"
   - "When an engagement ran long, was the cause usually you or the input?"

3. **The output**
   - "Was the final artifact substantially the same shape each time?"
   - "How much of it was reused versus written fresh?"

4. **The buyer**
   - "Who signed? Did they need a bespoke conversation, or would a page have done?"

---

## Method

### Step 1 — Measure variance before designing anything

This is the gate. Compute across the historical engagements:

- Median effort
- Range (minimum and maximum)
- **Coefficient of variation** — standard deviation over mean

Then apply the verdict:

| CV | Verdict |
|---|---|
| Below ~0.25 | Productize at a fixed price safely |
| 0.25–0.40 | Productize with a tight input contract and a stated exclusion boundary |
| Above ~0.40 | **Do not fix a price.** Either narrow the scope until variance falls, or keep it bespoke |

Fewer than five data points is itself a "do not fix a price" verdict. Sell it as a
fixed-scope day-rate engagement and collect the data.

### Step 2 — Separate the repeatable core from the variable tail

Three buckets:

- **Core** — performed every time. This is the product.
- **Conditional** — performed when a named condition holds. These become named
  add-ons with their own price, not silent inclusions.
- **Bespoke** — genuinely different each time. These are excluded, and the exclusion
  is explicit.

The discipline is that anything you *might* do is either conditional with a price or
excluded. There is no third category, because the third category is where fixed-price
margin is lost.

### Step 3 — Write the input contract

Fixed price is only safe when the inputs are guaranteed. For each required input:

| Input | Owner | Due | If late or absent |
|---|---|---|---|

The "if late" column must have real consequences — a clock that keeps running, a
rescheduling fee, or a defined pause with a restart charge. Without it, the client's
delay becomes your cost, which is exactly the risk a fixed price transfers to you.

### Step 4 — Standardise the process and the artifact

- **Process** — the same numbered steps every time, with the checkpoints named.
- **Artifact** — a template with the sections fixed. Variation lives in the content,
  not the structure.
- **Reusable assets** — checklists, scripts, question sets, analysis harnesses.

This step is where the margin comes from. A productized offer that is a fixed price
attached to an unstandardised process is just a fixed price with worse odds.

### Step 5 — Set duration and price from the distribution, not the median

- **Duration** — quote the 75th percentile of historical elapsed time, not the
  median. Half your engagements have exceeded the median by definition.
- **Price** — from `../../domain-finance/corporate-finance-fpa/finance_services_rate_floor_model.md`
  applied to the **75th-percentile effort**, not median effort. Fixed price must
  absorb its own variance; pricing at the median guarantees that roughly half of
  deliveries lose against plan.
- **Ceiling check** — the result must still sit inside the value band from
  `services_client_value_quantification.md`. If the variance-loaded price exceeds
  what the work is worth, the offer is not productizable at this scope. Narrow it.

### Step 6 — Define the escape hatch

Every productized offer needs a stated condition under which it converts back to
bespoke, decided early rather than absorbed. Typically: discovery reveals a condition
on the exclusion list, or a required input is unavailable. Name what happens —
convert to day rate, requote, or refund and stop.

---

## Output Format

```markdown
## Productized offer — [name]

### Variance evidence
| Engagement | Effort | Elapsed | Notable variation |
|---|---|---|---|
Median [x] · Range [min–max] · CV [x] · n = [x]
**Verdict:** [productize / productize with tight inputs / do not fix price]

### Core (every time)
1. ...

### Conditional add-ons
| Add-on | Triggered when | Price |
|---|---|---|

### Excluded
- ...

### Input contract
| Input | Owner | Due | If late |
|---|---|---|---|

### Standardised assets
| Asset | Replaces |
|---|---|

### Commercial terms
- Duration: [75th percentile] — quoted as [x]
- Price: [x], from [75th-pct effort] × [rate floor], variance-loaded
- Value-band check: [inside / outside] the band of [range]
- Payment: [structure]

### Escape hatch
Converts to bespoke if [condition] → [action]
```

---

## Verification

- [ ] Variance is computed from at least five delivered engagements, with real numbers.
- [ ] The CV verdict is stated and honoured — a CV above 0.40 does not get a fixed price.
- [ ] Every "might do" item is either a priced add-on or an explicit exclusion.
- [ ] Every input has a named consequence for lateness.
- [ ] Price uses 75th-percentile effort, not median.
- [ ] The escape hatch names a condition and an action.

**False-positive prevention.** The dominant failure is productizing on the strength
of two good engagements and a belief that the work is repeatable. Belief is not
variance data. If n is below five, the honest output is a fixed-scope day-rate
engagement plus instrumentation to collect the data — say that rather than producing
a package.

The second failure is pricing at median effort because it makes the offer look
competitive. A fixed price at median effort loses money on roughly half of
deliveries, and the losses are not symmetric: the long engagements are long because
something went wrong, which also consumes attention you cannot bill elsewhere.

The third is an input contract with no teeth. "Client will provide access promptly"
is not an input contract. If the consequence column reads as a hope, the fixed price
is effectively uncapped.

---

## Related

- `services_offer_definition_and_boundary.md` — the bespoke offer this narrows
- `services_pricing_model_selector.md` — the fixed-fee hard rules this must satisfy
- `../../domain-finance/corporate-finance-fpa/finance_engagement_profitability_postcalc.md` — the variance data this consumes
- `../../domain-legal/contracts-transactional/legal_sow_drafter.md` — the contractual form of the input contract
