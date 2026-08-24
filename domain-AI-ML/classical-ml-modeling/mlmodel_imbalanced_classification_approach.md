---
title: "ML Imbalanced Classification Approach"
category: AI-ML/classical-ml-modeling
description: "Design an end-to-end approach to class imbalance — metric choice, resampling vs class weighting, decision-threshold tuning, and leak-safe evaluation — anchored to the real cost of each error type."
techniques:
  - ST-02
  - DS-02
  - RT-02
  - QA-12
  - CM-02
difficulty: advanced
tags:
  - imbalanced-classification
  - resampling
  - class-weighting
  - threshold-tuning
  - pr-auc
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/classical-ml-modeling/mlmodel_probability_calibration.md
  - domain-AI-ML/classical-ml-modeling/mlmodel_baseline_modeling_plan.md
  - domain-AI-ML/classical-ml-modeling/mlmodel_cross_validation_design.md
---

# ML Imbalanced Classification Approach

**Objective:** Produce a coherent, end-to-end plan for a class-imbalanced classification problem: pick metrics that reflect the rare class and the cost of errors, decide between resampling and class weighting (and where in the pipeline they live), tune the decision threshold to the operating point, and evaluate it all without leakage or accuracy illusions.

**When to Use:**
- The positive (or target) class is rare (e.g., fraud, churn, defect, disease) and accuracy is misleading.
- A model "looks accurate" but misses almost all of the rare class.
- Designing the modeling approach where false negatives and false positives have very different costs.

**When NOT to Use:**
- Balanced-class problems where standard metrics suffice.
- Pure probability-calibration questions (use `mlmodel_probability_calibration.md`).
- General first-model design without an imbalance focus (use `mlmodel_baseline_modeling_plan.md`).

## Inputs / Context

Provide what you can:
- **Class ratio** — positive prevalence and absolute count of the rare class.
- **Error costs** — relative cost/consequence of false negatives vs false positives; any operating constraint (e.g., max alerts/day, min recall).
- **Downstream use** — is a hard label consumed, a ranked list, or a calibrated probability?
- **Data structure** — grouping/time, for the CV scheme.
- **Framework** — ask the user (sklearn / imbalanced-learn / XGBoost / LightGBM).

## Constraints

**Must:**
- Choose the primary metric from the rare-class perspective and the error costs (e.g., PR-AUC, recall at fixed precision, cost-weighted), and justify it against accuracy.
- Always compare to the majority-class baseline on the chosen metric.
- Keep any resampling strictly inside the training folds — never resample before the split or apply it to validation/test.

**Must Not:**
- Report accuracy as the headline metric on imbalanced data.
- Resample the whole dataset before cross-validation (a classic leakage/inflation bug).
- Quote expected lift from SMOTE/weighting as fact; treat all numbers as illustrative and to be measured.

**Instructions:**

1. **Quantify the imbalance and the cost asymmetry.** State prevalence, absolute rare-class count, and the relative cost of FN vs FP. The cost asymmetry — not the ratio alone — drives metric and threshold choices.

2. **Select metrics first.** Pick a primary metric tied to the decision: PR-AUC for ranking under rarity, recall@precision or precision@recall for an operating point, or expected cost for explicit costs. Add the majority-class baseline as the floor.

3. **Decide the imbalance mechanism.** Compare options on the same axes: class weighting (often the simplest first move), random under/oversampling, SMOTE-family synthesis, and ensemble approaches — noting that synthesis can fabricate unrealistic minority points and weighting avoids data duplication.

4. **Place the mechanism leak-safely.** Specify that resampling/weighting is applied within each training fold only; validation/test reflect the true prevalence. Confirm the CV scheme (defer to `mlmodel_cross_validation_design.md` if grouping/time apply).

5. **Tune the decision threshold separately.** Treat the threshold as a deployment choice tuned on validation to hit the operating constraint (target recall/precision or minimum expected cost), not left at 0.5.

6. **Check calibration if probabilities are consumed.** If downstream uses probabilities, note that resampling distorts them and calibration may be required (hand off to `mlmodel_probability_calibration.md`).

7. **Define success and stop.** State the operating-point target and the majority-baseline margin that justifies the approach; note when the rare-class signal is simply too weak to model usefully.

**Output Format:**

A markdown plan:
- **Imbalance & Cost Profile** — prevalence, counts, FN/FP cost asymmetry.
- **Metric Choice** — primary + secondary + majority baseline, with justification.
- **Mechanism Decision** — weighting vs resampling vs synthesis (axes + pick).
- **Leak-Safe Placement** — where the mechanism lives; CV scheme.
- **Threshold Plan** — operating point and how it's chosen.
- **Calibration Note** — whether probabilities need calibrating.
- **Success / Stop Criteria** — target operating point and the baseline margin.

## Verification

- [ ] The primary metric reflects the rare class and is justified against accuracy.
- [ ] The majority-class baseline is included as the floor.
- [ ] Resampling/weighting is confined to training folds; validation/test keep true prevalence.
- [ ] The decision threshold is tuned to the operating point, not fixed at 0.5.
- [ ] Calibration is addressed when probabilities are consumed downstream.
- [ ] No lift numbers from sampling/weighting are stated as fact.

## False-Positive Prevention

❌ **DON'T:**
- Report 97% accuracy on a 3%-positive problem as success — it can be worse than the majority baseline at the rare class.
- Apply SMOTE/oversampling to the entire dataset before splitting — it leaks synthetic neighbors across folds and inflates metrics.
- Leave the threshold at 0.5 and conclude the model "can't find" the rare class.
- Treat synthetic minority points as equivalent to real signal without checking they're plausible.

✅ **DO:**
- Lead with PR-AUC / recall-at-precision / expected cost and always show the majority-class floor.
- Resample or weight inside training folds only; evaluate at the true class prevalence.
- Tune the operating threshold on validation to the business constraint.
- Try class weighting before synthesis, and verify any synthetic data does not create implausible minority regions.

## Example Output

```markdown
## Imbalanced Approach: Card Fraud Detection

### Imbalance & Cost Profile
- Prevalence ~0.4% positive (~3,200 fraud rows in ~800k). FN (missed fraud) far costlier than FP (a declined-then-verified transaction), but FP volume is capped by the review team's capacity.

### Metric Choice
- Primary: PR-AUC (ranking under extreme rarity). Operating metric: recall at the precision implied by review capacity. Floor: majority baseline (~0.004 PR-AUC).

### Mechanism Decision
- Start with class_weight='balanced' on gradient-boosted trees (no data duplication, simplest). Compare against random undersampling of the majority. SMOTE deprioritized — high-dimensional transaction features risk implausible synthetic fraud.

### Leak-Safe Placement
- Weighting set per training fold; undersampling (if used) inside folds only. StratifiedGroupKFold on card_id; validation/test keep the real 0.4% prevalence.

### Threshold Plan
- Choose the score threshold on validation that maximizes recall subject to staying within daily review capacity (precision floor).

### Calibration Note
- Risk scores feed a triage queue ranking; if absolute probabilities are later shown to reviewers, calibrate (isotonic) post-hoc.

### Success / Stop Criteria
- Approach justified if recall at the capacity precision clearly beats the prior rules engine and the majority floor; stop if signal can't exceed the rules baseline within budget.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** cost → metric → mechanism → threshold flow.
- **DS-02 (Metric Specification):** rare-class metric selection matched to error costs.
- **RT-02 (Multi-Dimensional Analysis Framework):** weighting vs resampling vs synthesis on shared axes.
- **QA-12 (False Positives Identification):** guards against accuracy illusion and resample-before-split leakage.
- **CM-02 (Constraint Specification):** review-capacity and leak-safe placement constraints.

**Related Prompts:**
- `mlmodel_probability_calibration.md` — fix probabilities distorted by resampling.
- `mlmodel_baseline_modeling_plan.md` — the majority-class floor and honest baseline.
- `mlmodel_cross_validation_design.md` — the grouped/stratified scheme this approach assumes.
