---
title: "DCF Model Builder — FCFF/FCFE Projection, WACC, Terminal Value, Assumption Register"
category: finance/valuation
description: "Build a defensible discounted cash flow model with explicit FCFF or FCFE projections, a bottoms-up WACC, terminal value (exit-multiple and perpetuity-growth methods), and a full assumption register — with base/bull/bear scenarios and adversarial stress-testing."
techniques:
  - NE-11
  - NE-10
  - QA-01
  - QA-02
  - DS-02
difficulty: advanced
tags:
  - dcf
  - valuation
  - wacc
  - terminal-value
  - free-cash-flow
  - financial-modeling
updated: "2026-06-08"
related_prompts:
  - domain-finance/valuation/finance_dcf_model_auditor.md
  - domain-finance/valuation/finance_wacc_builder.md
  - domain-finance/valuation/finance_terminal_value_sanity_check.md
  - domain-finance/valuation/finance_valuation_sensitivity_scenario.md
  - domain-finance/financial-statement-analysis/finance_ratio_analysis_engine.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. All outputs must be reviewed by qualified finance professionals before use in any transaction or decision.**

## Objective

Construct a defensible, auditable discounted cash flow (DCF) valuation with: (1) a projection-period model of free cash flow to the firm (FCFF) or free cash flow to equity (FCFE), (2) a bottoms-up WACC calculation, (3) terminal value estimated by both the perpetuity-growth and exit-multiple methods, and (4) a complete assumption register with base / bull / bear scenario ranges. All formulas are shown and traceable to stated inputs.

## When to Use

- Intrinsic-value analysis for an investment decision, fairness opinion support, or board presentation
- Building the DCF leg of a football-field valuation (complement with trading comps and precedents)
- Stress-testing an existing valuation or challenging a counterparty's DCF
- Anchoring an LBO or M&A model to a standalone intrinsic-value reference point
- Academic or CFA-preparation modeling exercises requiring methodological rigor

## Inputs / Context Required

Provide as much of the following as available; the model will flag missing items and state assumptions made in their absence.

**Company & deal context**
- Company name, ticker (if public), industry / SIC code
- Accounting framework (US GAAP / IFRS) and fiscal year end
- Historical period available (minimum 3 years of income statement + balance sheet + cash flow statement)
- Target method: FCFF (enterprise-value output) or FCFE (equity-value output)
- Minority interest / non-controlling interest present? (yes / no)

**Projection assumptions**
- Explicit projection period (commonly 5–10 years)
- Revenue growth driver narrative (volume × price, market share × TAM, etc.)
- EBITDA or EBIT margin trajectory and operating leverage assumption
- Depreciation & amortization as % of revenue or capex linkage
- Capital expenditure intensity (% revenue, or maintenance vs. growth split)
- Working capital assumptions (days receivable, days inventory, days payable)
- Tax rate (effective statutory; note any NOL carryforwards)
- For FCFE: incremental borrowing / debt repayment schedule

**WACC inputs**
- Capital structure (debt / equity market weights, or target structure)
- Cost of debt (current yield, or estimated yield-to-maturity on existing debt)
- Beta source (regression, comparables, or Damodaran sector; state which)
- Risk-free rate (current 10-year or 30-year sovereign yield — specify)
- Equity risk premium source (Damodaran, Duff & Phelps, or custom — state)
- Size premium, country risk premium (if applicable — state source)
- Marginal tax rate for debt tax shield

**Terminal value**
- Perpetuity growth rate assumption (and basis for it)
- Exit EV/EBITDA multiple reference (peer median, long-run average, or stated)

**Scenario framework**
- Bull, base, and bear narrative labels and the 2–3 key variables that differ across them

## Constraints

### Must
- Show every formula explicitly before plugging in numbers.
- Build an assumption register listing every input, its value in each scenario, and the basis or source.
- Project FCFF or FCFE using the correct formula (see Instructions).
- Compute WACC using CAPM for cost of equity; show each component separately.
- Calculate terminal value using BOTH the Gordon Growth Model and the exit-multiple method; reconcile the two.
- Present enterprise value (for FCFF) or equity value (for FCFE) with a clear bridge to equity value per share.
- Run base / bull / bear scenarios; never present a single-point estimate as the answer.
- Flag any input derived from an assumption rather than a stated fact.
- State the accounting framework and note any GAAP/IFRS adjustments made.

### Must Not
- Invent financial figures not supplied by the user. If a number is missing, state the assumption and mark it `[ASSUMED]`.
- Apply the Gordon Growth Model with a perpetuity growth rate at or above the WACC — this produces a negative or undefined value.
- Use a growth rate in the terminal period that exceeds long-run nominal GDP growth without explicit, defended justification.
- Present a single DCF output as a point estimate without scenario bounds.
- Use book-value capital weights for WACC; use market-value weights.
- Omit the debt bridge (net debt subtraction) when moving from enterprise value to equity value.

## Instructions

**Step 1 — Select FCFF vs. FCFE and confirm formula**

FCFF (use when: multi-capital-structure comparisons; LBO context; preferred for most corporate analysis):
```
FCFF = EBIT × (1 − Tax Rate) + D&A − ΔWorking Capital − Capex
     = NOPAT + D&A − ΔWC − Capex
```
Discount FCFF at WACC → Enterprise Value. Bridge to equity: EV − Net Debt − Minority Interest + Cash = Equity Value.

FCFE (use when: banks, insurance, or equity-only perspective):
```
FCFE = Net Income + D&A − ΔWorking Capital − Capex + Net Borrowing
```
Discount FCFE at Cost of Equity → Equity Value directly.

**Step 2 — Build the assumption register (complete before projecting)**

| Input | Bear | Base | Bull | Source / Basis |
|---|---|---|---|---|
| Revenue growth — Year 1 | [%] | [%] | [%] | [state basis] |
| Revenue growth — Years 2–5 | [%] | [%] | [%] | [state basis] |
| Revenue growth — terminal | = g | = g | = g | locked to TV assumption |
| EBITDA margin — Year 1 | [%] | [%] | [%] | [state basis] |
| EBITDA margin — terminal | [%] | [%] | [%] | [state basis] |
| D&A as % revenue | [%] | [%] | [%] | historical / mgmt guidance |
| Capex as % revenue | [%] | [%] | [%] | maintenance + growth split |
| ΔWC as % ΔRevenue | [%] | [%] | [%] | CCC analysis |
| Tax rate (effective) | [%] | [%] | [%] | statutory ± adjustments |
| WACC | [%] | [%] | [%] | built in Step 3 |
| Terminal growth rate (g) | [%] | [%] | [%] | long-run nominal GDP ref |
| Exit EV/EBITDA multiple | [x] | [x] | [x] | peer median / precedents |

**Step 3 — Compute WACC**

```
WACC = (E/V) × Ke + (D/V) × Kd × (1 − Tax Rate)

Where:
  Ke = Rf + β × ERP + Size Premium + Country Risk Premium
  Rf  = current 10-year sovereign yield (state date and source)
  β   = [levered beta; source: regression / peer average / Damodaran sector]
  ERP = [equity risk premium; source: Damodaran / Duff & Phelps / other]
  Kd  = [pre-tax cost of debt: yield on existing debt / estimated at-market yield]
  E/V = equity / (equity + debt) at market values
  D/V = debt / (equity + debt) at market values
```

If unlevered beta is used (e.g., for a private company), re-lever at target structure:
```
β_levered = β_unlevered × [1 + (1 − Tax Rate) × (D/E)]
```

**Step 4 — Project cash flows for explicit period**

Build a columnar projection table (see Output Format). For each year:
1. Start from revenue (apply growth rate).
2. Apply EBITDA margin → EBITDA.
3. Subtract D&A → EBIT.
4. Apply tax rate → NOPAT (for FCFF) or apply to net income (for FCFE).
5. Add back D&A.
6. Subtract ΔWC (increase in WC is a use of cash).
7. Subtract Capex.
8. Result: FCFF (or FCFE if net borrowing adjustment added).

**Step 5 — Calculate terminal value**

Method A — Perpetuity Growth (Gordon Growth Model):
```
TV_PGM = FCFF_terminal × (1 + g) / (WACC − g)
Requires: WACC > g. If not, flag and halt.
```

Method B — Exit Multiple:
```
TV_Exit = EBITDA_terminal × EV/EBITDA_exit_multiple
```

Note: Method A embeds structural assumptions about long-run returns on capital; Method B anchors to market pricing. Reconcile the two: if they diverge by more than 20%, investigate the implied perpetuity growth rate embedded in the exit multiple (= WACC − FCFF_terminal / TV_Exit).

**Step 6 — Discount to present value**

```
PV(FCFF_t) = FCFF_t / (1 + WACC)^t

PV(TV) = TV / (1 + WACC)^n

Enterprise Value = Σ PV(FCFF_t) + PV(TV)
```

Show the % of EV attributable to terminal value (a high % — >80% — is a red flag warranting sensitivity analysis on TV inputs).

**Step 7 — Bridge to equity value per share**

```
Equity Value = Enterprise Value − Net Debt − Minority Interest + Non-Operating Assets
Equity Value Per Share = Equity Value / Diluted Shares Outstanding
```

Net Debt = Total Debt + Preferred Stock + Capital Leases − Cash & Cash Equivalents

**Step 8 — Run base / bull / bear scenarios and build sensitivity tables**

Vary the two highest-impact assumptions (typically WACC and terminal growth rate, or WACC and exit multiple) in a 5×5 grid. See `finance_valuation_sensitivity_scenario.md`.

**Step 9 — Adversarial stress-test**

For each scenario, challenge the key assumptions:
- What revenue growth rate makes the base-case DCF break even (= current price)?
- What is the implied EV/EBITDA multiple of the terminal value? Is it defensible vs. peers?
- What happens if the terminal growth rate is 0% (flat-line perpetuity)?
- If Capex intensity rises 200bps, what is the impact on equity value per share?
- Identify the single assumption the valuation is most sensitive to and flag it.

## Output Format

### Assumption Register

| Input | Bear | Base | Bull | Source |
|---|---|---|---|---|
| [all rows from Step 2] | | | | |

### WACC Build

| Component | Value | Source / Notes |
|---|---|---|
| Risk-free rate (Rf) | [%] | [10-yr Treasury as of date] |
| Beta (levered) | [x] | [source] |
| Equity risk premium | [%] | [source] |
| Size premium | [%] | [source or "none"] |
| Country risk premium | [%] | [source or "none"] |
| **Cost of equity (Ke)** | **[%]** | Rf + β×ERP + premia |
| Pre-tax cost of debt (Kd) | [%] | [source] |
| Tax rate | [%] | [source] |
| After-tax cost of debt | [%] | Kd × (1−t) |
| Equity weight (E/V) | [%] | market value |
| Debt weight (D/V) | [%] | market value |
| **WACC** | **[%]** | weighted sum |

### Projection Table (FCFF basis — replicate for each scenario)

| Line Item | Y-2A | Y-1A | Y0A | Y1E | Y2E | Y3E | Y4E | Y5E | Terminal |
|---|---|---|---|---|---|---|---|---|---|
| Revenue | | | | | | | | | |
| Revenue growth % | | | | | | | | | |
| EBITDA | | | | | | | | | |
| EBITDA margin % | | | | | | | | | |
| D&A | | | | | | | | | |
| EBIT | | | | | | | | | |
| Tax @ [%] | | | | | | | | | |
| NOPAT | | | | | | | | | |
| + D&A | | | | | | | | | |
| − ΔWorking Capital | | | | | | | | | |
| − Capex | | | | | | | | | |
| **FCFF** | | | | | | | | | |
| Discount factor | | | | | | | | | |
| PV(FCFF) | | | | | | | | | |

### Valuation Summary

| | Bear | Base | Bull |
|---|---|---|---|
| PV of projection-period FCF | | | |
| PV of terminal value (PGM) | | | |
| PV of terminal value (Exit) | | | |
| **Enterprise Value (PGM)** | | | |
| **Enterprise Value (Exit)** | | | |
| − Net Debt | | | |
| − Minority Interest | | | |
| + Non-operating assets | | | |
| **Equity Value (PGM)** | | | |
| **Equity Value (Exit)** | | | |
| Diluted shares | | | |
| **Equity Value / Share (PGM)** | | | |
| **Equity Value / Share (Exit)** | | | |
| TV as % of EV | | | |

### Sensitivity Table (WACC × Terminal Growth Rate)

| WACC ↓ / g → | [g−1%] | [g−0.5%] | [Base g] | [g+0.5%] | [g+1%] |
|---|---|---|---|---|---|
| [WACC+1%] | | | | | |
| [WACC+0.5%] | | | | | |
| [Base WACC] | | | | | |
| [WACC−0.5%] | | | | | |
| [WACC−1%] | | | | | |

### Stress-Test Findings

- **Break-even growth rate** (at current share price, base WACC): [%]
- **Implied TV multiple** (PGM method): [x] EV/EBITDA — [vs. peer median: x]
- **Flat-perpetuity scenario** (g = 0%): equity value / share = [x]
- **Capex +200bps sensitivity**: equity value / share impact = [−$x or −x%]
- **Most sensitive assumption**: [name it and quantify the impact of ±1σ move]

## Verification

- [ ] FCFF formula is correct: NOPAT + D&A − ΔWC − Capex (confirm sign convention: WC increase is negative cash flow).
- [ ] WACC components are each sourced and dated; Rf is a current market rate, not a historical average.
- [ ] Beta is correctly levered/unlevered for the subject company's actual capital structure.
- [ ] WACC > terminal growth rate g in all scenarios; if not, model halts and flags.
- [ ] Terminal value computed by both methods; implied perpetuity growth rate cross-checked.
- [ ] TV as % of EV is disclosed; if >75%, sensitivity on TV inputs is mandatory.
- [ ] Net debt bridge uses market value of debt where debt is publicly traded; book value where not (note the difference).
- [ ] Diluted share count includes in-the-money options, warrants, convertibles (treasury-stock method).
- [ ] All assumptions in the register have stated bases; `[ASSUMED]` flags are present where data is missing.
- [ ] Scenarios are internally consistent — bull revenue cannot pair with bear margin if margin is volume-driven.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Presenting a single DCF value as "the" intrinsic value | Output is always a range: bear / base / bull + sensitivity grid |
| Growth rate above WACC in perpetuity (produces nonsense value) | Hard check: WACC − g > 0 required; model halts if violated |
| Terminal value comprising >90% of EV presented without comment | Flag TV% explicitly; require sensitivity analysis on g and exit multiple when TV > 75% of EV |
| Using book-value capital weights for WACC | Require market-value weights; note when equity is private and estimate must be used |
| Treating EBITDA as a proxy for cash flow without capex/WC adjustment | FCFF/FCFE requires all four components; EBITDA shortcuts are rejected |
| Anchoring on management guidance without stress | Bear scenario must assume guidance miss, not merely low-end guidance |
| Precision illusion from detailed spreadsheet | Output range expressed as $X–$Y per share, not $X.XX; acknowledge model uncertainty |
| Omitting minority interest or non-operating assets from the bridge | Equity-value bridge checklist is mandatory and verified |
