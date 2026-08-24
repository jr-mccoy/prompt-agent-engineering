---
title: "Deep Learning Reproducibility Setup"
category: AI-ML/deep-learning
description: "Make DL training reproducible — seeds, deterministic ops, dataloader worker seeding, environment and data pinning — and document the residual sources of nondeterminism that cannot be removed."
techniques:
  - ST-02
  - CM-02
  - QA-01
  - QA-12
  - DS-02
difficulty: intermediate
tags:
  - reproducibility
  - determinism
  - seeds
  - environment-pinning
  - experiment-tracking
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/mlops-infrastructure/mlops_experiment_tracking_setup.md
  - domain-AI-ML/deep-learning/dl_training_not_converging_debug.md
  - domain-AI-ML/deep-learning/dl_distributed_training_plan.md
---

# Deep Learning Reproducibility Setup

**Objective:** Make a deep-learning training run reproducible to the degree the stack allows — seed every RNG, enable deterministic ops where available, seed dataloader workers, and pin the environment and data — while explicitly documenting the residual nondeterminism (nondeterministic kernels, multi-GPU reductions, hardware differences) so reproducibility claims are honest, not overstated.

**When to Use:**
- Two runs with the "same" config give different results and you need bit-or-close reproducibility.
- Establishing a deterministic reference for debugging (e.g., before the convergence or gradient triage).
- Preparing experiments for publication, audit, or regulated deployment where runs must be re-creatable.

**When NOT to Use:**
- You only need approximate run-to-run stability for casual experimentation (full determinism costs speed).
- The real problem is a training bug rather than nondeterminism (`dl_training_not_converging_debug.md`).
- You want experiment *logging/versioning* infrastructure specifically (`mlops_experiment_tracking_setup.md`) — pair with this prompt.

## Inputs / Context

Provide what you can:
- **Framework & version**, hardware (GPU/TPU/CPU), and whether training is single- or multi-device.
- **Current variance** — how different are "identical" runs (metric spread)?
- **Where reproducibility is needed** — debugging reference / publication / audit.
- **Tolerance** — bit-exact vs close-enough (within noise band).
- **Data pipeline** — augmentation randomness, shuffling, multi-worker loading.

## Constraints

**Must:**
- Seed all RNGs (framework, numpy, Python, CUDA) and seed dataloader workers individually.
- Enable deterministic algorithm modes and document the speed cost and any ops that lack deterministic kernels.
- Pin the environment (framework/library versions, hardware) and the dataset version/snapshot.

**Must Not:**
- Claim "fully reproducible" when nondeterministic reductions, atomic ops, or hardware differences remain — state the residual limits.
- Quote an exact slowdown from determinism as fact — frame it as to-be-measured.
- Assume seeding the framework alone is sufficient — worker, numpy, and CUDA RNGs must also be set.

**Instructions:**

1. **Define the reproducibility target.** State whether bit-exact (same hardware/env) or close-within-noise is required; the target sets how aggressive the determinism settings must be.

2. **Seed every RNG.** Set framework, numpy, Python `random`, and accelerator RNG seeds at startup; seed each dataloader worker deterministically (worker-init function) so augmentation/shuffling are repeatable.

3. **Enable deterministic algorithms.** Turn on the framework's deterministic mode and disable nondeterministic autotuning; identify ops with no deterministic kernel and decide to avoid, replace, or accept-and-document them.

4. **Make data order deterministic.** Fix the shuffle seed and any sampler randomness; ensure resumed/checkpointed runs restore RNG state so continuation is reproducible.

5. **Pin the environment and data.** Record and pin framework/library versions, accelerator/driver, container image, and a dataset snapshot/version hash. Log the full config with the run.

6. **Address multi-GPU/distributed nondeterminism.** Note that all-reduce ordering and atomic operations can introduce variance; document what remains nondeterministic and whether the target still holds (see `dl_distributed_training_plan.md`).

7. **Verify and document limits.** Run the same config twice and confirm results match within the stated target; publish a "Reproducibility Notes" block listing exactly what is pinned and the residual nondeterminism that cannot be eliminated.

**Output Format:**

A markdown report:
- **Reproducibility Target** — bit-exact vs within-noise + where needed.
- **Seeding Plan** — all RNGs + worker seeding.
- **Determinism Settings** — modes enabled + ops without deterministic kernels + cost note.
- **Data & Resume Determinism** — shuffle/sampler seeds + RNG-state checkpointing.
- **Environment/Data Pinning** — versions, image, dataset snapshot.
- **Residual Nondeterminism** — honest list of what remains.
- **Verification** — two-run match result.

## Verification

- [ ] All RNGs (framework, numpy, Python, accelerator) and dataloader workers are seeded.
- [ ] Deterministic mode is enabled and non-deterministic ops are identified.
- [ ] Environment and dataset versions are pinned and logged.
- [ ] Two identical-config runs are compared and match within the stated target.
- [ ] Residual nondeterminism is documented rather than glossed over.

## False-Positive Prevention

❌ **DON'T:**
- Set only the framework seed and assume runs are reproducible — workers/numpy/CUDA RNGs still vary.
- Claim full determinism while nondeterministic GPU reductions or atomic ops remain.
- Ignore dataloader worker seeding and then puzzle over augmentation variance.
- Forget to checkpoint RNG state, so resumed runs diverge from end-to-end runs.

✅ **DO:**
- Seed every RNG including per-worker seeds, and fix shuffle/sampler seeds.
- Enable deterministic algorithm modes and list ops lacking deterministic kernels.
- Pin framework versions, hardware, and a dataset snapshot; log it with the run.
- State the residual nondeterminism honestly and verify with a two-run match.

## Example Output

```markdown
## Reproducibility Setup: Single-GPU Image Model (debugging reference)

### Reproducibility Target
Close-within-noise on the same GPU/env (debugging reference, not publication bit-exactness).

### Seeding Plan
Seed framework + numpy + Python random + CUDA at startup; worker-init seeds each dataloader worker by id.

### Determinism Settings
Deterministic algorithms ON; autotuner OFF. One pooling op lacks a deterministic kernel → replaced with a deterministic variant. (Speed cost to be measured.)

### Data & Resume Determinism
Fixed shuffle seed; sampler seeded; RNG state saved in checkpoints so resume == end-to-end.

### Environment/Data Pinning
Pinned framework x.y.z, driver/CUDA, container image digest; dataset snapshot hash logged.

### Residual Nondeterminism
None expected single-GPU after kernel swap; would reappear with multi-GPU all-reduce ordering.

### Verification
Two runs, same config: final metric identical to logged precision. Target met.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** target → seed → determinism → pin → verify.
- **CM-02 (Constraint Specification):** the reproducibility target governs how aggressive settings are.
- **QA-01 (Self-Verification):** the two-run match confirms the setup.
- **QA-12 (False Positives Identification):** prevents overclaiming "fully reproducible" when limits remain.
- **DS-02 (Metric Specification):** the metric-match tolerance defines success.

**Related Prompts:**
- `mlops_experiment_tracking_setup.md` — log the pinned config/versions alongside results.
- `dl_training_not_converging_debug.md` — a deterministic reference makes bug isolation possible.
- `dl_distributed_training_plan.md` — multi-GPU reproducibility limits and their causes.
```