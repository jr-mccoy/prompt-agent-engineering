---
title: "Reverse DCF — Back Out Implied Growth and Margin from Current Price and Test Plausibility"
category: finance/valuation
description: "Solve the DCF model in reverse: given the current market price, back out the revenue growth, margin, or terminal growth assumptions the market is implicitly pricing in — then test whether those implied assumptions are plausible, achievable, or stretched."
techniques:
  - NE-11
  - QA-02
  - AG-02
  - NE-10
  - DS-02
difficulty: advanced
tags:
  - reverse-dcf
  - implied-growth
  - market-expectations
  - valuation
  - price-discovery
  - intrinsic-value
updated: "2026-06-08"
related_prompts:
  - domain-finance/valuation/finance_dcf_model_builder.md
  - domain-finance/valuation/finance_terminal_value_sanity_check.md
  - domain-finance/valuation/finance_valuation_sensitivity_scenario.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. All outputs must be reviewed by qualified finance professionals before use in any transaction or decision.**

## Objective

Solve a discounted cash flow model in reverse: starting from the current share price, derive the revenue growth, EBITDA margin, terminal growth rate, or WACC that the market is implicitly pricing into the stock — and then apply adversarial scrutiny to determine whether those implied assumptions are achievable, stretched, or implausible, thereby revealing where the market is priced for perfection or excessive pessimism.

## When to Use

- Evaluating whether a stock is priced for perfection (implied assumptions exceed historical or industry achievable levels)
- Framing an investment thesis around a variant view on the implied assumptions (e.g., "the market is pricing in 8% revenue growth; we think 5% is realistic")
- Stress-testing a current market price against a bear scenario to understand the margin of safety
- Communicating valuation risk to a non-technical audience by translating price into plain assumptions
- Short-thesis construction: identifying when implied assumptions are implausible
- CFA Level 2 / 3 study on equity valuation and market-implied expectation analysis

## Inputs / Context Required

**Current price and structure**
- Current share price (or EV, if working at enterprise level)
- Diluted shares outstanding
- Net debt (for EV → equity bridge)
- Fiscal year end and current LTM financials

**LTM financial summary**
- Revenue
- EBITDA and EBITDA margin
- EBIT
- D&A
- Capex
- ΔWorking Capital
- Tax rate (effective and statutory)
- Free cash flow to firm (FCFF) — computed or provided

**Model framework (from the forward DCF)**
- WACC (or range; from `finance_wacc_builder.md`)
- Explicit projection period (number of years)
- Fixed assumptions (inputs the analyst accepts as given): identify which inputs will be held constant and which will be solved for
- Terminal growth rate or exit multiple (one of these will typically be the "solve for" variable, or it will be fixed while a growth/margin assumption is solved)

**What to solve for (select one primary target):**
- Revenue CAGR needed to justify current price (given base WACC, margins, terminal g)
- EBITDA margin needed to justify current price (given base WACC, revenue growth, terminal g)
- Terminal growth rate needed to justify current price (given base WACC, revenue growth, margins)
- WACC implied by current price (given base revenue, margins, terminal g)
- Or: present a table solving for multiple targets simultaneously

## Constraints

### Must
- Show the forward DCF structure before solving in reverse — the reader must understand what model is being inverted.
- Hold constant the assumptions not being solved for, and state each explicitly.
- After deriving the implied assumption, test its plausibility against: (a) the company's own historical performance, (b) industry best-in-class benchmarks, and (c) the long-run structural ceiling for that assumption.
- Present implied assumptions for at least two "solve for" variables.
- Apply adversarial scrutiny (AG-02): assume the implied assumption is wrong and determine what the downside price is.
- Run the reverse calculation for bear, base, and bull current-price levels (±15–20% of current price) to show how the implied assumption changes with modest price movements.

### Must Not
- Present the implied assumption as "what the company must achieve" without a plausibility test.
- Use the reverse DCF as confirmation that the current price is correct; it reveals what the price implies, not whether the price is right.
- Solve for so many variables simultaneously that the model is unconstrained; fix all but 1–2 inputs per solve.
- Invent financial figures; use stated inputs or flagged estimates.

## Instructions

**Step 1 — Reconstruct the forward DCF skeleton**

Before reversing, confirm the model structure:

```
Forward DCF structure:
  Revenue (Year 0 = LTM)
  Revenue CAGR (projection period): [%]
  EBITDA margin (terminal year): [%]
  D&A as % revenue: [%]
  Capex as % revenue: [%]
  ΔWC as % ΔRevenue: [%]
  Tax rate: [%]
  FCFF derivation: NOPAT + D&A − ΔWC − Capex
  WACC: [%]
  Terminal growth rate (g): [%]
  Projection period: [n] years
  Terminal value method: Gordon Growth (TV = FCFF_n × (1+g) / (WACC−g))

Equity value per share = f(Revenue CAGR, EBITDA Margin, WACC, g, …)
```

Confirm: at base-case inputs, what equity value / share does the forward DCF produce? This is the reference point.

**Step 2 — Define the "solve for" target and fix all other inputs**

State clearly what is being held fixed and what is being solved:

Example:
```
FIXED:
  WACC = 9.0% (from CAPM build)
  EBITDA margin (terminal) = 22% (management guidance)
  Capex, D&A, ΔWC ratios = historical
  Terminal growth rate (g) = 2.5% (long-run nominal GDP)
  Projection period = 7 years

SOLVE FOR:
  Revenue CAGR over the projection period such that:
  f(Revenue CAGR) = Current Share Price of $P₀

This Revenue CAGR is the "implied revenue growth" the market is pricing in.
```

**Step 3 — Solve for the implied assumption (iterative or algebraic)**

For terminal-growth rate as the solve variable (simplest algebraic case):

```
Current EV = Equity Value + Net Debt
           = Share Price × Diluted Shares + Net Debt

PV of projection-period FCF = Σ [FCFF_t / (1 + WACC)^t]
  [Computed from fixed revenue/margin/capex assumptions]

PV(TV) = Current EV − PV of projection-period FCF

TV = PV(TV) × (1 + WACC)^n

From Gordon Growth:
  TV = FCFF_n × (1 + g_implied) / (WACC − g_implied)

Solve for g_implied:
  WACC × TV − g_implied × TV = FCFF_n + FCFF_n × g_implied
  TV × (WACC − FCFF_n / TV) = g_implied × (TV + FCFF_n) − [rearrange]
  g_implied = (TV × WACC − FCFF_n) / (TV + FCFF_n)
```

For revenue CAGR (requires numerical iteration — state the iteration approach):
```
Set up: Equity Value / Share = g(Revenue CAGR | fixed assumptions)
Iterate: vary Revenue CAGR from 0% to 20% in 0.5% steps
Find: the Revenue CAGR such that the model output = current share price
Report: Revenue CAGR_implied = [%]
```

**Step 4 — Build the implied-assumption matrix across current price levels**

Test how the implied assumption changes as the market price moves:

| Share Price | Price / Base | Implied Revenue CAGR | Implied EBITDA Margin | Implied g (terminal) | Implied WACC |
|---|---|---|---|---|---|
| Base × 0.70 (bear price) | −30% | [%] | [%] | [%] | [%] |
| Base × 0.85 | −15% | [%] | [%] | [%] | [%] |
| Current price | — | [%] | [%] | [%] | [%] |
| Base × 1.15 | +15% | [%] | [%] | [%] | [%] |
| Base × 1.30 (bull price) | +30% | [%] | [%] | [%] | [%] |

**Step 5 — Plausibility test for implied assumptions**

For each implied assumption, apply three tests:

| Implied Assumption | Value | Company Historical (5-yr avg) | Industry Best-in-Class | Structural Ceiling | Verdict |
|---|---|---|---|---|---|
| Revenue CAGR | [%] | [%] | [%] | [%] | Achievable / Stretched / Implausible |
| EBITDA margin (terminal) | [%] | [%] | [%] | [%] | Achievable / Stretched / Implausible |
| Terminal growth (g) | [%] | — | — | Nominal GDP [%] | Achievable / Stretched / Implausible |
| WACC | [%] | — | Sector range | — | Consistent / Low / High |

Verdict definitions:
- **Achievable**: implied assumption is within the company's historical range or is consistent with peer performance; requires no exceptional execution
- **Stretched**: implied assumption is above historical performance but within industry best-in-class; requires strong execution or favorable conditions
- **Implausible**: implied assumption exceeds industry best-in-class or structural ceiling; would require sustained performance that no comparator has achieved

**Step 6 — Adversarial downside: what price does a realistic bear case imply?**

Replace the "implied" assumptions with realistic bear-case assumptions and solve for the price:

```
Bear-case inputs (state each):
  Revenue CAGR = [%] (lower; e.g., historical mean or analyst downside estimate)
  EBITDA margin = [%] (lower; e.g., cost-pressure scenario)
  WACC = [%] (higher; e.g., rate-rise scenario)
  g = [%] (lower; e.g., mature-company terminal rate)

Bear-case equity value / share = [$]
  Bear-case discount to current price = [%]
```

**Step 7 — Synthesize the expectations gap**

Formulate the variant view:
```
Expectations Gap Analysis:
  Market is implying: [implied Revenue CAGR] revenue growth and [implied EBITDA margin] terminal margin
  Our view: [analyst's Revenue CAGR] revenue growth and [analyst's EBITDA margin] terminal margin
  Net implied value at our view: [$]
  Upside to current price if our view is correct: [+%]
  Downside to current price if our view is correct: [−%]
  Conviction threshold: [what evidence would confirm the market's implied view is wrong]
```

## Output Format

### Forward DCF Skeleton and Reference Point

[Step 1 — model structure and base-case output]

### Solve-For Definition

[Step 2 — fixed inputs and target variable]

### Implied Assumption at Current Price

| Solve-For Variable | Implied Value |
|---|---|
| Revenue CAGR | [%] |
| Terminal EBITDA margin | [%] |
| Terminal growth (g) | [%] |
| WACC | [%] |

### Implied-Assumption Matrix Across Price Levels

[Step 4 table]

### Plausibility Test

[Step 5 table — historical / best-in-class / ceiling / verdict]

### Bear-Case Price Derivation

[Step 6 — inputs and implied bear price]

### Expectations Gap Summary

[Step 7 — variant view and conviction threshold]

## Verification

- [ ] Forward DCF structure stated before inversion; base-case forward output confirmed.
- [ ] All fixed assumptions listed explicitly; only 1–2 inputs solved per iteration.
- [ ] Implied assumption computed for at least two solve variables.
- [ ] Implied-assumption matrix shows results at ±30% from current price.
- [ ] Plausibility test applies three benchmarks: historical, best-in-class, structural ceiling.
- [ ] Bear-case price computed from realistic (not arbitrarily pessimistic) inputs.
- [ ] Expectations gap formulated with a stated conviction threshold.
- [ ] WACC > g check preserved in reverse calculation; any scenario where g ≥ WACC is flagged.
- [ ] No financial figures invented; all base inputs sourced or labeled `[ASSUMED]`.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Using the reverse DCF to "confirm" the current price is fair | The reverse DCF reveals what the price implies; plausibility testing determines whether the implications are reasonable |
| Calling an implied assumption "implausible" without a benchmark comparison | Plausibility verdict requires ≥2 benchmarks (historical + best-in-class or structural ceiling) |
| Holding WACC perfectly constant in the reverse DCF while solving for g, when they are correlated in practice | Note the assumption that WACC is held constant; in rising-rate environments, both g and WACC may shift |
| Presenting the bear-case price as a "target price" | Bear-case price is a stress scenario, not a price target; label it as the downside case |
| Treating a "stretched" plausibility verdict as equivalent to "implausible" | Maintain clear verdict distinctions; "stretched" means achievable with strong execution, not impossible |
| Ignoring the net-debt bridge when converting EV to equity value in the reverse calculation | Equity value = EV − net debt; omitting debt produces an incorrect implied share price |
