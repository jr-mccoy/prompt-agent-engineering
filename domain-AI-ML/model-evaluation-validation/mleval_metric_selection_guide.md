---
title: "ML Metric Selection Guide"
category: AI-ML/model-evaluation-validation
description: "Choose a primary metric and guardrail metrics that align to the business objective and the real cost of each error type, instead of defaulting to accuracy."
techniques:
  - ST-02
  - RT-02
  - DS-02
  - CM-02
  - QA-17
difficulty: intermediate
tags:
  - metric-selection
  - evaluation
  - cost-sensitive
  - imbalanced-data
  - guardrail-metrics
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/model-evaluation-validation/mleval_baseline_comparison_protocol.md
  - domain-AI-ML/model-evaluation-validation/mleval_confusion_matrix_interpretation.md
  - domain-AI-ML/model-evaluation-validation/mleval_offline_online_alignment.md
---

# ML Metric Selection Guide

**Objective:** Translate a business objective and its error costs into a single primary optimization metric plus a small set of guardrail metrics, so that "the model improved" means something the business actually cares about — not just a number that went up.

**When to Use:**
- Starting a new modeling task and you need to define "success" before training.
- Accuracy is being reported on an imbalanced or cost-asymmetric problem.
- Two teams disagree on whether a model is better.
- You are reviewing someone else's metric choice for a launch decision.

**When NOT to Use:**
- For reading an already-chosen metric's confusion matrix (use `mleval_confusion_matrix_interpretation.md`).
- For testing whether a metric difference is significant (use `mleval_statistical_significance_testing.md`).

## Inputs / Context

Provide what you can; the guidance degrades gracefully:
- **Business objective** — the decision the model drives and what good/bad outcomes look like in money, risk, or user experience.
- **Task type** — binary/multiclass classification, ranking, regression, retrieval, generation.
- **Class balance / target distribution** — prevalence of positives, long-tail structure.
- **Error costs** — relative cost of a false positive vs false negative (or over- vs under-prediction); thresholds where cost changes.
- **Operating point** — fixed threshold, top-k, or a tunable score; any latency/volume constraints.
- **Downstream consumer** — does anything consume calibrated probabilities, or only the ranked/thresholded decision?

## Constraints

**Must:**
- Map each candidate metric to a specific business consequence; reject any metric that has no consequence attached.
- Distinguish a **threshold-dependent** metric (F1, precision, recall) from a **threshold-independent** one (AUROC, AUPRC) and state which the decision requires.
- Name a **majority-class / trivial baseline** value for each proposed metric so the reader can see what "doing nothing" scores.

**Must Not:**
- Recommend accuracy as primary on imbalanced data without flagging the majority-class trap.
- Fabricate metric values for the user's data; reason about *which* metric, not *what number* it will hit.
- Collapse multiple competing objectives into one metric silently — surface the tradeoff instead.

**Instructions:**

1. **Restate the decision.** Write one sentence: "This model exists to ____; a good prediction causes ____ and a bad one causes ____." Everything downstream serves this.

2. **Characterize the error cost asymmetry.** Determine whether false positives or false negatives hurt more, and by roughly how much. If costs are symmetric and balanced, say so — that changes the answer.

3. **Filter by task type and balance.** Rule out metrics that mislead here (e.g., accuracy under 2% prevalence; AUROC when positives are rare and ranking the tail matters → prefer AUPRC).

4. **Propose a primary metric.** Pick the single metric the team will optimize and gate launches on. Justify it against the decision and cost asymmetry, not convention.

5. **Add guardrail metrics.** Choose 2–4 metrics that must not regress even if the primary improves (e.g., worst-slice recall, calibration error, latency, a fairness slice). These catch "won by gaming."

6. **Define the operating point.** State the threshold/top-k and how it will be chosen (e.g., precision-at-fixed-recall, or the cost-minimizing threshold on a validation set).

7. **State the baseline target.** Give the trivial-baseline score for each metric so any reported gain is interpretable.

**Output Format:**

A markdown brief:
- **Decision Restatement** — one or two sentences.
- **Error-Cost Profile** — FP vs FN (or over/under) cost summary.
- **Primary Metric** — the metric, the operating point, and why.
- **Guardrail Metrics** — table: Metric | What it protects | Regression tolerance.
- **Baselines to Beat** — trivial/majority/prior values for each metric.
- **Rejected Metrics** — what you considered and why it misleads here.

## Verification

- [ ] The primary metric is tied to the stated decision and cost asymmetry, not chosen by default.
- [ ] Class balance / target distribution was used to filter metric choices.
- [ ] Threshold-dependence of each metric is stated and matches how the model is used.
- [ ] At least one guardrail protects against the most likely gaming path.
- [ ] A trivial/majority baseline value is named for every reported metric.
- [ ] No specific metric *values* for the user's model are asserted as fact.

## False-Positive Prevention

❌ **DON'T:**
- Recommend accuracy as the headline on a 1:99 imbalanced problem — it rewards predicting the majority class.
- Pick AUROC when the positive class is rare and you care about precision in the top slice — it can look strong while the actionable top-k is poor.
- Optimize a single metric and ignore a worst-case slice that the aggregate hides.
- Choose a threshold-independent metric (AUROC) when the product ships a fixed-threshold decision.

✅ **DO:**
- Demand class-specific metrics (precision/recall/AUPRC) and a majority-class baseline on imbalanced data.
- Match metric type to usage: threshold-independent for ranking/triage, threshold-dependent for fixed-decision products.
- Pair the primary metric with guardrails (worst-slice, calibration, latency) so a win can't come from a hidden regression.
- Express error costs explicitly so the threshold can be chosen to minimize cost, not picked at 0.5 by habit.

## Example Output

```markdown
## Metric Selection: Fraud Flagging for Manual Review

### Decision Restatement
This model flags transactions for a human review queue. A true flag prevents a chargeback;
a false flag costs analyst time and may annoy a legitimate customer.

### Error-Cost Profile
- False negative (missed fraud): high (~$120 average chargeback + reputational).
- False positive (good txn flagged): moderate (~$3 review cost + friction); review capacity is finite.
- Asymmetry favors recall, but review capacity caps how many positives we can afford.

### Primary Metric
**Precision at the recall the review team can staff** (precision @ recall = 0.80), because the
queue has a fixed daily capacity and we want the flagged set to be as clean as possible at that recall.

### Guardrail Metrics
| Metric | What it protects | Regression tolerance |
|---|---|---|
| Recall on high-value txns (> $500) | Don't miss the costly cases | none |
| Daily flag volume | Don't overflow the review queue | +/- 10% |
| Calibration (ECE) | Score thresholds stay meaningful | < 0.05 |
| FP rate on top loyalty tier | Don't over-friction best customers | <= current |

### Baselines to Beat
- Majority-class accuracy is 98.6% and is useless here (predicts "not fraud" always; recall 0).
- Current rules engine: precision 0.41 @ recall 0.80 — this is the bar.

### Rejected Metrics
- **Accuracy**: dominated by the 98.6% legitimate majority; uninformative.
- **AUROC**: positives are ~1.4% — AUROC can look strong while the actionable top of the queue is dirty; AUPRC / precision@recall is more honest here.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** decision → cost → filter → primary → guardrails → operating point.
- **RT-02 (Multi-Dimensional Analysis Framework):** weighs metrics across cost, balance, and usage.
- **DS-02 (Metric Specification):** the core deliverable is a precise metric spec with baselines.
- **CM-02 (Constraint Specification):** review capacity and threshold are governing constraints.
- **QA-17 (Named Scores for Multi-Dimensional Metrics):** primary + named guardrails form a scorecard.

**Related Prompts:**
- `mleval_baseline_comparison_protocol.md` — define the baselines each metric must beat.
- `mleval_confusion_matrix_interpretation.md` — read the chosen metric's error breakdown.
- `mleval_offline_online_alignment.md` — confirm the chosen metric tracks the business outcome.
