---
title: "Net-Worth & Cash-Flow Diagnostic — Balance Sheet, Savings Rate, and Liquidity Read"
category: finance/personal-finance-planning
description: "Build a personal balance sheet and cash-flow statement, compute net worth, savings rate, and core financial-health ratios, and produce a prioritized diagnostic of strengths and risks — every figure traceable to inputs."
techniques:
  - NE-11
  - DS-02
  - DS-04
  - DS-06
  - QA-01
difficulty: beginner
tags:
  - net-worth
  - cash-flow
  - savings-rate
  - balance-sheet
  - financial-health
  - liquidity
updated: "2026-06-08"
related_prompts:
  - domain-finance/personal-finance-planning/finance_emergency_fund_sizing.md
  - domain-finance/personal-finance-planning/finance_debt_payoff_strategy.md
  - domain-finance/personal-finance-planning/finance_retirement_projection_model.md
  - domain-finance/field_guide.md
---

**Informational only — not financial, investment, or tax advice. Personal financial decisions depend on individual circumstances; consult a qualified financial planner (CFP), CPA, or attorney as appropriate.**

## Objective

Construct a personal balance sheet and cash-flow statement, compute net worth, savings rate, and core financial-health ratios, identify patterns and concerns, and produce a prioritized diagnostic — with every figure traceable to inputs and no single ratio treated as a verdict.

## When to Use

- A household wants a clear picture of where it stands financially (net worth + cash flow).
- Establishing a baseline before retirement, debt, or goal planning.
- Diagnosing whether spending, debt, or low savings is the binding constraint.
- Tracking financial health over time (run periodically and compare).

## Inputs / Context Required

```
<diagnostic_inputs>
ASSETS:
  Cash & equivalents:        [$]
  Investments (taxable):     [$]
  Retirement accounts:       [$]
  Home / real estate (value):[$]
  Vehicles (value):          [$]
  Other assets:              [$]
LIABILITIES:
  Mortgage:                  [$ balance, rate]
  Auto loans:                [$ balance, rate]
  Student loans:             [$ balance, rate]
  Credit cards:              [$ balance, rate]
  Other debt:                [$]
CASH FLOW (monthly or annual — state which):
  Gross income:              [$]
  Taxes & payroll deductions:[$]
  Net (take-home) income:    [$]
  Essential expenses:        [$]
  Discretionary expenses:    [$]
  Debt payments:             [$]
  Savings/investing:         [$]
</diagnostic_inputs>
```

## Constraints

### Must
- Build a balance sheet (assets − liabilities = net worth) and a cash-flow statement (NE-11).
- Compute savings rate (gross and net basis; state which) and core ratios (DS-02).
- Distinguish liquid net worth from total net worth (home equity is illiquid).
- Identify patterns: where money goes, debt concentration, savings adequacy (DS-04).
- Prioritize findings by impact (DS-06).
- Run a verification pass on the arithmetic (QA-01).

### Must Not
- Treat home equity as spendable liquidity.
- Present a single ratio (e.g., net worth) as the whole picture.
- Assert benchmark "good" ratios as universal — context (age, income, goals) matters.
- Double-count or omit categories (assets/liabilities must reconcile).

## Instructions

**Step 1 — Balance sheet (NE-11)**

```
Total assets = cash + investments + retirement + real estate + vehicles + other
Total liabilities = mortgage + auto + student + credit cards + other
Net worth = Total assets − Total liabilities
Liquid net worth = (cash + taxable investments) − (short-term/high-rate debt)
   (excludes home equity, retirement-account penalties, vehicles)
```

**Step 2 — Cash-flow statement**

```
Net income = Gross income − taxes/deductions
Total outflows = essential + discretionary + debt payments + savings
Surplus/(deficit) = Net income − (essential + discretionary + debt payments)
   (should equal savings if balanced; flag if deficit = drawing down assets/borrowing)
```

**Step 3 — Core ratios (DS-02)**

```
Savings rate (gross) = Savings / Gross income
Savings rate (net)   = Savings / Net income          [state which is used]
Liquidity ratio      = Liquid assets / Monthly essential expenses   (months of runway)
Debt-to-income (DTI) = Total monthly debt payments / Gross monthly income
Consumer-debt ratio  = Non-mortgage debt payments / Net income
Housing ratio        = Housing costs / Gross income
Investment ratio     = Investable assets / Net worth
```

**Step 4 — Pattern recognition (DS-04)**

- Where does net income go (essential / discretionary / debt / savings split)?
- Is debt concentrated in high-rate balances (route to debt-payoff prompt)?
- Is liquidity adequate (route to emergency-fund prompt)?
- Is the savings rate consistent with stated goals (route to retirement/FIRE prompts)?

**Step 5 — Prioritized diagnostic (DS-06)**

| Priority | Finding | Metric | Suggested next step (route) |
|---|---|---|---|
| High | (e.g., high-rate credit card debt) | Consumer-debt ratio | Debt-payoff strategy |
| High | (e.g., <1 month liquidity) | Liquidity ratio | Emergency-fund sizing |
| Medium | (e.g., low savings rate vs. goals) | Savings rate | Retirement projection |
| Low | (e.g., concentrated assets) | Investment ratio | Asset-allocation glidepath |

**Step 6 — Verification (QA-01)**

Recompute net worth and surplus/deficit; confirm savings rate basis is stated; confirm liquid vs. total net worth distinction.

## Output Format

### Balance Sheet
[Step 1 — assets, liabilities, total and liquid net worth]

### Cash-Flow Statement
[Step 2 — inflows, outflows, surplus/deficit]

### Core Ratios
[Step 3 table]

### Patterns
[Step 4]

### Prioritized Diagnostic
[Step 5 table with routing]

### Verification Notes
[Step 6]

## Verification

- [ ] Net worth = assets − liabilities, reconciled.
- [ ] Liquid net worth distinguished from total (home equity excluded from liquid).
- [ ] Cash-flow surplus/deficit computed; deficit flagged if present.
- [ ] Savings rate basis (gross/net) stated.
- [ ] Core ratios computed with formulas shown.
- [ ] Findings prioritized by impact with next-step routing.
- [ ] Benchmarks framed contextually, not as universal verdicts.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Treating home equity as liquidity | Report liquid net worth separately; exclude home equity |
| Single ratio as a verdict | Present the full ratio set + context (age, income, goals) |
| Asserting universal "good" thresholds | Frame benchmarks as context-dependent ranges |
| Hidden deficit financed by debt/assets | Flag any cash-flow deficit explicitly |
| Optimism bias on savings rate | Use actual savings, not intended; reconcile to surplus |
| Double-counting accounts | Verification pass reconciles assets/liabilities and cash flow |
