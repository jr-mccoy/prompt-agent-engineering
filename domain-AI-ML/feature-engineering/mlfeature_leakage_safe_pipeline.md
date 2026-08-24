---
title: "Leakage-Safe Feature Pipeline"
category: AI-ML/feature-engineering
description: "Design a preprocessing and feature pipeline that fits only on training folds and cannot leak the target or the holdout — the structural defense behind the leakage detector."
techniques:
  - ST-02
  - CM-02
  - RT-05
  - DS-02
  - QA-12
difficulty: advanced
tags:
  - leakage-prevention
  - pipeline
  - cross-validation
  - train-serve-consistency
  - feature-engineering
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/data-for-ml/mldata_data_leakage_detector.md
  - domain-AI-ML/feature-engineering/mlfeature_encoding_strategy.md
  - domain-AI-ML/feature-engineering/mlfeature_store_design.md
---

# Leakage-Safe Feature Pipeline

**Objective:** Specify a preprocessing and feature pipeline whose every fitted step (imputation, scaling, encoding, selection, resampling) is fit on training folds only and applied to validation/serving data without peeking — so cross-validation estimates are honest and the same transforms run identically offline and online.

**When to Use:**
- Building the feature pipeline for a new model from the start.
- A leakage audit found preprocessing fit on the full dataset and you need the corrected design.
- You need offline training and online serving to apply identical transforms.

**When NOT to Use:**
- You're hunting for existing leaks rather than designing the pipeline (use `mldata_data_leakage_detector.md`).
- You need a feature store architecture spanning many models (use `mlfeature_store_design.md`).

## Inputs / Context

Provide what you can (ask for framework + version if code is expected):
- **Preprocessing steps** in play — imputation, scaling, encoding, selection, resampling (SMOTE), dimensionality reduction.
- **Validation scheme** — random/stratified/grouped/temporal CV; entity groups.
- **Target & prediction-time boundary** — when the label is known; when inference happens.
- **Serving context** — online vs batch; how features are computed at inference.
- **Any stateful/aggregate features** — windowed counts, target encodings, embeddings.

## Constraints

**Must:**
- Place every fitted transform inside the CV loop / a single pipeline object so it is fit on train folds only.
- Order steps so target-dependent steps (target encoding, supervised selection, resampling) are fit out-of-fold and never see the holdout.
- Ensure the identical transform code path is used at serving (no separate offline-only logic).

**Must Not:**
- Fit scalers/encoders/imputers/selectors on the full dataset before splitting.
- Apply resampling (SMOTE etc.) before the split or to validation folds.
- Invent that a step is leak-safe without tracing its fit/transform boundary; if unknown, mark it to verify.

**Instructions:**

1. **Map the fit/transform boundary of every step.** For each preprocessing step, state what it *learns* (statistics, vocabularies, weights) and confirm that learning happens on train folds only.

2. **Order the pipeline correctly.** Sequence steps so that supervised/target-dependent ones run after the split and are fit out-of-fold; unsupervised steps still must fit on train folds, not all data.

3. **Quarantine resampling.** Place class-resampling (SMOTE, undersampling) inside the CV loop on training data only — never on validation folds or before the split.

4. **Constrain windowed/aggregate features.** Ensure rolling counts, target encodings, and time-aggregates use only data strictly before the prediction-time boundary, computed per fold.

5. **Unify offline and online code paths.** Specify that the same pipeline (serialized) computes features at training and serving, so train/serve skew can't arise from divergent logic.

6. **Add a nested-CV plan for tuning.** If hyperparameters are tuned, require nested CV so selection/encoding/HPO don't overfit a reused holdout.

7. **Define verification probes.** Specify checks that would reveal a leak (e.g., metric drop when a step is correctly moved inside CV) and the train-vs-serve feature parity check.

**Output Format:**

A markdown pipeline spec:
- **Step-by-Step Fit/Transform Map** — table: Step | Learns | Fit on | Leakage risk if misplaced.
- **Pipeline Order** — the corrected sequence.
- **Resampling & Windowed-Feature Rules**
- **Offline/Online Parity** — how the same transforms serve inference.
- **Nested-CV / Tuning Plan**
- **Verification Probes** — tests that catch a regression to leaky behavior.

## Verification

- [ ] Every fitted step's fit-on scope is stated as train-folds-only.
- [ ] Target-dependent steps are out-of-fold; resampling is inside CV on train only.
- [ ] Windowed/aggregate features respect the prediction-time boundary, computed per fold.
- [ ] The same transform path is used offline and online (skew controlled).
- [ ] Nested CV is used when tuning.
- [ ] No step is asserted leak-safe without tracing its boundary.

## False-Positive Prevention

❌ **DON'T:**
- Fit a StandardScaler/imputer/encoder on the whole dataset and then split — test statistics bleed into training.
- Run SMOTE before the train/test split or on validation data — it manufactures optimistic recall.
- Compute a target encoding once over all rows — it leaks the label into every fold.
- Maintain separate offline and online feature code — they drift and create train/serve skew that no CV catches.

✅ **DO:**
- Wrap all transforms in one pipeline object fit inside each CV fold.
- Keep resampling and supervised selection strictly on the training portion of each fold.
- Constrain every aggregate to past-only windows relative to the prediction time.
- Serialize the fitted pipeline and reuse it verbatim at serving; add a feature-parity probe.

## Example Output

```markdown
## Leakage-Safe Pipeline: Loan Default Model (5-fold grouped CV on customer_id)

### Step-by-Step Fit/Transform Map
| Step | Learns | Fit on | Risk if misplaced |
|---|---|---|---|
| Imputer (median) | column medians | train fold | uses test stats |
| Target encoder (merchant) | OOF means + smoothing | train fold (OOF) | leaks label |
| Supervised selection (L1) | feature subset | train fold | selects using holdout |
| Scaler | mean/std | train fold | test bleeds in |
| SMOTE | synthetic minority | train fold only | inflates recall |
| Model | weights | train fold | — |

### Pipeline Order
impute → OOF target-encode → scale → (within-fold) SMOTE → supervised select → model.
All inside GroupKFold(customer_id); the holdout fold sees only transform(), never fit().

### Resampling & Windowed-Feature Rules
SMOTE applied only to each fold's training rows. Rolling features use windows ending before
application_ts, recomputed per fold.

### Offline/Online Parity
Serialize the fitted Pipeline; serving calls the same transform path. No offline-only feature SQL.

### Nested-CV / Tuning Plan
Outer 5-fold for estimation; inner CV for HPO + selection so the outer holdout stays untouched.

### Verification Probes
- Expect a metric DROP when scaler/encoder move from full-data to in-CV (the drop is the true signal).
- Train-vs-serve feature parity check on a sample of live requests.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** map boundaries → order → quarantine → unify → verify.
- **CM-02 (Constraint Specification):** the train-folds-only and prediction-time-boundary rules govern the design.
- **RT-05 (Evidence-Based Reasoning):** each step's leak risk is justified by what it learns.
- **DS-02 (Metric Specification):** uses the expected metric drop as a leak-detection probe.
- **QA-12 (False Positives Identification):** structurally prevents the leaks the detector hunts for.

**Related Prompts:**
- `mldata_data_leakage_detector.md` — the audit this pipeline is the structural answer to.
- `mlfeature_encoding_strategy.md` — supplies the OOF target-encoding detail.
- `mlfeature_store_design.md` — extends offline/online parity across many models.
