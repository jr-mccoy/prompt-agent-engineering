# Time Series

Forecasting, anomaly detection, and the temporal-specific discipline that separates a real result from a leaked one — backtesting design and the leakage audit are the two prompts most worth reading before any modelling.

**9 prompts.** Part of [`domain-AI-ML/`](../README.md) — see the domain README for the lifecycle routing table and the [boundary with adjacent domains](../README.md#boundary-with-adjacent-domains).

## When to enter here

- Forecasting, or detecting anomalies in temporal data.
- Validation results look strong and you suspect temporal leakage.
- The forecast needs intervals, a hierarchy that must reconcile, or handles intermittent demand.

**Not here:**
- The signal is audio → [`../other-modalities/mlmodal_audio_ml_design.md`](../other-modalities/mlmodal_audio_ml_design.md).
- The question is causal effect estimation over time → `domain-science/statistics/science_causal_inference_design.md`.

## Prompts

| Prompt | Use it to |
|---|---|
| [`ts_forecasting_model_selection.md`](ts_forecasting_model_selection.md) | Choose a forecasting approach — classical statistical, ML, or deep learning — matched to the series' structure (trend, seasonality, intermittency), forecast horizon, data volume, and the number of series to forecast. |
| [`ts_feature_engineering.md`](ts_feature_engineering.md) | Engineer time-series features — lags, rolling windows, calendar/event, and exogenous covariates — that capture temporal structure without look-ahead leakage, ensuring every feature uses only information available at prediction time. |
| [`ts_backtesting_design.md`](ts_backtesting_design.md) | Design rolling-origin / walk-forward backtesting for a forecaster that respects time order — choosing window scheme, gap/horizon alignment, and metrics — so evaluation honestly estimates future performance and never leaks the future. |
| [`ts_data_leakage_audit.md`](ts_data_leakage_audit.md) | Audit a time-series pipeline specifically for look-ahead / future leakage — features, splits, transforms, and target construction that let information from the future contaminate the past — with evidence-backed findings and fixes. |
| [`ts_seasonality_decomposition.md`](ts_seasonality_decomposition.md) | Decompose a series into trend, seasonality, and residual — choosing the right method and period(s), validating the decomposition, and using each component correctly in modeling without introducing look-ahead leakage. |
| [`ts_anomaly_detection_design.md`](ts_anomaly_detection_design.md) | Design a time-series anomaly detector — method, seasonality handling, thresholding, and honest evaluation — that separates real anomalies from seasonal/trend variation and noise, without leaking the future into its baseline. |
| [`ts_hierarchical_forecasting.md`](ts_hierarchical_forecasting.md) | Forecast across an aggregation hierarchy (e.g. SKU → category → region → total) and reconcile the levels into a coherent set, choosing among bottom-up, top-down, middle-out, and optimal (MinT) reconciliation based on where the signal lives in the structure. |
| [`ts_probabilistic_forecasting.md`](ts_probabilistic_forecasting.md) | Design forecasts that output a full distribution or set of quantiles rather than a single point, choosing among quantile regression, conformal prediction, and sampling approaches, scoring with proper rules (pinball / CRPS), and validating that intervals are actually calibrated to their nominal coverage. |
| [`ts_intermittent_demand_forecasting.md`](ts_intermittent_demand_forecasting.md) | Forecast series dominated by zeros and sporadic demand (spare parts, slow movers) using methods built for intermittency — Croston, SBA, TSB, and zero-inflated approaches — and evaluate them with metrics that don't break on zeros, avoiding MAPE entirely. |

## Conventions

- **Prefix:** `ts_` — one prefix per subdirectory, so a filename identifies its home.
- **Frontmatter:** the domain's eight fields — `title`, `category` (`AI-ML/specialized-ml/time-series`), `description`, `techniques` (validated against `techniques/MASTER_TECHNIQUE_INDEX.md`), `difficulty`, `tags`, `updated`, `related_prompts`.
- **Structure:** five H2 sections — `Inputs / Context`, `Constraints`, `Verification`, `False-Positive Prevention`, `Example Output` — with `Objective`, `When to Use`, `When NOT to Use`, `Instructions`, `Output Format`, `Techniques Used`, `Related Prompts` as bold labels inside them.
- **No fabrication:** no invented benchmark numbers, accuracy figures, SOTA claims, or dataset statistics. Quantities that would change a decision are marked for measurement or verification.
- **Framework-neutral:** the user names the stack; prompts avoid hardcoding APIs that drift.

## What lives elsewhere

- Conformal prediction for forecast intervals under temporal dependence → [`../../model-evaluation-validation/mleval_conformal_prediction_design.md`](../../model-evaluation-validation/mleval_conformal_prediction_design.md).
- General leakage detection → [`../../data-for-ml/mldata_data_leakage_detector.md`](../../data-for-ml/mldata_data_leakage_detector.md).
