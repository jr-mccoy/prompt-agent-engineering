---
title: "ML Cost Budgeting & Forecasting"
category: AI-ML/mlops-infrastructure
description: "Build a forward-looking ML cost model — unit economics ($/prediction, $/training run, $/1k tokens), volume drivers, budget envelopes, scenario forecasts under growth and retraining, and spend guardrails (budget alerts, anomaly detection, cost-per-unit regression gates) — using only stated unit costs and volumes."
techniques:
  - ST-02
  - DS-02
  - RT-05
  - DS-06
  - CM-02
difficulty: advanced
tags:
  - cost-forecasting
  - unit-economics
  - budgeting
  - guardrails
  - finops
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/mlops-infrastructure/mlops_cost_attribution_showback.md
  - domain-AI-ML/mlops-infrastructure/mlops_infra_cost_optimization.md
  - domain-AI-ML/ai-product-leadership/aipm_roi_business_case.md
---

# ML Cost Budgeting & Forecasting

**Objective:** Produce a forward-looking ML cost model grounded in unit economics and volume drivers — project spend under growth and retraining scenarios, set budget envelopes, and define guardrails (alerts, anomaly detection, cost-per-unit regression gates) so cost is governed before, not after, the bill lands.

**When to Use:**
- You must forecast ML spend for a quarter/year or justify a budget envelope for a model or platform.
- You need unit economics ($/prediction, $/training run, $/1k tokens) to reason about scaling.
- Leadership wants guardrails that catch cost regressions before they compound.

**When NOT to Use:**
- You're allocating *existing* spend to teams/models — use `mlops_cost_attribution_showback.md`.
- You're reducing spend through architecture/rightsizing — use `mlops_infra_cost_optimization.md`.

## Inputs / Context

- **Unit costs** — observed or quoted $/GPU-hour, $/1k tokens, storage $/GB-mo, data-pipeline costs.
- **Current volumes** — predictions/day, training runs/period, token throughput, data volume.
- **Growth drivers** — expected traffic growth, new models, retraining cadence changes.
- **Budget context** — the envelope to fit within or to justify.
- **Scenario set** — base, growth, aggressive-retraining, and any worst-case to model.
- **Guardrail appetite** — what spend deviation should alert, throttle, or block a deploy.

## Constraints

**Must:**
- Define unit economics explicitly: $/prediction, $/training run, $/1k tokens (whichever apply), each derived from stated unit costs.
- Tie cost to volume drivers so the forecast moves with usage, not a flat guess.
- Model at least base / growth / aggressive scenarios with the assumptions visible per scenario.
- Set budget envelopes and the guardrails that defend them (budget alert threshold, spend anomaly detection, cost-per-unit regression gate).
- Show the arithmetic so the forecast is auditable and reproducible.

**Must Not:**
- Invent unit prices, token volumes, GPU-hour rates, or growth figures — every input must be supplied or marked `UNKNOWN — confirm`; do not fill gaps with "typical" numbers.
- Present a single point forecast as certainty; carry the scenario range and its assumptions.

**Instructions:**

1. **Establish unit economics.** From stated unit costs and current volume, compute $/prediction, $/training run, and/or $/1k tokens. Show the formula.
2. **Identify volume drivers.** Map each cost line to the driver that scales it (requests, runs, tokens, GB).
3. **Set scenario assumptions.** Define base/growth/aggressive with explicit per-scenario growth rates and retraining cadence.
4. **Project spend.** Apply unit economics × projected volume per scenario across the forecast horizon; show monthly/quarterly rollup.
5. **Set budget envelopes.** State the target envelope and which scenarios fit/breach it.
6. **Define guardrails.** Budget alert thresholds, spend anomaly detection, and a cost-per-unit regression gate in CI/deploy.
7. **Stress-test.** Identify which assumption the forecast is most sensitive to and the worst-case breach.

**Output Format:**

A markdown cost model: Unit Economics (formulas + values) · Volume Drivers · Scenario Assumptions (table) · Spend Forecast (table by period × scenario) · Budget Envelopes · Guardrails · Sensitivity / Worst Case. Unknowns marked.

## Verification

- [ ] Unit economics are derived with visible formulas from stated unit costs.
- [ ] Each cost line is tied to a volume driver.
- [ ] At least base/growth/aggressive scenarios are modeled with explicit assumptions.
- [ ] Spend forecast rolls up by period and scenario and reconciles to the unit math.
- [ ] Budget envelopes and guardrails (alert, anomaly, regression gate) are defined.
- [ ] No price/volume/growth figure was invented; gaps are UNKNOWN.

## False-Positive Prevention

❌ **DON'T:**
- Forecast on average cost-per-unit when usage is bursty — a flat $/prediction hides the training spikes and retraining runs that dominate the monthly bill, so the envelope is set too low.
- Plug in a "typical $/1k tokens" or "standard GPU rate" because the user didn't supply one — a fabricated unit price propagates through every scenario and makes the whole forecast fiction.
- Forget retraining and data-pipeline cost — modeling only inference makes the forecast look cheap, then the first retraining cycle blows the budget.
- Set a budget alert at the forecast total — alerting only when you've already spent the whole budget gives no time to react; the regression should fire on cost-per-unit drift, not just the cumulative total.

✅ **DO:**
- Separate steady-state inference cost from spiky training/retraining cost and model each driver.
- Use only supplied unit prices/volumes; mark every missing input UNKNOWN and exclude it from precise totals.
- Include training, serving, storage, and data-pipeline lines so the forecast is whole.
- Add a cost-per-unit regression gate so a unit-economics drift (e.g., $/prediction creeping up) trips before cumulative spend does.

## Example Output

```markdown
## ML Cost Forecast — fraud-scoring (H2)

### Unit Economics (from stated unit costs)
- $/prediction = (endpoint $/hr ÷ predictions/hr). Value: UNKNOWN — confirm endpoint rate.
- $/training run = GPU-hrs/run × $/GPU-hr. e.g. 12 GPU-hrs × $Z = $T (Z from quote).
- $/1k tokens (n/a for this model).

### Volume Drivers
- Inference cost ← predictions/day. Training cost ← runs/month × retraining cadence. Storage ← feature GB held.

### Scenario Assumptions
| scenario | traffic growth | retraining cadence |
|---|---|---|
| base | +0% | monthly |
| growth | +30% QoQ | bi-weekly |
| aggressive | +60% QoQ | weekly |

### Spend Forecast (by month × scenario)
| month | base | growth | aggressive |
|---|---|---|---|
| Jul | $… | $… | $… |
(values = unit economics × projected volume; train spikes shown separately)

### Budget Envelopes
- Envelope: $E/quarter. Base fits; aggressive breaches by month 2.

### Guardrails
- Budget alert at 70% of envelope. Spend anomaly detection on daily spend z-score.
- Cost-per-unit regression gate: block deploy if $/prediction rises >15% vs trailing baseline. Baseline window: UNKNOWN — confirm.

### Sensitivity / Worst Case
- Most sensitive to retraining cadence; weekly retraining is the dominant cost lever.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** Ordered build from unit economics → drivers → scenarios → forecast → guardrails.
- **DS-02 (Metric Specification):** Defines unit economics and guardrail thresholds as explicit metrics.
- **RT-05 (Evidence-Based Reasoning):** Every figure traces to supplied unit costs/volumes with visible math.
- **DS-06 (Prioritization & Severity):** Sensitivity analysis ranks which assumption most drives spend.
- **CM-02 (Constraint Specification):** Encodes scenario discipline and the no-fabrication clause.

**Related Prompts:**
- `mlops_cost_attribution_showback.md` — supplies the historical per-model cost basis the forecast extrapolates.
- `mlops_infra_cost_optimization.md` — act on the cost levers the sensitivity analysis surfaces.
- `aipm_roi_business_case.md` — pair the forecast with revenue/benefit for the ROI case.
