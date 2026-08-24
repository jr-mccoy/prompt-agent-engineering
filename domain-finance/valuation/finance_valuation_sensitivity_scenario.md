---
title: "Valuation Sensitivity and Scenario Analysis — Tables, Scenario Matrix, and Key-Driver Identification"
category: finance/valuation
description: "Build structured sensitivity tables and a multi-variable scenario matrix across the value-driving assumptions of a DCF or comparable-company valuation — identifying the highest-impact drivers and stress-testing the range against base/bull/bear narratives."
techniques:
  - NE-10
  - NE-11
  - QA-02
  - DS-02
  - RT-02
difficulty: intermediate
tags:
  - sensitivity-analysis
  - scenario-analysis
  - dcf
  - valuation
  - stress-testing
  - key-drivers
updated: "2026-06-08"
related_prompts:
  - domain-finance/valuation/finance_dcf_model_builder.md
  - domain-finance/valuation/finance_terminal_value_sanity_check.md
  - domain-finance/valuation/finance_football_field_synthesizer.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. All outputs must be reviewed by qualified finance professionals before use in any transaction or decision.**

## Objective

Build a comprehensive sensitivity and scenario analysis layer on top of an existing valuation model — constructing one-variable and two-variable sensitivity tables, a multi-variable scenario matrix with internally consistent assumption sets, and a ranked key-driver analysis that quantifies which inputs matter most to the valuation output.

## When to Use

- Completing a DCF model that currently has only a base-case output
- Presenting a valuation to an investment committee, board, or counterparty and anticipating questions about key assumptions
- Stress-testing whether a value conclusion holds across a range of reasonable assumptions
- Identifying which assumptions an opponent or counterparty could most easily challenge
- CFA or valuation training on building rigorous sensitivity frameworks

## Inputs / Context Required

**Base model**
- Base-case valuation output (equity value per share, or enterprise value) from any method (DCF, LBO, DDM)
- The key input variables and their base-case values (e.g., WACC = 9%, g = 2.5%, revenue CAGR = 6%, EBITDA margin = 22%)
- The output variable to stress (equity value per share, IRR, EV/EBITDA implied, etc.)

**Assumptions and ranges**
- For each input variable: minimum (bear), base, and maximum (bull) values to test
- If no ranges provided: the model will propose defensible ranges based on the input type — all proposed ranges must be confirmed before use

**Scenario narratives (optional but recommended)**
- Named scenario labels (e.g., "Management Case," "Street Case," "Downside," "Stress")
- Qualitative descriptions of each scenario's business logic

## Constraints

### Must
- Build at minimum: two 5×5 two-variable sensitivity tables (one for the two highest-impact drivers).
- Build an internally consistent scenario matrix: each scenario's assumptions must be coherent (bull revenue cannot pair with bear margins if they are correlated).
- Identify and rank the top 3 value drivers by computing the % change in output per unit change in each input (partial derivative approach).
- Include at least one adversarial stress scenario that combines the most unfavorable end of each key driver simultaneously.
- All output cells must contain the calculation formula, not hardcoded values.

### Must Not
- Present a sensitivity table that only varies inputs within a trivially narrow range (±10bps on all variables).
- Create scenarios with contradictory assumptions without flagging the inconsistency (e.g., high revenue growth with declining capex intensity in a capital-intensive business).
- Use sensitivity analysis as a substitute for scenario analysis — they serve different purposes (sensitivity: isolate one variable; scenario: coherent multi-variable story).
- Invent the base-case model output; the starting point must be supplied or cross-referenced.

## Instructions

**Step 1 — Identify and rank input variables by materiality**

For each key input variable, compute the impact on the output of a ±10% change (or ±0.5% for rates):

```
Sensitivity Ratio = |ΔOutput / Output| / |ΔInput / Input|
  (elasticity: % change in output per 1% change in input)

OR for rate inputs (WACC, g, margins):
  Impact = |ΔOutput| per 50bps change in the input
```

Rank from highest to lowest sensitivity ratio. The top 2 variables drive the primary sensitivity tables; the top 5 variables enter the scenario matrix.

| Input Variable | Base Value | −10% or −50bps | Output | +10% or +50bps | Output | Sensitivity Rank |
|---|---|---|---|---|---|---|
| WACC | [%] | | [$] | | [$] | 1 |
| Terminal growth (g) | [%] | | [$] | | [$] | 2 |
| EBITDA margin (terminal) | [%] | | [$] | | [$] | 3 |
| Revenue CAGR | [%] | | [$] | | [$] | 4 |
| Exit multiple | [x] | | [$] | | [$] | 5 |

**Step 2 — Build the primary 5×5 sensitivity table (top two drivers)**

Identify the #1 and #2 ranked inputs from Step 1. Build a 5×5 grid:

```
Two-variable sensitivity:
  Rows = Variable 1 (e.g., WACC): base ± 50bps, base ± 100bps = 5 rows
  Columns = Variable 2 (e.g., terminal g): base ± 50bps, base ± 100bps = 5 columns
  Each cell = implied output (equity value / share, or EV)
```

**Table 1: [Variable 1] × [Variable 2] — Equity Value per Share**

| Variable 1 ↓ / Variable 2 → | [V2 − 1%] | [V2 − 0.5%] | [Base V2] | [V2 + 0.5%] | [V2 + 1%] |
|---|---|---|---|---|---|
| [V1 + 1%] | | | | | |
| [V1 + 0.5%] | | | | | |
| [Base V1] | | | **[BASE VALUE]** | | |
| [V1 − 0.5%] | | | | | |
| [V1 − 1%] | | | | | |

Highlight the base-case cell. Optionally shade: above-threshold green, below-threshold red.

**Step 3 — Build the secondary sensitivity table (drivers 3 & 4)**

Repeat Step 2 for the #3 and #4 ranked inputs (e.g., EBITDA margin × revenue growth CAGR).

**Table 2: [Variable 3] × [Variable 4] — Equity Value per Share**

[Same 5×5 structure]

**Step 4 — Build the scenario matrix (multi-variable, internally consistent)**

Define at minimum three scenarios (and ideally four):

| Assumption | Stress (Worst) | Bear | Base | Bull |
|---|---|---|---|---|
| Revenue CAGR | [%] | [%] | [%] | [%] |
| EBITDA margin (terminal) | [%] | [%] | [%] | [%] |
| Capex as % revenue | [%] | [%] | [%] | [%] |
| WACC | [%] | [%] | [%] | [%] |
| Terminal growth (g) | [%] | [%] | [%] | [%] |
| Exit multiple (if applicable) | [x] | [x] | [x] | [x] |
| **Implied EV** | [$] | [$] | [$] | [$] |
| **Implied Equity Value / Share** | [$] | [$] | [$] | [$] |
| **vs. Base (%)** | [%] | [%] | — | [%] |

Internal-consistency checks (state for each scenario):
- Are growth and margin assumptions in the same direction? (A bear scenario with low growth AND high margins is internally inconsistent for most operating businesses — state the exception if applicable.)
- Does the capex assumption align with the growth assumption? (High growth without higher capex intensity is only defensible for asset-light models — state if so.)
- Are WACC and g in the same interest-rate environment? (A bear scenario with high WACC should also have a lower g if it reflects a higher-rate macro environment.)

**Step 5 — Identify the "key assumption" and break-even analysis**

For the #1 ranked input, compute the break-even value (the input level at which the output equals a stated threshold):

```
Break-even analysis example (for WACC as #1 driver):
  At what WACC does equity value / share = current market price?
  Solve: P₀ = f(WACC_break_even)

Break-even WACC = [%]
  Interpretation: If the market is pricing the stock at $P₀, it is implicitly assuming a WACC of X%.
  This is [higher / lower] than the base-case WACC of Y%.
```

Repeat for the #2 and #3 ranked inputs.

**Step 6 — Adversarial stress combination (simultaneous unfavorable)**

Apply the bear-end of the top 3 inputs simultaneously to compute the "floor" scenario:

```
Adversarial Stress Scenario:
  [Variable 1] = bear-end value
  [Variable 2] = bear-end value
  [Variable 3] = bear-end value
  All other inputs = base case

Stress Output: Equity Value / Share = [$]
Stress Discount to Base: [%]
```

Note: The adversarial stress scenario is intentionally pessimistic and may be improbable (requiring all three unfavorable drivers to materialize simultaneously). It tests the downside floor, not the expected outcome.

**Step 7 — Key-driver narrative summary**

Translate the sensitivity analysis into a plain-English summary:

> **Most sensitive input:** [Variable 1]. A ±50bps change produces approximately ±$X per share (±Y% of base value). This means a [small / moderate / large] estimation error in [Variable 1] could change the investment conclusion.
>
> **Scenario range:** The valuation spans $X (bear) to $Y (bull), representing a [Z]% range around the base case of $Z. The bear-case still supports [investment thesis / does not support thesis / conditional support if catalyst materializes].
>
> **Break-even conditions:** The current market price of $P implies [WACC of X%] or [g of Y%] — [these are / are not] within the range of defensible assumptions.

## Output Format

### Key-Driver Ranking Table
[Step 1 table — all 5 inputs with sensitivity ratios]

### Sensitivity Table 1: [V1] × [V2]
[Step 2 — 5×5 grid of equity values]

### Sensitivity Table 2: [V3] × [V4]
[Step 3 — 5×5 grid]

### Scenario Matrix
[Step 4 — bear/base/bull/stress with all assumptions and outputs]

### Break-Even Analysis
[Step 5 — three break-even values with interpretations]

### Adversarial Stress Scenario
[Step 6 — floor case and % discount to base]

### Key-Driver Narrative
[Step 7 — plain-English summary]

## Verification

- [ ] At least two 5×5 sensitivity tables constructed, covering the top 4 ranked drivers.
- [ ] Sensitivity ranking applied before table construction — tables are not built on arbitrary variable selection.
- [ ] Scenario matrix has ≥3 named scenarios with internally consistent assumptions.
- [ ] Internal-consistency checks documented for each scenario (growth/margin/capex coherence).
- [ ] Break-even values computed for the top 3 drivers; interpreted relative to current market price.
- [ ] Adversarial stress scenario present; labeled as a floor test, not an expected outcome.
- [ ] All sensitivity outputs are computed from the base model formula, not hardcoded.
- [ ] Key-driver narrative translates quantitative output into an actionable investment implication.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Sensitivity table with only narrow ±5bps ranges that show trivial variation | Range must reflect the realistic uncertainty in each input; use ±50–100bps for rates, wider for multiples |
| Scenario with internally contradictory assumptions (low growth + high margins for a variable-cost business) | Internal-consistency check in Step 4 is required; contradictions must be resolved or flagged |
| Adversarial stress scenario presented as a "base-case downside" | Stress scenario is a floor test; label it clearly as the simultaneous-worst-case, not the most likely downside |
| Presenting a narrow valuation range from sensitivity tables as evidence of high confidence | A narrow range may reflect too-narrow input ranges; disclose the chosen range width and its basis |
| Using sensitivity analysis to "prove" a base case by surrounding it with outlier scenarios | Scenarios must be plausible and internally consistent; do not engineer the scenario set to make base case look uniquely reasonable |
