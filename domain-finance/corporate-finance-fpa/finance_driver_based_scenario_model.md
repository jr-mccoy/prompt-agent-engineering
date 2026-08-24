---
title: "Driver-Based Scenario Model — Toggle-Driven Operating Model with Probability-Weighted Scenarios"
category: finance/corporate-finance-fpa
description: "Build a driver-based operating model with switchable assumption sets (base/bull/bear), a clean input layer, sensitivity and tornado analysis, and probability-weighted expected outcomes."
techniques:
  - NE-10
  - NE-11
  - DS-02
  - RT-02
  - QA-02
difficulty: advanced
tags:
  - scenario-modeling
  - driver-based
  - fpa
  - sensitivity-analysis
  - tornado
  - probability-weighted
updated: "2026-06-08"
related_prompts:
  - domain-finance/corporate-finance-fpa/finance_three_statement_model_builder.md
  - domain-finance/corporate-finance-fpa/finance_rolling_forecast_designer.md
  - domain-finance/valuation/finance_valuation_sensitivity_scenario.md
  - domain-finance/field_guide.md
---

**Informational only — not financial or investment advice.**

## Objective

Build a driver-based operating model whose outputs are governed by a switchable assumption layer — so a single scenario toggle (base / bull / bear, or named scenarios) repropagates the entire model — plus single-variable sensitivity, a tornado ranking of which drivers move the output most, and a probability-weighted expected outcome. The goal is a model that answers "what moves this, and by how much" without manual rework.

---

## When to Use

- Stress-testing a plan before committing (board approval, fundraise, large investment).
- Quantifying which assumptions the outcome is most sensitive to (where to focus diligence).
- Pricing, capacity, or demand decisions where multiple drivers interact.
- Producing an expected value across discrete scenarios for a go/no-go decision.
- **Do not use** for full statement integration with a balancing balance sheet (use `finance_three_statement_model_builder.md`); this focuses on the driver/scenario/sensitivity layer, typically over an operating P&L or cash measure.

---

## Inputs / Context Required

```
<scenario_model_inputs>
Decision / question the model must answer:
Output metric(s) of interest: [EBITDA | FCF | cash runway | unit margin | other]
Horizon and periodicity:
Currency:

DRIVERS (provide ranges, not just points — low / base / high):
- Each operational driver with: definition, base value, plausible low, plausible high, source
  e.g., revenue growth %, gross margin %, price, volume, churn, CAC, headcount plan, capex %
DRIVER RELATIONSHIPS:
- Any dependencies (e.g., higher growth → higher CAC; volume → variable cost)
SCENARIO DEFINITIONS:
- Named scenarios with the driver settings for each (or use base/bull/bear)
- Subjective probability for each scenario (must sum to 100%); state basis
CONSTRAINTS:
- Hard limits (capacity ceilings, covenant thresholds, minimum cash)
</scenario_model_inputs>
```

---

## Constraints

### Must
- Separate a clean **input/assumption layer** from the **calculation layer** (DS-02); no assumptions buried in formulas.
- Implement a **single scenario switch** that repropagates all driver-dependent outputs (NE-11 — formula-driven, not copy-pasted scenarios).
- Provide each key driver as a **range (low/base/high)**, not a point (NE-10).
- Run **single-variable sensitivity** (hold all else at base; flex one driver across its range) and a **tornado chart** ranking drivers by output impact (RT-02 — multi-dimensional).
- Model **driver interactions** where they exist (e.g., growth↔CAC, volume↔variable cost); do not flex correlated drivers as if independent without noting it.
- Compute a **probability-weighted expected outcome** across discrete scenarios:
  ```
  Expected Value = Σ (Probability_i × Outcome_i)   ;   Σ Probability_i = 1.0
  ```
- Build in an **adversarial stress scenario** (QA-02): combine plausible-but-painful driver settings and test against hard constraints (covenant, cash floor, capacity).
- State probability basis and acknowledge that scenario probabilities are subjective (QA-04).

### Must Not
- Hardcode separate scenario outputs that don't recompute from the switch (they will drift from the logic).
- Flex one driver to an extreme while leaving a correlated driver at base without flagging the inconsistency.
- Present a probability-weighted EV as a forecast — it is an expected value across discrete states, not a likely single outcome.
- Invent driver ranges or probabilities; source or label them as the user's judgment.
- Omit the stress scenario or the hard-constraint check.

---

## Instructions

1. **Define the output and the question.** State the single decision the model serves and the output metric(s). Everything else supports answering it.

2. **Build the input layer (DS-02).** One block of assumption cells with low/base/high per driver, each defined and sourced. Calculations reference these cells only.

3. **Wire the scenario switch (NE-11).**
   ```
   ScenarioSelector ∈ {Base, Bull, Bear, Stress}
   Driver_active = CHOOSE(ScenarioSelector, Base_value, Bull_value, Bear_value, Stress_value)
   All downstream outputs reference Driver_active → one switch repropagates everything.
   ```

4. **Encode driver interactions.** Where drivers are correlated, link them:
   ```
   e.g.  CAC = base_CAC × (1 + α × max(0, growth − base_growth))   (growth pulls CAC up)
         Variable cost = unit_cost × volume                          (scales with volume)
   ```
   Document each relationship and its coefficient source.

5. **Single-variable sensitivity.** For each key driver, hold others at base and flex it low→high; record output range. Build the data table.

6. **Tornado ranking (RT-02).** Sort drivers by the absolute output swing they produce across their low/base/high range; the widest bars are where forecast risk and diligence value concentrate.

7. **Scenario outputs and EV (NE-10).** Compute the output under each named scenario; attach probabilities (summing to 1.0); compute the probability-weighted expected value. Show the distribution, not just the mean.

8. **Adversarial stress (QA-02).** Construct a coherent painful scenario (not just the worst of each driver independently — choose a plausible *combination*). Test outputs against hard constraints (covenant headroom, cash floor, capacity). Report breaches.

9. **Verification (QA-01).** Confirm the switch changes every dependent output. Confirm probabilities sum to 1.0. Confirm the tornado uses consistent low/base/high ranges. State the biggest assumption uncertainty.

---

## Output Format

```
## Driver-Based Scenario Model — [Decision]
Output metric: [EBITDA] | Horizon: [FY1–FY3] | Currency: [USD]
NOTE: figures below are ILLUSTRATIVE.

### Driver Assumption Layer
| Driver        | Low  | Base | High | Source | Linked to |
|---------------|------|------|------|--------|-----------|
| Revenue growth| 4%   | 10%  | 16%  | mgmt   | → CAC     |
| Gross margin  | 52%  | 56%  | 59%  | hist   | —         |
| CAC ($)       | 1,100| 1,000| 950  | finance| ← growth  |
| Churn %       | 12%  | 8%   | 6%   | data   | —         |

### Scenario Outputs & Expected Value
| Scenario | Prob | EBITDA | Note |
|----------|------|--------|------|
| Bear     | 25%  | 12     | growth 4%, churn 12% |
| Base     | 50%  | 22     | plan |
| Bull     | 20%  | 34     | growth 16%, churn 6% |
| Stress   | 5%   | 4      | combined demand + margin shock |
| **EV**   | 100% | **20.3** | Σ(prob × outcome) |

EV is an expected value across states, NOT a point forecast; base case (22) remains the planning anchor.

### Single-Variable Sensitivity (EBITDA, illustrative)
| Driver flexed low→high | EBITDA range | Swing |
|------------------------|--------------|-------|
| Revenue growth         | 14 → 31      | 17    |
| Gross margin           | 17 → 27      | 10    |
| Churn                  | 16 → 25      | 9     |
| CAC                    | 19 → 24      | 5     |

### Tornado (ranked by impact)
Revenue growth ████████████████  (17)
Gross margin   ██████████        (10)
Churn          █████████          (9)
CAC            █████              (5)
→ Diligence and monitoring effort should concentrate on growth and margin.

### Adversarial Stress Test
Combined: growth 4% + margin 52% + churn 12% → EBITDA 4; cash floor breached in FY2.
Hard-constraint check: covenant (Debt/EBITDA < 4.0x) → breached at 5.1x. ⚠
```

---

## Verification

- [ ] Input layer separated from calculations; no buried assumptions.
- [ ] Single scenario switch repropagates all dependent outputs.
- [ ] Each key driver has a low/base/high range, not a point.
- [ ] Driver interactions encoded and documented where correlations exist.
- [ ] Single-variable sensitivity and tornado ranking computed on consistent ranges.
- [ ] Scenario probabilities sum to 1.0; EV computed correctly.
- [ ] EV labeled as expected value, not a point forecast.
- [ ] Adversarial stress scenario tested against hard constraints; breaches reported.

---

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Scenarios hardcoded and drifting from the logic | One scenario switch must repropagate; verify changing the switch moves every dependent output |
| Flexing correlated drivers independently | Encode and document interactions (growth↔CAC, volume↔cost); flag when a flex assumes independence |
| Presenting EV as the likely outcome | EV is the probability-weighted mean across discrete states; keep the base case as the planning anchor |
| "Worst case" = worst of each driver | Build a coherent, plausible combined stress, not an unphysical stack of independent extremes |
| Invented probabilities | State probabilities as subjective judgment with their basis; show sensitivity of EV to the probabilities |
| Ignoring hard constraints | Always test stress outputs against covenant/cash/capacity limits and report breaches |
