---
title: "Dividend Discount Model — Gordon Growth and Multi-Stage with Implied-Growth and Reinvestment Checks"
category: finance/valuation
description: "Build a dividend discount model (DDM) using Gordon Growth or multi-stage structure, with explicit reinvestment-rate and return-on-equity checks, implied-growth cross-validation, and base/bull/bear scenario ranges."
techniques:
  - NE-11
  - NE-10
  - QA-01
  - DS-02
  - QA-04
difficulty: intermediate
tags:
  - ddm
  - dividend-discount-model
  - valuation
  - gordon-growth
  - cost-of-equity
  - dividend-paying-stocks
updated: "2026-06-08"
related_prompts:
  - domain-finance/valuation/finance_dcf_model_builder.md
  - domain-finance/valuation/finance_wacc_builder.md
  - domain-finance/valuation/finance_reverse_dcf_expectations.md
  - domain-finance/financial-statement-analysis/finance_ratio_analysis_engine.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. All outputs must be reviewed by qualified finance professionals before use in any transaction or decision.**

## Objective

Construct a defensible dividend discount model valuation — using either the Gordon Growth (single-stage) model or a two-to-three-stage DDM for companies with non-steady-state dividend patterns — with explicit reinvestment-rate checks, return-on-equity consistency tests, implied-growth back-calculation, and base / bull / bear scenario ranges.

## When to Use

- Intrinsic-value analysis for dividend-paying companies (utilities, REITs, banks, mature consumer staples)
- Validating a DCF result for a company that returns substantial cash via dividends
- Analyzing preferred stock or perpetual-income instruments where dividends are fixed or formula-driven
- Cross-checking an earnings-based valuation (P/E) for a mature, stable dividend payer
- CFA Level 2 / 3 study exercises on equity valuation with the dividend discount approach

**When NOT to use this prompt:**
- Companies that do not pay dividends and have no near-term prospect of initiating them (use DCF / FCFE instead)
- Companies in high-growth phases where dividends are minimal and earnings are reinvested (the growth assumptions will dominate and a DDM will be highly sensitive to terminal assumptions)

## Inputs / Context Required

**Company context**
- Company name, ticker, industry, and country
- Current annual dividend per share (DPS) — most recently declared annualized rate
- Current share price
- Payout ratio (dividends / net income, or dividends / FCFE)
- Dividend history: 5–10 years of DPS to establish trend
- Any announced dividend policy changes or guidance

**Fundamental inputs**
- Return on equity (ROE) — LTM and 5-year average
- Net income per share (EPS) — LTM and forward estimate (if available)
- Retention ratio (b) = 1 − payout ratio
- Cost of equity (Ke): provide either a computed value (use `finance_wacc_builder.md`) or the CAPM inputs (Rf, β, ERP)

**Stage structure**
- Model type: Gordon Growth (single-stage) or multi-stage (two or three stages)
- For multi-stage: growth rates and durations for each stage, and the basis for each
- Terminal (steady-state) growth rate assumption and basis

**Scenario framework**
- Bull, base, and bear assumptions for: growth rate(s), cost of equity, and payout ratio

## Constraints

### Must
- Show every formula before applying it.
- Verify internal consistency: sustainable growth rate (g = ROE × b) must be consistent with the stated dividend growth rate; any material divergence must be explained.
- Check that Ke > g in the terminal stage; if not, the model produces an undefined or nonsensical value — flag and halt.
- Present the implied growth rate embedded in the current stock price (reverse DDM calculation).
- Run base / bull / bear scenarios; never output a single-point value.
- Disclose the sensitivity of implied value to ±0.5% changes in both Ke and g.

### Must Not
- Apply the Gordon Growth Model to a company with non-steady dividend growth without using a multi-stage structure.
- Use a terminal growth rate that exceeds long-run nominal GDP without explicit, defended justification.
- Assume a payout ratio of 100% for a growing company (conflicts with reinvestment logic).
- Confuse dividend yield (DPS / Price) with dividend growth rate.
- Present the DDM as the only valuation method; note that it is most reliable for stable, mature dividend payers.

## Instructions

**Step 1 — Check applicability and select model structure**

Apply the applicability screen:
- Is the dividend history stable and growing? (Yes → DDM applicable; No → flag and consider FCFE DDM instead)
- Is the payout ratio stable (not rapidly changing)? (Yes → single-stage or two-stage; No → multi-stage required)
- Is the company in a mature, slow-growth industry? (Yes → Gordon Growth viable; No → multi-stage required)

For companies in high-growth or transition phases, a two-stage DDM is more appropriate:
- **Stage 1**: Explicit dividend forecast for years 1–N (e.g., 3–7 years), using projected EPS × payout ratio
- **Stage 2**: Stable perpetuity growth at long-run g

**Step 2 — Check sustainable growth rate consistency**

```
Sustainable Growth Rate:
  g_sustainable = ROE × Retention Rate (b)
  b = 1 − Payout Ratio

Test: Stated dividend growth rate vs. g_sustainable
  If stated g ≈ g_sustainable: internally consistent
  If stated g > g_sustainable: implies ROE expansion or increasing leverage — state the mechanism
  If stated g << g_sustainable: implies payout ratio is expected to rise, reducing reinvestment
```

**Step 3 — Estimate or confirm the cost of equity (Ke)**

```
CAPM:
  Ke = Rf + β × ERP + Size Premium + Country Risk Premium

Where:
  Rf  = current risk-free rate (10-year sovereign yield; state date and source)
  β   = levered beta (source: regression / peer / Damodaran sector)
  ERP = equity risk premium (source: Damodaran / Duff & Phelps / stated)

Verify: Ke > g in the terminal stage — required for the model to produce a finite positive value.
```

**Step 4A — Gordon Growth Model (single-stage)**

For stable, mature dividend payers where dividends grow at a constant rate in perpetuity:

```
Gordon Growth Model:
  V₀ = D₁ / (Ke − g)

Where:
  D₁ = D₀ × (1 + g) = next year's expected dividend
  D₀ = current annual dividend per share
  Ke = cost of equity
  g  = constant perpetuity dividend growth rate

Required check: Ke − g > 0.  If Ke ≤ g, the model is undefined. Flag as Critical and halt.
```

**Step 4B — Two-Stage DDM (for transition companies)**

```
Stage 1 — Explicit forecast (years 1 through N):
  D_t = D_{t-1} × (1 + g_stage1)  [or bottom-up: EPS_t × payout_ratio]
  PV(D_t) = D_t / (1 + Ke)^t

Stage 2 — Terminal value at end of year N:
  P_N = D_{N+1} / (Ke − g_stable)
  D_{N+1} = D_N × (1 + g_stable)
  PV(P_N) = P_N / (1 + Ke)^N

Intrinsic Value V₀ = Σ PV(D_t) [t=1 to N] + PV(P_N)
```

**Step 5 — Build the scenario-based projection table**

| | Bear | Base | Bull |
|---|---|---|---|
| D₀ (current DPS) | | | |
| Stage 1 growth rate | [%] | [%] | [%] |
| Stage 1 duration (years) | | | |
| Stage 2 (terminal) growth g | [%] | [%] | [%] |
| Cost of equity Ke | [%] | [%] | [%] |
| Ke − g (spread) | [%] | [%] | [%] |
| D₁ | | | |
| P_N (terminal value) | | | |
| PV of Stage 1 dividends | | | |
| PV of terminal value | | | |
| **Intrinsic Value V₀** | | | |
| Current share price | | | |
| Premium / (Discount) | [%] | [%] | [%] |

**Step 6 — Reverse DDM: implied growth at current price**

```
Implied growth rate at current price P₀:
  P₀ = D₁ / (Ke − g_implied)
  g_implied = Ke − D₁ / P₀

Test: Is g_implied reasonable?
  If g_implied > long-run nominal GDP: current price embeds above-GDP growth; flag as elevated expectation
  If g_implied < 0: market implies dividend erosion; investigate the basis
  If g_implied ≈ g in base case: model is consistent with current market pricing
```

**Step 7 — Sensitivity table**

| Ke ↓ / g → | [g − 1%] | [g − 0.5%] | [Base g] | [g + 0.5%] | [g + 1%] |
|---|---|---|---|---|---|
| [Ke + 1%] | | | | | |
| [Ke + 0.5%] | | | | | |
| [Base Ke] | | | | | |
| [Ke − 0.5%] | | | | | |
| [Ke − 1%] | | | | | |

Show implied intrinsic value V₀ at each combination.

**Step 8 — Reinvestment and payout consistency check**

- Confirm that the payout ratio + retention ratio = 100%.
- Cross-check: is the assumed dividend growth rate consistent with EPS growth projections? `DPS growth ≈ EPS growth × (1 ± change in payout ratio)`.
- If the company is expected to increase payout ratio over time, model this explicitly; a rising payout reduces reinvestment and may reduce sustainable long-run growth.

## Output Format

### Applicability Assessment

> [One paragraph: confirm the DDM is appropriate for this company, citing dividend history, payout stability, and business maturity. Flag any limitations.]

### Sustainable Growth Check

| Metric | Value | Source |
|---|---|---|
| ROE (LTM) | [%] | |
| Retention rate (b) | [%] | |
| Sustainable growth (ROE × b) | [%] | |
| Stated dividend growth rate | [%] | |
| Consistency | Pass / Flag | |

### CAPM / Cost of Equity Build

[Show Ke components — see Step 3]

### Scenario Projection Table

[Step 5 table — bear / base / bull]

### Reverse DDM: Implied Growth at Current Price

| Current Price | D₁ (next dividend) | Ke | Implied g | Assessment |
|---|---|---|---|---|
| [$] | [$] | [%] | [%] | [In-line / Elevated / Depressed] |

### Sensitivity Table

[Step 7 — Ke × g grid of intrinsic values]

## Verification

- [ ] Ke > g in the terminal stage in all scenarios; if violated, model is flagged and halted.
- [ ] D₁ = D₀ × (1 + g) confirmed — using next-year dividend, not current-year.
- [ ] Sustainable growth rate (ROE × b) cross-checked against stated g; any divergence explained.
- [ ] Reverse DDM applied to derive implied growth at current market price.
- [ ] Sensitivity table spans ±1% on both Ke and g.
- [ ] Model appropriateness assessment completed (dividend-paying, stable payout, mature business).
- [ ] Payout ratio + retention ratio confirmed to sum to 100%.
- [ ] Scenarios (bear / base / bull) have internally consistent Ke, g, and payout assumptions.
- [ ] No dividend figures invented; current DPS and history sourced and dated.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Applying the Gordon Growth Model to a high-growth, low-payout company | Applicability check in Step 1 is mandatory; non-dividend payers or thin payers are redirected to FCFE / DCF |
| Ke ≤ g produces a negative or undefined model value | Hard check in Step 4A; if violated, output is flagged Critical and model halts |
| Treating the DDM result as the "right" price | DDM is one method among several; cross-reference with DCF and trading comps; its reliability is highest for utilities and mature dividend payers |
| Ignoring payout ratio dynamics when modeling dividend growth | Rising payout ratio reduces reinvestment; model payout trajectory explicitly in multi-stage DDM |
| High sensitivity of output to g — small g changes produce large value swings | Sensitivity table is mandatory; flag if the Ke − g spread is ≤ 1% (model is highly sensitive) |
| Implied growth from reverse DDM dismissed without comment | The implied-growth check is a required output; a gap between implied g and modeled g must be explained |
