# Rate floor and post-calculation: derivation and failure modes

## The floor, step by step

```
Total cost = fixed_business
           + target_income
           + target_income × employment_burden_rate
           + pension_and_healthcare

Present days  = working_days − absence_days
Billable days = present_days × billable_fraction

Break-even day rate = Total cost / Billable days
Walk-away           = Break-even / ((1 − bad_debt_rate) × (1 + typical_overrun))
Floor               = Walk-away / (1 − target_margin)
Standard            = Floor × (1 + positioning_premium)
```

### Why margin is a divisor

A 20% margin means cost is 80% of price. `cost / 0.80` gives a 20% margin;
`cost × 1.20` gives 16.7%. The second is the common error and quietly removes
around three points of margin from every quote.

### Why the billable fraction dominates

It is the only term that divides. At 0.80 billable a practice with £112,000 of cost
and 220 present days needs about £636/day at break-even; at 0.50 it needs
£1,018 — a 60% increase from an assumption, not from a cost. Sales, proposals,
invoicing, bookkeeping, learning and tooling do not disappear when you are busy.

A measured fraction for an established solo practice usually lands between 0.55 and
0.70. If it has not been measured, use 0.60 and mark it assumed. Using a figure
from a good quarter produces a floor roughly 20% too low, and the error is invisible
until the year ends short.

## The three thresholds

| Threshold | Meaning |
|---|---|
| **Walk-away** | Risk-loaded break-even. Below this the engagement consumes capacity and returns nothing |
| **Floor** | Break-even plus target margin. The standard quote basis |
| **Standard** | Floor plus positioning premium, where the market supports it |

Discounting toward walk-away is a decision about reserves and pipeline. Discounting
*below* walk-away is a subsidy paid to the client out of your own reserves.

## Post-calculation: the two corrections

```
Collected revenue = invoiced − write_offs − outstanding
Net revenue       = Collected revenue − direct costs
Total effort      = billed_days + unbilled_days
Realised rate     = Net revenue / Total effort
```

Both corrections are necessary and either alone still flatters the result.

- **Collected, not invoiced.** An unpaid invoice is not revenue. Carrying it at face
  value is how practices discover at year end that a profitable year was not.
- **Total effort, not billed.** Unbilled effort — rework, absorbed scope, extra
  meetings, client-specific admin — is the number most consistently under-reported,
  and it is exactly the number that turns an apparently profitable engagement into
  a marginal one.

## The estimate-error series

Each close-out appends `total_effort / estimated_days`. With five or more points:

| Coefficient of variation | Fixed-price eligibility |
|---|---|
| < 0.25 | Yes |
| 0.25 – 0.40 | With a tight input contract |
| > 0.40 | No — quote day rate or milestone |

Fewer than five points is itself a "do not fix a price" verdict: sell a fixed-scope
day-rate engagement and collect the data.

This series is the most valuable financial artifact a services practice owns, and it
only exists if the post-calculation is run on **every** engagement — including the
ones that went well, which establish the lower bound of the range.

## Not advice

Employment-burden rates, self-funded pension and healthcare treatment, deductibility
and entity structure are jurisdiction-specific and change. See
`domain-finance/tax-planning/solo_dev_tax_strategy.md` and speak to an accountant.
