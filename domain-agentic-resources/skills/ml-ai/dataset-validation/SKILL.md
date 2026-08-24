---
name: dataset-validation
description: Validate ML datasets for schema, distribution, leakage, label quality, and drift before training and at inference time. Use when onboarding a new dataset, when production accuracy regresses without code changes, or when you suspect train/test contamination.
metadata:
  tags:
    - ml
    - data-quality
    - validation
    - drift
    - leakage
  updated: "2026-05-05"
---

# Dataset Validation

Models fail because of data. Always. The harness catches it as a metric regression; this skill catches it before training even starts. Validate schema, distribution, label quality, leakage, and drift — automatically, on every dataset version.

## When to Use This Skill

- Onboarding a new dataset
- A model regressed in production with no code change (data drift suspected)
- A training run produced wildly different results than the last run
- You're about to train on a freshly-scraped or freshly-labeled corpus
- CI gate before any expensive training run

## What to Validate

### 1. Schema Conformance
- Column names, types, nullability
- Categorical values within expected vocabulary
- Numeric ranges within plausible bounds
- Tools: Pandera, Great Expectations, pydantic for record-level

### 2. Distribution Sanity
- Feature distributions vs. baseline (KS test, PSI, Jensen-Shannon)
- Class balance vs. expected proportions
- Categorical cardinality (sudden explosion = upstream bug)
- Missing-value rates per column

### 3. Train/Test/Val Leakage
- Hash-based identity overlap between splits
- Temporal leakage: any test timestamp before any train timestamp?
- Group leakage: same user/entity in multiple splits?
- Near-duplicate detection (text: minhash; embeddings: nearest-neighbor)

### 4. Label Quality
- Inter-annotator agreement (Cohen's kappa, Krippendorff's alpha)
- Label distribution per slice
- Suspicious patterns: all-positive batches, single-annotator monocultures
- Confidence-based filtering for noisy labels

### 5. Drift Detection (Production)
- Compare incoming inference data to training distribution
- Per-feature drift signals (PSI > 0.2 is a warning)
- Concept drift: same input distribution, different label distribution

## Validation Pipeline Skeleton

```python
# data/validate.py
from dataclasses import dataclass

@dataclass
class ValidationResult:
    passed: bool
    failures: list[str]
    warnings: list[str]
    summary: dict

def validate_dataset(path: str, baseline: BaselineStats) -> ValidationResult:
    df = load(path)
    failures, warnings = [], []

    # Schema
    schema_errors = validate_schema(df, EXPECTED_SCHEMA)
    failures.extend(schema_errors)

    # Distribution
    drift = compute_drift(df, baseline)
    for feature, psi in drift.items():
        if psi > 0.2:
            warnings.append(f"PSI({feature}) = {psi:.3f} — possible drift")
        if psi > 0.5:
            failures.append(f"PSI({feature}) = {psi:.3f} — significant drift")

    # Leakage (if multiple splits)
    if has_splits(df):
        overlap = identity_overlap(df)
        if overlap > 0:
            failures.append(f"Identity overlap between splits: {overlap} rows")
        temporal = temporal_leakage(df)
        if temporal:
            failures.append(f"Temporal leakage: test rows before train cutoff")

    # Label quality
    label_stats = analyze_labels(df)
    if label_stats.min_class_count < 100:
        warnings.append(f"Class imbalance: min count = {label_stats.min_class_count}")

    return ValidationResult(
        passed=len(failures) == 0,
        failures=failures,
        warnings=warnings,
        summary={"n_rows": len(df), "drift": drift, "labels": label_stats},
    )
```

## Schema Validation with Pandera

```python
import pandera as pa
from pandera.typing import Series

class TransactionSchema(pa.DataFrameModel):
    user_id: Series[str] = pa.Field(nullable=False)
    amount: Series[float] = pa.Field(ge=0, le=100_000)
    category: Series[str] = pa.Field(isin=["food", "transport", "entertainment", "other"])
    timestamp: Series[pa.DateTime] = pa.Field(nullable=False)
    is_fraud: Series[bool] = pa.Field(nullable=False)

    class Config:
        strict = True  # reject extra columns
        coerce = False  # don't silently convert types
```

## Drift Metric: PSI

```python
def population_stability_index(expected, actual, bins=10):
    """PSI < 0.1: no drift. 0.1-0.2: moderate. > 0.2: significant."""
    e_perc, _ = np.histogram(expected, bins=bins, density=False)
    a_perc, _ = np.histogram(actual, bins=bins, density=False)
    e_perc = e_perc / e_perc.sum()
    a_perc = a_perc / a_perc.sum()
    e_perc = np.where(e_perc == 0, 1e-6, e_perc)
    a_perc = np.where(a_perc == 0, 1e-6, a_perc)
    return float(np.sum((a_perc - e_perc) * np.log(a_perc / e_perc)))
```

## Leakage Checks

```python
def identity_overlap(df: pd.DataFrame, id_col="user_id", split_col="split") -> int:
    train_ids = set(df[df[split_col] == "train"][id_col])
    test_ids = set(df[df[split_col] == "test"][id_col])
    return len(train_ids & test_ids)

def temporal_leakage(df: pd.DataFrame, ts_col="timestamp", split_col="split") -> bool:
    train_max = df[df[split_col] == "train"][ts_col].max()
    test_min = df[df[split_col] == "test"][ts_col].min()
    return test_min <= train_max
```

## Implementation Checklist

- [ ] Schema is defined in code (Pandera/Great Expectations) and version-controlled
- [ ] Validation runs on every new dataset version
- [ ] Validation runs in CI before training jobs are allowed to start
- [ ] Baseline statistics are stored alongside the dataset version
- [ ] PSI or equivalent drift metric is computed per feature
- [ ] Leakage checks (identity, temporal, group) run on any multi-split dataset
- [ ] Label quality metrics are computed when annotations exist
- [ ] Validation result is serialized as an artifact alongside the dataset
- [ ] A "warnings" tier is distinct from "failures" — warnings inform, failures block
- [ ] Production inference monitoring uses the same drift detector as training-time validation

## Anti-Patterns to Avoid

- **Validating in a notebook** — not reproducible, not in CI
- **Only validating types, not values** — `amount = -1e9` passes a float type check
- **Random splits on time-series data** — temporal leakage is the default outcome
- **Ignoring near-duplicates** — text datasets are full of them
- **Validating only at training time** — production drift is invisible without runtime checks
- **Silent coercion** — letting Pandera/pydantic auto-convert "yes"/"no" to bool hides bugs
- **No baseline** — drift detection requires something to drift from

## Companion Skills

- `model-evaluation-harness` — uses validated test data
- `training-loop-scaffolding` — calls validate_dataset before kicking off training

## Related Resources

- ../../../domain-software-engineering/testing/testing_property_based_fuzzing.md
- Pandera: https://pandera.readthedocs.io
- Great Expectations: https://greatexpectations.io
