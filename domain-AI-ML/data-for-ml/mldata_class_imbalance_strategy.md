---
title: "ML Class Imbalance Strategy"
category: AI-ML/data-for-ml
description: "Choose among resampling, class-weighting, threshold-moving, and the right metrics for imbalanced data — driven by the cost of each error type, not by reflexively rebalancing to 50/50."
techniques:
  - ST-02
  - RT-02
  - DT-04
  - DS-02
  - QA-12
difficulty: intermediate
tags:
  - class-imbalance
  - resampling
  - class-weighting
  - threshold-tuning
  - metric-selection
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/data-for-ml/mldata_train_test_split_strategy.md
  - domain-AI-ML/data-for-ml/mldata_data_augmentation_plan.md
  - domain-AI-ML/data-for-ml/mldata_synthetic_data_strategy.md
---

# ML Class Imbalance Strategy

**Objective:** Recommend how to handle an imbalanced target — choosing among resampling (over/under/SMOTE), class-weighting, decision-threshold moving, and the evaluation metric — driven by the relative cost of false positives vs false negatives and the deployment base rate, rather than by reflexively rebalancing classes to 50/50.

**When to Use:**
- The target is skewed (fraud, defects, rare disease, churn) and accuracy is misleadingly high.
- A model "predicts the majority class for everything" and you need a principled fix.
- You must pick a metric and operating threshold for a rare-event classifier.

**When NOT to Use:**
- The imbalance is mild and a standard metric suffices — don't over-engineer.
- You need to expand minority *data* via realistic transforms (use `mldata_data_augmentation_plan.md`) or generation (use `mldata_synthetic_data_strategy.md`); this prompt decides whether/when to.

## Inputs / Context

Provide what you can; the recommendation degrades gracefully if some are missing:
- **Class distribution** — counts/base rate per class, train and (if known) deployment.
- **Error costs** — the business/clinical cost of a false positive vs a false negative; any hard constraints (e.g., min recall).
- **Downstream use of outputs** — labels only, or calibrated probabilities (ranking, thresholds, expected-value decisions)?
- **Split design** — how validation is set up (resampling must live inside it).
- **Volume of the minority class** — absolute count, not just ratio.
- **Model family** — whether it supports class weights / cost-sensitive learning.

## Constraints

**Must:**
- Drive the recommendation from the asymmetric cost of errors and the deployment base rate, not from achieving balanced classes.
- Specify metrics suited to imbalance (PR-AUC, recall at fixed precision, F-beta, cost-weighted) and a majority-class baseline to beat.
- Keep any resampling strictly inside the training folds; evaluate on the *natural* (un-resampled) distribution.

**Must Not:**
- Recommend accuracy as the primary metric for a skewed target, or claim improvement without a majority-class baseline.
- Present oversampling/SMOTE as universally best — note its risks (overfitting duplicates, synthesizing implausible points, breaking calibration).
- Distort the base rate so that downstream probabilities/thresholds become meaningless without flagging recalibration.

**Instructions:**

1. **Quantify the imbalance and its stakes.** State the base rate (train and deployment) and the cost asymmetry between FP and FN; this, not the ratio alone, sets the strategy.

2. **Fix the metric first.** Choose the evaluation metric(s) that reflect the costs (PR-AUC, recall@precision, F-beta, cost matrix) and define the majority-class/random baseline to beat — before touching the data.

3. **Decide whether the output is labels or probabilities.** If downstream consumes probabilities, prefer methods that preserve calibration (class weights + threshold-moving) over aggressive resampling that distorts base rates.

4. **Compare the levers on the merits.** Lay out resampling (over/under/SMOTE), class-weighting/cost-sensitive learning, and threshold-moving across effectiveness, calibration impact, overfitting risk, and minority-count requirements.

5. **Select and combine.** Recommend a primary lever (often class weights or threshold-moving for tabular) and note when resampling adds value (very low minority counts), keeping methods compatible with the metric and calibration needs.

6. **Place it leak-safely in the pipeline.** Specify that any resampling is fit on training folds only and that evaluation uses the natural distribution; cross-link the split strategy.

7. **Tune the operating threshold to the cost.** Set the decision threshold from the cost matrix / required recall on validation, not the default 0.5, and report the resulting operating point.

8. **State residual risks and monitoring.** Note calibration drift, the minority-count floor, and what to watch in production (per-class recall, base-rate shift).

**Output Format:**

A markdown recommendation:
- **Imbalance & Cost Profile** — base rates + FP/FN cost asymmetry + constraints.
- **Metric & Baseline** — chosen metric(s) and the baseline to beat.
- **Lever Comparison** — table: Lever | Effectiveness | Calibration impact | Overfit risk | Min minority count.
- **Recommended Approach** — primary + combination, with rationale.
- **Pipeline Placement** — where resampling/weights live; evaluation on natural distribution.
- **Operating Threshold** — value derived from cost / required recall.
- **Risks & Monitoring** — calibration, minority floor, production signals.

## Verification

- [ ] The strategy is justified by error costs and base rate, not by reaching 50/50.
- [ ] The primary metric suits imbalance and a majority-class baseline is named.
- [ ] Resampling (if any) is confined to training folds; evaluation uses the natural distribution.
- [ ] Calibration impact is addressed when downstream consumes probabilities.
- [ ] The operating threshold is set from cost/required recall, not left at 0.5.

## False-Positive Prevention

❌ **DON'T:**
- Report accuracy (or "99% accurate!") on a 1% positive rate — the majority-class baseline already gets 99%.
- Apply SMOTE/oversampling to the whole dataset before splitting — it leaks synthetic neighbors into validation.
- Rebalance to 50/50 and then trust the model's probabilities — the base rate, and thus calibration, is now wrong.
- Treat oversampling as strictly better than class weights; on tabular data they often match, and weights preserve calibration.

✅ **DO:**
- Pick PR-AUC / recall@precision / cost-weighted metrics and always compare to a majority/random baseline.
- Keep resampling inside training folds and evaluate on the real, skewed distribution.
- Prefer class weights + threshold-moving when calibrated probabilities are consumed downstream; recalibrate if you resample.
- Choose the decision threshold from the explicit FP/FN cost or a required recall, and report the operating point.

## Example Output

```markdown
## Class Imbalance Strategy: Manufacturing Defect Detection

### Imbalance & Cost Profile
- Base rate: defects 1.8% (train), ~1.5% expected in deployment.
- Cost asymmetry: a missed defect (FN) costs ~30× a false alarm (FP) — recall is paramount.
- Constraint: min recall 0.90 on defects.

### Metric & Baseline
- Primary: recall at precision ≥ 0.40; secondary: PR-AUC. Baseline: majority-class predictor (recall 0 on defects).

### Lever Comparison
| Lever | Effectiveness | Calibration impact | Overfit risk | Min minority count |
|---|---|---|---|---|
| Class weights | High | Preserves | Low | low ok |
| Threshold-moving | High | Preserves | Low | low ok |
| Random oversample | Medium | Distorts | High (dupes) | low ok |
| SMOTE | Medium | Distorts | Medium (implausible pts) | needs moderate count |

### Recommended Approach
- Primary: class-weighted model + threshold-moving to hit recall 0.90. Skip SMOTE (only ~900 defects, but
  features are correlated → synthetic points risk implausibility). Recalibrate if any resampling is added later.

### Pipeline Placement
- Weights set in the estimator; no resampling. Evaluate on the natural 1.8% distribution per fold.

### Operating Threshold
- Threshold 0.21 (from cost matrix) yields recall 0.91 at precision 0.43 on validation.

### Risks & Monitoring
- Watch per-class recall and base-rate drift weekly; alert if defect rate shifts >0.5pp (threshold may need retuning).
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** quantify → metric → lever comparison → select → threshold.
- **RT-02 (Multi-Dimensional Analysis Framework):** levers compared across effectiveness, calibration, overfit, count.
- **DT-04 (Decision Criteria Specification):** cost asymmetry and required recall drive lever and threshold choice.
- **DS-02 (Metric Specification):** mandates imbalance-appropriate metrics and a majority-class baseline.
- **QA-12 (False Positives Identification):** preempts the accuracy-trap and resample-leakage failures.

**Related Prompts:**
- `mldata_train_test_split_strategy.md` — ensure resampling lives inside a leak-safe split.
- `mldata_data_augmentation_plan.md` — expand minority data via realistic transforms.
- `mldata_synthetic_data_strategy.md` — when generated minority data is warranted, and its risks.
