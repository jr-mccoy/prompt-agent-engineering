---
title: "Time-Series Look-Ahead Leakage Audit"
category: AI-ML/specialized-ml/time-series
description: "Audit a time-series pipeline specifically for look-ahead / future leakage — features, splits, transforms, and target construction that let information from the future contaminate the past — with evidence-backed findings and fixes."
techniques:
  - ST-02
  - RT-05
  - QA-12
  - CM-02
  - DS-06
difficulty: advanced
tags:
  - time-series
  - look-ahead-leakage
  - temporal-leakage
  - data-leakage
  - validation
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/data-for-ml/mldata_data_leakage_detector.md
  - domain-AI-ML/specialized-ml/time-series/ts_feature_engineering.md
  - domain-AI-ML/specialized-ml/time-series/ts_backtesting_design.md
---

# Time-Series Look-Ahead Leakage Audit

**Objective:** Audit a time-series modeling pipeline for the specific failure of look-ahead (future) leakage — any place where information not yet available at the prediction time bleeds into training or evaluation — covering features, splits, transforms, target/horizon construction, and resampling, producing ranked, evidence-backed findings with concrete fixes. This is the temporal-leakage-focused complement to the general `mldata_data_leakage_detector.md`.

**When to Use:**
- Backtesting/CV metrics look excellent but live forecasts are far worse (the canonical look-ahead signature).
- Before trusting any time-series model's reported performance.
- Inheriting a forecasting or time-series classification pipeline you didn't write.

**When NOT to Use:**
- For non-temporal/i.i.d. leakage broadly (use `mldata_data_leakage_detector.md` for the full three-family audit).
- For building leak-free features from scratch (use `ts_feature_engineering.md`).
- For designing the evaluation protocol (use `ts_backtesting_design.md`).

## Inputs / Context

Provide what you can; the audit degrades gracefully:
- **Target & horizon** — what's predicted, how far ahead, and the exact forecast origin (the prediction-time boundary).
- **Feature list with timing** — each feature's name and *when it is observable* relative to the origin.
- **Split/backtest setup** — random vs temporal split, fold geometry, any gap between train and test.
- **Transforms** — scalers, encoders, imputation, target transforms, resampling/interpolation — and whether each is fit per-fold on past data only.
- **Target construction** — how the label is built (e.g., future-window aggregate) and whether its horizon can bleed backward.
- **Headline metrics** and any suspiciously strong features.

## Constraints

**Must:**
- Anchor every finding to a specific feature, transform, split decision, or target-construction step in the user's input — no generic warnings.
- Reference the prediction-time boundary (forecast origin) as the standard against which every timing claim is judged.
- Classify each finding as Confirmed (mechanism identified) vs Suspected (pattern consistent with leakage, needs a check) with a confidence level.

**Must Not:**
- Declare leakage on suspicion alone; distinguish a shown mechanism from a smell that needs a probe.
- Invent feature observation timing the user didn't provide; if timing is unknown, list it as an open question.
- Fabricate metric drops; instead predict the leakage signature (e.g., "removing X should collapse backtest accuracy toward the naive baseline") and recommend the test.

**Instructions:**

1. **Reconstruct the forecast origin.** Pin the exact instant of prediction and the horizon. Every input observed after the origin is a look-ahead candidate; every label built from a future window must not bleed into past features.

2. **Audit the split/backtest for time order.** Confirm the split is temporal (train past, test future). Random/shuffled CV on time data is itself the leak. Check that any required feature lead-time gap exists between train and test.

3. **Audit features for future observability.** For each feature, ask whether its value could only be known at or after a future time relative to the origin. Flag centered rolling windows, full-series statistics, and "static" aggregates secretly computed over future rows.

4. **Audit transforms for global fitting.** Check whether scalers, encoders, imputers, target transforms, or interpolation/resampling were fit on the whole series (or on test) rather than per-fold on past-only data — a subtle but common future leak.

5. **Audit target construction and horizon bleed.** If the label is a future-window aggregate (e.g., next-7-day sum), verify that future window doesn't overlap with feature windows or adjacent training rows, and that the gap matches the real horizon.

6. **Run the leakage signature cross-check.** Compare backtest performance to a naive/seasonal-naive baseline and to plausibility. Identify single features whose removal would collapse the metric and interrogate them as prime suspects.

7. **Rank and remediate.** Order findings by (consequence × confidence). For each, give the specific fix (temporal split, trailing-shifted windows, per-fold transform fitting, gap insertion, recompute target with a clean horizon) and the test that confirms it.

**Output Format:**

A markdown audit (mirroring the data-leakage-detector format):
- **Look-Ahead Risk Summary** — table: Finding | Mechanism | Confidence | Production Impact.
- **Confirmed Leaks** — mechanism + evidence + remediation, ranked.
- **Suspected Leaks / Open Questions** — what to check and how (the predicted signature).
- **Clean Aspects Verified** — what was checked and found sound.
- **Recommended Re-Validation Protocol** — the corrected, time-honest setup to re-run before trusting metrics.
- **INSUFFICIENT EVIDENCE** — an available confidence value, used where the data carries no distinction between event time, ingest time, and revision time. Without that distinction a restated series is indistinguishable from a clean one, so name the unblocking datum: per-field as-of timestamps, or a vintage/point-in-time snapshot of the source.

## Verification

- [ ] The forecast origin / prediction-time boundary is stated and used to judge every timing claim.
- [ ] The split is confirmed temporal; random/shuffled CV on time data is flagged if present.
- [ ] Features, transforms, and target construction are each checked for future bleed.
- [ ] Each finding is labeled Confirmed vs Suspected with a confidence level and a specific anchor.
- [ ] Remediations are actionable and name where in the pipeline they apply.
- [ ] No fabricated metric drops; the expected leakage signature is stated as a test instead.
- [ ] Where event time cannot be separated from ingest or revision time, the finding is INSUFFICIENT EVIDENCE with as-of timestamps named — a series is not declared clean because no leak was visible in it.

## False-Positive Prevention

❌ **DON'T:**
- Flag a legitimately past-observed, highly predictive feature as leakage just because it's strong.
- Assume a transform leaked without confirming it was fit on the full/test data rather than per-fold on the past.
- Call a temporal split "leaky" when a required feature lead-time gap is genuinely present and correct.
- Treat strong backtest accuracy as proof of no leakage — that's exactly the symptom you're investigating.

✅ **DO:**
- Establish *when* each feature is observable relative to the forecast origin before judging it; ask when unknown.
- Trace the fit/transform boundary of every preprocessing step to the fold's training window.
- Separate "this is look-ahead leakage" (mechanism shown) from "this smells like it" (needs a probe), and label accordingly.
- Confirm a suspected leak by predicting its signature (e.g., "remove X → backtest MASE rises toward seasonal-naive") and recommending that test.

## Example Output

```markdown
## Look-Ahead Leakage Audit: 7-Day Sales Forecaster v2

### Look-Ahead Risk Summary
| Finding | Mechanism | Confidence | Production Impact |
|---|---|---|---|
| 5-fold shuffled CV on daily series | Split | High | Trains on future, inflates backtest; collapses live |
| `roll_mean_7` centered, not shifted | Feature | High | Includes the target day + future → leaks label |
| StandardScaler fit on full series pre-split | Transform | High | Test statistics leak into train scaling |
| Target = next-7-day sum, no gap from features | Target horizon | Medium | Label window may overlap feature windows |
| `monthly_total` "static" feature | Feature | Medium | Likely computed over the full (future) month |

### Confirmed Leaks (ranked)
1. **Shuffled CV on a time series.** `KFold(shuffle=True)` lets each fold train on future days to predict past ones. Remediation: rolling-origin backtest (train past → test future); see `ts_backtesting_design.md`.
2. **Centered rolling mean.** `rolling(7, center=True).mean()` includes day t and t+1..t+3 — the target leaks into its own feature. Remediation: trailing window + `.shift(1)`.
3. **Global scaling pre-split.** Scaler fit on all rows before splitting. Remediation: fit per-fold on training window only.

### Suspected Leaks / Open Questions
- **`monthly_total`**: confirm whether it's computed over the full calendar month (includes future days) or month-to-date. Test: recompute as month-to-date; expect backtest MASE to rise toward seasonal-naive if it was leaking.
- **Target gap**: confirm the next-7-day label window starts strictly after the last feature observation.

### Clean Aspects Verified
- Lag features (lag_7, lag_14) are strictly past and valid for the 7-day horizon.
- Holiday flags are future-known and safe.

### Recommended Re-Validation Protocol
1. Rolling-origin backtest, expanding window, test window = 7 days, gap = 0 (features need no lead).
2. Refit scaler/encoders inside each fold's training window only.
3. Replace centered rolling features with trailing-shifted ones; recompute `monthly_total` as month-to-date.
4. Re-measure against seasonal-naive. Expect backtest error to rise from the inflated level toward the real ~baseline-relative number — that gap is the leakage you removed.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** origin → split → features → transforms → target → signature → remediate.
- **RT-05 (Evidence-Based Reasoning):** every finding anchored to a named feature/transform/split decision.
- **QA-12 (False Positives Identification):** core to separating confirmed look-ahead leaks from strong-but-legitimate features.
- **CM-02 (Constraint Specification):** the forecast origin / prediction-time boundary is the governing constraint.
- **DS-06 (Prioritization & Severity Guidance):** findings ranked by consequence × confidence.

**Related Prompts:**
- `mldata_data_leakage_detector.md` — the general three-family leakage audit this temporal audit specializes.
- `ts_feature_engineering.md` — build features that don't leak in the first place.
- `ts_backtesting_design.md` — the time-honest re-validation protocol referenced in remediation.
