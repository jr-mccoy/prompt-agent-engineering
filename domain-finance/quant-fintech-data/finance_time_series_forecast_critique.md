---
title: "Time-Series Forecast Critique — Stationarity, Validation, and Error Bands"
category: finance/quant-fintech-data
description: "Critique a financial time-series forecast (revenue, demand, rates, volatility, price): test stationarity and the spurious-regression trap, check that validation respects temporal order, demand honest error bands and a naive-baseline comparison, and expose look-ahead leakage and overfitting before the forecast is trusted."
techniques:
  - QA-02
  - DS-02
  - QA-04
  - NE-10
  - RT-05
difficulty: intermediate
tags:
  - time-series
  - forecasting
  - stationarity
  - backtesting
  - prediction-intervals
  - validation
updated: "2026-06-08"
related_prompts:
  - domain-finance/quant-fintech-data/finance_backtest_design_critique.md
  - domain-finance/quant-fintech-data/finance_factor_model_builder.md
  - domain-finance/corporate-finance-fpa/finance_rolling_forecast_designer.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. Forecasts are uncertain estimates; point forecasts without error bands overstate confidence. All outputs must be reviewed by qualified professionals before use.**

## Objective

Pressure-test a time-series forecast so its reported accuracy can be trusted — or exposed as an artifact. The critique covers whether the series was made stationary before modeling (and whether the apparent fit is a spurious regression), whether validation respected the arrow of time, whether the forecast beats a naive baseline, whether prediction intervals are honest, and whether look-ahead or overfitting inflated the in-sample error. The deliverable is a defect list, a baseline-relative accuracy read, and a corrected expectation with error bands.

## When to Use

- Vetting a demand/revenue/cash-flow forecast before it drives a plan or model
- Reviewing a rates/FX/volatility forecast feeding a trading or hedging decision
- Auditing an ML time-series model (ARIMA, Prophet, gradient boosting, LSTM) for validity
- Diagnosing why a forecast that looked accurate in development is failing live
- Setting forecast-accuracy KPIs and the baseline they should beat
- Teaching/learning the standard pitfalls of financial time-series modeling

## Inputs / Context Required

```
<forecast_context>
What is being forecast: [series, frequency, horizon]
Method: [ARIMA/ETS, Prophet, regression, gradient boosting, RNN/LSTM, judgmental]
Training window & test window: [dates; how the split was made]
Features/regressors used: [and whether each is known at forecast time]
Transformations applied: [differencing, logs, deflation, seasonal adjustment]
Reported accuracy: [RMSE/MAE/MAPE; in-sample vs out-of-sample — as provided]
Baseline compared against: [naive/seasonal-naive/random walk — or "none"]
Prediction intervals provided? [Y/N; method]
Known structural breaks / regime changes in the series: [ ]
</forecast_context>
```

If the train/test split method, baseline, or interval method is unstated, treat the reported accuracy as provisional and flag it.

## Constraints

### Must
- Test **stationarity**: is the series (or its modeled transform) stationary? Non-stationary levels regressed on each other invite **spurious regression** — high R² with no real relationship. Require differencing/cointegration reasoning where relevant.
- Verify **temporal validation**: train must precede test; cross-validation must be time-aware (rolling-origin / walk-forward with purge/embargo), never a random shuffle.
- Demand a **naive baseline**: random walk (or seasonal-naive) is the bar. A forecast that doesn't beat the baseline out-of-sample has not demonstrated skill (RT-05).
- Require **honest error bands** (QA-04 / NE-10): prediction intervals, not just a point path; state coverage and whether intervals were validated (do realized values fall inside the stated % of the time?).
- Audit **look-ahead leakage**: are all regressors known at forecast time? Is any target-derived or future-dated feature used? Is seasonal adjustment fit using the full sample (leakage)?
- Use **out-of-sample** error as the headline; report in-sample only as context. The in-sample/out-of-sample gap measures overfitting.
- Flag **structural breaks**: a model fit across a regime change may forecast a regime that no longer exists.

### Must Not
- Invent RMSE/MAE/MAPE, R², or interval-coverage numbers — compute from supplied data or label `[REQUIRES DATA]`.
- Accept in-sample fit as evidence of forecasting skill.
- Report a point forecast without an uncertainty band.
- Treat a high R² on non-stationary data as a real relationship without a stationarity/cointegration check.

## Instructions

**Step 1 — Characterize the series.**
Frequency, trend, seasonality, volatility clustering, and any known structural breaks. State the transformation applied and whether it plausibly induces stationarity.

**Step 2 — Stationarity & spurious-regression check.**
```
Questions:
  - Is the modeled series stationary (mentally: ADF/KPSS-style reasoning, or stated test result)?
  - If levels are used, are predictor and target cointegrated, or is this a spurious regression?
  - Was differencing/log/deflation applied appropriately (and not over-differenced)?
Red flag: very high R² on undifferenced financial levels with autocorrelated residuals.
```

**Step 3 — Validation discipline.**
```
Classify (weakest → strongest):
  V0  In-sample only.
  V1  Single chronological holdout (train earlier, test later).
  V2  Rolling-origin / walk-forward.
  V3  V2 with purge/embargo to prevent leakage across the split boundary.
Reject random K-fold on time series (it leaks the future). State the tier.
```

**Step 4 — Baseline comparison (RT-05).**
```
Compute the naive benchmark on the SAME out-of-sample window:
  Random walk: forecast_t = actual_{t-1}
  Seasonal-naive: forecast_t = actual_{t-season}
Skill = baseline error − model error (positive = model adds value).
If the model does not beat the baseline out-of-sample, it has shown no skill.
```

**Step 5 — Error bands & calibration (QA-04 / NE-10).**
```
Require prediction intervals (e.g., 80%/95%) on the forecast path.
Calibration test: over the OOS window, do ~X% of actuals fall within the X% interval?
  Under-coverage → overconfident intervals; over-coverage → too wide.
Report point error AND interval coverage.
```

**Step 6 — Leakage & overfitting audit (QA-02).**
- Are all regressors available at forecast time, or do any embed future information?
- Was seasonal adjustment / scaling fit on the full sample (leakage) or only on train?
- In-sample vs out-of-sample error gap → overfitting magnitude.
- "If I froze this model and ran it forward, what would most likely break first?"

**Step 7 — Defect list and corrected expectation.**
List each defect with severity, then state the corrected, baseline-relative expectation as a band, with the caveats that survive the critique.

## Output Format

```
## Time-Series Forecast Critique — [Series]
Method: [ ] | Horizon: [ ] | Prepared: [date] | Data: user-supplied

### 1. Series Characterization
[Trend/seasonality/breaks/transformation]

### 2. Stationarity & Spurious-Regression Check
[Verdict + reasoning]

### 3. Validation Tier (V0–V3)
[Rating + what reaches the next tier]

### 4. Baseline Comparison
[Model vs random-walk/seasonal-naive on OOS; skill]

### 5. Error Bands & Calibration
[Point error + interval coverage test]

### 6. Leakage & Overfitting Audit
[Regressor-availability, seasonal-adjustment leakage, IS/OOS gap]

### 7. Defect List & Corrected Expectation
[Severity-ranked defects + baseline-relative band]

### Known Limitations
[Short history, structural breaks, unverified interval method]
```

## Verification

- [ ] Stationarity assessed; spurious-regression risk flagged on undifferenced levels.
- [ ] Validation tier (V0–V3) stated; random K-fold on time series rejected.
- [ ] Naive baseline computed on the same OOS window; skill stated as model-minus-baseline.
- [ ] Prediction intervals required and their calibration (coverage) tested.
- [ ] Out-of-sample error is the headline; IS/OOS gap reported as overfitting measure.
- [ ] Regressor availability and seasonal-adjustment leakage audited.
- [ ] Structural breaks flagged where the series spans a regime change.
- [ ] No accuracy or coverage figures invented; missing data labeled.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| High R² on non-stationary levels read as a real relationship | Require stationarity/cointegration check; autocorrelated residuals signal spurious regression |
| In-sample accuracy presented as forecasting skill | Headline must be out-of-sample; report the IS/OOS gap as overfitting |
| Random cross-validation on time series | Use rolling-origin/walk-forward with purge/embargo; random folds leak the future |
| "Accurate" forecast that doesn't beat random walk | Always compare to a naive baseline on the same window; no baseline beat = no skill shown |
| Point forecast quoted without uncertainty | Require prediction intervals and test their realized coverage |
| Forecasting through a regime change | Flag structural breaks; a model fit across a break may predict a vanished regime |
