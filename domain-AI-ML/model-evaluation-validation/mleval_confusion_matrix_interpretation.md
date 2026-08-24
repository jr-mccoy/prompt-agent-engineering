---
title: "Confusion Matrix Interpretation"
category: AI-ML/model-evaluation-validation
description: "Read a confusion matrix and per-class metrics correctly — separating which errors are frequent, which are costly, and which are threshold artifacts — then decide next actions."
techniques:
  - ST-02
  - RT-05
  - DS-02
  - DS-06
  - QA-12
difficulty: beginner
tags:
  - confusion-matrix
  - per-class-metrics
  - precision-recall
  - threshold
  - imbalanced-data
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/model-evaluation-validation/mleval_metric_selection_guide.md
  - domain-AI-ML/model-evaluation-validation/mleval_error_analysis_slicing.md
  - domain-AI-ML/model-evaluation-validation/mleval_calibration_assessment.md
---

# Confusion Matrix Interpretation

**Objective:** Take a confusion matrix (binary or multiclass) plus its per-class metrics and produce a correct reading — which errors are most frequent, which are most costly, which classes are confused with which, and whether the picture is a model problem or a threshold/imbalance artifact — ending in a concrete next action.

**When to Use:**
- You have a confusion matrix and need to understand what it actually says.
- Per-class precision/recall disagree with the aggregate accuracy and you need to reconcile them.
- Deciding whether the fix is a threshold change, more data for a class, or a different model.

**When NOT to Use:**
- You haven't chosen the right metric yet (use `mleval_metric_selection_guide.md`).
- You need probability quality rather than discrete decisions (use `mleval_calibration_assessment.md`).

## Inputs / Context

Provide what you can:
- **The confusion matrix** — counts of predicted vs. actual per class (binary or multiclass).
- **Class prevalence** — how common each true class is in this evaluation set.
- **The decision threshold / operating point** used to produce the predictions.
- **Error costs** — relative cost of each error type / off-diagonal cell, if known.
- **Primary + guardrail metrics** for context, if already defined.

## Constraints

**Must:**
- Compute or restate per-class precision, recall, and support — never reason from a single accuracy number.
- Distinguish frequent errors (large off-diagonal counts) from costly errors (high per-error cost), and treat them separately.
- State which findings are threshold-movable vs. which reflect genuine class confusion.

**Must Not:**
- Read accuracy as "good" on an imbalanced matrix without comparing to the majority-class baseline.
- Fabricate cell counts, costs, or prevalence not provided; mark unknowns as unknown.
- Recommend retraining when a threshold or class-weight change would address the observed pattern.

**Instructions:**

1. **Normalize the matrix two ways.** Show it normalized by row (recall view: of each true class, where did predictions go) and by column (precision view: of each predicted class, what was it really). The two views answer different questions.

2. **Baseline the aggregate.** State the majority-class baseline accuracy so the headline number is interpretable; flag if accuracy is misleading under imbalance.

3. **Read the per-class table.** Report precision, recall, F1, and support per class. Identify the weakest class by recall and the noisiest by precision, with their support.

4. **Locate the dominant confusions.** Find the largest off-diagonal cells and describe them as "true A predicted as B." Note whether confusions are symmetric (A↔B mutual) or one-directional.

5. **Weigh frequency vs. cost.** Re-rank the off-diagonal cells by (count × per-error cost) if costs are known; the most damaging cell is rarely the most frequent one.

6. **Separate threshold artifacts from model errors.** Identify whether shifting the threshold (or class weights) would move the problematic cells — a precision/recall trade — versus errors that persist at any threshold (genuine confusion).

7. **Recommend the next action.** Map the dominant finding to one action: move threshold, rebalance/weight a class, add data for a class, merge ambiguous classes, or escalate to error-analysis slicing.

**Output Format:**

A markdown reading:
- **Matrix Views** — row-normalized and column-normalized summaries.
- **Aggregate vs. Baseline** — accuracy and the majority-class baseline.
- **Per-Class Table** — Class | Precision | Recall | F1 | Support.
- **Dominant Confusions** — top off-diagonal cells (by count and, if costs known, by cost).
- **Threshold vs. Model** — which problems move with the threshold.
- **Recommended Next Action** — one prioritized step.

## Verification

- [ ] Per-class precision/recall/support are reported, not just aggregate accuracy.
- [ ] The majority-class baseline is stated when classes are imbalanced.
- [ ] The largest confusions are described directionally (true X → predicted Y).
- [ ] Frequent vs. costly errors are distinguished (cost-weighted if costs are available).
- [ ] Threshold-movable findings are separated from genuine class confusion.
- [ ] No cell counts, prevalence, or costs are invented beyond the input.

## False-Positive Prevention

❌ **DON'T:**
- Celebrate 96% accuracy when one class is 96% of the data and its recall on the minority class is near zero.
- Treat the largest off-diagonal cell as the priority when a smaller, far costlier confusion exists.
- Recommend retraining for a problem a threshold shift would solve (or vice versa).
- Conclude "class C is broken" from low precision without checking its support (it may be 9 examples).

✅ **DO:**
- Always pair accuracy with per-class recall and the majority-class baseline.
- Cost-weight the confusions when error costs differ so the ranking reflects real harm.
- Test mentally whether moving the threshold trades the two cells before prescribing a model change.
- Check support before declaring a class broken; route low-n classes to data collection, not redesign.

## Example Output

```markdown
## Confusion Matrix Reading: 3-Class Document Router (n=4,000, threshold = argmax)

### Aggregate vs. Baseline
Accuracy = 0.88. Majority class (invoice, 70%) baseline accuracy = 0.70. Real gain is modest.

### Per-Class Table
| Class | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| invoice | 0.93 | 0.96 | 0.94 | 2,800 |
| receipt | 0.74 | 0.71 | 0.72 | 900 |
| contract | 0.66 | 0.52 | 0.58 | 300 |

### Dominant Confusions
- True contract → predicted invoice: 96 cases (32% of contracts). Largest *rate* of error.
- True receipt → predicted invoice: 180 cases. Largest *count*.
- If a misrouted contract costs ~10× a misrouted receipt, contract→invoice is the priority cell.

### Threshold vs. Model
- contract recall is low across thresholds (genuine confusion with invoice layout) — not threshold-movable.
- receipt↔invoice errors shrink if the invoice decision threshold is raised — threshold-movable.

### Recommended Next Action
Prioritize contract: collect more contract examples + a layout feature; it's a model/data gap, not a
threshold artifact. Separately, raise the invoice threshold to recover receipt recall (cheap win).
Route the contract slice to `mleval_error_analysis_slicing.md` for example-level cause confirmation.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** normalize → baseline → per-class → confusions → threshold → action.
- **RT-05 (Evidence-Based Reasoning):** conclusions are tied to specific cells and supports.
- **DS-02 (Metric Specification):** precise per-class metric definitions and operating point.
- **DS-06 (Prioritization & Severity Guidance):** cost-weighted ranking of confusions.
- **QA-12 (False Positives Identification):** guards against low-support and baseline-blind conclusions.

**Related Prompts:**
- `mleval_metric_selection_guide.md` — make sure the metric you're reading is the right one.
- `mleval_error_analysis_slicing.md` — drill into a confused class with example-level analysis.
- `mleval_calibration_assessment.md` — when the threshold matters, check the scores are calibrated.
