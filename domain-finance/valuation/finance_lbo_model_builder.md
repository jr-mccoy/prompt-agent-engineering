---
title: "LBO Model Builder — Sources/Uses, Debt Schedule, IRR/MOIC Returns, and Covenant Headroom"
category: finance/valuation
description: "Build a leveraged buyout model with a defensible sources-and-uses table, multi-tranche debt schedule with amortization and interest, equity-return analysis (IRR and MOIC), and covenant-headroom projection under base and downside scenarios."
techniques:
  - NE-11
  - NE-10
  - QA-01
  - QA-02
  - DS-02
difficulty: advanced
tags:
  - lbo
  - leveraged-buyout
  - private-equity
  - irr
  - moic
  - debt-schedule
  - covenant-headroom
updated: "2026-06-08"
related_prompts:
  - domain-finance/valuation/finance_dcf_model_builder.md
  - domain-finance/valuation/finance_wacc_builder.md
  - domain-finance/valuation/finance_valuation_sensitivity_scenario.md
  - domain-finance/financial-statement-analysis/finance_ratio_analysis_engine.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. All outputs must be reviewed by qualified finance professionals before use in any transaction or decision.**

## Objective

Construct an auditable leveraged buyout (LBO) model covering: (1) entry assumptions and sources-and-uses of funds, (2) operating projections linked to a multi-tranche debt schedule, (3) equity-return analysis (IRR and MOIC) across exit scenarios and holding periods, and (4) covenant-headroom projection under base and downside cases — with all formulas shown and assumptions explicit.

## When to Use

- Evaluating whether an acquisition target meets a financial-sponsor return threshold
- Structuring the debt and equity mix for a buyout or recapitalization
- Stress-testing a proposed deal structure against downside operating scenarios
- Building the "financial buyer" floor in a sell-side valuation analysis
- Private equity investment committee preparation or LBO training exercises

## Inputs / Context Required

**Target company**
- Name and industry
- Accounting framework (US GAAP / IFRS) and fiscal year end
- LTM financial summary: Revenue, EBITDA, D&A, Capex, ΔWorking Capital, Cash, Net Debt
- NTM and multi-year projections (or assumptions to build them)
- Tax rate (statutory marginal rate; any NOL carryforwards)

**Entry assumptions**
- Entry EV/EBITDA multiple (or target enterprise value)
- LTM EBITDA used for entry pricing
- Transaction fees and expenses (M&A advisory, legal, financing)
- Management rollover equity (if any)

**Debt structure**
- Tranche names and sizes (e.g., First Lien TL, Second Lien, Subordinated Notes, Revolving Credit Facility)
- Interest rate per tranche (fixed or SOFR/LIBOR + spread; state base rate)
- Amortization schedule per tranche (% per year or bullet at maturity)
- Maturity dates
- Financial covenants per tranche (e.g., Total Leverage ≤ 5.5x, Interest Coverage ≥ 2.0x)

**Exit assumptions**
- Holding period range (3 / 5 / 7 years)
- Exit EV/EBITDA multiple range (base, bull, bear)
- Expected exit: strategic sale, IPO, or secondary buyout (note any exit-multiple haircut for sponsor → sponsor)

**Return targets**
- Sponsor return threshold: IRR (commonly 20%+) and / or MOIC (commonly 2.5x+)

## Constraints

### Must
- Build a complete sources-and-uses table; total sources must equal total uses (to the penny).
- Model each debt tranche separately with its own interest expense, amortization, and maturity.
- Show the correct interest expense formula including PIK (paid-in-kind) if applicable.
- Project free cash flow available for debt repayment in each year; apply cash sweep to most-senior tranche first (unless otherwise specified).
- Calculate IRR and MOIC at entry for each combination of exit year × exit multiple.
- Compute covenant headroom in every projection year; flag the year with minimum headroom.
- Run base / bull / bear operating scenarios; each scenario must have internally consistent growth, margin, and capex assumptions.
- Flag if any scenario results in a covenant breach or liquidity crisis; specify the year.

### Must Not
- Use a single-point return estimate without scenario analysis across exit years and multiples.
- Omit financing fees from sources-and-uses; they are a real use of proceeds.
- Apply a constant exit multiple without noting it may differ from entry (entry/exit multiple compression or expansion is a key return driver).
- Present a return that exceeds the threshold without acknowledging the covenant and downside risk.
- Allow cash balance to go negative in any projection year without flagging as a liquidity problem.

## Instructions

**Step 1 — Build the sources-and-uses table**

```
USES:
  Purchase equity value (entry EV − existing net debt)   = [EV × entry multiple − net debt]
  Refinance existing debt                                 = [existing net debt]
  Transaction fees (advisory + legal)                    = [% of EV, stated]
  Financing fees (OID, arrangement fees)                 = [% of debt drawn, stated]
  Minimum cash at close                                  = [stated]
  ─────────────────────────────────────────────────────
  Total Uses                                             = [sum]

SOURCES:
  Revolver draw (if any)                                 = [amount]
  First Lien Term Loan                                   = [amount]
  Second Lien / Sub Notes                                = [amount]
  Preferred equity                                       = [amount, if any]
  Sponsor equity                                         = [amount]
  Management rollover                                    = [amount]
  ─────────────────────────────────────────────────────
  Total Sources                                          = [sum]

CHECK: Total Sources − Total Uses = 0 [required]
```

**Step 2 — Set entry-day leverage statistics**

```
Entry Enterprise Value = LTM EBITDA × Entry EV/EBITDA Multiple
Entry Equity Value = Entry EV − Pro-forma Net Debt at Close
Pro-forma Net Debt = All Drawn Debt − Minimum Cash

Entry leverage ratios:
  Total Debt / LTM EBITDA = [x]   [test vs. covenant max]
  Net Debt / LTM EBITDA   = [x]
  EBITDA / Interest Expense = [x] [test vs. covenant min]
  (use LTM EBITDA and pro-forma interest for entry-day ratios)
```

**Step 3 — Project operating financials (base / bull / bear)**

| Line Item | Year 0 (LTM) | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|---|---|---|---|---|---|---|
| Revenue | | | | | | |
| Revenue growth % | | | | | | |
| EBITDA | | | | | | |
| EBITDA margin % | | | | | | |
| D&A | | | | | | |
| EBIT | | | | | | |
| Interest expense (cash) | | | | | | |
| EBT | | | | | | |
| Taxes @ [%] | | | | | | |
| Net Income | | | | | | |
| + D&A | | | | | | |
| − ΔWorking Capital | | | | | | |
| − Capex | | | | | | |
| = Unlevered FCF (FCFF pre-interest) | | | | | | |
| − Cash Interest (all tranches) | | | | | | |
| − Mandatory Amortization | | | | | | |
| = FCF Available for Debt Sweep | | | | | | |
| − Cash Sweep (senior tranche first) | | | | | | |
| = Net Change in Cash | | | | | | |
| Ending Cash | | | | | | |

**Step 4 — Build the debt schedule**

For each tranche (replicate the block):

```
Tranche: [Name, e.g., First Lien TL]
  Principal Outstanding (BOP)   = [prior year ending balance]
  Interest Rate                 = [SOFR/fixed rate + spread; state base rate and date]
  Cash Interest Expense         = Principal × Interest Rate
  PIK Interest (if any)         = Principal × PIK Rate [added to principal]
  Mandatory Amortization        = [% per year × original principal]
  Cash Sweep                    = min(FCF available, remaining principal)
  Principal Outstanding (EOP)   = BOP − Mandatory Amort. − Cash Sweep + PIK

Aggregate Interest Expense Year t = Σ (Cash Interest across all tranches)
```

**Step 5 — Compute covenant headroom**

For each financial covenant in each projection year:

```
Total Leverage Covenant: Maximum Net Debt / EBITDA ≤ [covenant threshold, e.g., 5.5x]
  Actual: Pro-forma Net Debt_t / EBITDA_t
  Headroom: Covenant − Actual [negative = breach]

Interest Coverage Covenant: Minimum EBITDA / Cash Interest ≥ [covenant threshold, e.g., 2.0x]
  Actual: EBITDA_t / Cash Interest_t
  Headroom: Actual − Covenant [negative = breach]

Flag: Year of minimum headroom, value of headroom, and scenario under which breach occurs
```

**Step 6 — Build the return analysis**

```
IRR: Solve for r such that:
  −Sponsor Equity Invested + Σ [Equity Proceeds_t / (1+r)^t] = 0

Where:
  Equity Proceeds at Exit = Exit EV − Net Debt at Exit − Transaction Fees at Exit

Exit EV = Exit Year EBITDA × Exit EV/EBITDA Multiple

MOIC = Total Equity Proceeds / Sponsor Equity Invested
```

Present a return matrix across exit years and exit multiples:

### IRR Matrix

| Exit Multiple ↓ / Exit Year → | Year 3 | Year 4 | Year 5 | Year 6 | Year 7 |
|---|---|---|---|---|---|
| Entry − 1.0x (bear exit) | | | | | |
| Entry − 0.5x | | | | | |
| Entry (flat) | | | | | |
| Entry + 0.5x | | | | | |
| Entry + 1.0x (bull exit) | | | | | |

### MOIC Matrix

[Same structure as IRR matrix]

**Step 7 — Adversarial stress-test**

For the bear scenario:
- What entry multiple would still generate a 20% IRR at a flat (entry = exit) multiple in 5 years?
- What minimum EBITDA growth rate is required to avoid a covenant breach?
- At what revenue decline does the model show negative free cash flow, requiring revolver draw?
- What is the impact of a 100bps interest-rate increase on IRR and covenant headroom?

## Output Format

### Sources and Uses
[Step 1 table — must balance to zero]

### Entry Statistics
[Step 2 calculations]

### Operating Projections (Base Case)
[Step 3 table — all years]

### Debt Schedule Summary

| Tranche | Initial Balance | Year 1 Balance | Year 3 Balance | Year 5 Balance | Rate | Maturity |
|---|---|---|---|---|---|---|
| Revolver | | | | | | |
| First Lien TL | | | | | | |
| Second Lien | | | | | | |
| Sub Notes | | | | | | |
| **Total Debt** | | | | | | |
| Cash | | | | | | |
| **Net Debt** | | | | | | |

### Covenant Headroom

| Covenant | Threshold | Year 1 Actual | Y1 Headroom | Year 3 Actual | Y3 Headroom | Min Headroom Year |
|---|---|---|---|---|---|---|
| Total Leverage | ≤ [x] | | | | | |
| Interest Coverage | ≥ [x] | | | | | |

### Return Matrices
[IRR Matrix and MOIC Matrix from Step 6]

### Stress-Test Summary
[Step 7 findings — break-even assumptions, covenant-breach thresholds]

## Verification

- [ ] Sources equal uses to the penny; check cell is present.
- [ ] Each debt tranche modeled separately with correct interest, amortization, and cash-sweep logic.
- [ ] Cash balance is positive in every projection year; any negative balance flagged as a liquidity event.
- [ ] Covenant headroom calculated for every covenant in every year; breach years identified.
- [ ] IRR and MOIC calculated for ≥3 exit years and ≥3 exit multiples (return matrix).
- [ ] Return matrix includes at least one scenario where the IRR target is not met.
- [ ] Financing fees are included in uses and amortized through interest expense or expensed immediately (state treatment).
- [ ] Scenarios (base / bull / bear) are internally consistent; bear scenario stresses both revenue and margin.
- [ ] Adversarial stress-test identifies break-even EBITDA growth rate for covenant compliance.
- [ ] All interest-rate inputs are dated and sourced (base rate + spread stated separately).

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Presenting only the base-case IRR that clears the threshold | Return matrix required; present all exit-year × exit-multiple combinations; at least one must show sub-threshold return |
| Sources ≠ Uses due to omitted financing fees | Sources-and-uses check row is mandatory; model cannot proceed if it doesn't balance |
| Ignoring cash sweep in favor of treating debt as a bullet | Cash sweep is the primary deleveraging mechanism; model it explicitly |
| Presenting covenant headroom as comfortable without stress-testing | Bear-scenario covenant headroom is required; minimum headroom year must be flagged |
| Using entry EBITDA for exit value without noting EBITDA growth | Exit equity value formula must show exit year EBITDA × exit multiple, not entry EBITDA |
| Treating a 20%+ IRR as de-risked if it is concentrated in a single exit scenario | Return distribution across years and multiples reveals scenario concentration; highlight if >80% of IRR scenarios cluster narrowly |
