---
title: "Notebook → Production 3: Package & Serve the Model as an API"
category: AI-ML/learning-ai-ml/notebook-to-production
description: "Step 3 of the notebook-to-production arc — package the trained model and serve it behind an API/container with input validation, a versioned artifact, train/serve parity, latency/throughput basics, and a smoke test."
techniques:
  - ST-02
  - CM-02
  - QA-01
  - DS-02
  - RP-01
difficulty: advanced
tags:
  - notebook-to-production
  - model-serving
  - api
  - train-serve-skew
  - deployment
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/learning-ai-ml/notebook-to-production/mllearn_n2p_02_reproducible_training_pipeline.md
  - domain-AI-ML/learning-ai-ml/notebook-to-production/mllearn_n2p_04_deploy_monitor_cicd.md
  - domain-AI-ML/mlops-infrastructure/mlops_model_serving_architecture.md
---

# Notebook → Production 3: Package & Serve the Model as an API

**Objective:** Guide a learner through the third step of taking an ML project to production — packaging the reproducibly-trained model and serving it behind an API/container — with input validation, a versioned artifact, **train/serve parity** as the central concern, basic latency/throughput awareness, and a smoke test, so the served model produces the same predictions as offline and is safe to deploy.

**When to Use:**
- The model trains reproducibly (step 2 done) and now needs to be callable as a service.
- Moving from "a model file" to "a model endpoint" for an app or downstream system.
- Before deploy/monitoring/CI/CD (step 4) — serving correctly comes first.

**When NOT to Use:**
- The training pipeline isn't reproducible yet (do step 2 first).
- The learner wants serving-architecture depth/scale design (use `mlops_model_serving_architecture.md`).
- Batch scoring is the actual need, not an online API (a simpler path).

## Inputs / Context

- **The trained model + pipeline** — the versioned artifact and the feature/preprocessing code from steps 1–2.
- **Serving need** — online API vs batch; expected request shape and volume.
- **Latency/throughput target** — even rough numbers shape choices.
- **Stack** — container/runtime available for serving.

## Constraints

**Must:**
- Reuse the **exact same feature/preprocessing code path** for serving as for training — train/serve skew (features computed differently online vs offline) is the dominant failure mode here and must be designed out, then tested.
- Validate inputs at the API boundary (schema, types, ranges) and load a **versioned** model artifact (the endpoint must report which model version it serves).
- Include a smoke test that sends a known input and asserts the served prediction matches the offline prediction for that input.

**Must Not:**
- Reimplement preprocessing inside the API (the classic skew bug) — import the shared code.
- Invent specific latency numbers, framework API details, or "the best serving stack is X" from memory — describe what to measure on the learner's stack and direct them to current docs.
- Serve an unversioned blob with no way to know which model is live.

**Instructions:**

1. **Define the serving contract.** Specify the request/response schema, the prediction the endpoint returns, and the model-version field it reports.

2. **Reuse the training feature path.** Import the same preprocessing/feature code from the package so inputs are transformed identically online and offline — do not rewrite it.

3. **Load a versioned artifact.** Load the model produced by the reproducible pipeline, tagged with its version/data/code provenance; expose the version via the API.

4. **Add input validation.** Validate schema, types, and ranges at the boundary; define how invalid/edge inputs are handled (reject vs default) rather than letting them silently mispredict.

5. **Containerize the service.** Package the API + dependencies (reusing the pinned environment) so it runs identically across machines.

6. **Write the parity smoke test.** Send a fixed input through both the offline pipeline and the API; assert the predictions match (within numerical tolerance). This is the test that catches skew.

7. **Measure basic latency/throughput.** Record p50/p95 latency and rough throughput on the learner's stack against the target; note where to optimize if needed (don't assert numbers — measure).

**Output Format:**

A markdown serving guide:
- **Serving Contract** — request/response schema + reported model version.
- **Shared Feature Path** — how training preprocessing is reused (not reimplemented).
- **Artifact Loading** — versioned model + provenance exposed.
- **Input Validation** — schema/type/range checks + edge-case policy.
- **Containerization** — how the service is packaged.
- **Parity Smoke Test** — the offline-vs-API prediction-match test.
- **Latency/Throughput** — measured p50/p95 + throughput vs target.

## Verification

- [ ] Serving reuses the exact training feature/preprocessing code (no reimplementation).
- [ ] A parity smoke test asserts API predictions match offline predictions for known inputs.
- [ ] Inputs are validated at the boundary; edge-case handling is defined.
- [ ] The endpoint loads a versioned artifact and reports the model version.
- [ ] Latency/throughput are measured (not assumed) on the learner's stack against the target.

## False-Positive Prevention

❌ **DON'T:**
- Reimplement preprocessing in the API — the #1 source of train/serve skew.
- Serve an unversioned model with no way to know what's live.
- Assert latency numbers from memory instead of measuring on the real stack.
- Skip the parity test and discover skew in production.

✅ **DO:**
- Import the same feature/preprocessing code used in training.
- Load and expose a versioned artifact with provenance.
- Validate inputs and define edge-case behavior at the boundary.
- Write a parity smoke test and measure latency on the actual stack.

## Example Output

```markdown
## Serve the Model — tabular classifier API

### Serving Contract
POST /predict {features…} → {prediction, score, model_version}.

### Shared Feature Path
API imports `pkg.data.transform` — the identical function used in training. No reimplementation.

### Artifact Loading
Loads model v2026-06-19-abc123 (commit + data hash in metadata); /health reports the version.

### Input Validation
Schema + dtype + range checks; out-of-range numeric → 422 with a clear error (not a silent default).

### Containerization
Dockerfile reuses the pinned lockfile from step 2; runs identically locally and in cloud.

### Parity Smoke Test
Fixed sample → offline pipeline score 0.732; API score 0.732 (Δ < 1e-6). Skew test passes.

### Latency/Throughput
Measured on the dev box: p50 8ms, p95 21ms, ~600 rps single instance — meets the 50ms target.
(Numbers measured, not assumed.)
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** contract → shared features → artifact → validation → container → parity → latency.
- **CM-02 (Constraint Specification):** train/serve parity and versioned artifacts as hard constraints.
- **QA-01 (Self-Verification):** the parity smoke test verifies the served model matches offline.
- **DS-02 (Metric Specification):** measured p50/p95 latency and throughput against a target.
- **RP-01 (Audience/Level Adaptation):** depth tuned to the learner's serving/infra comfort.

**Related Prompts:**
- `notebook-to-production/mllearn_n2p_02_reproducible_training_pipeline.md` — previous step: the reproducible pipeline that produces the artifact.
- `notebook-to-production/mllearn_n2p_04_deploy_monitor_cicd.md` — next step: deploy, monitor, and add CI/CD.
- `mlops_model_serving_architecture.md` — deeper reference on serving architecture and scale.
