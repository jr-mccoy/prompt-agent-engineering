---
title: "Retirement Projection Model — Required Savings Rate, Funding Gap, and Scenario Bands"
category: finance/personal-finance-planning
description: "Build an auditable retirement projection that solves for required savings rate, quantifies the funding gap against a target nest egg, and reports outcomes as base/optimistic/pessimistic scenario bands paired with a sequence-of-returns stress view — never a single deterministic number."
techniques:
  - NE-11
  - NE-10
  - QA-01
  - QA-02
  - DS-02
difficulty: intermediate
tags:
  - retirement
  - savings-rate
  - funding-gap
  - future-value
  - scenario-analysis
  - sequence-risk
updated: "2026-06-08"
related_prompts:
  - domain-finance/personal-finance-planning/finance_monte_carlo_withdrawal_analysis.md
  - domain-finance/personal-finance-planning/finance_asset_allocation_glidepath.md
  - domain-finance/personal-finance-planning/finance_fire_planning_model.md
  - domain-finance/personal-finance-planning/finance_net_worth_cashflow_diagnostic.md
  - domain-finance/field_guide.md
---

**Informational only — not financial, investment, or tax advice. Personal financial decisions depend on individual circumstances; consult a qualified financial planner (CFP), CPA, or attorney as appropriate.**

## Objective

Construct an auditable retirement-accumulation projection that: (1) estimates the target nest egg needed to fund retirement spending, (2) projects the future value of current savings plus ongoing contributions, (3) solves for the required savings rate to close any funding gap, and (4) reports results as base / optimistic / pessimistic scenario bands paired with a sequence-of-returns stress view — with every formula, input, and assumption made explicit.

## When to Use

- A user wants to know whether they are on track to retire at a target age and spending level.
- Translating a vague "Am I saving enough?" into a quantified required-savings-rate answer.
- Stress-testing an existing retirement plan against weaker returns, higher inflation, or a longer life.
- Comparing the impact of retiring earlier/later or saving more/less.

## Inputs / Context Required

```
<retirement_inputs>
Current age:                          [years]
Target retirement age:                [years]
Planning horizon (life expectancy):   [age; default test to 95+]
Current retirement savings balance:   [$]
Current annual contribution:          [$ or % of income]
Current gross annual income:          [$]
Expected retirement annual spending:  [$ in today's dollars]  (or % of pre-retirement income, e.g., 70–85%)
Expected Social Security / pension:   [$/yr in today's dollars; mark "verify with SSA statement"]

ASSUMPTIONS (user-supplied; state ranges, do not assert as fact):
  Pre-retirement real return:         [mean %, e.g., 4–6% real]
  Post-retirement real return:        [mean %, e.g., 2–4% real]
  Inflation:                          [%, e.g., 2.5–3.5%]
  Return volatility (std dev):        [%, for sequence-risk view]
  Safe withdrawal rate at retirement: [%, e.g., 3.5–4.0%; see critiques in step 4]
  Salary growth:                      [%/yr]
  Current-year contribution limits:   [input current-year limit; verify]
</retirement_inputs>
```

## Constraints

### Must
- Show formula → inputs → result for every calculation (NE-11).
- Express returns in **real** (inflation-adjusted) terms OR nominal-then-deflate, and state which; never mix silently.
- Produce three scenario bands (base / optimistic / pessimistic) with internally consistent return + inflation assumptions (NE-10).
- Pair the deterministic projection with a sequence-of-returns stress view (a poor-returns-early path), since average-return math overstates safety.
- Solve explicitly for the required savings rate and the funding gap.
- Run a verification pass recomputing the headline numbers (QA-01).

### Must Not
- Present a single point estimate of the ending balance as "the answer."
- Assert current contribution limits, COLA, or historical return figures as authoritative.
- Assume returns are earned smoothly every year without a sequence-risk caveat.
- Ignore taxes and Social Security where the user supplied them.

## Instructions

**Step 1 — Estimate the target nest egg (capital needed at retirement).**
```
Net annual spending from portfolio = Retirement spending − Social Security/pension (today's $)
Target nest egg (today's $) = Net annual spending / Safe Withdrawal Rate
   e.g., $60,000 / 0.04 = $1,500,000
Inflate to retirement-year dollars (if working in nominal):
   Target_nominal = Target_today × (1 + inflation)^(years to retirement)
```
State that the SWR denominator is itself uncertain (step 4).

**Step 2 — Project future value of current savings + contributions.**
```
FV of current balance  = PV × (1 + r)^n
FV of contributions (ordinary annuity, level) = PMT × [((1 + r)^n − 1) / r]
   r = real return per year, n = years to retirement, PMT = annual contribution
Projected nest egg = FV_balance + FV_contributions
If contributions grow with salary g:
   FV = PMT × [((1+r)^n − (1+g)^n) / (r − g)]   (growing annuity)
```

**Step 3 — Compute the funding gap and required savings rate.**
```
Funding gap = Target nest egg − Projected nest egg   (negative = surplus)
Required annual contribution to hit target:
   PMT_required = (Target − PV×(1+r)^n) × r / ((1+r)^n − 1)
Required savings rate = PMT_required / Current gross income
Compare to current savings rate; report the delta.
```

**Step 4 — Apply the SWR critique (precision-illusion guardrail).**
- The "4% rule" derives from historical US data over 30-year horizons; it is not guaranteed. Note that early retirement (40+ year horizons), lower forward return expectations, and high equity valuations argue for 3.0–3.5%.
- Show target nest egg at SWR of 3.0%, 3.5%, and 4.0% so the user sees the sensitivity.

**Step 5 — Build scenario bands (NE-10).**

| Scenario | Real return | Inflation | Projected nest egg | Gap vs. target | Req. savings rate |
|---|---|---|---|---|---|
| Optimistic | high | low | | | |
| Base | mid | mid | | | |
| Pessimistic | low | high | | | |

**Step 6 — Sequence-of-returns stress view (QA-02).**
- Illustrate a path where the worst return years cluster in the 5 years before and after retirement. Show how this lowers the sustainable spending versus the smooth-average projection.
- Report: "Under a poor-early-returns sequence, the same average return supports roughly X% less spending / requires Y% more capital."

**Step 7 — Verification pass (QA-01).** Recompute FV of balance and FV of contributions independently; confirm gap arithmetic; confirm required-savings-rate solve reproduces the target when plugged back in.

## Output Format

```
## Retirement Projection — [Age X → Retire at Y]
Assumptions (user-supplied): [returns / inflation / SWR / horizon]

### Target Nest Egg
[Step 1 formula + result at SWR 3.0% / 3.5% / 4.0%]

### Projected Nest Egg (current trajectory)
[Step 2 formulas + result]

### Funding Gap & Required Savings Rate
Current savings rate: __%   |   Required savings rate: __%   |   Delta: __ pts
Funding gap: $___ ( surplus / shortfall )

### Scenario Bands
[Step 5 table]

### Sequence-of-Returns Stress View
[Step 6 narrative + adjusted figure]

### Key Sensitivities & Disconfirming Check
[Which assumption moves the answer most; what would prove the plan off-track]
```

## Verification

- [ ] Every figure shows formula → inputs → result.
- [ ] Real vs. nominal treatment stated and consistent.
- [ ] Target nest egg shown at 3 SWR levels.
- [ ] Three scenario bands present, internally consistent.
- [ ] Sequence-of-returns stress view included and quantified.
- [ ] Required savings rate, when applied, reproduces the target nest egg (round-trip check).
- [ ] Contribution limits marked "[input current-year limit; verify]" — not asserted.
- [ ] Disclaimer present near top.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| "You're on track" from a single average-return projection | Require scenario bands + sequence-risk view; the smooth-average path is the optimistic edge, not the expectation |
| Treating the 4% rule as a law | Show 3.0/3.5/4.0% SWR sensitivity; state historical/conditional basis |
| Optimism bias on savings rate | Compare required vs. current savings rate explicitly; flag if required > 25% of income |
| Recency bias on returns | Returns are user-supplied ranges, not recent-decade extrapolations; require a low-return band |
| Longevity underestimation | Default horizon test to age 95+; flag if user plans only to ~85 |
| Precision illusion (a $1,503,228 target) | Round targets; present as ranges; state that any single figure is one path among many |
