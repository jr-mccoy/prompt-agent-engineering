---
title: "ML Baseline Modeling Plan"
category: AI-ML/classical-ml-modeling
description: "Design the first honest model for a problem — a simple, leak-safe baseline plus the evaluation protocol that makes its score trustworthy and a fair reference for everything that follows."
techniques:
  - ST-02
  - RT-05
  - QA-12
  - DS-02
  - CM-02
difficulty: intermediate
tags:
  - baseline
  - evaluation-protocol
  - reproducibility
  - metric-selection
  - validation
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/classical-ml-modeling/mlmodel_algorithm_selection_matrix.md
  - domain-AI-ML/classical-ml-modeling/mlmodel_cross_validation_design.md
  - domain-AI-ML/data-for-ml/mldata_data_leakage_detector.md
---

# ML Baseline Modeling Plan

**Objective:** Specify the first model that should be built for a problem — deliberately simple, leak-safe, and reproducible — together with the evaluation protocol (metric, split, baseline-of-the-baseline) that makes its number honest. The output is a plan that yields a trustworthy reference score every later model must beat to justify its complexity.

**When to Use:**
- At the very start of a modeling effort, before any tuning or fancy architecture.
- When a project jumped straight to a complex model and has no honest reference point.
- Before committing to a model-improvement roadmap (you cannot measure improvement without a baseline).

**When NOT to Use:**
- When a sound, well-evaluated baseline already exists (move to tuning/ensembling).
- For choosing among model families (use `mlmodel_algorithm_selection_matrix.md`).
- For diagnosing an already-trained model's fit (use `mlmodel_overfitting_underfitting_diagnosis.md`).

## Inputs / Context

Provide what you can:
- **Task & target** — type, label definition, and the moment the label becomes known.
- **Data** — size, feature types, missingness, class balance (for classification).
- **Success definition** — the business/decision metric and any threshold of usefulness.
- **Constraints** — interpretability, latency, training budget.
- **Existing work** — prior models, current metrics, known data issues.
- **Framework** — ask the user (sklearn / XGBoost / LightGBM / statsmodels); don't assume.

## Constraints

**Must:**
- Specify at least two reference points: a trivial baseline (majority/mean/random or a one-rule heuristic) and a simple-but-real model baseline.
- Make the plan leak-safe by construction — preprocessing fit inside the split, prediction-time boundary respected.
- Choose the primary metric to match the decision being made, and state why aggregate accuracy is or isn't appropriate.

**Must Not:**
- Report or assume any metric value as a result — this is a plan; numbers in examples are illustrative only.
- Recommend a complex first model "to save time later."
- Use accuracy as the headline metric on imbalanced data without justification.

**Instructions:**

1. **Lock the success metric and the trivial baseline.** State the primary metric (matched to the decision), any secondary metrics, and the trivial reference (majority-class / mean predictor / simple heuristic) that the model must beat to be worth anything.

2. **Define the evaluation split.** Choose the split/CV scheme appropriate to the data structure (grouped, stratified, temporal) and state it explicitly. Defer the detailed scheme to `mlmodel_cross_validation_design.md` if non-trivial, but name the choice here.

3. **Specify the leak-safe pipeline.** Order preprocessing (impute → encode → scale → select) inside the fit boundary so nothing learns from validation/test data. Name the prediction-time boundary.

4. **Pick the simple real model.** Choose a transparent, low-variance model family (e.g., regularized linear/logistic, shallow tree, or a default-config boosted model) as the honest baseline — minimal tuning, default-ish hyperparameters.

5. **Define reproducibility controls.** Fix random seeds, record library versions, pin the data snapshot, and log the exact metric computation so the baseline can be reproduced.

6. **State the "good enough to proceed" and "stop" conditions.** What baseline result would justify investing in stronger models, and what result (e.g., baseline already meets the usefulness threshold) would mean stop here.

7. **List the next-step hypotheses.** Name 2–3 specific improvements to try next and the expected mechanism, so the baseline becomes the launchpad for a measured roadmap.

**Output Format:**

A markdown plan:
- **Metric & Trivial Baseline** — primary/secondary metric, the must-beat reference.
- **Evaluation Protocol** — split/CV scheme, seed/versioning/snapshot controls.
- **Leak-Safe Pipeline** — ordered steps and the fit boundary.
- **Baseline Model Spec** — family, config, why it's the honest first model.
- **Decision Gates** — proceed condition / stop condition.
- **Next-Step Hypotheses** — ranked improvements to test against this baseline.

## Verification

- [ ] Both a trivial baseline and a simple-model baseline are specified.
- [ ] The primary metric is justified against the decision (and against imbalance if relevant).
- [ ] The pipeline is leak-safe by construction with the fit boundary named.
- [ ] Reproducibility controls (seed, versions, data snapshot) are listed.
- [ ] Proceed/stop gates are stated; no metric is presented as an actual result.

## False-Positive Prevention

❌ **DON'T:**
- Call a model "good" because it beats a coin flip — beat the *majority-class* baseline on the right metric.
- Use accuracy as the headline on imbalanced data; a 95%-negative dataset makes 95% accuracy meaningless.
- Fit scalers/encoders on the full dataset before splitting and call the score honest.
- Start with a heavily tuned complex model and have nothing simple to compare it against.

✅ **DO:**
- Always include a majority/mean/heuristic reference and report the model relative to it.
- Choose class-aware metrics (e.g., PR-AUC, recall at fixed precision) when classes are imbalanced.
- Fit all preprocessing inside the CV/train boundary and verify the prediction-time boundary.
- Keep the first model simple and reproducible so later gains are attributable.

## Example Output

```markdown
## Baseline Modeling Plan: Equipment Failure Prediction (next 7 days)

### Metric & Trivial Baseline
- Primary: PR-AUC (failures are ~3% of windows; accuracy would be misleading).
- Secondary: recall at the precision the maintenance team can act on.
- Trivial baseline: majority class (always "no failure") — illustratively ~0.97 accuracy but ~0.03 PR-AUC; the bar to beat is the PR-AUC, not accuracy.

### Evaluation Protocol
- Temporal split (train on older windows, validate on most recent) — failures are time-ordered; random CV would leak the future.
- Seed fixed; library versions pinned; data snapshot tagged `2026-05-29`.

### Leak-Safe Pipeline
- impute (median, fit on train) → encode (OOF target encoding) → scale (fit on train) → model. Prediction-time boundary: features must be computable from sensor data available before the 7-day horizon opens.

### Baseline Model Spec
- Regularized logistic regression, default-ish C, class_weight balanced. Transparent, low-variance, fast to retrain — the honest reference.

### Decision Gates
- Proceed to stronger models if logistic PR-AUC materially clears the majority baseline yet falls short of the usefulness threshold.
- Stop here if logistic already meets the maintenance team's actionable precision/recall target.

### Next-Step Hypotheses
1. Gradient-boosted trees — expected to capture nonlinear sensor interactions.
2. Lag/rolling features — expected to add temporal signal.
3. Threshold tuning — expected to trade recall for precision toward the action point.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** metric → split → pipeline → model → gates flow.
- **RT-05 (Evidence-Based Reasoning):** every choice is tied to data structure and the decision.
- **QA-12 (False Positives Identification):** guards against accuracy-on-imbalance and leaky pipelines.
- **DS-02 (Metric Specification):** primary/secondary metric selection matched to the decision.
- **CM-02 (Constraint Specification):** prediction-time boundary and reproducibility controls.

**Related Prompts:**
- `mlmodel_algorithm_selection_matrix.md` — choose the family before baselining it.
- `mlmodel_cross_validation_design.md` — design the split this plan references.
- `mldata_data_leakage_detector.md` — confirm the baseline isn't leaking before trusting it.
