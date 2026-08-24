# Feature Engineering

Turning data into the inputs a model actually consumes — ideation, selection, encoding, leak-safe pipelines, importance, and the feature-store decision. The leakage-safe pipeline prompt is the one most worth reading before anything else here.

**9 prompts.** Part of [`domain-AI-ML/`](../README.md) — see the domain README for the lifecycle routing table and the [boundary with adjacent domains](../README.md#boundary-with-adjacent-domains).

## When to enter here

- Deciding what features to build, or which of many to keep.
- A model performs suspiciously well and the feature pipeline is the suspect.
- Training and serving compute features differently and you need them not to.

**Not here:**
- The question is about the raw data rather than derived features — [`../data-for-ml/`](../data-for-ml/README.md).
- The features are text, image, or audio representations — see the relevant [`../specialized-ml/`](../specialized-ml/README.md) vertical.

## Prompts


**Build and select**

| Prompt | Use it to |
|---|---|
| [`mlfeature_ideation_workshop.md`](mlfeature_ideation_workshop.md) | Systematically brainstorm candidate features from domain knowledge and available data, framed as testable hypotheses with a defined availability-at-prediction-time check. |
| [`mlfeature_selection_strategy.md`](mlfeature_selection_strategy.md) | Choose a feature-selection approach (filter, wrapper, embedded) appropriate to data size, model, and goal — without leaking the target or selecting on the test set. |
| [`mlfeature_encoding_strategy.md`](mlfeature_encoding_strategy.md) | Choose encodings for categorical, numeric, text, and datetime features — including high-cardinality handling and the target-encoding leakage trap — matched to the model and pipeline. |
| [`mlfeature_importance_analysis.md`](mlfeature_importance_analysis.md) | Interpret feature importance correctly — permutation, SHAP, and model-native scores — without sliding from correlation into causal claims or being fooled by collinearity and leakage. |

**Keep it correct**

| Prompt | Use it to |
|---|---|
| [`mlfeature_leakage_safe_pipeline.md`](mlfeature_leakage_safe_pipeline.md) | Design a preprocessing and feature pipeline that fits only on training folds and cannot leak the target or the holdout — the structural defense behind the leakage detector. |
| [`mlfeature_drift_audit.md`](mlfeature_drift_audit.md) | Audit individual features for distribution drift over time against a reference window, with significance and magnitude thresholds — and decide which drift actually matters. |

**Feature stores**

| Prompt | Use it to |
|---|---|
| [`mlfeature_store_design.md`](mlfeature_store_design.md) | Design a feature store with offline/online consistency so the same feature values are used for training and serving — eliminating train/serve skew at the source. |
| [`mlfeature_feast_feature_store_playbook.md`](mlfeature_feast_feature_store_playbook.md) | Stand up Feast for ML feature serving — entities, feature views, offline/online stores, point-in-time-correct training retrieval, and materialization — so training and serving share consistent features without train/serve skew, and without inventing version-specific API behavior. |
| [`mlfeature_tecton_feature_store_playbook.md`](mlfeature_tecton_feature_store_playbook.md) | Design an ML feature workflow on Tecton — feature views/services, batch/stream/on-demand feature types, offline training retrieval and online serving, freshness SLAs, and train/serve consistency — without inventing version-specific API behavior or pricing. |

## Conventions

- **Prefix:** `mlfeature_` — one prefix per subdirectory, so a filename identifies its home.
- **Frontmatter:** the domain's eight fields — `title`, `category` (`AI-ML/feature-engineering`), `description`, `techniques` (validated against `techniques/MASTER_TECHNIQUE_INDEX.md`), `difficulty`, `tags`, `updated`, `related_prompts`.
- **Structure:** five H2 sections — `Inputs / Context`, `Constraints`, `Verification`, `False-Positive Prevention`, `Example Output` — with `Objective`, `When to Use`, `When NOT to Use`, `Instructions`, `Output Format`, `Techniques Used`, `Related Prompts` as bold labels inside them.
- **No fabrication:** no invented benchmark numbers, accuracy figures, SOTA claims, or dataset statistics. Quantities that would change a decision are marked for measurement or verification.
- **Framework-neutral:** the user names the stack; prompts avoid hardcoding APIs that drift.

## What lives elsewhere

- Feature *pipeline* orchestration and serving → [`../mlops-infrastructure/mlops_feature_pipeline_design.md`](../mlops-infrastructure/mlops_feature_pipeline_design.md).
- Feature importance as an explainability requirement → [`../responsible-ai-governance/rai_explainability_plan.md`](../responsible-ai-governance/rai_explainability_plan.md).
