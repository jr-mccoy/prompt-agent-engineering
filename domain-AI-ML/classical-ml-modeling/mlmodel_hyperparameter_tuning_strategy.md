---
title: "ML Hyperparameter Tuning Strategy"
category: AI-ML/classical-ml-modeling
description: "Design a hyperparameter optimization plan — search space, search method, budget, and a nested-CV protocol — that improves the model without quietly overfitting to the validation set."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - QA-12
  - DS-02
difficulty: advanced
tags:
  - hyperparameter-optimization
  - nested-cv
  - search-space
  - bayesian-optimization
  - overfitting
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/classical-ml-modeling/mlmodel_cross_validation_design.md
  - domain-AI-ML/classical-ml-modeling/mlmodel_overfitting_underfitting_diagnosis.md
  - domain-AI-ML/classical-ml-modeling/mlmodel_regularization_strategy.md
---

# ML Hyperparameter Tuning Strategy

**Objective:** Produce a concrete hyperparameter optimization (HPO) plan for a chosen model family: which hyperparameters to search and over what ranges, which search method fits the budget, how the search budget is allocated, and — critically — a validation protocol (nested CV or a held-out golden set) that prevents the reported score from being optimistically biased by repeated tuning against the same data.

**When to Use:**
- You have a baseline and a chosen family and want to extract more performance honestly.
- A model was "tuned" but the tuning protocol is unknown or suspected of overfitting the validation set.
- You need to defend a tuned model's reported metric as unbiased.

**When NOT to Use:**
- Before an honest baseline exists (use `mlmodel_baseline_modeling_plan.md`).
- To choose the model family (use `mlmodel_algorithm_selection_matrix.md`).
- When the real problem is fit diagnosis, not search (use `mlmodel_overfitting_underfitting_diagnosis.md`).

## Inputs / Context

Provide what you can:
- **Model family & framework** — e.g., LightGBM/XGBoost/sklearn (ask if unspecified) and the hyperparameters it exposes.
- **Compute & time budget** — how many model fits you can afford; parallelism available.
- **Current evaluation setup** — split/CV scheme, primary metric, current baseline score.
- **Data scale** — rows/columns; whether a single train fit is seconds or hours.
- **Priors** — any hyperparameters known to matter or known good ranges from related work.

## Constraints

**Must:**
- Separate the *tuning* loop from the *reporting* estimate — name how the final unbiased score is obtained (nested CV inner/outer, or a never-touched golden test set).
- Justify the search space ranges from the family's mechanics (e.g., learning rate × n_estimators tradeoff), not arbitrary defaults.
- Match the search method to the budget and dimensionality.

**Must Not:**
- Report the best inner-CV score as the model's expected performance — that is the optimistic, selection-biased number.
- Quote specific "optimal" hyperparameter values or expected gains as fact from memory; treat all values as illustrative and data-dependent.
- Expand the search space without a stopping/budget rule.

**Instructions:**

1. **Fix the objective and the honest estimator.** State the metric being optimized and the protocol that will yield the *unbiased* final estimate: nested CV (outer folds for reporting, inner folds for selection) or a sealed golden test set used exactly once.

2. **Select the search space.** List the hyperparameters worth tuning for this family, each with a range and scale (log vs linear) justified by mechanics — and explicitly exclude low-impact knobs to conserve budget.

3. **Choose the search method.** Map budget × dimensionality to a method: grid (tiny, low-dim), random (broad, cheap, good default), or Bayesian/sequential (expensive fits, higher dim). State why.

4. **Allocate the budget.** Set the number of trials/fits, early-stopping rules for individual fits, and any successive-halving/pruning to spend more on promising configs.

5. **Wire the leak-safe pipeline.** Ensure preprocessing is re-fit inside every inner fold so tuning cannot peek at validation data; coupled hyperparameters (e.g., learning rate ↔ n_estimators) are searched together.

6. **Define selection and tie-breaking.** Pick the config by mean inner-CV score, but prefer simpler/more-regularized configs within noise (one-standard-error rule) to reduce overfitting risk.

7. **Specify the final fit and reporting.** Refit on the full training data with the selected config; report the *outer-CV* (or golden-set) score as the expected performance, distinct from the best inner score.

8. **State the stop condition.** When to stop tuning (diminishing returns within noise, budget exhausted, or target met).

**Output Format:**

A markdown plan:
- **Objective & Honest-Estimate Protocol** — metric + nested CV / golden-set design.
- **Search Space** — table: hyperparameter | range | scale | rationale.
- **Search Method & Budget** — method choice, trial count, pruning/early stopping.
- **Leak-Safe Wiring** — pipeline-in-fold confirmation, coupled-param notes.
- **Selection Rule** — selection metric + one-SE / simplicity tie-break.
- **Final Fit & Reporting** — refit and which number is reported as expected performance.
- **Stop Condition** — when to declare done.

## Verification

- [ ] The reported-performance estimate is produced by a protocol distinct from the selection loop (nested CV or sealed golden set).
- [ ] Each tuned hyperparameter has a mechanically justified range and scale.
- [ ] The search method matches the budget and dimensionality, with reasoning.
- [ ] Preprocessing is confirmed re-fit inside inner folds.
- [ ] A simplicity/one-SE tie-break is specified.
- [ ] No hyperparameter values or gains are stated as fact; all are illustrative.

## False-Positive Prevention

❌ **DON'T:**
- Report the best inner-CV score as "the model's accuracy" — selecting the max over many trials inflates it.
- Tune against the same holdout repeatedly and treat its final score as unbiased.
- Search learning rate and n_estimators independently as if they were unrelated.
- Grid-search a 6-dimensional space and exhaust the budget on a coarse, mostly-useless lattice.

✅ **DO:**
- Use nested CV or a single-use golden set so the reported number reflects unseen-data performance.
- Treat the validation set as a consumable resource and count how many times it's been queried.
- Search coupled hyperparameters jointly and on the right scale (log for learning rate, regularization).
- Prefer the simplest config within one standard error of the best to curb tuning overfit.

## Example Output

```markdown
## HPO Strategy: Gradient-Boosted Trees (binary classification, PR-AUC)

### Objective & Honest-Estimate Protocol
- Optimize PR-AUC. Nested CV: 5 outer folds (reporting) × 4 inner folds (selection), grouped by customer_id to avoid leakage. The mean outer-fold PR-AUC is the reported number — never an inner-CV max.

### Search Space
| Hyperparameter | Range | Scale | Rationale |
|---|---|---|---|
| learning_rate | 0.01–0.3 | log | trades off with n_estimators; dominant knob |
| n_estimators | 100–2000 | linear | paired with LR via early stopping |
| num_leaves / max_depth | 15–255 / 3–10 | linear | controls capacity → variance |
| min_child_samples | 5–200 | log | regularization on small leaves |
| subsample / colsample | 0.6–1.0 | linear | variance reduction |
| reg_lambda | 1e-3–10 | log | L2 on leaf weights |

### Search Method & Budget
- Bayesian (TPE) — fits are ~minutes, space is 7-dim. ~80 trials, with early stopping (50 rounds no-improve) per fit, and successive-halving pruning of weak trials.

### Leak-Safe Wiring
- OOF target encoding + imputation re-fit inside each inner fold. learning_rate and n_estimators searched jointly via early stopping.

### Selection Rule
- Best mean inner PR-AUC, then one-SE rule: prefer the config with fewer leaves / higher regularization within one SE.

### Final Fit & Reporting
- Refit selected config on full training data. Report mean outer-fold PR-AUC ± SD as expected performance.

### Stop Condition
- Stop when the best outer estimate stops improving beyond noise across two halving rounds, or budget (80 trials) is spent.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** objective → space → method → wiring → reporting flow.
- **RT-02 (Multi-Dimensional Analysis Framework):** balances budget, dimensionality, and overfit risk.
- **CM-02 (Constraint Specification):** budget and the leak-safe boundary govern the design.
- **QA-12 (False Positives Identification):** central to separating selection score from reported score.
- **DS-02 (Metric Specification):** the tuned objective is matched to the decision.

**Related Prompts:**
- `mlmodel_cross_validation_design.md` — design the CV scheme the nested protocol relies on.
- `mlmodel_overfitting_underfitting_diagnosis.md` — diagnose whether tuning is chasing noise.
- `mlmodel_regularization_strategy.md` — many tuned knobs are regularization controls.
