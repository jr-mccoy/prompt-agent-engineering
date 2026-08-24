---
title: "Probabilistic Forecasting Design"
category: AI-ML/specialized-ml/time-series
description: "Design forecasts that output a full distribution or set of quantiles rather than a single point, choosing among quantile regression, conformal prediction, and sampling approaches, scoring with proper rules (pinball / CRPS), and validating that intervals are actually calibrated to their nominal coverage."
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
  - probabilistic
  - quantiles
  - calibration
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/specialized-ml/time-series/ts_forecasting_model_selection.md
  - domain-AI-ML/specialized-ml/time-series/ts_backtesting_design.md
  - domain-AI-ML/specialized-ml/time-series/ts_hierarchical_forecasting.md
---

# Probabilistic Forecasting Design

**Objective:** Recommend how to produce and validate *distributional* forecasts — quantiles, prediction intervals, or full predictive densities — instead of bare point estimates. The recommendation must match the method (quantile regression, conformal prediction, sampling/ensemble) to the data and decision, specify a proper scoring rule (pinball loss / CRPS), and make interval *calibration and coverage* — not interval width — the primary validation criterion, with the empirical winner deferred to rolling-origin backtesting.

**When to Use:**
- Downstream decisions need uncertainty (safety stock, capacity buffers, risk limits), not just a single number.
- You must report prediction intervals or specific quantiles (e.g. P10/P50/P90).
- Stakeholders are over-trusting point forecasts and you need honest uncertainty.

**When NOT to Use:**
- A point forecast genuinely suffices and no decision uses the spread — use `ts_forecasting_model_selection.md`.
- You first need to fix the base point model's accuracy before adding intervals — start with model selection.
- You need coherence across an aggregation hierarchy — pair this with `ts_hierarchical_forecasting.md`.

## Inputs / Context

Provide what you can:
- **Target quantiles / intervals** — which quantiles or coverage levels decisions need (e.g. 80%, 95%).
- **Decision use** — how the uncertainty is consumed (inventory buffer, risk limit, alert threshold).
- **Asymmetry of cost** — whether over- vs under-forecasting carry different costs.
- **Base model & data** — current point model, data volume, history length, frequency.
- **Horizon** — single-step vs multi-step (interval widening over horizon).
- **Non-stationarity / regime risk** — whether the error distribution drifts.
- **Coverage requirement** — nominal levels that must be honored in production.

## Constraints

**Must:**
- Establish a naive baseline interval (e.g. seasonal-naive point ± empirical residual quantiles) as the bar to beat.
- Score with a proper rule (pinball loss per quantile, or CRPS for full distributions).
- Validate *calibration* — empirical coverage of each nominal interval — on held-out, time-ordered data.
- Defer the final method choice to rolling-origin backtesting.

**Must Not:**
- Fabricate coverage percentages, CRPS values, or benchmark results from memory; reason from the user's setup and mark unknowns as "measure on your data."
- Present a point estimate as if it were certain, or imply an interval is calibrated without a coverage test.
- Evaluate intervals by width alone — a narrow interval that under-covers is worse, not better.
- Use random train/test splits on time-ordered data to assess coverage.

**Instructions:**

1. **Clarify the decision.** Identify which quantiles/intervals the downstream decision actually consumes and whether costs are asymmetric — this sets the scoring weights.
2. **Set the baseline.** Build a naive interval from empirical residual quantiles of a seasonal-naive forecast; every probabilistic method must beat it on the proper score and on coverage.
3. **List candidate methods.** Quantile regression (directly model target quantiles via pinball loss), conformal prediction (wrap any point model with distribution-free coverage guarantees), and sampling/ensemble or parametric-density approaches (Monte Carlo paths, predictive distributions).
4. **Match method to constraints.** Conformal when you need finite-sample coverage guarantees over an existing point model; quantile regression when you want flexible per-quantile fits; sampling when you need full predictive paths (e.g. for aggregation over horizon).
5. **Handle multi-step and non-stationarity.** Plan how intervals widen with horizon and how drifting error distributions are handled (e.g. adaptive/online conformal).
6. **Design the calibration check.** Specify reliability evaluation: for each nominal level, measure empirical coverage on rolling-origin holdouts; flag over- and under-coverage separately. Add a sharpness (width) check *only as a secondary tiebreaker* among well-calibrated methods.
7. **Decide and document.** Recommend a primary method + fallback, the proper score, and the calibration acceptance criteria. Mark all empirical claims as to-be-measured.

**Output Format:**

A markdown recommendation:
- **Decision & Quantiles** — what uncertainty the decision needs and cost asymmetry.
- **Baseline Interval** — the naive interval and how it's scored.
- **Candidate Methods** — table of quantile regression / conformal / sampling with fit notes.
- **Recommendation** — primary method + fallback and base model.
- **Scoring & Calibration Plan** — proper rule + coverage/reliability test, sharpness as secondary.
- **Horizon & Drift Handling** — interval widening and adaptation strategy.
- **Open Questions / Data to Gather** — unknowns before committing.

## Verification

- [ ] Output is distributional (quantiles/intervals/density), not a single point passed off as certain.
- [ ] A naive baseline interval is defined and used as the bar to beat.
- [ ] Scoring uses a proper rule (pinball / CRPS), and calibration is tested by empirical coverage per nominal level.
- [ ] Coverage is validated on time-ordered (rolling-origin) holdouts, never random splits.
- [ ] No fabricated coverage, CRPS, or benchmark numbers — empirical claims marked "measure on your data."

## False-Positive Prevention

❌ **DON'T:**
- Dress up a point estimate as certainty — a single number with no interval hides the risk the decision actually faces.
- Declare an interval "90%" without testing that it empirically covers ~90% of outcomes.
- Optimize for narrow intervals and call them "confident" when they under-cover.
- Judge a probabilistic forecast by interval width instead of coverage.

✅ **DO:**
- Treat **miscalibrated intervals** (nominal 90% covering far less) as a first-class failure and test reliability per level.
- Report honest prediction intervals alongside the point, and let cost asymmetry shape the quantiles you emphasize.
- Use a proper scoring rule (pinball/CRPS) so sharpness and calibration trade off correctly.
- Use interval width only as a secondary tiebreaker among methods that are already well-calibrated.

## Example Output

```markdown
## Decision & Quantiles
- Inventory safety stock uses P50 and P90 weekly demand; under-stocking costs ~3× over-stocking.

### Baseline Interval
- Seasonal-naive point ± empirical residual quantiles. Scored by pinball loss at P10/P50/P90.

### Candidate Methods
| Method | Fit |
|--------|-----|
| Quantile regression | flexible per-quantile; needs enough data |
| Conformal (adaptive) | distribution-free coverage; wraps existing point model |
| Sampling / ensemble | full paths; good for horizon aggregation |

### Recommendation
- Primary: adaptive conformal over current point model (coverage guarantee under drift).
- Fallback: quantile regression with pinball loss.

### Scoring & Calibration Plan
- Proper score: pinball loss per quantile; CRPS for full distribution.
- Calibration: rolling-origin coverage per nominal level; flag over/under-coverage.
- Sharpness: secondary tiebreaker among calibrated methods only.

### Horizon & Drift Handling
- Intervals widen with horizon; online conformal adapts to error drift.
- Coverage and CRPS numbers TBD — measure on your data.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** sequences decision → baseline → method match → calibration design.
- **RT-02 (Multi-Dimensional Analysis Framework):** frames the model as a probabilistic-forecasting specialist focused on calibration.
- **DS-01 (Framework Application):** the candidate-methods table forces an explicit, criteria-based method choice.
- **CM-02 (Constraint Specification):** Must/Must Not block pins coverage-over-width and anti-fabrication as hard constraints.
- **DS-06 (Prioritization & Severity Guidance):** routes the final method pick to rolling-origin backtesting and a coverage test.

**Related Prompts:**
- `ts_forecasting_model_selection.md` — selects the base point model the intervals are built on.
- `ts_backtesting_design.md` — designs the rolling-origin evaluation used to measure coverage and proper scores.
- `ts_hierarchical_forecasting.md` — extends coherent reconciliation to distributional, not just point, forecasts.
