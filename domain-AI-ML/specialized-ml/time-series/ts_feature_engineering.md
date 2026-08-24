---
title: "Time-Series Feature Engineering (Leak-Free)"
category: AI-ML/specialized-ml/time-series
description: "Engineer time-series features — lags, rolling windows, calendar/event, and exogenous covariates — that capture temporal structure without look-ahead leakage, ensuring every feature uses only information available at prediction time."
techniques:
  - ST-02
  - RT-05
  - QA-12
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - time-series
  - feature-engineering
  - lag-features
  - look-ahead-leakage
  - rolling-windows
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/specialized-ml/time-series/ts_data_leakage_audit.md
  - domain-AI-ML/specialized-ml/time-series/ts_backtesting_design.md
  - domain-AI-ML/specialized-ml/time-series/ts_forecasting_model_selection.md
---

# Time-Series Feature Engineering (Leak-Free)

**Objective:** Design a time-series feature set — lag features, rolling-window aggregates, calendar/event features, and exogenous covariates — that captures the series' temporal structure for forecasting while guaranteeing every feature uses only information available at or before the prediction time, eliminating look-ahead (future) leakage at the source.

**When to Use:**
- Building features for an ML/regression forecaster (lags, rolling stats, calendar effects).
- A model with strong features scores great in cross-validation but fails on truly future data (suspected leakage).
- Standardizing a feature pipeline so offline-engineered features match what's computable online.

**When NOT to Use:**
- For choosing the model family (use `ts_forecasting_model_selection.md`).
- For the evaluation split mechanics (use `ts_backtesting_design.md`).
- For a forensic leakage audit of an existing pipeline (use `ts_data_leakage_audit.md`).

## Inputs / Context

Provide what you can:
- **Target & horizon** — what's predicted and how far ahead (the forecast origin and horizon define the prediction-time boundary).
- **Raw signals** — the target series, related series, and exogenous variables, with their observation timing.
- **Covariate availability** — which covariates are known in the future (holidays, scheduled promos) vs only known historically (weather actuals).
- **Frequency & gaps** — sampling frequency, missing timestamps, irregular spacing.
- **Multiple series** — whether features must be computed per-group (per SKU/sensor) to avoid cross-series bleed.
- **Constraints** — online computability, retraining cadence, latency.

## Constraints

**Must:**
- Anchor every feature to the prediction-time boundary: at forecast origin t for horizon h, a feature may use only data observed at or before t (and future-known covariates only where genuinely known).
- Compute rolling/lag features with a shift so the current target value (and any future value) never enters its own feature.
- Compute features per-group for multi-series data so one series' values never leak into another's.

**Must Not:**
- Use centered rolling windows, full-series statistics, or global scalers fit on all time (these see the future).
- Use a covariate's actual future value when only its historical value is known at prediction time.
- Invent covariate timing the user didn't provide; if availability is unknown, mark it as an open question, not a usable feature.

**Instructions:**

1. **Fix the prediction-time boundary.** State the forecast origin and horizon precisely. Everything observed after the origin is off-limits as an input — this single rule governs the whole feature set.

2. **Design lag features.** Choose lags that reflect the seasonality and autocorrelation (e.g., lag-1, lag-7, lag-364 for daily data). Ensure each lag is strictly in the past relative to the origin and respects the horizon (a lag must be available h steps ahead at scoring time).

3. **Design rolling-window features safely.** Use trailing (not centered) windows, and shift so the window ends before the origin. Specify min-periods handling and how warm-up rows are treated, never letting the current/future target contaminate the aggregate.

4. **Engineer calendar and event features.** Day-of-week, month, holiday flags, promotion windows — these are typically future-known and safe, but verify each is actually known at the origin for the full horizon.

5. **Handle exogenous covariates by availability.** Split covariates into future-known (usable at their future value) and historical-only (must be lagged like the target). Never feed a historical-only covariate's future actual.

6. **Enforce per-group computation and alignment.** For multiple series, group features by entity so no cross-series leakage occurs; align all features to the same time index and document missing-value treatment.

7. **Specify train/serve parity.** Define a single transform path so a feature computed in training equals the feature computed online at the same origin — preventing train/serve skew that mimics or masks leakage.

**Output Format:**

A markdown feature specification:
- **Prediction-Time Boundary** — origin, horizon, and the resulting cutoff rule.
- **Feature Catalog** — table: Feature | Type (lag/rolling/calendar/exog) | Window/Lag | Available at origin? | Notes.
- **Leakage Safeguards** — the shift/trailing/per-group rules applied.
- **Covariate Availability Map** — future-known vs historical-only handling.
- **Train/Serve Parity** — the shared transform path.
- **Open Questions** — covariates whose timing must be confirmed.

## Verification

- [ ] The prediction-time boundary (origin + horizon) is stated and used as the cutoff for every feature.
- [ ] All rolling features are trailing/shifted; no centered windows or full-series statistics.
- [ ] Lags are valid for the horizon (computable h steps ahead at scoring time).
- [ ] Covariates are split into future-known vs historical-only with correct handling each.
- [ ] Multi-series features are computed per-group with no cross-series bleed.
- [ ] A single train/serve transform path is specified; unknown covariate timing is flagged, not assumed.

## False-Positive Prevention

❌ **DON'T:**
- Use a centered rolling mean or `rolling().mean()` without a shift — it includes the current (and sometimes future) value, leaking the target.
- Fit a scaler/encoder on the full series before the time split — its statistics encode the future.
- Feed tomorrow's weather *actual* as a feature when only the historical weather is known at the forecast origin.
- Compute a "global average" feature across all timestamps and call it a static feature — it's computed using future rows.

✅ **DO:**
- Tie every feature to the origin and shift trailing windows so they end strictly before it.
- Lag historical-only covariates exactly as you lag the target; reserve actual-future values for genuinely future-known covariates.
- Compute and fit all statistics within the training window only, then apply forward (matching backtesting folds).
- Mark any covariate with unclear availability as an open question and exclude it until confirmed.

## Example Output

```markdown
## Feature Spec: Daily Store Sales Forecast (h = 14 days)

### Prediction-Time Boundary
Forecast origin t = end of day D. Horizon h = 14. Cutoff rule: features may use data observed through D only; future-known covariates allowed at their scheduled future value.

### Feature Catalog
| Feature | Type | Window/Lag | Available at origin? | Notes |
|---|---|---|---|---|
| sales_lag_7, lag_14 | lag | 7, 14 | Yes | valid for 14-day horizon |
| sales_roll_mean_28 | rolling | trailing 28, shifted | Yes | ends at D, excludes D+1.. |
| sales_roll_std_28 | rolling | trailing 28, shifted | Yes | trailing only |
| dow, month | calendar | — | Yes | future-known |
| holiday_flag | event | — | Yes | scheduled, known for horizon |
| promo_planned | exog (future-known) | future value | Yes | promo calendar is fixed ahead |
| weather_actual | exog (historical-only) | lagged 1+ | Lagged only | future actual NOT used |

### Leakage Safeguards
All rolling features use `.shift(1)` after a trailing window (end < origin). No centered windows. No full-series statistics. Scalers fit on training fold only.

### Covariate Availability Map
Future-known: promo calendar, holidays, day-of-week → used at future value.
Historical-only: weather, foot-traffic actuals → used only as lags.

### Train/Serve Parity
One feature-transform module called by both the training job and the online scorer at the same origin → identical values.

### Open Questions
- Is the competitor-pricing feed available before the forecast origin, or does it arrive late? If late, lag it; otherwise confirm timing.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** boundary → lags → rolling → calendar → covariates → parity.
- **RT-05 (Evidence-Based Reasoning):** each feature's safety is justified against its observation timing.
- **QA-12 (False Positives Identification):** centered windows / future actuals are the classic leakage false positives.
- **CM-02 (Constraint Specification):** the prediction-time boundary is the governing constraint.
- **DS-02 (Metric Specification):** lags/windows chosen against seasonality and autocorrelation structure.

**Related Prompts:**
- `ts_data_leakage_audit.md` — forensic check that these features didn't introduce look-ahead leakage.
- `ts_backtesting_design.md` — the rolling-origin folds these features must be computed within.
- `ts_forecasting_model_selection.md` — the model that consumes these features.
