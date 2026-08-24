---
title: "ML Overfitting / Underfitting Diagnosis"
category: AI-ML/classical-ml-modeling
description: "Read learning and validation curves to diagnose whether a model is overfitting (high variance) or underfitting (high bias), then prescribe targeted remedies matched to the diagnosis."
techniques:
  - ST-02
  - RT-09
  - RT-10
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - overfitting
  - underfitting
  - bias-variance
  - learning-curves
  - diagnosis
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/classical-ml-modeling/mlmodel_regularization_strategy.md
  - domain-AI-ML/classical-ml-modeling/mlmodel_hyperparameter_tuning_strategy.md
  - domain-AI-ML/data-for-ml/mldata_data_leakage_detector.md
---

# ML Overfitting / Underfitting Diagnosis

**Objective:** Use learning curves (performance vs training-set size) and validation curves (performance vs model complexity) to classify a model's failure as high variance (overfitting), high bias (underfitting), or neither — then prescribe remedies that fit the diagnosis, so effort is not wasted adding capacity to an overfit model or regularizing an underfit one.

**When to Use:**
- A model's validation/test performance is disappointing and you need to know *why* before fixing it.
- You're about to add capacity or regularization and want to confirm the direction is right.
- Train and validation metrics diverge (or both are stuck low) and you need a diagnosis.

**When NOT to Use:**
- The suspect is leakage, not fit (a too-good train *and* validation score) — use `mldata_data_leakage_detector.md`.
- You already have a confirmed diagnosis and just need the remedy detail (use `mlmodel_regularization_strategy.md`).

## Inputs / Context

Provide what you can:
- **Train vs validation metric** — values on the same metric and CV scheme.
- **Curves if available** — learning curve (metric vs train size) and/or validation curve (metric vs a complexity knob).
- **Model & complexity knobs** — family and the levers that change capacity (depth, leaves, features, penalty).
- **Data size** — total rows; whether more data is obtainable.
- **Target performance** — the bar the model needs to clear (so "good enough" is defined).

## Constraints

**Must:**
- Base the diagnosis on the *pattern* of train vs validation across size/complexity, not a single number.
- Distinguish high variance (large train-validation gap) from high bias (both low and close) from leakage (both implausibly high).
- Match each prescribed remedy to the diagnosis and order remedies by expected impact.

**Must Not:**
- Diagnose from a single train/validation pair without considering the curve shape (or request it if missing).
- Prescribe "get more data" for a high-bias model (more data won't fix bias).
- Quote expected metric improvements from a remedy as fact; treat them as hypotheses to measure.

**Instructions:**

1. **Gather the evidence.** Collect train vs validation on the same metric/CV; obtain or request a learning curve and/or validation curve. Without curve shape, state the diagnosis is provisional.

2. **Rule out leakage first.** If both train and validation are implausibly high for the domain, suspect leakage before fit — redirect to the leakage detector. Fit diagnosis assumes an honest split.

3. **Read the learning curve.** A large persistent train-validation gap that more data would close → high variance. Both curves converging at a low plateau that more data won't lift → high bias.

4. **Read the validation curve.** Validation improving then worsening as complexity rises → overfitting past the sweet spot. Validation flat-low across complexity → underfitting (capacity or features are the limit, not tuning).

5. **Classify the regime.** State the diagnosis (high variance / high bias / well-fit-but-below-target / leakage-suspected) with the curve evidence that supports it.

6. **Prescribe matched remedies.** Variance → regularize, simplify, more data, bagging, fewer/cleaner features. Bias → add capacity, richer features/interactions, weaker regularization, a more expressive family. Order by impact and reversibility.

7. **Define the re-check.** Name the curve change that would confirm the remedy worked (gap narrows for variance; plateau lifts for bias) and guard against overshooting into the opposite regime.

**Output Format:**

A markdown report:
- **Evidence** — train vs validation; curve shapes (or note they're missing).
- **Leakage Screen** — ruled in/out and why.
- **Diagnosis** — variance / bias / well-fit / leakage-suspected, with curve evidence.
- **Matched Remedies (ranked)** — each tied to the diagnosis, with expected mechanism.
- **Re-check Criteria** — curve change that confirms success; overshoot guard.

## Verification

- [ ] Diagnosis rests on curve patterns, not a single metric pair (or is flagged provisional).
- [ ] Leakage is screened before fit is concluded.
- [ ] The diagnosis distinguishes variance vs bias vs well-fit explicitly.
- [ ] Remedies match the diagnosis (no "more data" for bias; no added capacity for variance).
- [ ] Remedies are ranked by impact; a re-check + overshoot guard is stated.
- [ ] No remedy's improvement is quoted as fact.

## False-Positive Prevention

❌ **DON'T:**
- Add model capacity (deeper trees, more features) to a model that is overfitting — it widens the gap.
- Regularize or simplify a model that is underfitting — it deepens the bias.
- Prescribe "collect more data" for high bias — more samples don't fix a too-simple model.
- Read a high train-and-validation score as great fit when it may be leakage.

✅ **DO:**
- Diagnose from the learning/validation curve shape, requesting curves if only a single pair is given.
- Screen for leakage when both train and validation look implausibly strong.
- Match remedies to the regime: variance → regularize/simplify/more data; bias → capacity/features.
- Re-measure after each change and watch for tipping into the opposite failure mode.

## Example Output

```markdown
## Fit Diagnosis: Gradient-Boosted Sales Forecast Classifier

### Evidence
- Train ROC-AUC ~0.95, validation ~0.78 — a wide gap. Learning curve: validation rises with more data but the gap stays large; validation curve: AUC peaks at moderate depth then declines as depth grows.

### Leakage Screen
- Validation ~0.78 is plausible for this noisy domain; no single feature collapses performance when removed → leakage unlikely. Fit diagnosis proceeds.

### Diagnosis
- High variance (overfitting). Evidence: large persistent train-validation gap; validation worsens past moderate complexity.

### Matched Remedies (ranked)
1. Reduce capacity (cap depth/num_leaves at the validation-curve peak) — highest impact, reversible.
2. Add regularization (min_child_samples, L2 leaf penalty, subsample/colsample).
3. Acquire more training data — learning curve suggests the gap would narrow.
4. Prune noisy/redundant features.

### Re-check Criteria
- Success: train-validation gap narrows while validation holds/improves. Overshoot guard: if validation falls toward train at a low plateau, capacity was cut too far (now underfitting).
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** evidence → leakage screen → read curves → diagnose → remedy.
- **RT-09 (Root Cause Explanation):** ties poor performance to variance vs bias.
- **RT-10 (Troubleshooting Decision Tree):** branches on curve shapes to a diagnosis.
- **RT-05 (Evidence-Based Reasoning):** diagnosis anchored to curve patterns.
- **DS-06 (Prioritization & Severity Guidance):** remedies ranked by impact.

**Related Prompts:**
- `mlmodel_regularization_strategy.md` — the variance-side remedy detail.
- `mlmodel_hyperparameter_tuning_strategy.md` — find the complexity sweet spot honestly.
- `mldata_data_leakage_detector.md` — when the "great fit" is actually leakage.
