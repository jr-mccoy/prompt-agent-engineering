---
title: "Time-Series Backtesting Design (Rolling-Origin)"
category: AI-ML/specialized-ml/time-series
description: "Design rolling-origin / walk-forward backtesting for a forecaster that respects time order — choosing window scheme, gap/horizon alignment, and metrics — so evaluation honestly estimates future performance and never leaks the future."
techniques:
  - ST-02
  - DS-02
  - QA-12
  - CM-02
  - RT-05
difficulty: advanced
tags:
  - time-series
  - backtesting
  - walk-forward
  - rolling-origin
  - evaluation
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/specialized-ml/time-series/ts_data_leakage_audit.md
  - domain-AI-ML/specialized-ml/time-series/ts_feature_engineering.md
  - domain-AI-ML/specialized-ml/time-series/ts_forecasting_model_selection.md
---

# Time-Series Backtesting Design (Rolling-Origin)

**Objective:** Design a rolling-origin (walk-forward) backtesting protocol for a forecasting model that strictly respects time order — specifying the window scheme (expanding vs sliding), the train/gap/test alignment to the real forecast horizon, the number of folds, and horizon-appropriate metrics — so the offline estimate honestly predicts future performance and no future information leaks into any fold.

**When to Use:**
- Establishing a trustworthy evaluation for any time-series forecaster before deployment.
- Comparing forecasting models or tuning hyperparameters without leaking the future.
- A model's k-fold CV looked great but live performance collapsed (random CV on time data is the likely culprit).

**When NOT to Use:**
- For engineering the features themselves (use `ts_feature_engineering.md`).
- For a forensic leakage hunt across the pipeline (use `ts_data_leakage_audit.md`).
- For choosing the model family (use `ts_forecasting_model_selection.md`).

## Inputs / Context

Provide what you can:
- **Series & frequency** — the target, its sampling frequency, and total span.
- **Forecast horizon & cadence** — how far ahead the model forecasts and how often it's refit/used in production.
- **Data volume** — total observations and per-series history (limits the number of folds).
- **Regime/seasonality** — known structural breaks or strong seasonality that folds must span.
- **Feature pipeline** — whether features/scalers are fit per-fold on training data only.
- **Constraints** — compute budget for refitting per fold, multiple series, latency.

## Constraints

**Must:**
- Every fold must train only on data strictly before its test window — train past, test future, always.
- Align the train/test split to the production forecast horizon (and insert a gap if features need lead time) so the backtest mimics real deployment.
- Refit (or re-derive) all data-dependent transforms (scalers, encoders, feature stats) inside each fold's training window only.

**Must Not:**
- Use random k-fold, shuffled, or stratified splits on time-ordered data — they leak future into past.
- Let any single fold's test period overlap with another fold's training period in a future-leaking way.
- Fabricate fold-level error numbers; reason from the user's setup and mark unknowns.

**Instructions:**

1. **Mirror production in the protocol.** State how the model is actually used (refit cadence, horizon) and design folds to imitate it — the backtest's job is to estimate the live deployment, not an idealized split.

2. **Choose expanding vs sliding window.** Expanding (growing training set) suits stable processes and limited data; sliding (fixed-length window) suits regime change / concept drift. Justify the choice from the series' stationarity.

3. **Align train / gap / test windows.** Set the test window equal to the forecast horizon. Insert a gap between train end and test start if features require lead time (so no feature peeks across the boundary), matching real availability.

4. **Set fold count and spacing.** Pick the number of origins (folds) given total history; ensure folds span seasonal cycles and any known regime breaks so the estimate isn't from one lucky period.

5. **Fit transforms per-fold.** Specify that scalers, encoders, target transforms, and feature statistics are fit on each fold's training data only and applied forward — the most common leak in "time-aware" setups.

6. **Choose horizon-aware metrics.** Select scale-free, horizon-appropriate metrics (MASE, sMAPE, RMSSE) plus interval coverage if intervals matter; report per-horizon-step error, not just an aggregate, and compare against a naive/seasonal-naive baseline.

7. **Aggregate honestly with uncertainty.** Aggregate fold errors with variance across folds (and across series if global), so a single good fold isn't mistaken for a robust result.

**Output Format:**

A markdown backtesting spec:
- **Production Mirror** — refit cadence + horizon the protocol imitates.
- **Window Scheme** — expanding vs sliding, with justification.
- **Fold Layout** — table: Fold | Train range | Gap | Test range.
- **Per-Fold Fitting Rule** — what's refit inside each fold.
- **Metrics** — horizon-aware metrics + baseline + interval coverage.
- **Aggregation** — across folds (and series) with variance reported.

## Verification

- [ ] Every fold trains strictly on data before its test window (train past, test future).
- [ ] No random/shuffled/stratified split is used on time-ordered data.
- [ ] Test window length matches the production forecast horizon; a gap is inserted if features need lead time.
- [ ] Data-dependent transforms are refit inside each fold's training window only.
- [ ] Metrics are horizon-aware, baselined against naive/seasonal-naive, and reported with variance.
- [ ] No fabricated fold-level error numbers.

## False-Positive Prevention

❌ **DON'T:**
- Use `KFold`/shuffled CV on a time series — it trains on the future to predict the past and grossly overstates accuracy.
- Fit a scaler or target transform on the whole series before folding — fold "training" then contains future-derived statistics.
- Use a 1-step test window when production forecasts 14 steps ahead — the backtest won't reflect real horizon error.
- Report one aggregate MAPE across folds and treat it as robust without showing fold-to-fold variance.

✅ **DO:**
- Make every fold imitate real deployment: train on the past, forecast the production horizon forward.
- Refit all transforms and feature statistics within each fold's training window, then apply forward.
- Insert a gap matching feature lead-time so no feature crosses the train/test boundary.
- Report per-horizon and per-fold errors with variance, against a seasonal-naive baseline, before declaring a winner.

## Example Output

```markdown
## Backtesting Spec: Weekly Demand Forecaster (h = 8 weeks)

### Production Mirror
Model refit every 4 weeks; forecasts 8 weeks ahead. Backtest origins spaced 4 weeks apart, each forecasting 8 weeks — mirrors live use.

### Window Scheme
Sliding window (104 weeks). Chosen because demand shows regime shifts after a 2024 catalog change → an expanding window would dilute recent dynamics.

### Fold Layout
| Fold | Train range | Gap | Test range |
|---|---|---|---|
| 1 | W1–W104 | 0 | W105–W112 |
| 2 | W5–W108 | 0 | W109–W116 |
| 3 | W9–W112 | 0 | W113–W120 |
| ... | ... | ... | ... |
(12 folds spanning >2 seasonal cycles incl. the 2024 break)

### Per-Fold Fitting Rule
Within each fold: fit scaler, target log-transform, and rolling-feature statistics on the train range only; apply to test. Nothing fit on global data.

### Metrics
Primary: RMSSE and MASE (scale-free, baselined to seasonal-naive). Per-horizon-step error (week 1..8) reported separately. Interval coverage at 80%/95% checked. Baseline: seasonal-naive (same week last year).

### Aggregation
Mean ± std of RMSSE across the 12 folds; flag any fold where the model loses to seasonal-naive. Decision uses the distribution, not a single number.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** mirror → window scheme → fold layout → per-fold fit → metrics → aggregation.
- **DS-02 (Metric Specification):** horizon-aware, baselined metrics with interval coverage.
- **QA-12 (False Positives Identification):** random CV and global-fit transforms are the canonical false-positive traps.
- **CM-02 (Constraint Specification):** the forecast horizon and refit cadence govern fold geometry.
- **RT-05 (Evidence-Based Reasoning):** the window/gap choices are justified from stationarity and feature lead-time.

**Related Prompts:**
- `ts_data_leakage_audit.md` — confirm the protocol and features didn't leak the future.
- `ts_feature_engineering.md` — features must be computed within these folds' training windows.
- `ts_forecasting_model_selection.md` — the model comparison this backtest adjudicates.
