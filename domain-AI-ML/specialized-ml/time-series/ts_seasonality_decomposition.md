---
title: "Time-Series Seasonality & Trend Decomposition"
category: AI-ML/specialized-ml/time-series
description: "Decompose a series into trend, seasonality, and residual — choosing the right method and period(s), validating the decomposition, and using each component correctly in modeling without introducing look-ahead leakage."
techniques:
  - ST-02
  - RT-02
  - DS-01
  - QA-12
  - RT-05
difficulty: intermediate
tags:
  - time-series
  - decomposition
  - seasonality
  - trend
  - stationarity
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/specialized-ml/time-series/ts_forecasting_model_selection.md
  - domain-AI-ML/specialized-ml/time-series/ts_feature_engineering.md
  - domain-AI-ML/specialized-ml/time-series/ts_anomaly_detection_design.md
---

# Time-Series Seasonality & Trend Decomposition

**Objective:** Decompose a time series into trend, seasonal, and residual components — selecting the appropriate method (additive vs multiplicative, classical vs STL vs multi-seasonal) and the correct period(s), validating that the decomposition is sound, and prescribing how each component is used in downstream modeling without smuggling future information into present-time features.

**When to Use:**
- Understanding a series' structure before choosing a forecasting model.
- Building seasonally-adjusted features or detecting anomalies on residuals.
- A model keeps mistaking seasonal swings for trend or signal, or struggles with multiple overlapping cycles.

**When NOT to Use:**
- For end-to-end model selection (use `ts_forecasting_model_selection.md`).
- For building the full leak-free feature set (use `ts_feature_engineering.md`).
- For designing the anomaly detector itself (use `ts_anomaly_detection_design.md`).

## Inputs / Context

Provide what you can:
- **Series & frequency** — values, sampling rate, total span (need enough cycles to estimate seasonality).
- **Suspected periods** — daily, weekly, yearly, business cycles; multiple seasonalities?
- **Behavior** — does seasonal amplitude grow with level (multiplicative) or stay constant (additive)? Known holidays/events?
- **Intended use of components** — seasonal adjustment, feature input, anomaly residuals, or interpretation.
- **Irregularities** — missing data, outliers, regime changes that distort decomposition.
- **Constraints** — whether the decomposition feeds an online/streaming pipeline (forces past-only estimation).

## Constraints

**Must:**
- Identify the seasonal period(s) from the data/domain before decomposing, and justify the choice.
- Choose additive vs multiplicative based on whether seasonal amplitude scales with the level.
- If components feed a forecasting/online pipeline, estimate them using past-only data so no future leaks into present features.

**Must Not:**
- Assume one seasonal period when the series has multiple overlapping cycles (e.g., daily + weekly).
- Use a full-series decomposition's seasonal/trend values as features for a point whose forecast must be made before that data exists (leakage).
- Fabricate component magnitudes; reason from the data's structure and mark unknowns.

**Instructions:**

1. **Establish periodicity.** Determine the seasonal period(s) from domain knowledge and evidence (autocorrelation, spectral peaks, period-over-period plots). State each period and whether multiple coexist.

2. **Pick additive vs multiplicative.** If seasonal swings grow with the level, use multiplicative (or log-transform then additive); if constant, additive. Justify from the amplitude-vs-level relationship.

3. **Choose the decomposition method.** Classical moving-average decomposition, STL (robust, handles changing seasonality), or multi-seasonal methods (MSTL/TBATS-style) for several periods. Right-size to the periods present and robustness needed.

4. **Run and validate.** Inspect the residual: it should look like noise (no leftover trend or seasonal pattern, roughly stable variance). Leftover structure in residuals means the period or method is wrong — iterate.

5. **Handle outliers and gaps.** Use a robust method or pre-treat outliers/missing points so a few spikes don't distort the trend/seasonal estimate.

6. **Prescribe correct downstream use.** Specify how components are used: seasonal-adjustment for trend analysis, seasonal indices as features, residuals for anomaly detection — and crucially, for forecasting, estimate components on a rolling/expanding past-only basis to avoid look-ahead leakage.

7. **State the stationarity implication.** Note whether removing trend/seasonality yields a (more) stationary residual suitable for models that assume it, and what remains (e.g., autocorrelation in residuals).

**Output Format:**

A markdown decomposition report:
- **Periodicity** — identified period(s) with the evidence.
- **Additive vs Multiplicative** — decision + justification.
- **Method** — chosen approach and why.
- **Component Summary** — trend / seasonal / residual characterization.
- **Validation** — residual diagnostics (is structure fully removed?).
- **Downstream Use & Leakage Note** — how components are used, and the past-only rule for forecasting.

## Verification

- [ ] Seasonal period(s) are identified with evidence, and multiple seasonalities are considered.
- [ ] Additive vs multiplicative is chosen from the amplitude-vs-level relationship.
- [ ] The residual is validated to confirm trend/seasonality were actually removed.
- [ ] Outliers/missing data handling is addressed.
- [ ] Downstream use specifies a past-only estimation rule when components feed a forecaster.
- [ ] No fabricated component magnitudes.

## False-Positive Prevention

❌ **DON'T:**
- Decompose with a single period when daily *and* weekly cycles both exist — the leftover cycle contaminates trend and residual.
- Use additive decomposition when seasonal amplitude clearly grows with the level (you'll mis-split trend and seasonality).
- Feed a full-series STL trend/seasonal value as a feature for a forecast that must be made before that point — it leaks the future.
- Declare the decomposition "good" without checking the residual for leftover trend or seasonal structure.

✅ **DO:**
- Confirm the period(s) from autocorrelation/spectral evidence and the domain, and use a multi-seasonal method when needed.
- Choose additive/multiplicative (or log-transform) from how amplitude relates to level.
- Validate by inspecting residuals for remaining structure and stable variance.
- For forecasting, estimate trend/seasonal components on a past-only rolling basis so present features never see future data.

## Example Output

```markdown
## Decomposition: Hourly Energy Consumption

### Periodicity
Two strong seasonalities: 24-hour (daily) and 168-hour (weekly), confirmed by ACF peaks at lags 24 and 168 and a spectral peak at 1/24h. Mild yearly trend over the 3-year span.

### Additive vs Multiplicative
Multiplicative: daily swing amplitude scales with overall load (winter swings larger than summer). Applied via log-transform, then additive decomposition.

### Method
MSTL (multi-seasonal STL) to capture both 24h and 168h periods; robust to occasional meter-outage spikes.

### Component Summary
- Trend: slow upward drift (~3%/yr), no abrupt breaks.
- Seasonal: dominant daily double-peak (morning/evening) + weekday>weekend weekly pattern.
- Residual: near-noise after both periods removed; mild residual autocorrelation at lag 1.

### Validation
Residual ACF shows the lag-24 and lag-168 peaks are gone (seasonality removed); variance roughly stable post-log. Remaining lag-1 autocorrelation → an AR(1) residual term in the forecaster.

### Downstream Use & Leakage Note
Seasonal indices used as forecasting features and residuals fed to anomaly detection. For forecasting, decomposition is re-estimated on a rolling past-only window at each origin — never on the full series — so seasonal/trend features at time t use only data through t.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** periodicity → additive/multiplicative → method → validate → downstream use.
- **RT-02 (Multi-Dimensional Analysis Framework):** weighs single vs multi-seasonal, robustness, and downstream fit.
- **DS-01 (Framework Application):** applies the classical/STL/multi-seasonal decomposition framework.
- **QA-12 (False Positives Identification):** single-period and full-series-feature leakage are the key traps.
- **RT-05 (Evidence-Based Reasoning):** period and method choices are grounded in ACF/spectral evidence and residual diagnostics.

**Related Prompts:**
- `ts_forecasting_model_selection.md` — uses this structural understanding to pick a model.
- `ts_feature_engineering.md` — turns seasonal components into leak-free features.
- `ts_anomaly_detection_design.md` — detects anomalies on the residual component.
