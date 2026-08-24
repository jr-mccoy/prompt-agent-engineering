---
name: model-evaluation-harness
description: Build a reproducible evaluation harness for ML models — fixed test sets, deterministic seeds, slice-based metrics, regression gates, and result serialization. Use when standing up a new model project, when "model accuracy" needs to be defended in PRs, or when CI keeps shipping silently-worse models.
metadata:
  tags:
    - ml
    - evaluation
    - testing
    - mlops
    - regression-gates
  updated: "2026-05-05"
---

# Model Evaluation Harness

A model isn't done because the loss went down. It's done because you can answer, every time: "Is this version better than the last, on which slices, by how much, with what confidence?" This skill gives you a harness that survives team turnover, framework changes, and the impulse to optimize a single number.

## When to Use This Skill

- New ML project — set up evaluation before training the first model
- Existing project where "did the model get better?" is hard to answer
- A model regressed in production and the team can't reproduce the prior eval
- You need a CI gate that blocks merges on metric regression
- Stakeholders ask for slice-level performance (per-segment, per-cohort)

## Core Principles

1. **Eval is a contract, not a script.** It defines what "better" means before you train.
2. **The test set is frozen.** Adding examples requires a versioned dataset bump.
3. **Determinism is mandatory.** Seed everything. If results vary, the harness is broken.
4. **Slices matter more than aggregates.** A 92% average can hide a 40% on a critical cohort.
5. **Metrics are stored, not just printed.** Every run produces an artifact you can diff.

## Components of a Harness

### 1. Frozen Test Set

```
data/
  test_v1.parquet          # Frozen — never edited
  test_v1.sha256           # Hash committed to git
  test_versions.md         # Changelog of dataset versions
```

- Hash the test file. Verify on every eval run.
- New examples → `test_v2.parquet`, never overwrite v1.
- Track which model version was evaluated against which test version.

### 2. Slice Definitions

Define slices in code, not in notebooks:

```python
# eval/slices.py
SLICES = {
    "all": lambda df: df,
    "high_value_users": lambda df: df[df["ltv"] > 1000],
    "new_users": lambda df: df[df["account_age_days"] < 30],
    "language_es": lambda df: df[df["lang"] == "es"],
    "edge_long_text": lambda df: df[df["input_len"] > 500],
}
```

- Each slice gets every metric computed.
- A failure on one slice can block the merge even if "all" improves.

### 3. Metric Definitions

```python
# eval/metrics.py
def precision_at_k(y_true, y_pred, k=10):
    ...

def calibration_error(y_true, y_prob, bins=10):
    ...

METRICS = {
    "precision@10": precision_at_k,
    "ece": calibration_error,
    "p95_latency_ms": latency_p95,
}
```

- Include latency and cost as first-class metrics, not afterthoughts.
- Document each metric: what it measures, what range is good, what's a regression.

### 4. Deterministic Run Configuration

```python
# eval/config.py
@dataclass(frozen=True)
class EvalConfig:
    model_version: str
    test_set_version: str
    seed: int = 42
    batch_size: int = 32
    slices: list[str] = field(default_factory=lambda: list(SLICES.keys()))
    metrics: list[str] = field(default_factory=lambda: list(METRICS.keys()))

def run_eval(model, config: EvalConfig) -> EvalResult:
    set_all_seeds(config.seed)
    verify_test_set_hash(config.test_set_version)
    ...
```

### 5. Result Serialization

```json
{
  "run_id": "2026-05-05T14-22-09Z-a3f2b1",
  "model_version": "ranker-v0.4.2",
  "test_set_version": "test_v1",
  "config_hash": "sha256:9c4...",
  "git_sha": "a3f2b1c",
  "slices": {
    "all": {"precision@10": 0.843, "ece": 0.041, "p95_latency_ms": 87, "n": 12450},
    "high_value_users": {"precision@10": 0.912, "ece": 0.038, "p95_latency_ms": 91, "n": 1240},
    "new_users": {"precision@10": 0.671, "ece": 0.082, "p95_latency_ms": 84, "n": 3120}
  },
  "compared_to": "ranker-v0.4.1",
  "deltas": {
    "all.precision@10": "+0.012",
    "new_users.precision@10": "-0.024"
  }
}
```

- Store in object storage with run_id as the key.
- The model registry links each model version to its eval artifact.

### 6. Regression Gate

```python
# eval/gate.py
def check_regression(current: EvalResult, baseline: EvalResult) -> list[GateFailure]:
    failures = []
    for slice_name, metrics in current.slices.items():
        for metric_name, value in metrics.items():
            baseline_value = baseline.slices[slice_name][metric_name]
            threshold = THRESHOLDS[metric_name]  # absolute or relative
            if regressed(value, baseline_value, threshold):
                failures.append(GateFailure(slice_name, metric_name, value, baseline_value))
    return failures
```

- CI calls this on every PR that touches model code.
- Block merge on any failure unless overridden with documented justification.

## Implementation Checklist

- [ ] Test set is in object storage, hashed, and version-pinned
- [ ] Test set hash is verified on every eval run
- [ ] All randomness is seeded (numpy, torch, random, dataset shuffling)
- [ ] Slices are defined in code, not notebooks
- [ ] At least one slice represents an underrepresented or failure-prone cohort
- [ ] Latency and cost metrics are included alongside accuracy metrics
- [ ] Eval results are serialized to JSON and stored with run_id
- [ ] Each result includes config hash and git SHA
- [ ] Comparison against baseline is automated
- [ ] Regression gate runs in CI
- [ ] Slice-level regressions can fail the gate even when aggregate improves
- [ ] Eval runs are reproducible from run_id alone

## Anti-Patterns to Avoid

- **Aggregate-only reporting** ("the model got 0.4% better" hides slice regressions)
- **Notebook-only evals** (not reproducible, not in CI, not diff-able)
- **Drifting test sets** (new examples added between versions makes comparison meaningless)
- **Unseeded randomness** (results vary between runs, regression detection breaks)
- **Latency as a "future" concern** (it's never added later — bake it in now)
- **Per-PR threshold negotiation** (thresholds live in code; changing them is its own PR)

## Example Workflow

1. Engineer trains a new model: `ranker-v0.4.2`
2. CI triggers eval against `test_v1`
3. Harness loads model, runs through all 5 slices, computes 3 metrics
4. Result serialized as `eval-runs/2026-05-05T14-22-09Z-a3f2b1.json`
5. Gate compares to baseline (`ranker-v0.4.1`)
6. `new_users.precision@10` regressed by 0.024 — gate fails
7. PR is blocked until either (a) the regression is fixed, or (b) the team explicitly overrides with justification recorded in the PR description

## Companion Skills

- `dataset-validation` — validate inputs before they reach the model
- `training-loop-scaffolding` — produce models that this harness can evaluate
- `hyperparameter-sweep-templates` — generate the candidates this harness ranks

## Related Resources

- ../../../domain-software-engineering/testing/testing_property_based_fuzzing.md
- ../../../domain-prompt-engineering/evaluation/correctness_eval_design_prompt.md
