---
title: "Deal Financing Structure Analysis — Cash, Stock, and Debt Mix and Their Impact"
category: finance/mergers-acquisitions
description: "Analyze how the consideration mix (cash, stock, new debt) for an acquisition affects pro-forma leverage, coverage, EPS, ownership dilution, and risk — and identify the constrained-optimal structure given covenant, rating, and accretion constraints."
techniques:
  - RT-03
  - NE-10
  - NE-11
  - DS-02
  - CM-02
difficulty: intermediate
tags:
  - deal-financing
  - consideration-mix
  - cash-vs-stock
  - leverage
  - dilution
  - m-and-a
updated: "2026-06-08"
related_prompts:
  - domain-finance/mergers-acquisitions/finance_accretion_dilution_analysis.md
  - domain-finance/mergers-acquisitions/finance_ma_deal_model_builder.md
  - domain-finance/treasury-capital-markets/finance_capital_structure_optimization.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. All outputs must be reviewed by qualified finance professionals before use in any transaction or decision.**

## Objective

Compare alternative ways to finance an acquisition — cash on hand, new debt, equity issuance, and blends — and quantify each structure's impact on pro-forma leverage, interest coverage, EPS accretion/dilution, ownership dilution, and downside resilience. Identify the structure that best satisfies the binding constraints (covenant/rating ceiling, accretion floor, ownership limit) rather than optimizing a single metric in isolation.

## When to Use

- Choosing the consideration mix for an announced or contemplated acquisition
- Testing whether a deal can be funded without breaching a leverage covenant or rating threshold
- Trading off EPS accretion against balance-sheet risk and ownership dilution
- Preparing financing options for a board, rating agency, or financing process
- Setting the maximum debt-funded portion given a target post-deal leverage ceiling

## Inputs / Context Required

- Purchase price (equity value) and assumed/refinanced target net debt
- Acquirer: cash available (and minimum operating cash to retain), existing debt, EBITDA, interest, diluted shares, share price (dated), tax rate
- Target: EBITDA (and synergized EBITDA if applicable), net income
- Financing options: incremental debt capacity and pricing (rate + base, dated); equity issuance feasibility and price
- Binding constraints: target/maximum Net Debt/EBITDA, minimum interest coverage, rating threshold if relevant, minimum acceptable EPS accretion, maximum acceptable ownership dilution
- Accounting framework (US GAAP / IFRS)

## Constraints

### Must
- Define the candidate structures explicitly (e.g., 100% cash/debt, 50/50 cash-stock, 100% stock, plus a constrained blend) and analyze each (RT-03).
- For each structure, compute pro-forma metrics (NE-11, DS-02):
  - `Pro-forma Net Debt/EBITDA = (Combined Debt − Combined Cash) ÷ Pro-forma EBITDA`
  - `Pro-forma EBITDA/Interest = Pro-forma EBITDA ÷ Pro-forma Cash Interest`
  - `EPS accretion/(dilution) %` vs. acquirer standalone
  - `Ownership dilution = New Shares ÷ Pro-forma Shares`
- State the binding constraints as must/must-not limits (CM-02) and test each structure against them; mark pass/fail.
- Run base/downside scenarios (NE-10): under a downside EBITDA, recompute leverage and coverage and flag any covenant/rating breach.
- Recommend the constrained-optimal structure: the one that best satisfies all binding constraints, not the one that maximizes accretion alone.
- Note the strategic signaling of stock vs. cash (stock can signal the acquirer believes its shares are richly valued; cash signals confidence).

### Must Not
- Recommend the most accretive structure without checking leverage, coverage, and ownership constraints.
- Treat acquirer cash as free or unlimited; retain minimum operating cash and account for foregone interest.
- Ignore the downside case where leverage spikes as EBITDA falls.
- Present ownership dilution and EPS dilution as the same thing — they are distinct effects.
- Assume equity can always be issued at the current price (issuance pressure can move the price).

## Instructions

**Step 1 — Define candidate structures (RT-03)**

List 3–5 structures spanning the cash/stock/debt space, including at least one constrained blend designed to sit just inside the leverage ceiling.

**Step 2 — Compute funding and pro-forma capitalization per structure (NE-11)**

```
For each structure:
  Cash used        = % cash × funding need (≤ available cash − minimum operating cash)
  New debt         = % debt × funding need
  New equity value = % stock × funding need → New shares = New equity ÷ share price
  Pro-forma Debt   = acquirer debt + new debt (+ target debt if assumed)
  Pro-forma Cash   = acquirer cash + target cash − cash used − fees
  Pro-forma EBITDA = acquirer + target (+ synergies if modeled)
```

**Step 3 — Compute impact metrics (DS-02)**

```
Net Debt/EBITDA     = (Pro-forma Debt − Pro-forma Cash) ÷ Pro-forma EBITDA
EBITDA/Interest     = Pro-forma EBITDA ÷ (existing + new debt interest − forgone cash interest)
EPS accretion/(dil) = (Pro-forma EPS ÷ Standalone EPS) − 1
Ownership dilution  = New shares ÷ (Acquirer shares + New shares)
```

**Step 4 — Constraint test (CM-02)**

| Structure | Net Debt/EBITDA (≤ ceiling) | Coverage (≥ floor) | EPS accretion (≥ floor) | Ownership dil. (≤ limit) | Pass/Fail |
|---|---|---|---|---|---|

**Step 5 — Downside scenario (NE-10)**

Recompute leverage and coverage under a downside EBITDA (e.g., −15% to −25%); flag structures that breach covenant/rating in the downside even if they pass in base.

**Step 6 — Recommendation & signaling**

Select the constrained-optimal structure; explain the trade-offs it makes and note the market-signaling implication of the chosen cash/stock balance.

## Output Format

### Candidate Structures
[Step 1 — list with rationale]

### Pro-Forma Capitalization & Impact Metrics

| Structure | Net Debt/EBITDA | Coverage | EPS Accretion/(Dil) % | Ownership Dilution | Forgone Cash Int. |
|---|---|---|---|---|---|
| 100% cash/debt | | | | | |
| 50/50 cash-stock | | | | | |
| 100% stock | | | | | |
| Constrained blend | | | | | |

### Constraint Test
[Step 4 pass/fail table]

### Downside Scenario
[Step 5 — leverage/coverage under stress; breach flags]

### Recommendation
[Step 6 — constrained-optimal structure, trade-offs, signaling note]

## Verification

- [ ] At least three structures analyzed, including a constrained blend.
- [ ] Pro-forma leverage, coverage, EPS accretion, and ownership dilution computed for each.
- [ ] Binding constraints stated as explicit limits and each structure marked pass/fail.
- [ ] Forgone interest on cash and new debt interest both reflected in coverage.
- [ ] Downside EBITDA scenario recomputes leverage/coverage and flags breaches.
- [ ] Ownership dilution and EPS dilution reported separately.
- [ ] Recommendation satisfies all binding constraints, not just maximum accretion.
- [ ] Minimum operating cash retained; cash not treated as unlimited.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Recommending the most accretive structure regardless of risk | Constraint test is mandatory; recommendation must pass leverage, coverage, and ownership limits |
| Treating acquirer cash as free/unlimited | Retain minimum operating cash; include forgone interest in coverage |
| Base-case leverage looks fine, downside breaches | Downside EBITDA scenario required; flag structures that pass base but fail downside |
| Conflating ownership and EPS dilution | Report both metrics separately with distinct formulas |
| Assuming equity issues at today's price | Note issuance-pressure risk to the share price; sensitivity on issue price |
| Ignoring the signal sent by all-stock vs. all-cash | Include the market-signaling implication in the recommendation |
