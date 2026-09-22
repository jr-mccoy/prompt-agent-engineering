---
title: "Services Rate Floor Model"
category: corporate-finance-fpa/services-practice
description: "Derive the minimum defensible billable rate for a services practice from total cost of delivery — overhead, unbilled time, self-employment burden, benefits self-funding, and target margin — producing a floor below which work destroys value rather than earning less"
techniques:
  - RT-05
  - CM-02
  - OC-03
  - QA-08
  - MP-04
difficulty: intermediate
tags:
  - services-practice
  - rate-setting
  - cost-of-delivery
  - utilization
  - overhead-absorption
  - solo-operator
  - consulting
updated: "2026-09-21"
---

# Services Rate Floor Model

**Objective:** Compute the **minimum billable rate** at which a services practice
covers its full cost of delivery and target margin. The output is a floor — a number
below which an engagement destroys value regardless of how attractive the client is —
plus the sensitivity of that floor to the utilization assumption behind it.

**When to Use:** Use annually, whenever cost structure changes, and before quoting an
engagement at a discount. Every discount conversation should be held against this
number rather than against the last rate you charged.

**Scope note.** `domain-finance/EXPANSION_ROADMAP.md` positions this domain as
institution-grade practitioner finance. This prompt is deliberately the one-person
and small-shop exception, following the precedent already set in-domain by
`../tax-planning/solo_dev_tax_strategy.md` and
`../personal-finance-planning/solo_dev_financial_planning.md`.

This is **distinct from** `finance_unit_economics_model.md`, which models CAC, LTV
and contribution margin for a *product* with a variable cost per unit sold, and from
`finance_breakeven_operating_leverage.md`, which analyses fixed-versus-variable cost
structure at a firm. Neither derives a billable-hour floor from the non-billable
ratio, which is the dominant term here and has no product analogue.

---

## Context Gathering

1. **Fixed annual cost of being in business**
   - "Software, subscriptions, tooling, hosting."
   - "Insurance — professional indemnity, public liability, equipment."
   - "Accounting, legal, banking, payment fees."
   - "Workspace, equipment amortisation, phone, connectivity."
   - "Professional development, conferences, memberships, certifications."
   - "Marketing, website, any retained help."

2. **Compensation and its burden**
   - "Target personal income before tax."
   - "Self-employment or employer-equivalent payroll burden — what rate applies?"
   - "Pension or retirement contribution you are self-funding."
   - "Healthcare, if self-funded."
   - "Paid time off you must fund yourself — days of holiday and expected sick days."

3. **Utilization**
   - "Sellable days per year, from `services_capacity_and_utilization_planner.md`."
   - "Realistic billable percentage of those — measured, not hoped."

4. **Risk and margin**
   - "Bad-debt rate — what fraction of invoiced work has gone unpaid?"
   - "Typical estimate overrun — actual over quoted, last five engagements."
   - "Target margin above cost, and what it is for."

The margin question needs pressing. Margin in a solo practice is not profit in the
casual sense: it funds the gap between engagements, the reinvestment that keeps the
practice sellable, and the reserve that lets you decline bad work. A practice running
at zero margin cannot say no, which is what makes it a practice rather than a job.

---

## Method

### Step 1 — Total the annual cost base

```
Fixed business cost                                  A
Target personal income (pre-tax)                     B
Employment burden on B (rate × B)                    C
Self-funded pension / healthcare                     D
                                          Total cost = A + B + C + D
```

Do not net anything off. Every cost of being in business is absorbed by billable
hours, because there is no other revenue line.

### Step 2 — Compute genuinely billable days

```
Working days available                               W
− holiday and expected sick days                     H
= present days                                       P = W − H
× billable fraction                                  U
= billable days                                      Bd = P × U
```

`U` is the number people get wrong. Sales, proposals, invoicing, bookkeeping,
learning and tooling are all real and all unbillable. A measured `U` for an
established solo practice usually lands between 0.55 and 0.70. Using 0.85 because it
is achievable in a good month produces a floor roughly 20% too low — and the error
is invisible until the year ends short.

### Step 3 — Load for risk

Two adjustments, applied to the rate rather than the cost base:

- **Bad debt** — divide by `(1 − bad-debt rate)`. Work that is delivered and not paid
  for still consumed capacity.
- **Estimate overrun** — divide by `(1 + typical overrun)` where the practice quotes
  fixed prices. Overrun is unbilled delivery; it lowers the effective rate on every
  fixed-fee engagement.

### Step 4 — Compute the floor

```
Break-even day rate   = Total cost / Bd
Risk-loaded           = Break-even / ((1 − bad debt) × (1 + overrun))
Floor at target margin = Risk-loaded / (1 − target margin)
Floor hourly          = Floor day rate / billable hours per day
```

Note the margin is applied as a divisor, not a multiplier. A 20% target margin means
cost is 80% of price, so the divisor is `(1 − 0.20)`. Multiplying cost by 1.20 yields
a 16.7% margin and is the most common arithmetic error in rate setting.

### Step 5 — Test the utilization sensitivity

Recompute the floor at `U` of 0.50, 0.60, 0.70 and 0.80 and tabulate. The spread is
usually startling, and it is the honest answer to "why does my rate feel high?" — the
rate carries the unbillable time. Present this table to anyone, including yourself,
who argues the rate down.

### Step 6 — State the three thresholds

Convert the single number into three decision lines:

| Line | Meaning |
|---|---|
| **Walk-away** | The risk-loaded break-even. Below this, the engagement consumes capacity and returns nothing. |
| **Floor** | Break-even plus target margin. The standard quote basis. |
| **Standard** | Floor plus positioning premium, where the market supports it. |

Discounting toward walk-away is a decision about reserves and pipeline (see the bench
date in `services_capacity_and_utilization_planner.md`), not about the client.
Discounting *below* walk-away is not a discount; it is a subsidy paid to the client
out of your own reserves.

---

## Output Format

```markdown
## Rate floor — [practice], [year]

### Cost base
| Line | Annual |
|---|---|
| Fixed business cost | |
| Target income (pre-tax) | |
| Employment burden @ [x]% | |
| Pension / healthcare | |
| **Total cost** | |

### Billable capacity
| Line | Days |
|---|---|
| Working days | |
| − holiday / sick | |
| = present days | |
| × billable fraction [U] | |
| **= billable days** | |

### Risk loading
| Factor | Value |
|---|---|
| Bad-debt rate | |
| Typical overrun | |

### Result
| Threshold | Day rate | Hourly |
|---|---|---|
| Walk-away (risk-loaded break-even) | | |
| Floor (at [x]% margin) | | |
| Standard (with premium) | | |

### Utilization sensitivity
| U | Floor day rate |
|---|---|
| 0.50 | |
| 0.60 | |
| 0.70 | |
| 0.80 | |

**Current quoted rate:** [x] — [above floor / between walk-away and floor / below walk-away]
```

---

## Verification

- [ ] Every cost of being in business is in the base; nothing is netted off.
- [ ] `U` is measured from actual billable days, not assumed.
- [ ] Employment burden is applied at the correct rate for the jurisdiction and entity.
- [ ] Margin is applied as `/(1 − m)`, not `× (1 + m)`.
- [ ] Bad debt and overrun are both applied, even if small.
- [ ] The sensitivity table is present and spans 0.50 to 0.80.
- [ ] The three thresholds are distinct numbers, and the current rate is placed
      against them.

**False-positive prevention.** The dominant failure is an optimistic `U`. It is the
single largest lever in the model and the one most subject to wishful thinking. If
the practice has not measured billable days, use 0.60 and mark it assumed rather than
using a number from a good quarter.

The second failure is omitting the employment burden and self-funded benefits, which
between them commonly add 25–40% to the cost of the same take-home pay an employee
receives. A rate benchmarked against an employed salary without this loading is
systematically below cost.

The third is treating the floor as a target. The floor is where value creation stops,
not where pricing starts. Quoting at the floor means every overrun is a loss.

**This is not tax or accounting advice.** Employment-burden rates, deductibility and
entity treatment vary by jurisdiction and circumstance. Use the output as the input
to a conversation with an accountant, not as a substitute for one. See
`../tax-planning/solo_dev_tax_strategy.md` and
`../tax-planning/finance_entity_structure_tax_comparison.md`.

---

## Related

- `../../domain-business-strategy/client-services/services_capacity_and_utilization_planner.md` — supplies `U`
- `../../domain-business-strategy/client-services/services_pricing_model_selector.md` — the structure this floor prices into
- `../../domain-business-strategy/client-services/services_client_value_quantification.md` — the ceiling
- `finance_engagement_profitability_postcalc.md` — measures whether the floor held
- `finance_breakeven_operating_leverage.md` — the firm-level analogue
