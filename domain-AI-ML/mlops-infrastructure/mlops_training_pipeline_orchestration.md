---
title: "MLOps Training Pipeline Orchestration"
category: AI-ML/mlops-infrastructure
description: "Orchestrate a multi-step training pipeline as a DAG with idempotent steps, retries, and caching so runs are reliable, resumable, and reproducible."
techniques:
  - ST-02
  - CM-02
  - RT-10
  - QA-04
  - DS-06
difficulty: advanced
tags:
  - orchestration
  - dag
  - idempotency
  - caching
  - retries
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/mlops-infrastructure/mlops_ml_cicd_pipeline_design.md
  - domain-AI-ML/mlops-infrastructure/mlops_feature_pipeline_design.md
  - domain-AI-ML/mlops-infrastructure/mlops_experiment_tracking_setup.md
---

# MLOps Training Pipeline Orchestration

**Objective:** Design a multi-step training pipeline as an explicit DAG whose steps are idempotent, individually retryable, and cache-aware — so a run can fail partway and resume without recomputing completed work, and so the same inputs always produce the same outputs.

**When to Use:**
- A training process is a long monolithic script that must restart from scratch on any failure.
- Steps (ingest → validate → feature → train → eval → register) need to run reliably, on schedule, with retries.
- Recompute cost is high and unchanged upstream steps should be cached.

**When NOT to Use:**
- Designing the CI/CD gates around training (use `mlops_ml_cicd_pipeline_design.md` — this is the DAG it invokes).
- Designing feature computation logic itself (use `mlops_feature_pipeline_design.md`).

## Inputs / Context

Provide what you can; the design degrades gracefully:
- **Pipeline steps** — the stages from raw data to a registered model, and their dependencies.
- **Orchestrator** — Airflow / Kubeflow Pipelines / SageMaker Pipelines / Vertex Pipelines / Dagster / Prefect / Metaflow. Ask if unspecified.
- **Step cost & duration** — which steps are expensive (training, large joins) and which are cheap.
- **Failure modes** — what tends to fail (transient infra, OOM, bad data) and how it currently behaves.
- **Triggers & schedule** — what kicks off a run and how often; concurrency expectations.
- **Resource needs** — per-step compute (CPU/GPU), so steps can be sized independently.

## Constraints

**Must:**
- Make each step idempotent: re-running it with the same inputs produces the same outputs and side effects, safely.
- Define step boundaries with explicit inputs/outputs so caching and resumption are deterministic.
- Distinguish retryable (transient) failures from non-retryable (bad data/logic) ones, with a defined policy for each.

**Must Not:**
- Design steps that append/mutate shared state non-idempotently (a retry must not double-write).
- Cache a step on a weak key (e.g., wall-clock) that lets stale or wrong outputs be reused.
- Assume the orchestrator's defaults are correct for retries/concurrency; specify them.

**Instructions:**

1. **Define the DAG.** Lay out steps and their dependency edges (ingest → validate → feature → train → eval → register). Each node has explicit, named inputs and outputs.

2. **Make each step idempotent.** For every step, define how re-execution is safe — write to content-addressed or versioned outputs, use atomic writes / write-then-rename, and avoid in-place mutation of shared tables.

3. **Design the cache key.** For each step, specify the cache key (hash of code version + input data version + config). A step is skipped only when its key matches a prior successful output — never on time.

4. **Set retry policy per step.** Classify each step's failures: transient (retry with backoff, capped) vs deterministic (fail fast, alert). Specify max retries and backoff per step.

5. **Define resumption.** Specify how a failed run resumes from the last successful step using the cache, rather than from the start, and how partial outputs are cleaned or reused.

6. **Handle concurrency and triggers.** Define what happens when a new run starts while one is in flight (queue, cancel-in-progress, skip), and how scheduled vs event triggers interact, so two runs don't corrupt shared outputs.

7. **Wire lineage and observability.** Emit per-step status, inputs/outputs (data + code version), and metrics to the tracker, so a run is auditable and a stuck/failed step is diagnosable.

8. **Plan resource sizing.** Assign compute per step (e.g., CPU for ingest, GPU for train) so each scales independently and cost matches need.

**Output Format:**

A markdown design doc:
- **DAG** — steps, edges, per-step inputs/outputs (text/ASCII).
- **Idempotency Plan** — per step: how re-execution is made safe.
- **Caching Plan** — table: Step | Cache key | Skip condition.
- **Retry Policy** — table: Step | Failure class | Retries | Backoff.
- **Resumption Behavior** — how a failed run continues.
- **Concurrency & Triggers** — collision rules.
- **Lineage & Resourcing** — emitted signals + per-step compute.

## Verification

- [ ] Each step has explicit named inputs and outputs.
- [ ] Each step's idempotency mechanism is stated (re-run is safe, no double-write).
- [ ] Cache keys are content/version-based, never time-based.
- [ ] Retry policy distinguishes transient from deterministic failures per step.
- [ ] Resumption from the last successful step (not from scratch) is defined.
- [ ] Concurrent-run collisions on shared outputs are prevented.

## False-Positive Prevention

❌ **DON'T:**
- Call a step idempotent because it "usually works on retry" — verify it does not double-write or corrupt on re-run.
- Key the cache on a timestamp or run id, which defeats reuse and can serve stale outputs.
- Apply one global retry count to all steps; a deterministic data error should fail fast, not retry 5×.
- Let a scheduled run and a manual run write the same output table concurrently.

✅ **DO:**
- Make steps write to versioned/content-addressed outputs with atomic rename so retries are safe.
- Build cache keys from code version + input data version + config, and skip only on an exact match.
- Set per-step retry policy: backoff for transient infra, fail-fast-and-alert for bad data/logic.
- Enforce concurrency control (cancel-in-progress or queue) on steps that touch shared state.

## Example Output

```markdown
## Training Pipeline Orchestration — Credit Model (orchestrator: Kubeflow Pipelines)

### DAG
ingest → validate_data → build_features → train → evaluate → register
(register depends on evaluate passing; evaluate depends on train; etc.)

### Idempotency Plan
- ingest: writes to `s3://.../snapshots/{data_hash}/` (content-addressed); re-run no-ops if path exists.
- build_features: atomic write-then-rename to `features/{feat_key}/`.
- train: model written to `models/{run_key}/`; never overwrites a different key.

### Caching Plan
| Step | Cache key | Skip if |
|---|---|---|
| ingest | hash(source query + cutoff) | snapshot exists |
| build_features | hash(ingest_key + feature_code_ver) | feature set exists |
| train | hash(feature_key + config + train_code_ver + seed) | model exists |

### Retry Policy
| Step | Failure class | Retries | Backoff |
|---|---|---|---|
| ingest | transient (network) | 3 | exp, 30s |
| validate_data | deterministic (bad data) | 0 | fail + alert |
| train | transient (spot/OOM) | 2 | exp, 60s |

### Resumption Behavior
- On failure, re-trigger reuses cached ingest/features; resumes at train. No full recompute.

### Concurrency & Triggers
- Schedule (daily) + manual. cancel-in-progress per pipeline; shared output paths guarded by run key.

### Lineage & Resourcing
- Each step logs status + input/output versions to MLflow. ingest/validate: CPU; train: 1×A10G.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** DAG → idempotency → caching → retries → resumption.
- **CM-02 (Constraint Specification):** idempotency and content-based cache keys are the binding constraints.
- **RT-10 (Troubleshooting Decision Tree):** the retry policy is a per-step failure decision tree.
- **QA-04 (Consistency Checking):** cache keys guarantee output consistency across runs.
- **DS-06 (Prioritization & Severity Guidance):** failure classes ordered by retry vs fail-fast severity.

**Related Prompts:**
- `mlops_ml_cicd_pipeline_design.md` — the CI/CD layer that triggers and gates this DAG.
- `mlops_feature_pipeline_design.md` — the feature step's internal logic.
- `mlops_experiment_tracking_setup.md` — where each step emits lineage and metrics.
