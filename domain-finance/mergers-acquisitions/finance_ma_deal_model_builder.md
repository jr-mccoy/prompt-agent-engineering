---
title: "M&A Merger Model Builder — Combined Financials, Financing, and Pro-Forma Metrics"
category: finance/mergers-acquisitions
description: "Build a full merger model: purchase-price and sources-and-uses, combined three-statement projections with synergies and purchase-accounting adjustments, the financing plan, and pro-forma credit and EPS metrics under base/upside/downside scenarios — all formulas shown."
techniques:
  - NE-11
  - NE-10
  - QA-01
  - QA-02
  - DS-02
difficulty: advanced
tags:
  - merger-model
  - m-and-a
  - pro-forma
  - purchase-accounting
  - combined-financials
  - deal-financing
updated: "2026-06-08"
related_prompts:
  - domain-finance/mergers-acquisitions/finance_accretion_dilution_analysis.md
  - domain-finance/mergers-acquisitions/finance_purchase_price_allocation.md
  - domain-finance/mergers-acquisitions/finance_synergy_estimation_framework.md
  - domain-finance/corporate-finance-fpa/finance_three_statement_model_builder.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. All outputs must be reviewed by qualified finance professionals before use in any transaction or decision.**

## Objective

Construct an auditable merger model that combines acquirer and target financials, layers in the financing structure and purchase-accounting adjustments, integrates synergies, and produces pro-forma three-statement projections plus key credit and EPS metrics — with a balancing sources-and-uses, an explicit goodwill calculation, and scenario analysis.

## When to Use

- Modeling a strategic (corporate) acquisition where the buyer integrates the target
- Producing combined pro-forma financials for a board or financing process
- Testing how a deal affects the acquirer's leverage, coverage, and EPS over time
- Comparing financing structures (cash/stock/debt) on combined credit metrics
- Building the analytical backbone for accretion/dilution and synergy work

## Inputs / Context Required

**Both companies (standalone)**
- Income statement: Revenue, EBITDA, D&A, EBIT, interest, taxes, net income
- Balance sheet: cash, debt, working-capital items, PP&E, equity, existing goodwill/intangibles
- Cash flow drivers: capex, change in NWC
- Diluted shares; share price (acquirer, dated); tax rate; accounting framework (US GAAP / IFRS)

**Deal terms**
- Offer price / equity purchase price; control premium
- Consideration mix (% cash / % stock / % new debt)
- Transaction fees (advisory, legal) and financing fees
- New debt tranches: size, rate (base + spread, dated), amortization, maturity
- Target net debt: assumed or refinanced

**Synergies & purchase accounting**
- Run-rate cost/revenue synergies and phase-in; integration costs
- Step-up of identifiable intangibles and useful lives (or assumption set)

## Constraints

### Must
- Build a sources-and-uses table that balances to the penny; financing/transaction fees are uses.
- Compute goodwill: `Goodwill = Equity Purchase Price − (Net Identifiable Assets at Fair Value)`, showing the step-up and deferred-tax effects.
- Combine the three statements: pro-forma IS, BS (with PPA), and CFS must articulate (net income flows to retained earnings; balance sheet balances).
- Model financing explicitly: new debt interest, forgone cash interest, new shares issued.
- Layer synergies (after-tax) and integration costs (one-time) with stated phase-in.
- Project pro-forma metrics each year: EPS, Net Debt/EBITDA, EBITDA/Interest, and accretion/(dilution) vs. acquirer standalone.
- Run base/upside/downside scenarios with internally consistent revenue, margin, synergy, and rate assumptions.
- Verify the balance sheet balances in every projection year (Assets = Liabilities + Equity).

### Must Not
- Present combined financials that do not balance, or where sources ≠ uses.
- Omit the deferred-tax liability arising from non-deductible intangible step-up (US GAAP stock deals) where relevant.
- Double-count target net debt (either assume it or refinance it — state which).
- Treat one-time integration/transaction costs as recurring, or recurring synergies as one-time.
- Use a single scenario or a point EPS estimate without scenario analysis.

## Instructions

**Step 1 — Purchase price & sources-and-uses**

```
Equity Purchase Price = Offer Price/Share × Target Diluted Shares
Total Enterprise Value Paid = Equity Purchase Price + Target Net Debt Assumed

USES: Equity purchase price; refinance target debt (if refinanced);
      transaction fees; financing fees; minimum cash.
SOURCES: New debt (by tranche); new equity (stock consideration);
         acquirer cash; (revolver if needed).
CHECK: Total Sources − Total Uses = 0  [required]
```

**Step 2 — Purchase accounting & goodwill**

```
Fair value of net identifiable assets = Target book equity
  + Intangible step-up + PP&E step-up − Deferred tax liability on step-up
Goodwill = Equity Purchase Price − Fair value of net identifiable assets
DTL on step-up = Step-up × tax rate  (where step-up is not tax-deductible)
New intangible amortization = Σ (Intangible_i ÷ Useful Life_i)
```

**Step 3 — Combined income statement (per year)**

| Line | Acquirer | Target | Adjustments | Pro-Forma |
|---|---|---|---|---|
| Revenue | | | + revenue synergies | |
| EBITDA | | | + cost synergies − integration costs | |
| D&A | | | + new intangible amort. | |
| EBIT | | | | |
| Interest expense | | | + new debt int. − forgone cash int. | |
| Pre-tax income | | | | |
| Taxes @ [%] | | | | |
| Net income | | | | |
| Diluted shares | | | + new shares issued | |
| **EPS** | | | | |

**Step 4 — Combined balance sheet at close (and projected)**

```
Cash: acquirer + target − cash used in deal − fees
Debt: acquirer + new debt (+ target debt if assumed)
Goodwill: existing + new goodwill (Step 2)
Intangibles: existing + step-up (amortized over time)
Equity: acquirer equity + new equity issued − fees charged to equity
  (target equity is eliminated in consolidation)
CHECK: Assets = Liabilities + Equity each year
```

**Step 5 — Combined cash flow & debt paydown**

```
CFO = Net income + D&A (incl. new amort.) ± ΔNWC
CFI = − capex (combined) − cash paid in deal (year of close)
CFF = + new debt − mandatory amort − optional sweep ± equity
Ending cash = Beginning cash + CFO + CFI + CFF
```

**Step 6 — Pro-forma metrics & scenarios (NE-10)**

```
Net Debt / EBITDA   = (Total Debt − Cash) ÷ Pro-Forma EBITDA
EBITDA / Interest   = Pro-Forma EBITDA ÷ Cash Interest
Accretion/(Dilution)% = (Pro-Forma EPS ÷ Acquirer Standalone EPS) − 1
```
Repeat for base / upside / downside (vary synergy realization, revenue, and rates).

**Step 7 — Adversarial stress-test (QA-02)**

- Under the downside, does pro-forma Net Debt/EBITDA breach a typical covenant level the new debt would carry?
- If synergies slip 12 months, what is the Year-1 and Year-2 EPS impact?
- Does the model still balance if intangible step-up is 50% higher (more amortization, larger DTL)?
- Is accretion an artifact of leverage rather than operating combination? Recompute all-equity.

## Output Format

### Sources & Uses
[Step 1 — must balance to zero]

### Goodwill & Purchase Accounting
[Step 2 calculations]

### Combined Income Statement (Base Case, all years)
[Step 3 table]

### Combined Balance Sheet at Close + Balancing Check
[Step 4]

### Pro-Forma Metrics by Year
| Metric | Year 1 | Year 2 | Year 3 |
|---|---|---|---|
| EPS | | | |
| Accretion/(Dilution) % | | | |
| Net Debt / EBITDA | | | |
| EBITDA / Interest | | | |

### Scenario Summary
[Base / upside / downside key metrics]

### Stress-Test Summary
[Step 7 findings]

## Verification

- [ ] Sources equal uses to the penny; check row present.
- [ ] Goodwill computed from equity purchase price less fair-valued net identifiable assets, including DTL on step-up.
- [ ] Balance sheet balances (A = L + E) in every projection year.
- [ ] Target equity eliminated in consolidation; target debt either assumed or refinanced (stated, not double-counted).
- [ ] New debt interest, forgone cash interest, and new shares all reflected.
- [ ] Synergies after-tax with phase-in; integration costs one-time.
- [ ] EPS and credit metrics shown for each projection year vs. acquirer standalone.
- [ ] Base/upside/downside scenarios internally consistent.
- [ ] Intangible amortization links from PPA to the income statement and balance sheet.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Combined statements that silently don't balance | Mandatory A = L + E check each year; model cannot proceed otherwise |
| Goodwill plug that hides a missing DTL | Goodwill formula must net the deferred-tax liability on non-deductible step-up |
| Double-counting target net debt | State whether target debt is assumed or refinanced; only one path may be modeled |
| Accretion that is purely leverage-driven | Provide an all-equity recomputation to isolate operating vs. financing effect |
| Synergies booked Day 1 with no phase-in | Require a phase-in schedule; integration costs front-loaded as one-time |
| Single-scenario EPS presented as "the" outcome | Base/upside/downside required with consistent driver assumptions |
