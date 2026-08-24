---
title: "Intermittent & Sparse Demand Forecasting"
category: AI-ML/specialized-ml/time-series
description: "Forecast series dominated by zeros and sporadic demand (spare parts, slow movers) using methods built for intermittency — Croston, SBA, TSB, and zero-inflated approaches — and evaluate them with metrics that don't break on zeros, avoiding MAPE entirely."
techniques:
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - DS-06
difficulty: advanced
tags:
  - time-series
  - forecasting
  - intermittent-demand
  - sparse
  - croston
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/specialized-ml/time-series/ts_forecasting_model_selection.md
  - domain-AI-ML/specialized-ml/time-series/ts_backtesting_design.md
  - domain-AI-ML/specialized-ml/time-series/ts_hierarchical_forecasting.md
---

# Intermittent & Sparse Demand Forecasting

**Objective:** Recommend how to forecast series with many zeros and irregular, sporadic demand — where standard models and metrics quietly fail. The recommendation must classify the intermittency pattern, choose a method designed for it (Croston, SBA, TSB, or zero-inflated/count approaches), split the problem into demand-occurrence vs demand-size, and select metrics that remain defined on zeros (never MAPE), with the empirical winner deferred to rolling-origin backtesting.

**When to Use:**
- Many periods have zero demand (spare parts, slow-moving SKUs, low-volume items).
- Demand arrives in sporadic bursts rather than a smooth signal.
- Standard models predict near-constant small values or all-zeros and your metrics look "fine" but decisions suffer.

**When NOT to Use:**
- Demand is continuous and rarely zero — use `ts_forecasting_model_selection.md`.
- You have a hierarchy and want coherence across levels — pair with `ts_hierarchical_forecasting.md` after fixing the leaf method here.
- You only need distributional intervals on a non-sparse series — see `ts_probabilistic_forecasting.md`.

## Inputs / Context

Provide what you can:
- **Zero fraction & gap structure** — share of zero periods and typical gaps between non-zero demands.
- **Demand-size distribution** — when demand occurs, how variable is its magnitude.
- **Classification signals** — average inter-demand interval and coefficient of variation of sizes (smooth / erratic / intermittent / lumpy).
- **Decision use** — reorder point, stocking level, service-level target.
- **Obsolescence risk** — items that may stop selling (TSB handles this).
- **Data volume & history length**, frequency, and horizon.
- **Service-level / cost asymmetry** between stockout and overstock.

## Constraints

**Must:**
- Establish a naive baseline appropriate to sparse data (e.g. seasonal-naive or a simple moving-average rate) and require any method to beat it.
- Split the problem into demand-occurrence (when) and demand-size (how much) and address both.
- Use metrics that are defined on zeros — MASE / scaled error, or count-appropriate metrics — and explicitly exclude MAPE/sMAPE.
- Defer the final method choice to rolling-origin backtesting.

**Must Not:**
- Fabricate accuracy numbers or quote method win rates from memory; reason from the user's data and mark unknowns as "measure on your data."
- Use MAPE/sMAPE on zero-heavy series (undefined/exploding on zero actuals).
- Reward a model for predicting all-zeros via an error metric that a constant-zero forecast can win.
- Ignore the occurrence-vs-size split and treat the series as ordinary continuous data.

**Instructions:**

1. **Classify the intermittency.** Use average inter-demand interval and the coefficient of variation of non-zero sizes to place the series (smooth / erratic / intermittent / lumpy). The class drives method choice.
2. **Set a sparse-aware baseline.** Use a simple demand-rate estimate (e.g. mean over recent periods or seasonal-naive) as the bar; confirm it isn't trivially beaten by a constant-zero forecast under the chosen metric.
3. **List candidate methods.** Croston (separately smooth inter-arrival interval and size), SBA (bias-corrected Croston), TSB (handles obsolescence/declining demand via a probability term), and zero-inflated / count (Poisson/negative-binomial, hurdle) models.
4. **Match method to class and risk.** SBA over Croston when bias matters; TSB when items can go obsolete; zero-inflated/count models when you want an explicit occurrence probability and size distribution for downstream service-level math.
5. **Model occurrence and size separately.** Make the demand-occurrence (probability of a non-zero period) and demand-size (magnitude given non-zero) split explicit, since stocking decisions depend on both.
6. **Choose metrics that survive zeros.** Recommend MASE/scaled error and count-appropriate scores; for stocking, evaluate against the service-level/fill-rate decision, not point error alone. Explicitly forbid MAPE.
7. **Decide and document.** Recommend a primary method + fallback, the metric set, and how the occurrence/size split feeds the reorder decision. Mark all empirical claims as to-be-measured.

**Output Format:**

A markdown recommendation:
- **Intermittency Classification** — class + the interval/CV signals behind it.
- **Baseline** — the sparse-aware naive and why a constant-zero forecast can't win the metric.
- **Candidate Methods** — table of Croston / SBA / TSB / zero-inflated with fit notes.
- **Recommendation** — primary method + fallback.
- **Occurrence vs Size Plan** — how each is modeled and combined.
- **Metrics & Decision Link** — zero-safe metrics + tie to service level.
- **Open Questions / Data to Gather** — unknowns before committing.

## Verification

- [ ] Intermittency is classified using inter-demand interval and size variability.
- [ ] A sparse-aware naive baseline is set and isn't trivially beaten by all-zeros under the metric.
- [ ] Demand-occurrence and demand-size are addressed separately.
- [ ] Metrics are zero-safe (MASE/scaled or count-appropriate); MAPE/sMAPE explicitly excluded.
- [ ] No fabricated accuracy or method-win-rate numbers — empirical claims marked "measure on your data."

## False-Positive Prevention

❌ **DON'T:**
- Use **MAPE on zero-heavy series** — it is undefined or explodes whenever the actual is zero, producing meaningless or infinite errors.
- Trust a low RMSE that an all-zeros forecast achieves; on sparse data a constant-zero model can look "accurate" while being useless for stocking.
- Treat the series as ordinary continuous data and skip the occurrence-vs-size split.
- Pick a method by intermittency class alone without backtesting on the actual data.

✅ **DO:**
- Use zero-safe metrics (MASE/scaled error, count-appropriate scores) and evaluate against the service-level decision.
- Model demand occurrence and demand size separately, since reorder points depend on both.
- Choose TSB when obsolescence/declining demand is a risk, and SBA over plain Croston for bias correction.
- Confirm the baseline can't be won by predicting all-zeros before declaring any method better.

## Example Output

```markdown
## Intermittency Classification
- Avg inter-demand interval ≈ 4.2 periods; size CV² ≈ 0.7 → "intermittent."
- Zero fraction ≈ 76%.

### Baseline
- Recent-mean demand rate; checked that all-zeros forecast does NOT win under MASE.

### Candidate Methods
| Method | Fit |
|--------|-----|
| Croston | classic, but biased |
| SBA | bias-corrected Croston — preferred default |
| TSB | use if items may go obsolete |
| Zero-inflated / NB | explicit occurrence + size for service-level math |

### Recommendation
- Primary: SBA. Fallback: TSB (obsolescence risk on long-tail SKUs).

### Occurrence vs Size Plan
- Occurrence: probability of non-zero period. Size: NB-distributed given non-zero.
- Combine for reorder point at target fill rate.

### Metrics & Decision Link
- MASE (zero-safe); MAPE excluded.
- Evaluate fill rate / stockout against service target. Numbers TBD — measure on your data.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** orders classify → baseline → method match → occurrence/size split → metrics.
- **RT-02 (Multi-Dimensional Analysis Framework):** frames the model as an intermittent-demand specialist who knows standard metrics break on zeros.
- **DS-01 (Framework Application):** the candidate-methods table forces an explicit, criteria-based method choice.
- **CM-02 (Constraint Specification):** Must/Must Not block pins zero-safe metrics, the occurrence/size split, and anti-fabrication as hard constraints.
- **DS-06 (Prioritization & Severity Guidance):** routes the final method pick to rolling-origin backtesting on the user's data.

**Related Prompts:**
- `ts_forecasting_model_selection.md` — the general selector for non-sparse series; this prompt is the sparse-data specialization.
- `ts_backtesting_design.md` — designs the rolling-origin evaluation with zero-safe metrics.
- `ts_hierarchical_forecasting.md` — reconciles sparse leaf forecasts up an aggregation hierarchy after the leaf method is fixed.
