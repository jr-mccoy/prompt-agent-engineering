---
title: "MLOps Model Packaging Strategy"
category: AI-ML/mlops-infrastructure
description: "Package a trained model for deployment — containerization, pinned dependencies, and an explicit input/output contract — so the artifact runs identically wherever it is served."
techniques:
  - ST-02
  - CM-02
  - QA-04
  - ST-03
  - DS-02
difficulty: intermediate
tags:
  - model-packaging
  - containerization
  - dependency-pinning
  - inference-contract
  - deployment
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/mlops-infrastructure/mlops_model_serving_architecture.md
  - domain-AI-ML/mlops-infrastructure/mlops_environment_dependency_management.md
  - domain-AI-ML/mlops-infrastructure/mlops_model_registry_design.md
---

# MLOps Model Packaging Strategy

**Objective:** Define how a trained model is packaged for deployment — the container/artifact, the pinned dependency set, the model-loading and preprocessing code, and an explicit input/output contract — so the same artifact produces identical predictions in CI, staging, and production, on any host.

**When to Use:**
- A model trained in a notebook now needs to run as a deployable, reproducible artifact.
- "Works on my machine" but fails or differs in the serving environment.
- Standardizing how models hand off from training to serving/registry.

**When NOT to Use:**
- Choosing the serving *pattern* (online/batch) — that is `mlops_model_serving_architecture.md`.
- Managing the *training/dev* environment broadly (use `mlops_environment_dependency_management.md`; this focuses on the deployment artifact).

## Inputs / Context

Provide what you can; the strategy adapts to gaps:
- **Model artifact** — framework and format (pickle, ONNX, SavedModel, TorchScript, safetensors), size, accelerator needs.
- **Preprocessing** — any transformation that must travel with the model (tokenizer, scaler, encoder) to avoid train/serve skew.
- **Serving target** — where it deploys (SageMaker endpoint / Vertex / KServe / container on K8s / Lambda) and the runtime constraints (CPU/GPU, memory, cold start).
- **Interface expectations** — how callers send inputs and consume outputs.
- **Platform & registry** — packaging conventions of the target platform. Ask if unspecified.

## Constraints

**Must:**
- Pin every dependency to an exact version (lockfile or image digest) — an unpinned package is a future silent behavior change.
- Define an explicit input/output contract: schema, types, ranges, and the output shape/meaning.
- Bundle preprocessing with the model so the serving transformation matches training exactly.

**Must Not:**
- Ship a `latest`-tagged base image or unpinned requirements into a production artifact.
- Assume the framework version at serve time matches training; verify and pin it.
- Separate the model from its preprocessing such that they can be updated independently and drift.

**Instructions:**

1. **Choose the artifact format.** Decide the serialization format from portability and runtime needs (e.g., ONNX/TorchScript for framework-independent serving vs native format), and state the tradeoff.

2. **Pin the dependency set.** Specify the exact runtime dependencies (and their versions), the base image, and any system/accelerator libraries (CUDA/cuDNN). Produce a lockfile and an image digest target.

3. **Bundle preprocessing and post-processing.** Package the tokenizer/scaler/encoder and any output decoding with the model, so the artifact takes raw input to final output by the same code path as training.

4. **Define the inference contract.** Write the input schema (fields, types, ranges, required/optional), the output schema (shape, type, meaning, e.g., calibrated probability vs logit), and error responses.

5. **Build the load-and-predict interface.** Specify the standard handler — load(), preprocess(), predict(), postprocess() — and how the artifact exposes it to the serving runtime.

6. **Add a packaging contract test.** Define a test that loads the packaged artifact in a clean container and runs golden inputs through it, asserting outputs match expected values within tolerance — the gate that proves the package works in isolation.

7. **Address size, startup, and security.** State image size targets, model-load/cold-start time, where weights are stored (in-image vs fetched), and basic supply-chain hygiene (pinned, scanned base image, no secrets baked in).

8. **Wire to the registry.** Specify what metadata travels with the package (version, contract, dependency digest) so the registry/serving can resolve and verify it.

**Output Format:**

A markdown packaging spec:
- **Artifact Format Decision** — chosen format + tradeoff.
- **Dependency Pinning** — runtime deps, base image, accelerator libs, lockfile/digest plan.
- **Bundled Preprocessing** — what travels with the model and why.
- **Inference Contract** — input schema | output schema | errors (table).
- **Handler Interface** — load/preprocess/predict/postprocess outline.
- **Packaging Contract Test** — golden inputs, expected outputs, tolerance.
- **Size / Startup / Security** — targets and hygiene.

## Verification

- [ ] Every dependency and the base image are pinned to exact versions/digests.
- [ ] An explicit input AND output contract is defined (types, ranges, output meaning).
- [ ] Preprocessing is bundled so the serving transform matches training.
- [ ] A packaging contract test runs golden inputs in a clean container and asserts outputs.
- [ ] The output meaning is unambiguous (e.g., calibrated probability vs raw score).

## False-Positive Prevention

❌ **DON'T:**
- Treat a model that loads as a model that is correctly packaged — loading ≠ producing the right output.
- Pin the framework but leave transitive dependencies floating; a transitive bump can change numerics.
- Assume the serving runtime applies the same preprocessing the notebook did.
- Ship outputs as bare numbers without stating whether they are probabilities, logits, or class indices.

✅ **DO:**
- Verify the artifact in a clean container with golden inputs, not just in the training environment.
- Pin the full resolved dependency graph (lockfile) and the base image by digest.
- Bundle and version preprocessing with the model as one unit.
- Document the output contract explicitly so consumers cannot misinterpret the prediction.

## Example Output

```markdown
## Packaging Spec — Sentiment Classifier (target: KServe on K8s)

### Artifact Format Decision
- Export to ONNX. Tradeoff: loses some HF convenience but removes the torch version coupling at serve time and speeds CPU inference.

### Dependency Pinning
- Base image `python:3.11-slim@sha256:...`; runtime: onnxruntime==1.18.0, numpy==1.26.4, tokenizers==0.19.1 (lockfile committed). No CUDA (CPU serving).

### Bundled Preprocessing
- HF tokenizer (vocab + config) packaged in-image; same tokenizer object used in training, pinned by hash.

### Inference Contract
| Direction | Schema |
|---|---|
| Input | `{ "text": str (1–512 chars, required) }` |
| Output | `{ "label": "pos"|"neg"|"neu", "prob": float (calibrated, 0–1) }` |
| Errors | 400 on empty/oversized text; 503 on model-load failure |

### Handler Interface
- load(): read ONNX + tokenizer once. preprocess(): tokenize+truncate. predict(): ort run. postprocess(): softmax→calibrated prob→label.

### Packaging Contract Test
- 20 golden (text → expected label, prob±0.02) run in a freshly built container in CI. Fail blocks registration.

### Size / Startup / Security
- Image < 400MB; cold start < 3s; weights in-image; base image scanned; no secrets baked.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** format → pinning → preprocessing → contract → test sequence.
- **CM-02 (Constraint Specification):** exact pinning and the I/O contract are the binding constraints.
- **QA-04 (Consistency Checking):** the contract test verifies the artifact behaves identically in isolation.
- **ST-03 (Output Format Specification):** the inference contract locks input/output schemas.
- **DS-02 (Metric Specification):** output meaning (calibrated prob vs logit) is specified, not assumed.

**Related Prompts:**
- `mlops_model_serving_architecture.md` — the runtime this artifact deploys into.
- `mlops_environment_dependency_management.md` — broader env reproducibility upstream.
- `mlops_model_registry_design.md` — registers and governs this packaged artifact.
