---
title: "Feature Drift Audit"
category: AI-ML/feature-engineering
description: "Audit individual features for distribution drift over time against a reference window, with significance and magnitude thresholds — and decide which drift actually matters."
techniques:
  - ST-02
  - DS-02
  - RT-05
  - DS-06
  - QA-12
difficulty: advanced
tags:
  - feature-drift
  - distribution-shift
  - monitoring
  - reference-window
  - feature-engineering
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/feature-engineering/mlfeature_store_design.md
  - domain-AI-ML/feature-engineering/mlfeature_importance_analysis.md
  - domain-AI-ML/data-for-ml/mldata_data_leakage_detector.md
---

# Feature Drift Audit

**Objective:** Audit each feature for distribution drift between a defined reference window and a current window, quantify drift with appropriate statistics and a magnitude threshold, and prioritize which drifts matter — distinguishing benign shifts from those likely to degrade the model, so monitoring drives action rather than noise.

**When to Use:**
- Model performance is slipping and you suspect input distribution shift.
- Setting up or reviewing feature monitoring for a deployed model.
- Validating that a retrain is warranted (or not) based on input drift.

**When NOT to Use:**
- You're designing the feature store/serving (use `mlfeature_store_design.md`).
- The concern is label/concept drift specifically and you have outcome data — that's a related but distinct analysis.

## Inputs / Context

Provide what you can (ask for framework + version if code is expected):
- **Reference window** — the baseline period (e.g., training distribution) per feature.
- **Current window(s)** — the period(s) being compared.
- **Feature inventory** — types (numeric/categorical) and importances if known.
- **Model sensitivity** — which features the model relies on most.
- **Action context** — what a "drift detected" result would trigger (alert, retrain, investigate).

## Constraints

**Must:**
- Compare against an explicit reference window — never declare drift from a single window with no baseline.
- Use drift statistics appropriate to feature type (e.g., PSI/KS/Wasserstein for numeric; chi-square/PSI for categorical) and set both a magnitude and a significance threshold.
- Prioritize drift by the feature's importance/model-sensitivity, not by raw drift magnitude alone.

**Must Not:**
- Call any change "drift" without a threshold — sampling noise always produces some difference.
- Invent PSI/KS values or thresholds as facts — state the statistic, mark computed-vs-illustrative, and justify the threshold.
- Equate input drift with performance degradation; flag that labels/outcomes are needed to confirm impact.

**Instructions:**

1. **Fix the reference window.** State the baseline distribution per feature (often training data) and the current window(s) being compared. Drift is only meaningful against this reference.

2. **Pick the statistic per feature type.** Numeric: KS, Wasserstein, or PSI on bins; categorical: chi-square or PSI on category frequencies. Note the statistic's sensitivity to sample size.

3. **Set magnitude and significance thresholds.** Define what counts as material drift (e.g., PSI bands) and guard against large samples flagging trivial differences as "significant."

4. **Compute (or specify computation of) drift per feature.** Produce drift scores; where not computed, describe how, never fabricate values.

5. **Weight by model importance.** Cross-reference with feature importance/model sensitivity so high-importance drifting features rank above unimportant ones with larger raw drift.

6. **Distinguish benign from harmful drift.** Some shifts are expected (seasonality, scale changes the model is robust to). Flag which drifts plausibly degrade the model and which don't.

7. **Recommend actions per finding.** For material, high-importance drift: investigate cause (data pipeline change, real-world shift, possible leakage/serving bug), and whether retrain/rollback/feature-fix is warranted. Note that outcome labels are needed to confirm performance impact.

**Output Format:**

A markdown drift report:
- **Windows** — reference and current windows used.
- **Drift Scorecard** — table: Feature | Type | Statistic | Drift score | Threshold | Material? | Importance | Priority.
- **Material High-Importance Drifts** — likely cause + recommended action.
- **Benign Drifts Noted** — explained-away shifts (so they're not re-flagged).
- **Impact Caveat** — what label data is needed to confirm degradation.
- **Open Computations** — drift scores still to compute.
- **INSUFFICIENT EVIDENCE** — an enumerated value in the `Material?` column, for features whose statistic was not computed or whose windows are not comparable (different lengths, a partial current window, a reference spanning a known regime change). Name the unblocking datum: matched-length windows and the computed statistic for that feature.

## Verification

- [ ] An explicit reference window is defined per feature.
- [ ] The statistic matches the feature type and a threshold (magnitude + significance) is set.
- [ ] Drift is prioritized by model importance, not raw magnitude alone.
- [ ] Benign vs harmful drift is distinguished.
- [ ] The report notes that input drift ≠ confirmed performance loss without labels.
- [ ] No drift scores/thresholds are fabricated; computed-vs-illustrative is marked.
- [ ] Features with uncomputed statistics or mismatched windows are marked INSUFFICIENT EVIDENCE rather than defaulted to not-material.

## False-Positive Prevention

❌ **DON'T:**
- Declare drift from one current window with no reference — there's nothing to drift *from*.
- Use a p-value alone on a huge sample; statistical significance flags trivial, immaterial shifts.
- Rank a large drift in an unimportant feature above a small drift in a top feature.
- Assume detected input drift means the model got worse — without labels, that's unproven.

✅ **DO:**
- Anchor every drift score to a stated reference window.
- Require both a magnitude threshold (e.g., PSI band) and significance, sized for the sample.
- Weight drift by feature importance so monitoring surfaces actionable shifts first.
- Treat a sudden drift in one feature as a possible pipeline/serving bug or leakage, not only real-world change, and require labels to confirm performance impact.

## Example Output

```markdown
## Feature Drift Audit: Fraud Model (reference = training Q1; current = last 30d)

### Windows
Reference: training distribution (Q1). Current: trailing 30 days of serving inputs.

### Drift Scorecard
| Feature | Type | Statistic | Drift | Threshold | Material? | Importance | Priority |
|---|---|---|---|---|---|---|---|
| txn_amount | numeric | PSI | 0.28 (illustrative) | PSI>0.2 | Yes | high | P0 |
| merchant_cat | categorical | PSI | 0.05 | PSI>0.2 | No | high | — |
| device_age_days | numeric | KS | sig. but small | mag. small | No | low | — |
| hour_of_day | numeric | PSI | 0.22 | PSI>0.2 | Yes | low | P2 |

### Material High-Importance Drifts
- txn_amount (PSI 0.28, high importance): investigate first. Possible causes: currency/units
  change in upstream pipeline (serving bug) vs real spending shift. Check pipeline before retrain.

### Benign Drifts Noted
- hour_of_day shift (P2): likely seasonal traffic pattern; model is robust to it.

### Impact Caveat
These are input-distribution signals. Confirm performance degradation with recent labeled
outcomes before triggering a retrain.

### Open Computations
PSI for the remaining 40 features; per-segment drift for txn_amount.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** reference → statistic → threshold → importance → action.
- **DS-02 (Metric Specification):** defines drift statistics and thresholds precisely.
- **RT-05 (Evidence-Based Reasoning):** every drift claim is anchored to a reference and a score.
- **DS-06 (Prioritization & Severity Guidance):** ranks drift by importance × materiality.
- **QA-12 (False Positives Identification):** prevents baseline-free and significance-without-magnitude errors.

**Related Prompts:**
- `mlfeature_store_design.md` — the served features whose drift this monitors.
- `mlfeature_importance_analysis.md` — supplies the importance weighting for prioritization.
- `mldata_data_leakage_detector.md` — a sudden single-feature drift can signal a serving/leak bug.
