# Classical ML Modeling

Non-deep-learning modelling: algorithm choice, baselines, tuning, validation design, imbalance, regularization, ensembling, calibration, and fit diagnosis. For tabular problems this is usually where the answer is, and the baseline prompt is the one to run first.

**10 prompts.** Part of [`domain-AI-ML/`](../README.md) — see the domain README for the lifecycle routing table and the [boundary with adjacent domains](../README.md#boundary-with-adjacent-domains).

## When to enter here

- Choosing an approach for a tabular or structured problem.
- Diagnosing over- or under-fitting.
- Probabilities are used downstream and need to mean something.

**Not here:**
- The model is a neural network — [`../deep-learning/`](../deep-learning/README.md).
- The question is which metric to optimize or whether a result is real — [`../model-evaluation-validation/`](../model-evaluation-validation/README.md).

## Prompts


**Choose and baseline**

| Prompt | Use it to |
|---|---|
| [`mlmodel_algorithm_selection_matrix.md`](mlmodel_algorithm_selection_matrix.md) | Choose a model family for a tabular/classical ML problem by scoring candidates against task type, data size and shape, interpretability needs, and latency constraints in a transparent decision matrix. |
| [`mlmodel_baseline_modeling_plan.md`](mlmodel_baseline_modeling_plan.md) | Design the first honest model for a problem — a simple, leak-safe baseline plus the evaluation protocol that makes its score trustworthy and a fair reference for everything that follows. |
| [`mlmodel_interpretability_first_modeling.md`](mlmodel_interpretability_first_modeling.md) | Decide when to prefer an inherently interpretable model over a black box, and how to build a glass-box model (linear, rule-based, GAM/EBM, shallow tree) that meets the explainability mandate without surrendering too much performance. |

**Validate and tune**

| Prompt | Use it to |
|---|---|
| [`mlmodel_cross_validation_design.md`](mlmodel_cross_validation_design.md) | Choose the cross-validation scheme that matches the data's structure — k-fold, stratified, grouped, or time-series — so the estimated performance reflects real-world generalization instead of a leaky fold split. |
| [`mlmodel_hyperparameter_tuning_strategy.md`](mlmodel_hyperparameter_tuning_strategy.md) | Design a hyperparameter optimization plan — search space, search method, budget, and a nested-CV protocol — that improves the model without quietly overfitting to the validation set. |

**Diagnose and correct**

| Prompt | Use it to |
|---|---|
| [`mlmodel_overfitting_underfitting_diagnosis.md`](mlmodel_overfitting_underfitting_diagnosis.md) | Read learning and validation curves to diagnose whether a model is overfitting (high variance) or underfitting (high bias), then prescribe targeted remedies matched to the diagnosis. |
| [`mlmodel_regularization_strategy.md`](mlmodel_regularization_strategy.md) | Diagnose excess variance and prescribe the right regularization — L1/L2/elastic-net, early stopping, or tree/complexity constraints — matched to the model family and the evidence of overfitting. |
| [`mlmodel_imbalanced_classification_approach.md`](mlmodel_imbalanced_classification_approach.md) | Design an end-to-end approach to class imbalance — metric choice, resampling vs class weighting, decision-threshold tuning, and leak-safe evaluation — anchored to the real cost of each error type. |

**Improve and calibrate**

| Prompt | Use it to |
|---|---|
| [`mlmodel_ensembling_strategy.md`](mlmodel_ensembling_strategy.md) | Decide whether and how to ensemble — bagging, boosting, or stacking — by weighing the error-decorrelation payoff against the real risks: correlated base learners, stacking leakage, and runaway complexity. |
| [`mlmodel_probability_calibration.md`](mlmodel_probability_calibration.md) | Assess whether a classifier's predicted probabilities are trustworthy (reliability curve, ECE, Brier) and, if not, apply and validate the right calibration method — Platt, isotonic, or temperature scaling — on held-out data. |

## Conventions

- **Prefix:** `mlmodel_` — one prefix per subdirectory, so a filename identifies its home.
- **Frontmatter:** the domain's eight fields — `title`, `category` (`AI-ML/classical-ml-modeling`), `description`, `techniques` (validated against `techniques/MASTER_TECHNIQUE_INDEX.md`), `difficulty`, `tags`, `updated`, `related_prompts`.
- **Structure:** five H2 sections — `Inputs / Context`, `Constraints`, `Verification`, `False-Positive Prevention`, `Example Output` — with `Objective`, `When to Use`, `When NOT to Use`, `Instructions`, `Output Format`, `Techniques Used`, `Related Prompts` as bold labels inside them.
- **No fabrication:** no invented benchmark numbers, accuracy figures, SOTA claims, or dataset statistics. Quantities that would change a decision are marked for measurement or verification.
- **Framework-neutral:** the user names the stack; prompts avoid hardcoding APIs that drift.

## What lives elsewhere

- Calibration *assessment* as an evaluation activity → [`../model-evaluation-validation/mleval_calibration_assessment.md`](../model-evaluation-validation/mleval_calibration_assessment.md).
- Interpretability as a governance obligation → [`../responsible-ai-governance/rai_interpretability_analysis.md`](../responsible-ai-governance/rai_interpretability_analysis.md).
