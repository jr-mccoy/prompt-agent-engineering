---
title: "WACC Builder — CAPM Cost of Equity, Capital Weights, Size/Country Premia, and Sensitivity"
category: finance/valuation
description: "Build a defensible weighted average cost of capital from first principles: CAPM-based cost of equity with beta sourcing and relevering, cost of debt, capital-structure weights, size and country risk premia, and a sensitivity matrix across key inputs."
techniques:
  - NE-11
  - DS-02
  - QA-01
  - QA-04
  - NE-10
difficulty: intermediate
tags:
  - wacc
  - cost-of-capital
  - capm
  - beta
  - discount-rate
  - equity-risk-premium
updated: "2026-06-08"
related_prompts:
  - domain-finance/valuation/finance_dcf_model_builder.md
  - domain-finance/valuation/finance_terminal_value_sanity_check.md
  - domain-finance/valuation/finance_valuation_sensitivity_scenario.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. All outputs must be reviewed by qualified finance professionals before use in any transaction or decision.**

## Objective

Build a defensible, auditable weighted average cost of capital (WACC) from first principles — computing the cost of equity via CAPM with appropriately sourced and relevered beta, the after-tax cost of debt, market-value capital-structure weights, and any applicable size or country risk premia — then presenting a sensitivity matrix that reveals how WACC responds to key input changes.

## When to Use

- Establishing the discount rate for a DCF model (`finance_dcf_model_builder.md`)
- Benchmarking a discount rate provided by a counterparty in a negotiation or fairness process
- Computing a hurdle rate for capital-allocation decisions (capex, M&A, new business lines)
- Estimating the cost of capital for a private company using comparable-public-company betas
- CFA or valuation training requiring a step-by-step WACC derivation

## Inputs / Context Required

**Company and capital structure**
- Company name and industry
- Current market capitalization (equity market value)
- Market value of total debt outstanding (use book value if market value is not available; note the substitution)
- Preferred stock (if any) — market value and dividend rate
- Minority interest (if any) — approximate market value
- Marginal corporate tax rate (statutory, not effective; note any known deviations)
- Target capital structure, if different from current (state rationale)

**Cost-of-equity inputs**
- Risk-free rate: specify the tenor (10-year or 30-year sovereign yield) and the date/source
- Equity risk premium (ERP): specify source (Damodaran annual update, Duff & Phelps, or custom)
- Beta: specify source — regression beta from Bloomberg or similar, peer-average beta, or Damodaran sector beta
- Levered or unlevered beta: state which is provided; re-levering will be done in Steps 3–4
- Size premium (if applicable): specify source (Duff & Phelps CRSP size study or stated)
- Country risk premium (if applicable for non-US or emerging-market companies): state source

**Cost-of-debt inputs**
- Pre-tax cost of debt: yield-to-maturity on existing public debt (preferred), or estimated at-market rate based on credit rating / spread (state method)
- Do not use the coupon rate on old fixed-rate debt as the current cost of debt

**Scenario / sensitivity preferences**
- Which inputs to vary in the sensitivity matrix (default: β and ERP; or user-specified)

## Constraints

### Must
- Show every formula explicitly before plugging in numbers.
- Use market-value capital weights, not book-value weights; if equity is private, document the estimation method.
- Relever beta at the subject company's actual (or target) capital structure using the Hamada equation.
- Source and date the risk-free rate and ERP; do not use averages from the wrong time period.
- Present WACC as a range across scenarios (base / bull / bear correspond to different beta / ERP / capital structure assumptions).
- Produce a sensitivity matrix across at least two inputs.
- State the marginal (statutory) tax rate for the debt tax shield; note if effective tax rate is lower.

### Must Not
- Use book-value capital weights; WACC requires market-value weights.
- Apply the coupon rate on existing debt as the cost of new debt.
- Use an ERP without identifying its source.
- Relever using a peer-group beta without un-levering each peer first (the raw peer beta embeds each peer's own leverage).
- Omit the size premium for small-cap companies without at least disclosing the potential adjustment.
- Apply a single-point WACC without acknowledging the range of defensible inputs.

## Instructions

**Step 1 — Establish the capital structure weights**

```
Total Capital = Market Equity + Market Debt + Market Preferred + Minority Interest
  (use book value of debt if market value is unavailable; note the substitution)

E/V = Market Equity / Total Capital
D/V = Market Debt / Total Capital
P/V = Market Preferred / Total Capital
MI/V = Minority Interest / Total Capital

Check: E/V + D/V + P/V + MI/V = 1.0
```

If a target capital structure is used instead of the current structure, state the target and justify (e.g., "Company has announced a leverage-reduction plan toward X% debt weight").

**Step 2 — Compute the risk-free rate**

```
Rf = Current yield on 10-year (or 30-year) sovereign bond
   [State: country, tenor, yield, and date — e.g., US 10-yr Treasury at 4.35% as of 2026-06-01]

For long-duration assets / long DCF projections: consider the 30-year Treasury or a maturity-matched rate.
For near-term projects or shorter holding periods: 10-year Treasury is standard.

Do not use a historical average; use the current market rate.
```

**Step 3 — Source and unlever the beta**

If using a regression or reported beta for the subject company:
```
β_levered (observed) = [from Bloomberg / FactSet / stated source]
β_unlevered = β_levered / [1 + (1 − Tax Rate) × (D/E)]
  where D/E = Market Debt / Market Equity at the observation date
```

If using peer-group betas (for private companies or to cross-check):
```
For each comparable company i:
  β_unlevered_i = β_levered_i / [1 + (1 − Tax Rate_i) × (D/E_i)]

β_unlevered (subject) = Median(β_unlevered_i across peers)
  [state the peer set; at minimum 4 peers]
```

**Step 4 — Relever beta at target/current capital structure (Hamada equation)**

```
Hamada Re-levering:
  β_levered = β_unlevered × [1 + (1 − Tax Rate) × (D/E)]

Where D/E = target (or current) debt-to-equity ratio at market values.

Note: The Hamada equation assumes debt is risk-free and perpetual. For more precise treatments
with risky debt, the Miles-Ezzell or Harris-Pringle adjustments may be used (state if applied).
```

**Step 5 — Compute cost of equity (CAPM)**

```
Ke = Rf + β_levered × ERP + SP + CRP

Where:
  Rf  = risk-free rate (Step 2)
  β   = relevered beta (Step 4)
  ERP = equity risk premium [source: Damodaran / Duff & Phelps / other — state and date]
  SP  = size premium [source: CRSP decile / Duff & Phelps; apply only if relevant; default = 0 for large-cap]
  CRP = country risk premium [apply for non-US or emerging-market operations; state source and calculation method]
```

Size premium guidance (illustrative order of magnitude; always use sourced values):
- Large-cap (>$10B market cap): commonly 0–0.5%
- Mid-cap ($1–10B): commonly 0.5–1.5%
- Small-cap ($250M–$1B): commonly 1.5–3%
- Micro-cap (<$250M): commonly 3–5%+

**Step 6 — Compute after-tax cost of debt**

```
Kd_pre_tax = Yield-to-maturity on existing long-term debt (public)
           OR estimated at-market rate = Risk-free rate + Credit Spread
           [Credit spread derived from: public rating (Aaa/Aa/A/Baa/Ba/B/Caa) + spread table,
            or from traded CDS / bond spread for public issuers]

Kd_after_tax = Kd_pre_tax × (1 − Marginal Tax Rate)

Use MARGINAL (statutory) tax rate for the debt tax shield, not the effective rate.
If the company has NOL carryforwards reducing near-term taxes, note that the tax shield
may not be realized immediately and may warrant adjustment.
```

**Step 7 — Compute WACC**

```
WACC = (E/V) × Ke + (D/V) × Kd_after_tax + (P/V) × Kp

Where:
  Kp = cost of preferred = Preferred Dividend / Preferred Market Value
       (preferred dividends are not tax-deductible in most jurisdictions;
        if IFRS treatment differs, note)

WACC = [insert calculation here, showing each term explicitly]
```

**Step 8 — Scenario range and sensitivity matrix**

Vary the highest-uncertainty inputs to produce a WACC range:

| Scenario | β_levered | ERP | Rf | Size Prem | WACC |
|---|---|---|---|---|---|
| Bear (higher discount rate) | [x] | [%] | [%] | [%] | [%] |
| Base | [x] | [%] | [%] | [%] | [%] |
| Bull (lower discount rate) | [x] | [%] | [%] | [%] | [%] |

Sensitivity matrix — WACC across β and ERP:

| β ↓ / ERP → | [ERP − 1%] | [ERP − 0.5%] | [Base ERP] | [ERP + 0.5%] | [ERP + 1%] |
|---|---|---|---|---|---|
| [β + 0.3] | | | | | |
| [β + 0.15] | | | | | |
| [Base β] | | | | | |
| [β − 0.15] | | | | | |
| [β − 0.3] | | | | | |

## Output Format

### Capital Structure Weights

| Component | Market Value ($M) | Weight (%) | Notes |
|---|---|---|---|
| Market Equity | | | |
| Market Debt | | | |
| Preferred Stock | | | |
| **Total Capital** | | 100% | |

### Beta Derivation

| Step | Value | Source / Notes |
|---|---|---|
| Reported β_levered | | [source, date] |
| Observed D/E at observation date | | |
| Tax rate used for unlevering | | |
| β_unlevered | | computed |
| Target D/E for relevering | | |
| β_levered (relevered) | | Hamada |

### WACC Build

| Component | Value | Source / Notes |
|---|---|---|
| Risk-free rate (Rf) | [%] | [tenor, date, source] |
| Relevered beta (β) | [x] | |
| Equity risk premium (ERP) | [%] | [source] |
| Size premium (SP) | [%] | [source or "N/A"] |
| Country risk premium (CRP) | [%] | [source or "N/A"] |
| **Cost of equity (Ke)** | **[%]** | Rf + β×ERP + SP + CRP |
| Pre-tax cost of debt (Kd) | [%] | [YTM / estimated; source] |
| Marginal tax rate | [%] | [statutory] |
| After-tax cost of debt | [%] | Kd × (1 − t) |
| Cost of preferred (Kp) | [%] | [if applicable] |
| Equity weight (E/V) | [%] | market value |
| Debt weight (D/V) | [%] | market value |
| **WACC** | **[%]** | weighted sum |

### Scenario Summary and Sensitivity Matrix

[Step 8 tables]

## Verification

- [ ] Capital weights are market-value weights; book-value substitution is disclosed if used.
- [ ] Beta is sourced and dated; un-levered from observed leverage; re-levered at target structure using Hamada equation.
- [ ] Risk-free rate is a current market rate, not a historical average; tenor stated.
- [ ] ERP source is identified (Damodaran, Duff & Phelps, or named); not an arbitrary percentage.
- [ ] Size premium applied only where relevant to company size; source cited.
- [ ] Cost of debt is YTM or credit-spread-based, not the coupon on old fixed-rate debt.
- [ ] Marginal (statutory) tax rate used for debt tax shield.
- [ ] WACC formula components sum correctly (check with arithmetic).
- [ ] Scenario range and sensitivity matrix present.
- [ ] WACC > terminal growth rate cross-check noted (for any linked DCF).

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Using book-value capital weights (understates equity weight for profitable companies) | Market-value weights required; book-value is not a substitute without disclosure and adjustment |
| Using raw peer beta without un-levering first (embeds peer leverage, not subject company leverage) | Always un-lever each peer beta before averaging, then re-lever at subject D/E |
| Applying an ERP that is a memorized "standard" number rather than a current sourced estimate | ERP must be attributed to a named, dated source; the right ERP changes over time |
| Using the coupon rate on 5-year-old fixed-rate bonds as today's cost of debt | Use YTM or credit-spread-based estimate; coupon rate reflects historical borrowing cost |
| Applying a single-point WACC as if it is precise | WACC is inherently uncertain; sensitivity matrix is mandatory; express WACC as a range |
| Omitting the size premium for micro-cap companies, materially understating the discount rate | Size premium applicability check is required; omission must be explicitly defended |
