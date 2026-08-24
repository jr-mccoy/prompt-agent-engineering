---
title: "Asset-Allocation Glidepath Builder — Age/Goal-Based Equity Path and Rebalancing Rules"
category: finance/personal-finance-planning
description: "Design an age- and goal-based asset-allocation glidepath with an explicit equity-percent rule, rebalancing bands and cadence, and a sequence-of-returns-aware de-risking schedule — framed as a policy with stated assumptions, not a market forecast."
techniques:
  - NE-11
  - NE-10
  - DS-02
  - QA-02
  - CM-02
difficulty: intermediate
tags:
  - asset-allocation
  - glidepath
  - rebalancing
  - equity-percent
  - risk-tolerance
  - sequence-risk
updated: "2026-06-08"
related_prompts:
  - domain-finance/personal-finance-planning/finance_retirement_projection_model.md
  - domain-finance/personal-finance-planning/finance_monte_carlo_withdrawal_analysis.md
  - domain-finance/personal-finance-planning/finance_fire_planning_model.md
  - domain-finance/field_guide.md
---

**Informational only — not financial, investment, or tax advice. Personal financial decisions depend on individual circumstances; consult a qualified financial planner (CFP), CPA, or attorney as appropriate.**

## Objective

Design an auditable asset-allocation glidepath: an equity/fixed-income (and cash) allocation that changes over the investor's horizon according to a stated rule, with explicit rebalancing bands, a rebalancing cadence, and a de-risking schedule that addresses sequence-of-returns risk near the goal date — presented as an investment policy with transparent assumptions, not a return forecast.

## When to Use

- Setting a target-date-style allocation path for retirement or another dated goal.
- Translating a risk-tolerance profile into a concrete equity-percent rule.
- Defining rebalancing bands and cadence to control drift.
- Building the "glide-down" near retirement to manage sequence risk.

## Inputs / Context Required

```
<glidepath_inputs>
Current age:                          [years]
Goal / retirement date (target year): [year or age]
Goal type:                            [retirement | education | home | other]
Current allocation:                   [equity % / bonds % / cash % / other]
Risk tolerance:                       [conservative | moderate | aggressive]
Risk capacity notes:                  [job stability, other income, time horizon, liquidity needs]
Account types:                        [tax-deferred / Roth / taxable — affects rebalancing tax cost]
Liquidity needs in next 1–3 yrs:      [$]

ASSUMPTIONS (user-supplied; state, do not assert):
  Equity-rule preference:             [e.g., "(110 − age)% equity" | "target-date style" | custom]
  Rebalancing band:                   [e.g., ±5 absolute pts or ±25% relative]
  Rebalancing cadence:                [annual | semiannual | threshold-triggered]
  Expected long-run return by sleeve: [equity / bonds / cash — ranges, not facts]
  Volatility by sleeve:               [for sequence-risk illustration]
</glidepath_inputs>
```

## Constraints

### Must
- State the equity-percent rule as an explicit formula and tabulate the path by age/year (NE-11, DS-02).
- Define rebalancing bands (absolute or relative) and cadence precisely (CM-02).
- Include a sequence-of-returns-aware de-risking glide in the ~10 years around the goal date (QA-02).
- Distinguish risk *tolerance* (psychological) from risk *capacity* (financial ability to bear loss).
- Frame allocations as policy targets, not predictions; mark all return/volatility inputs user-supplied.
- Present a base allocation plus a more-conservative and more-aggressive variant (NE-10).

### Must Not
- Present a single allocation without a path over time.
- Assert expected returns or volatility as authoritative.
- Recommend specific securities or funds (this is allocation policy, not security selection).
- Ignore the tax cost of rebalancing in taxable accounts.

## Instructions

**Step 1 — Choose and state the equity-percent rule**

```
Common rules (state the one used; all are heuristics, not optimal):
  Equity % = 100 − age            (classic, conservative)
  Equity % = 110 − age            (moderate)
  Equity % = 120 − age            (aggressive)
  Target-date style: high equity early, glide to a landing equity % (e.g., 30–50%) at/after the goal
Apply risk tolerance/capacity to pick the rule and the landing equity %.
```

**Step 2 — Tabulate the glidepath**

| Age / Year | Years to goal | Equity % | Bonds % | Cash % | Rationale |
|---|---|---|---|---|---|
| now | | | | | |
| +5 | | | | | |
| +10 | | | | | |
| goal − 10 | | | | | de-risk begins |
| goal − 5 | | | | | sequence-risk buffer building |
| goal | | | | | landing allocation |
| goal + 10 | | | | | (rising-equity or flat post-goal, state choice) |

**Step 3 — Define rebalancing rules (CM-02)**

```
Bands: rebalance when any sleeve drifts beyond ± [band] from target
  Absolute example: target equity 60% → rebalance if <55% or >65%
  Relative example: ±25% of target weight
Cadence: check [annual/semiannual]; act on band breach or on schedule
Tax-aware note: in taxable accounts, prefer rebalancing with new contributions
  and dividends before realizing gains; harvest losses where available.
```

**Step 4 — Sequence-of-returns buffer (QA-02)**

- Within ~5 years of the goal, hold a cash/short-bond buffer (e.g., 2–3 years of withdrawals) so a market drop does not force selling equities at a loss early in drawdown.
- Optionally describe a "rising equity glidepath" post-retirement (de-risk into retirement, then slowly re-risk) and state the rationale and the evidence is debated.

**Step 5 — Variants (NE-10)**

Present three glidepaths — conservative / base / aggressive — differing in landing equity % and the speed of de-risking. State the tradeoff: more equity raises expected growth and volatility (and sequence risk near the goal).

**Step 6 — Verification (QA-01)**

Confirm each row's sleeves sum to 100%; confirm the rule produces the tabulated equity %; confirm de-risking begins before the goal.

## Output Format

### Allocation Policy Summary
[Rule chosen, risk tolerance vs. capacity, landing equity %]

### Glidepath Table
[Step 2 — base case]

### Rebalancing Rules
[Step 3 — bands, cadence, tax-aware notes]

### Sequence-Risk Buffer
[Step 4]

### Variants
[Step 5 — conservative / base / aggressive]

### Verification Notes
[Step 6]

## Verification

- [ ] Equity-percent rule stated as a formula and tabulated over time.
- [ ] Each allocation row sums to 100%.
- [ ] Rebalancing bands and cadence defined precisely.
- [ ] De-risking glide near the goal included with a sequence-risk buffer.
- [ ] Risk tolerance vs. risk capacity distinguished.
- [ ] Three variants presented with the growth/volatility tradeoff stated.
- [ ] Return/volatility inputs marked user-supplied; no specific securities named.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Presenting an allocation as optimized | State that equity rules are heuristics, not optimal; show variants |
| Implying returns are known | Mark return/volatility user-supplied; frame as policy not forecast |
| Ignoring sequence risk near the goal | Mandatory de-risking glide + cash buffer in the ~5 years pre-goal |
| Conflating tolerance and capacity | Require both to be assessed; a high tolerance with low capacity should de-risk |
| Recency bias (max equity after a bull run) | Aggressive variant must show its drawdown/sequence-risk cost |
| Ignoring rebalancing tax drag | Tax-aware rebalancing guidance required for taxable accounts |
