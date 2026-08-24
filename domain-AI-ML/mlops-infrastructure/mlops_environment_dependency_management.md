---
title: "MLOps Environment & Dependency Management"
category: AI-ML/mlops-infrastructure
description: "Manage Python, CUDA, and library environments so training and serving are reproducible and consistent — pinned, locked, and verified across dev, CI, and production."
techniques:
  - ST-02
  - CM-02
  - QA-04
  - RT-09
  - DS-06
difficulty: intermediate
tags:
  - dependency-management
  - cuda
  - lockfile
  - reproducible-environment
  - containers
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/mlops-infrastructure/mlops_reproducibility_audit.md
  - domain-AI-ML/mlops-infrastructure/mlops_model_packaging_strategy.md
  - domain-AI-ML/mlops-infrastructure/mlops_experiment_tracking_setup.md
---

# MLOps Environment & Dependency Management

**Objective:** Establish a strategy for managing Python, CUDA/accelerator, and library dependencies so that the training and serving environments are exactly reproducible, mutually consistent, and verifiable — eliminating "works in dev, breaks in prod" and silent numerical drift from floating dependency versions.

**When to Use:**
- Builds or results differ between a laptop, CI, and production due to environment differences.
- CUDA/cuDNN/driver mismatches break GPU training or serving.
- Standardizing how environments are defined so they can be rebuilt identically months later.

**When NOT to Use:**
- Packaging the deployable model artifact specifically (use `mlops_model_packaging_strategy.md`; this is the broader env strategy).
- A full reproducibility audit across all five axes (use `mlops_reproducibility_audit.md`; env is one axis there).

## Inputs / Context

Provide what you can; the strategy adapts to gaps:
- **Stack** — Python version, key frameworks (torch/tf/jax/sklearn), and whether GPU is used.
- **Accelerator details** — GPU model, required CUDA/cuDNN versions, driver constraints (if GPU).
- **Current setup** — how environments are defined now (requirements.txt, conda, poetry/uv, Docker, none).
- **Environments to keep consistent** — dev, CI, training, serving — and where they currently diverge.
- **Tooling preference & platform** — package manager, container registry, base images. Ask if unspecified.

## Constraints

**Must:**
- Pin the full resolved dependency graph (a lockfile), not just top-level requirements.
- Treat CUDA/cuDNN/driver compatibility explicitly when GPU is involved — Python pins alone do not cover the accelerator stack.
- Ensure training and serving environments are derived from the same source of truth so they cannot silently diverge.

**Must Not:**
- Rely on unpinned or range-pinned (`>=`) production dependencies — a transitive bump can change numerics or break loading.
- Use `latest` base images or implicit system packages that vary by host.
- Assume the framework version determines the CUDA version; verify the compatible matrix.

**Instructions:**

1. **Inventory the environment surface.** List Python version, frameworks, GPU/CUDA needs, and system libraries. Identify which environments (dev/CI/train/serve) must match and where they diverge today.

2. **Choose the management approach.** Decide the layering: a lockfile-based package manager (uv/poetry/conda-lock) for Python, plus containerization (pinned base image by digest) for the full environment including system/accelerator libs. Justify against the stack.

3. **Pin the full graph.** Generate a lockfile capturing exact versions of all transitive dependencies. State how it is regenerated and reviewed when intentionally updated.

4. **Handle the accelerator stack.** When GPU is used, specify the CUDA/cuDNN versions and the framework build compatible with them, and the base image that bundles them — so the GPU stack is reproducible, not host-dependent.

5. **Unify train and serve.** Specify how serving derives from the same locked source as training (shared lockfile/base layer), so a model is run against the versions it was trained with.

6. **Verify the environment.** Define a check that rebuilds the environment from scratch (clean container) and runs a smoke test (import + tiny train/predict), proving the lock actually reproduces a working environment.

7. **Define the update workflow.** State how a dependency is upgraded deliberately: change the spec → relock → rebuild → re-run smoke + eval → commit. Block ad-hoc `pip install` in production images.

8. **Plan diagnosis.** Specify how environment-related failures are diagnosed (capture full env fingerprint per run; compare failing vs known-good), so drift is traceable.

**Output Format:**

A markdown strategy doc:
- **Environment Surface** — Python, frameworks, GPU/CUDA, system libs; divergences today.
- **Management Approach** — package manager + container layering, with rationale.
- **Pinning Plan** — lockfile scope and regeneration workflow.
- **Accelerator Stack** — CUDA/cuDNN/framework compatibility and base image.
- **Train/Serve Unification** — shared source of truth.
- **Verification** — clean-rebuild smoke test.
- **Update & Diagnosis Workflow** — deliberate upgrades + drift tracing.

## Verification

- [ ] The full transitive dependency graph is locked, not just top-level requirements.
- [ ] CUDA/cuDNN/driver compatibility is addressed explicitly (when GPU is used).
- [ ] Training and serving environments derive from the same locked source.
- [ ] A clean-rebuild smoke test proves the lock reproduces a working environment.
- [ ] No production path allows `latest` images or ad-hoc installs.

## False-Positive Prevention

❌ **DON'T:**
- Treat `requirements.txt` with top-level pins as reproducible — unpinned transitives still drift.
- Assume installing the right torch version handles CUDA; the driver/cuDNN/base image still must match.
- Let serving images be built independently from training, so they silently diverge in library versions.
- Fix a broken env by `pip install`-ing into a running container without updating the lock.

✅ **DO:**
- Lock the complete dependency graph and regenerate it through a reviewed workflow.
- Pin the accelerator stack (CUDA/cuDNN/base image by digest) alongside the Python pins.
- Build train and serve from a shared locked base so they cannot diverge.
- Verify by rebuilding from scratch in a clean container and running a smoke test before trusting the env.

## Example Output

```markdown
## Environment Strategy — NLP Training & Serving (GPU; tooling: uv + Docker)

### Environment Surface
- Python 3.11; torch 2.3 (CUDA 12.1); transformers, datasets. GPU: A10G, driver 535+.
- Divergence: dev on macOS (CPU torch), CI on CPU, training/serving on CUDA — version drift caused a serving load failure.

### Management Approach
- uv for Python deps (lockfile committed); Docker for full env. Base image pinned by digest bundling CUDA 12.1 + cuDNN.

### Pinning Plan
- `uv.lock` captures all transitive versions. Regenerated only via `uv lock --upgrade-package X`, reviewed in PR.

### Accelerator Stack
- Base: `nvidia/cuda:12.1.1-cudnn8-runtime@sha256:...`; torch build `+cu121`. CPU dev uses a separate `+cpu` extra, but train/serve share the CUDA lock.

### Train/Serve Unification
- Serving Dockerfile `FROM` the same locked base layer as training; same `uv.lock`.

### Verification
- CI rebuilds image clean, runs `import torch; torch.cuda.is_available()` (in GPU CI) + a 2-step train and 1 predict. Fail blocks merge.

### Update & Diagnosis Workflow
- Each run logs `env_hash` (lock digest) + image digest to MLflow. Failing run's env compared to last-good to localize drift.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** surface → approach → pinning → accelerator → verify → update.
- **CM-02 (Constraint Specification):** full-graph locking and CUDA compatibility are the binding constraints.
- **QA-04 (Consistency Checking):** the clean-rebuild smoke test verifies the lock is consistent and working.
- **RT-09 (Root Cause Explanation):** the diagnosis workflow localizes env drift to its cause.
- **DS-06 (Prioritization & Severity Guidance):** orders pinning concerns (graph, accelerator, base image).

**Related Prompts:**
- `mlops_reproducibility_audit.md` — environment is one axis of the broader audit.
- `mlops_model_packaging_strategy.md` — packages the deployable artifact on this env.
- `mlops_experiment_tracking_setup.md` — logs the env fingerprint per run for lineage.
