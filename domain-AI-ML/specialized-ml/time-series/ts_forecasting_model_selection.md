---
title: "Time-Series Forecasting Model Selection"
category: AI-ML/specialized-ml/time-series
description: "Choose a forecasting approach — classical statistical, ML, or deep learning — matched to the series' structure (trend, seasonality, intermittency), forecast horizon, data volume, and the number of series to forecast."
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
  - model-selection
  - seasonality
  - horizon
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/specialized-ml/time-series/ts_feature_engineering.md
  - domain-AI-ML/specialized-ml/time-series/ts_backtesting_design.md
  - domain-AI-ML/specialized-ml/time-series/ts_seasonality_decomposition.md
---

# Time-Series Forecasting Model Selection

**Objective:** Recommend a forecasting approach — classical (ARIMA/ETS/Theta), machine-learning (gradient-boosted trees on engineered features), or deep learning (RNN/Temporal-CNN/transformer/global models) — justified against the series' structure (trend, seasonality, intermittency, exogenous drivers), the forecast horizon, the available history, and the number of series to forecast, with a simple baseline established first.

**When to Use:**
- Starting a forecasting project and choosing the model family.
- A current forecaster underperforms a naive baseline and you're reconsidering the approach.
- Deciding between per-series classical models and a single global ML/DL model across many series.

**When NOT to Use:**
- For engineering the input features (use `ts_feature_engineering.md`).
- For evaluation/backtesting design (use `ts_backtesting_design.md`).
- For anomaly detection rather than forecasting (use `ts_anomaly_detection_design.md`).

## Inputs / Context

Provide what you can:
- **Series structure** — frequency (hourly/daily/weekly), trend, seasonality (single/multiple periods), intermittency/zeros, regime changes.
- **History length** — how many observations per series; whether it's long enough for the candidate models.
- **Number of series** — one, a few, or thousands (drives per-series vs global modeling).
- **Horizon** — how far ahead, and whether single-step or multi-step.
- **Exogenous variables** — known-future covariates (holidays, promotions, weather forecasts) vs only-historical.
- **Constraints** — accuracy target, need for prediction intervals, retraining cadence, latency, interpretability.

## Constraints

**Must:**
- Establish a naive baseline (last value, seasonal-naive, drift) first — every model must beat it to justify itself.
- Tie the family choice to series structure, history length, series count, and horizon — not to model fashion.
- State whether prediction intervals (uncertainty) are required and whether the chosen approach provides them honestly.

**Must Not:**
- Recommend deep learning for a handful of short series — it will rarely beat ETS/ARIMA and risks overfitting.
- Fabricate accuracy numbers or cite benchmark results from memory; reason from the user's data and mark unknowns.
- Ignore the look-ahead/backtesting requirement; model choice and honest evaluation are inseparable.

**Instructions:**

1. **Characterize the series.** Classify trend, seasonality (one or multiple periods), intermittency/zero-inflation, regime shifts, and noise level. This structure is the primary driver of the family choice.

2. **Establish the baseline.** Define naive / seasonal-naive / drift baselines. State that the chosen model must beat these in backtesting; many "model failures" are simply losing to seasonal-naive.

3. **Assess data volume and series count.** Short history per series favors classical; many series with shared structure favor a single global ML/DL model; abundant per-series history can support per-series ML/DL.

4. **Match horizon and covariates.** Long multi-step horizons and known-future covariates (promotions, holidays) favor ML/DL or regression-with-features; short horizons on a clean seasonal series may be best served by ETS/ARIMA.

5. **Shortlist families and trade them off.** Compare classical vs ML vs DL on accuracy potential, data hunger, interpretability, interval quality, and operational cost. Right-size: complexity must earn its place.

6. **Decide intervals and uncertainty.** Specify how prediction intervals are produced (analytic for classical, quantile/conformal for ML, sampling for DL) and whether they'll be honest under the backtesting protocol.

7. **Recommend and stage.** Give the recommendation with rationale, a fallback, and a staged plan: baseline → chosen family → complexity only if backtesting shows a real, interval-honest gain.

**Output Format:**

A markdown recommendation:
- **Series Characterization** — structure, history, count, horizon in a short table.
- **Baseline Definition** — the naive/seasonal-naive benchmarks to beat.
- **Family Trade-off** — table: Family | Fit to Structure | Data Need | Intervals | Cost | Verdict.
- **Recommendation** — chosen approach + fallback, tied to inputs.
- **Uncertainty Plan** — how prediction intervals are produced.
- **Staged Plan** — baseline → model → complexity gate, evaluated by backtesting.

## Verification

- [ ] A naive/seasonal-naive baseline is defined and named as the bar to beat.
- [ ] The family choice cites series structure, history length, series count, and horizon.
- [ ] Deep learning is not recommended for few/short series without explicit justification.
- [ ] Prediction-interval generation is specified if uncertainty is required.
- [ ] The plan references honest backtesting (no random split) for the model comparison.
- [ ] No fabricated accuracy or benchmark numbers.

## False-Positive Prevention

❌ **DON'T:**
- Reach for an LSTM/transformer on 200 daily observations across 3 series — classical models almost always win there.
- Skip the seasonal-naive baseline; a "good" MAPE can still be worse than simply repeating last season.
- Assume more model complexity means better forecasts — it usually means more variance and worse intervals on small data.
- Pick a family without checking whether it produces honest prediction intervals when the business needs them.

✅ **DO:**
- Let the series' structure (trend/seasonality/intermittency) and data volume drive the family, then beat the baseline.
- Prefer a global ML model when you have many related series with shared patterns and limited per-series history.
- Right-size complexity and only graduate to DL when backtesting shows a real, interval-honest improvement.
- Treat model selection and look-ahead-safe backtesting as one decision, not two.

## Example Output

```markdown
## Forecasting Approach: Retail SKU Demand (12k SKUs, daily)

### Series Characterization
| Property | Value |
|---|---|
| Frequency | Daily |
| Seasonality | Weekly + yearly (holidays) |
| Intermittency | ~25% of SKUs have sparse/zero days |
| History | 2–3 years for most; <6 months for new SKUs |
| Series count | ~12,000 |
| Horizon | 28-day multi-step; intervals required |

### Baseline Definition
Seasonal-naive (same weekday last week) + a holiday-adjusted variant. Any model must beat these in rolling-origin backtesting.

### Family Trade-off
| Family | Fit to Structure | Data Need | Intervals | Cost | Verdict |
|---|---|---|---|---|---|
| ETS/ARIMA per SKU | Good for stable seasonal | Per-series history | Analytic | High (12k fits) | Fallback for stable SKUs |
| Global GBM on features | Handles many series + covariates | Pools across SKUs | Quantile/conformal | Moderate | Recommended |
| Global DL (e.g., temporal) | Strong with scale + covariates | Lots of data | Sampling/quantile | High | Stage 3 only if GBM gains plateau |

### Recommendation
Global gradient-boosted model over engineered lag/calendar/promo features across all SKUs (handles intermittency, new SKUs via shared structure, known-future promos). Fallback: seasonal-naive for ultra-sparse SKUs.

### Uncertainty Plan
Quantile regression (or conformal calibration) for 28-day interval bands, validated for coverage in backtesting.

### Staged Plan
1. Seasonal-naive baseline.
2. Global GBM — gate: beats seasonal-naive on rolling-origin MASE with calibrated intervals.
3. Global DL — only if GBM gains plateau and data volume justifies it.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** characterize → baseline → volume → horizon → trade-off → recommend.
- **RT-02 (Multi-Dimensional Analysis Framework):** weighs fit, data need, intervals, and cost across families.
- **DS-01 (Framework Application):** applies the classical/ML/DL forecasting taxonomy and global-vs-local framing.
- **CM-02 (Constraint Specification):** horizon, series count, and interval requirements constrain the choice.
- **DS-06 (Prioritization & Severity Guidance):** staged plan earns complexity by measured gain.

**Related Prompts:**
- `ts_feature_engineering.md` — build the lag/calendar features the ML approach needs (leak-free).
- `ts_backtesting_design.md` — the rolling-origin protocol that decides the model comparison.
- `ts_seasonality_decomposition.md` — characterize the seasonal structure that drives the choice.
