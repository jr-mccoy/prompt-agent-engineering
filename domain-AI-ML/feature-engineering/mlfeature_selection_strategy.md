---
title: "Feature Selection Strategy"
category: AI-ML/feature-engineering
description: "Choose a feature-selection approach (filter, wrapper, embedded) appropriate to data size, model, and goal — without leaking the target or selecting on the test set."
techniques:
  - ST-02
  - RT-02
  - DS-02
  - CM-02
  - QA-12
difficulty: advanced
tags:
  - feature-selection
  - dimensionality
  - filter-wrapper-embedded
  - leakage-aware
  - feature-engineering
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/feature-engineering/mlfeature_ideation_workshop.md
  - domain-AI-ML/feature-engineering/mlfeature_importance_analysis.md
  - domain-AI-ML/feature-engineering/mlfeature_leakage_safe_pipeline.md
---

# Feature Selection Strategy

**Objective:** Recommend a feature-selection strategy — filter, wrapper, embedded, or a staged combination — matched to the dataset size, model family, and goal (predictive lift vs interpretability vs serving cost), with an explicit, leakage-safe protocol for *how* selection is run inside cross-validation.

**When to Use:**
- You have many candidate features and need a principled way to reduce them.
- Interpretability, serving cost, or overfitting pressure motivates a smaller feature set.
- A prior selection process is suspected of leaking or overfitting.

**When NOT to Use:**
- You're still generating candidates (use `mlfeature_ideation_workshop.md`).
- You only need to interpret importances, not select (use `mlfeature_importance_analysis.md`).

## Inputs / Context

Provide what you can (ask for framework + version if code is expected):
- **Dataset size** — rows and number of candidate features.
- **Model family** — linear, tree ensemble, neural, etc.
- **Goal** — max predictive lift, interpretability, serving cost reduction, or stability.
- **Feature types** — numeric/categorical/text/sparse; collinearity if known.
- **Validation setup** — split/CV scheme; whether grouped/temporal.

## Constraints

**Must:**
- Match the method to data size and model (e.g., filters for very wide data; embedded for trees/linear; wrappers only when affordable).
- Specify selection *inside* the CV loop, fit on train folds only, so selection cannot leak the target or peek at the holdout.
- Tie the recommendation to the stated goal (lift vs interpretability vs cost).

**Must Not:**
- Recommend selecting features on the full dataset before splitting (a classic leak that inflates metrics).
- Invent feature counts, correlations, or performance numbers — mark unknowns and how to measure.
- Treat univariate filter scores as proof a feature is useless in combination (interactions matter).

**Instructions:**

1. **Clarify the goal and constraints.** Determine whether the objective is maximum lift, interpretability, serving cost, or stability — each favors different methods and stopping rules.

2. **Right-size the method to the data.** Very high dimensionality / small n favors fast filters first; moderate sizes allow embedded methods; wrappers (RFE, sequential) are reserved for when compute permits and lift is paramount.

3. **Choose the method family.** Filter (correlation, mutual information, variance), embedded (L1, tree importance/gain, regularization paths), or wrapper (RFE, forward/backward) — or a staged pipeline (filter → embedded).

4. **Handle collinearity and redundancy.** Plan for correlated features (grouped importance, VIF, clustering) so selection doesn't arbitrarily drop one of a redundant pair and mislead interpretation.

5. **Specify the leakage-safe protocol.** State that selection is fit on training folds within CV (e.g., inside a Pipeline), never on the full data or the holdout, and that the final feature count is chosen by nested CV, not by peeking.

6. **Define the stopping rule.** How many features to keep — by performance plateau, stability across folds, or a cost budget — with the metric used to decide.

7. **Plan a stability check.** Recommend checking that the selected set is stable across folds/seeds; an unstable selection is a warning, not a result to trust.

**Output Format:**

A markdown strategy:
- **Goal & Data Profile** — size, model, objective.
- **Recommended Method(s)** — with justification and a staged plan if relevant.
- **Leakage-Safe Protocol** — exactly where selection sits in the CV loop.
- **Collinearity Handling** — approach for redundant features.
- **Stopping Rule & Metric** — how many features and why.
- **Stability Check** — how to confirm the set is robust.
- **Open Measurements** — counts/correlations to obtain.

## Verification

- [ ] Method matches data size and model family.
- [ ] Selection is specified inside the CV loop, train-folds-only.
- [ ] Collinearity/redundancy handling is addressed.
- [ ] A stopping rule and metric are defined.
- [ ] A stability check is included.
- [ ] No feature counts/correlations/scores are fabricated.

## False-Positive Prevention

❌ **DON'T:**
- Run feature selection on the entire dataset before splitting — the holdout informs which features are kept, leaking the target and inflating CV scores.
- Drop a feature because its univariate correlation with the target is low; it may be valuable in interaction with others.
- Trust a single-run selection; correlated features make the chosen subset unstable across seeds.
- Use a wrapper on wide data without compute budget — it overfits the validation set through repeated tuning.

✅ **DO:**
- Embed selection in the CV pipeline so each fold selects from its own train data.
- Use grouped/cluster-based handling for collinear features rather than arbitrary single drops.
- Choose the feature count by nested CV and confirm stability across folds/seeds.
- Match the method to the goal: embedded/L1 for interpretable lean models, staged filter→embedded for very wide data.

## Example Output

```markdown
## Feature Selection Strategy: 1,200 candidate features, ~50k rows, gradient-boosted trees

### Goal & Data Profile
Goal: predictive lift + manageable serving cost. Model: GBT. Many engineered aggregates;
moderate collinearity expected. Validation: 5-fold grouped CV (group = customer_id).

### Recommended Method(s)
Staged: (1) variance + low-MI filter to drop dead/near-constant features; (2) embedded tree
gain + permutation importance within CV to rank; (3) keep top-k by stability. Skip wrappers
(too costly at this width).

### Leakage-Safe Protocol
All steps fit inside each training fold via a Pipeline; the holdout fold is never used to select.
Final k chosen by nested CV.

### Collinearity Handling
Cluster correlated features (|r|>0.9); keep one representative per cluster or use grouped
permutation importance to avoid splitting credit.

### Stopping Rule & Metric
Increase k until PR-AUC plateaus within fold-to-fold noise; prefer the smaller set at the plateau.

### Stability Check
Selected set must overlap ≥ 80% across folds; otherwise widen k or revisit collinearity handling.

### Open Measurements
Per-feature variance and MI; correlation clusters; PR-AUC vs k curve.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** goal → method → protocol → stopping → stability.
- **RT-02 (Multi-Dimensional Analysis Framework):** trades lift vs interpretability vs cost.
- **DS-02 (Metric Specification):** stopping rule is tied to a named metric and noise band.
- **CM-02 (Constraint Specification):** the train-folds-only rule is a hard constraint.
- **QA-12 (False Positives Identification):** guards against select-on-full-data leakage and univariate dismissal.

**Related Prompts:**
- `mlfeature_ideation_workshop.md` — generates the candidates this selects from.
- `mlfeature_importance_analysis.md` — interpret the importances driving selection.
- `mlfeature_leakage_safe_pipeline.md` — implement selection inside a leak-safe pipeline.
