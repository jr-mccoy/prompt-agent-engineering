---
title: "Feature Encoding Strategy"
category: AI-ML/feature-engineering
description: "Choose encodings for categorical, numeric, text, and datetime features — including high-cardinality handling and the target-encoding leakage trap — matched to the model and pipeline."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - DS-02
  - QA-12
difficulty: intermediate
tags:
  - encoding
  - categorical
  - high-cardinality
  - target-encoding
  - leakage-aware
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/feature-engineering/mlfeature_leakage_safe_pipeline.md
  - domain-AI-ML/feature-engineering/mlfeature_selection_strategy.md
  - domain-AI-ML/data-for-ml/mldata_data_leakage_detector.md
---

# Feature Encoding Strategy

**Objective:** Recommend encoding choices for each feature type — categorical (incl. high-cardinality), numeric, datetime, and text — matched to the model family and serving constraints, with explicit guardrails against the target-encoding leakage trap and against encodings fit on the full dataset.

**When to Use:**
- You've selected features and must decide how to represent each for the model.
- A categorical feature has high cardinality and one-hot is impractical.
- Target/mean encoding is being considered and you want to avoid leaking the label.

**When NOT to Use:**
- You haven't chosen features yet (use `mlfeature_selection_strategy.md`).
- You suspect existing encodings already leaked (use `mldata_data_leakage_detector.md`).

## Inputs / Context

Provide what you can (ask for framework + version if code is expected):
- **Feature inventory** — name, type, cardinality (for categoricals), and rough distribution.
- **Model family** — tree ensemble, linear, neural — encoding suitability differs.
- **Target & task** — needed to assess target-encoding risk.
- **Validation setup** — split/CV scheme (target encoding must be fit out-of-fold).
- **Serving constraints** — online latency, vocabulary updates, unseen-category handling.

## Constraints

**Must:**
- Recommend an encoding per feature type, justified by the model family and cardinality.
- For any target/mean/frequency encoding, mandate out-of-fold (or train-fold-only) fitting and describe the leakage if not.
- Specify handling of unseen categories at serving time and missing values per encoding.

**Must Not:**
- Recommend target encoding fit on the full dataset (it leaks the label into every row).
- Invent cardinalities or distributions — mark unknowns and how to check.
- One-hot a very-high-cardinality feature without flagging the dimensionality/sparsity cost.

**Instructions:**

1. **Group features by type and cardinality.** Bucket into low-card categorical, high-card categorical, numeric, datetime, and text — the encoding decision differs per bucket.

2. **Match encoding to model family.** Trees tolerate ordinal/label encoding and need less scaling; linear/NN models need one-hot or learned embeddings and benefit from scaling. State the rationale.

3. **Handle high cardinality deliberately.** For many-level categoricals, weigh frequency encoding, hashing, learned embeddings, or carefully-fit target encoding — each with its tradeoff (collision, leakage risk, cold start).

4. **Make target/mean encoding leakage-safe.** If used, require out-of-fold encoding within CV and train-fold statistics at fit time, with smoothing for rare levels. Describe the metric inflation that occurs if fit on all data.

5. **Encode numeric and datetime thoughtfully.** Decide scaling/transforms for numerics (and whether the model needs them); decompose datetimes into cyclical/seasonal/elapsed components rather than raw timestamps.

6. **Plan text representation.** Choose among bag-of-words/TF-IDF, hashing, or embeddings per the model and latency budget; note vocabulary management and OOV handling.

7. **Specify serving-time behavior.** State unseen-category handling, missing-value strategy, and how encoders are persisted/fit-once to avoid train/serve skew.

**Output Format:**

A markdown encoding plan:
- **Per-Feature Encoding Table** — Feature | Type | Cardinality | Chosen encoding | Rationale | Leakage/skew note.
- **High-Cardinality Plan** — method + tradeoff.
- **Target-Encoding Guardrails** — OOF protocol + smoothing (if used).
- **Numeric/Datetime/Text Notes**
- **Serving-Time Rules** — unseen categories, missing values, fit-once persistence.
- **Open Checks** — cardinalities/distributions to verify.

## Verification

- [ ] Each feature type has a justified encoding matched to the model.
- [ ] Any target/frequency encoding specifies OOF/train-only fitting + smoothing.
- [ ] High-cardinality handling is explicit with its tradeoff.
- [ ] Unseen-category and missing-value handling are defined for serving.
- [ ] Encoders are specified as fit-on-train-only to prevent skew.
- [ ] No cardinality/distribution is invented; unknowns are flagged.

## False-Positive Prevention

❌ **DON'T:**
- Fit target/mean encoding on the entire dataset — every row then carries information about its own label, inflating CV and collapsing in production.
- One-hot a 50k-level ID column — it explodes dimensionality and overfits; use hashing/embeddings.
- Feed raw timestamps to the model when cyclical/seasonal/elapsed decompositions carry the actual signal.
- Forget unseen categories at serving — an encoder that errors on a new level breaks production.

✅ **DO:**
- Use out-of-fold target encoding with smoothing for rare levels, fit inside the CV loop.
- Match encoding to the model: ordinal/label for trees, one-hot/embeddings for linear/NN.
- Decompose datetimes and decide scaling based on whether the model needs it.
- Define explicit fallbacks for unseen categories and missing values, and persist fit-once encoders.

## Example Output

```markdown
## Encoding Plan: Transaction Risk Model (gradient-boosted trees)

### Per-Feature Encoding
| Feature | Type | Cardinality | Encoding | Rationale | Leakage/skew note |
|---|---|---|---|---|---|
| merchant_category | categorical | ~300 | frequency encoding | trees handle it; avoids one-hot blowup | fit on train folds only |
| merchant_id | categorical | ~80k | hashing (2^16) or OOF target enc | too high for one-hot | if target enc: OOF + smoothing |
| amount | numeric | — | none (trees) / log for linear | trees split raw fine | — |
| txn_timestamp | datetime | — | hour-of-day (cyclical), day-of-week, days_since_signup | seasonality carries signal | windows must be past-only |
| device_str | text | — | hashing vectorizer | low-latency serving | OOV via hashing |

### High-Cardinality Plan
merchant_id: prefer hashing for serving simplicity; OOF target encoding only if lift justifies
the leakage-control overhead.

### Target-Encoding Guardrails (if used)
Fit per training fold (out-of-fold means), smoothing toward global mean for rare merchants.
Fitting on all rows would inflate AUC and not reproduce online.

### Serving-Time Rules
Unseen merchant_id → hash bucket / global prior; missing category → dedicated "unknown" level;
encoders persisted and fit-once from training.

### Open Checks
Confirm merchant_id cardinality and the rare-level tail; verify timestamp coverage.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** group → match model → high-card → target-safe → serving.
- **RT-02 (Multi-Dimensional Analysis Framework):** trades dimensionality, leakage risk, and serving cost.
- **CM-02 (Constraint Specification):** train-only fitting and unseen-category handling are hard rules.
- **DS-02 (Metric Specification):** ties target-encoding misuse to metric inflation.
- **QA-12 (False Positives Identification):** centers on the target-encoding leakage trap.

**Related Prompts:**
- `mlfeature_leakage_safe_pipeline.md` — where OOF encoding is implemented safely.
- `mlfeature_selection_strategy.md` — selection precedes encoding decisions.
- `mldata_data_leakage_detector.md` — audit if encodings may have already leaked.
