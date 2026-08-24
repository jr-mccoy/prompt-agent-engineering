---
title: "Insurance Needs Analysis — Life, Disability, and LTC Coverage Gap"
category: finance/personal-finance-planning
description: "Quantify life, disability, and long-term-care insurance needs using both the human-life-value and needs-based (DIME/capital-needs) methods, identify the coverage gap against existing policies, and report results as scenario bands with stated assumptions."
techniques:
  - NE-11
  - NE-10
  - RT-02
  - DS-02
  - QA-04
difficulty: intermediate
tags:
  - insurance
  - life-insurance
  - disability-insurance
  - long-term-care
  - coverage-gap
  - needs-analysis
updated: "2026-06-08"
related_prompts:
  - domain-finance/personal-finance-planning/finance_net_worth_cashflow_diagnostic.md
  - domain-finance/personal-finance-planning/finance_emergency_fund_sizing.md
  - domain-finance/personal-finance-planning/finance_estate_beneficiary_review.md
  - domain-finance/field_guide.md
---

**Informational only — not financial, investment, or tax advice. Personal financial decisions depend on individual circumstances; consult a qualified financial planner (CFP), licensed insurance professional, or attorney as appropriate.**

## Objective

Quantify a household's life, disability, and long-term-care (LTC) insurance needs across multiple methods, compare the need to existing coverage to derive the coverage gap, and present the result as scenario bands — with every formula and assumption explicit and the calculation routed to a licensed professional for product selection.

## When to Use

- A household wants to know how much life/disability/LTC coverage it needs.
- A major life event (marriage, child, mortgage, business) changes coverage needs.
- Reviewing whether existing policies leave a gap.
- Comparing the human-life-value and needs-based methods for life insurance.

## Inputs / Context Required

```
<insurance_inputs>
Household:
  Ages of insured(s) and dependents:   [years]
  Number/ages of dependents:           [years to independence]
Income:
  Insured annual income (each earner):  [$]
  Income replacement years desired:     [until kids independent / spouse retirement]
Obligations:
  Mortgage balance:                     [$]
  Other debts:                          [$]
  Future education funding goal:         [$]
  Final expenses (funeral, etc.):        [$]
Assets available to offset need:
  Liquid savings/investments:            [$]
  Existing life insurance (face):        [$ each policy]
  Existing disability coverage:          [% of income; group/individual]
  Existing LTC coverage:                 [daily/monthly benefit, period]
ASSUMPTIONS (user-supplied; state ranges):
  Discount rate / return on proceeds:    [%]
  Income growth / inflation:             [%]
  Spouse's own income:                   [$]
</insurance_inputs>
```

## Constraints

### Must
- Apply BOTH the human-life-value (HLV) and needs-based (capital-needs/DIME) methods for life insurance and reconcile them (RT-02, NE-11).
- Compute disability need as income-replacement gap (after existing coverage), noting benefit taxability depends on who paid premiums (verify).
- Estimate LTC need from cost-of-care assumptions and self-funding capacity (DS-02).
- Derive the coverage gap = need − existing coverage − offsetting assets.
- Present scenario bands (replacement years, discount rate, inflation) (NE-10).
- State that this is needs sizing, not product selection; route product choice to a licensed agent (QA-04).

### Must Not
- Assert tax treatment of benefits, policy specifics, or premium costs as fact — mark "[verify with licensed professional]".
- Use a single method for life insurance; reconcile two.
- Ignore offsetting assets and existing coverage (over-insuring).
- Recommend a specific product, carrier, or rider.

## Instructions

**Step 1 — Life insurance: human-life-value method (NE-11)**

```
HLV = Present value of future after-tax income the insured would provide to dependents
HLV = Σ [ (Income_t × (1 − self-consumption %)) / (1 + discount rate)^t ]
   over the income-replacement years
(self-consumption % = portion the insured spends on themselves, not dependents)
```

**Step 2 — Life insurance: needs-based (DIME / capital-needs)**

```
DIME framework:
  D — Debt: mortgage + other debts to retire
  I — Income: PV of income to replace for N years
        Income need = (Annual income gap) × [1 − (1+g)^N/(1+r)^N] / (r − g)  (growing annuity PV)
  M — Mortgage (if not in D)
  E — Education: future funding goal (see education prompt)
  + Final expenses + emergency buffer for survivors
Total need = D + I + M + E + final expenses
Less: liquid assets + existing life insurance
= Net life insurance gap
```

**Step 3 — Reconcile HLV vs. needs-based**

State both figures; explain why they differ (HLV = income capitalization; needs-based = specific obligations). Recommend a coverage range bounded by the two, not a single number.

**Step 4 — Disability insurance need**

```
Monthly income need in disability = essential expenses (after spouse income, any passive income)
Existing coverage = group LTD benefit (% of income; often taxable if employer-paid — verify)
Disability gap = income need − existing after-tax benefit
Note: own-occupation vs. any-occupation definition materially changes value (verify policy).
```

**Step 5 — LTC need**

```
Estimated annual cost of care = [user-supplied local cost; verify]
Expected duration assumption = [years; state range, e.g., 2–4]
Self-funding capacity = portion of assets/income available without derailing the plan
LTC gap = PV(expected care cost) − self-funding capacity
Note: alternatives include self-insuring, hybrid life/LTC, traditional LTC — route to agent.
```

**Step 6 — Coverage gap summary & scenario bands (NE-10)**

| Coverage | Need (low/base/high) | Existing | Offsetting assets | Gap |
|---|---|---|---|---|
| Life | | | | |
| Disability | | | | |
| LTC | | | | |

**Step 7 — Verification (QA-01)**

Recompute the needs-based income PV; confirm gap = need − existing − assets; confirm HLV and needs figures are both shown.

## Output Format

### Life Insurance Need
[HLV and needs-based; reconciled range]

### Disability Need
[Income gap after existing coverage; policy-definition caveat]

### LTC Need
[Cost-of-care estimate and self-funding capacity]

### Coverage Gap Summary
[Step 6 table with bands]

### Caveats & Routing
[Product selection to licensed agent; tax treatment "[verify]"]

### Verification Notes
[Step 7]

## Verification

- [ ] Both HLV and needs-based life methods computed and reconciled to a range.
- [ ] Disability gap nets out existing coverage; benefit-taxability caveat noted.
- [ ] LTC need from cost-of-care and self-funding capacity.
- [ ] Coverage gap = need − existing − offsetting assets for each type.
- [ ] Scenario bands (replacement years, discount rate) presented.
- [ ] Benefit tax treatment and policy specifics marked "[verify]".
- [ ] No specific product/carrier recommended.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Single life-insurance number | Reconcile HLV and needs-based; present a range |
| Over-insuring by ignoring assets | Net out liquid assets and existing coverage |
| Asserting benefit taxability | Mark "[verify]"; employer-paid LTD benefits are often taxable |
| Ignoring own-occ vs. any-occ | Note the definition materially changes disability value |
| Optimism bias on LTC duration | Use a range; note tail-risk of multi-year care |
| Recommending a product | Size the need only; route product choice to a licensed agent |
