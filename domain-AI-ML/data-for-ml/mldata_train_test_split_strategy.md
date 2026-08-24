---
title: "ML Train/Test Split Strategy"
category: AI-ML/data-for-ml
description: "Choose a leak-safe split scheme — random, stratified, grouped, or temporal — and ratios that match how the model will be used, so offline validation reflects production performance."
techniques:
  - ST-02
  - RT-02
  - DT-04
  - CM-02
  - QA-12
difficulty: intermediate
tags:
  - train-test-split
  - cross-validation
  - temporal-split
  - grouped-split
  - validation-design
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/data-for-ml/mldata_data_leakage_detector.md
  - domain-AI-ML/data-for-ml/mldata_class_imbalance_strategy.md
  - domain-AI-ML/data-for-ml/mldata_sampling_bias_audit.md
---

# ML Train/Test Split Strategy

**Objective:** Recommend a train/validation/test split scheme (random, stratified, grouped, temporal, or a combination) and the ratios/fold design that make offline validation a faithful estimate of production performance — and that are *leak-safe* by construction.

**When to Use:**
- Setting up validation for a new model and you must decide how to partition the data.
- Offline metrics don't transfer to production and you suspect the split, not the model.
- The data has structure (time order, grouped entities, rare classes) that a naive random split would violate.

**When NOT to Use:**
- You suspect leakage is already present and want to hunt it (use `mldata_data_leakage_detector.md`) — though this prompt is its prevention counterpart.
- You only need to handle class imbalance within a chosen split (use `mldata_class_imbalance_strategy.md`).

## Inputs / Context

Provide what you can; the recommendation degrades gracefully if some are missing:
- **Task & prediction-time boundary** — what is predicted and *when* inference happens relative to the data.
- **Data structure** — is there a time order? grouped entities (user/device/patient) with multiple rows? a hierarchy?
- **Target distribution** — class balance, rare classes, or continuous-target range.
- **Deployment scenario** — will the model score *new entities*, *future time periods*, or both? This is the question the split must mimic.
- **Volume** — rows and counts of the smallest important group/class.
- **Preprocessing pipeline** — what is fit on the data (scalers, encoders, resampling) and where.

## Constraints

**Must:**
- Pick the split scheme by matching it to the *deployment scenario* (new entity vs future time vs new distribution), not by default to random.
- Make the scheme leak-safe: preprocessing fit on train folds only; grouped entities never straddle folds; temporal order respected when relevant.
- Reserve a true held-out test set untouched by tuning, distinct from the validation/CV used for model selection.

**Must Not:**
- Recommend a specific ratio or fold count as universally optimal — tie it to data volume and the smallest group/class count.
- Use a random split when entities repeat across rows or when the process is time-ordered, without flagging the leakage it causes.
- Assume class proportions are preserved without stratification when classes are rare.

**Instructions:**

1. **Identify the prediction scenario.** Determine whether production scores brand-new entities, future time windows, or a shifted population — the split must reproduce that gap between train and test.

2. **Detect blocking data structure.** Check for repeated entities (grouping), time ordering (temporal), and rare classes (stratification need). Each rules certain schemes in or out.

3. **Select the split scheme.** Map structure → scheme: grouped entities → GroupKFold/grouped holdout; time order → temporal/forward-chaining split; rare classes + i.i.d. → stratified; genuinely i.i.d. → random. Combine when needed (e.g., grouped + temporal).

4. **Set ratios and fold design.** Choose train/val/test proportions or k folds from data volume and the smallest important group/class count, ensuring each split has enough of every class/group to estimate metrics.

5. **Place preprocessing inside the split.** Specify that scalers, encoders, imputers, feature selection, and resampling are fit on train folds only — and call out exactly where leakage would occur if not.

6. **Reserve the golden test set.** Define a final holdout (and, for time data, the most recent window) that is never used for tuning, plus nested CV if hyperparameters are searched.

7. **Stress-test the split for leakage.** Confirm no entity, near-duplicate, or future-derived feature crosses the boundary; cross-link the leakage detector for a full audit.

8. **State expected metric implications.** Note how the chosen scheme will likely change reported metrics versus a naive random split, so the team interprets the (often lower, more honest) numbers correctly.

**Output Format:**

A markdown recommendation:
- **Prediction Scenario & Data Structure** — what production does; grouping/time/rarity flags.
- **Recommended Scheme** — scheme + rationale tied to scenario and structure.
- **Ratios / Fold Design** — proportions or k, justified by volume and smallest class/group.
- **Leak-Safe Pipeline Placement** — where each preprocessing step is fit.
- **Golden Test Set & HPO Protocol** — final holdout + nested CV if tuning.
- **Expected Metric Implications** — how honest numbers will differ from naive random.

## Verification

- [ ] The scheme is justified by the deployment scenario (new entity / future time / shift), not chosen by default.
- [ ] Grouping, temporal order, and rare-class needs were each checked and addressed or marked N/A.
- [ ] Ratios/fold count are tied to volume and the smallest important class/group count.
- [ ] Preprocessing is explicitly fit on train-only, with the leakage point named.
- [ ] A true golden test set (and recent-window holdout for time data) is reserved from tuning.

## False-Positive Prevention

❌ **DON'T:**
- Default to a random k-fold when the same user/device/patient appears in many rows — that leaks identity and inflates metrics.
- Use a random split on time-ordered data, letting the model "see the future" during validation.
- Pick 80/20 reflexively when a rare class then has too few test examples to estimate its metric.
- Fit scalers/encoders/SMOTE on the full dataset before splitting and call the split "clean."

✅ **DO:**
- Match the split to what production actually does (score new entities vs future periods) and reproduce that gap.
- Use grouped and/or temporal splits when structure demands, even though numbers drop — that drop is honesty.
- Size folds so every important class/group has enough examples in each split to be measured.
- Fit all preprocessing inside the training folds and reserve an untouched golden test set.

## Example Output

```markdown
## Split Strategy: Churn Prediction (monthly snapshots, repeat customers)

### Prediction Scenario & Data Structure
- Production scores *existing customers* for *next-month* churn → both grouped AND temporal.
- Structure: customers appear in many monthly rows (grouping); strong time order; churn ~7% (rare class).

### Recommended Scheme
- Temporal split as the primary axis (train on months ≤ T, test on T+1..T+3), with grouping enforced so a
  customer never trains and tests in the same fold. Stratify the validation metric by churn class.
- Rationale: mirrors "predict next month for known customers"; prevents both future-leak and identity-leak.

### Ratios / Fold Design
- Forward-chaining CV over 5 expanding time windows; final test = most recent 3 months.
- Each test window has ≥1,200 churners (≥ the floor needed to estimate recall stably).

### Leak-Safe Pipeline Placement
- Imputer, target-encoder (OOF), scaler all fit on the training window only, re-fit per fold.

### Golden Test Set & HPO Protocol
- Last 3 months held out untouched; hyperparameters tuned via nested forward-chaining on earlier windows.

### Expected Metric Implications
- AUC will likely fall vs a naive random split (which leaked customer identity + future). Treat the lower,
  temporally-honest AUC as the real estimate; cross-check with the leakage detector before trusting it.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** scenario → structure → scheme → ratios → pipeline → holdout.
- **RT-02 (Multi-Dimensional Analysis Framework):** weighs grouping, time order, and class rarity jointly.
- **DT-04 (Decision Criteria Specification):** explicit structure-→-scheme mapping rules.
- **CM-02 (Constraint Specification):** prediction-time boundary and leak-safety govern the design.
- **QA-12 (False Positives Identification):** preempts the classic split-induced leakage patterns.

**Related Prompts:**
- `mldata_data_leakage_detector.md` — audit the chosen split for residual leakage.
- `mldata_class_imbalance_strategy.md` — handle rare classes within the split you chose.
- `mldata_sampling_bias_audit.md` — confirm the partitions reflect the deployment population.
