---
title: "Notebook → Production 2: Reproducible Training Pipeline + Tracking"
category: AI-ML/learning-ai-ml/notebook-to-production
description: "Step 2 of the notebook-to-production arc — turn the refactored package into a reproducible training pipeline with a pinned environment, seeds, data versioning, deterministic splits, and experiment tracking, so a run is re-runnable and comparable."
techniques:
  - ST-02
  - CM-02
  - DS-02
  - QA-01
  - RT-05
difficulty: intermediate
tags:
  - notebook-to-production
  - training-pipeline
  - reproducibility
  - experiment-tracking
  - data-versioning
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/learning-ai-ml/notebook-to-production/mllearn_n2p_01_refactor_notebook_to_package.md
  - domain-AI-ML/learning-ai-ml/notebook-to-production/mllearn_n2p_03_package_and_serve_model.md
  - domain-AI-ML/mlops-infrastructure/mlops_mlflow_experiment_tracking_playbook.md
---

# Notebook → Production 2: Reproducible Training Pipeline + Tracking

**Objective:** Guide a learner through the second step of taking an ML project to production — turning the refactored package into a reproducible training pipeline with a pinned environment, controlled randomness, versioned data, deterministic splits, and experiment tracking — so any run can be exactly re-run and any two runs honestly compared, which is the foundation everything downstream (serving, monitoring, retraining) depends on.

**When to Use:**
- The project is already a clean package (step 1 done) and now needs to be reproducible and tracked.
- Runs can't be reproduced, or two experiments can't be compared because conditions drifted.
- Before serving — you should never serve a model you can't retrain reproducibly.

**When NOT to Use:**
- The notebook hasn't been refactored yet (do step 1 first).
- The learner wants a specific tracking-tool playbook (use `mlops_mlflow_experiment_tracking_playbook.md`).
- It's a throwaway experiment that will never be productionized.

## Inputs / Context

- **The package** — the refactored training package from step 1.
- **Data source** — where data comes from and whether/how it changes over time.
- **Compute/stack** — local or cloud; what's available for environment pinning and tracking.
- **Tracking preference** — a tracking tool the learner has or wants (capability, not mandated).

## Constraints

**Must:**
- Pin the environment (dependencies + versions) and control all randomness (seeds for data, splits, and model init) so a run is bit-for-bit-or-close reproducible.
- Version the data and make splits deterministic — a "reproducible" pipeline on silently-changing data or random splits is not reproducible.
- Track each run's config, code version, data version, metrics, and artifacts so two runs are comparable and a result is traceable to its inputs.

**Must Not:**
- Claim reproducibility while leaving the environment unpinned, seeds uncontrolled, or data unversioned.
- Invent specific tool version facts, pricing, or "the best tracker is X" from memory — describe the capability and direct the learner to the current tool/docs.
- Re-introduce leakage when defining splits (e.g., shuffling time-ordered data, leaking across groups).

**Instructions:**

1. **Pin the environment.** Lock dependencies and versions (a lockfile/container) so the pipeline runs the same elsewhere; record the runtime details.

2. **Control randomness.** Set and record seeds for data shuffling, splitting, and model initialization; note any remaining nondeterminism (e.g., GPU ops) and its expected magnitude.

3. **Version the data.** Establish a way to identify exactly which data a run used (a hash, snapshot, or data-versioning tool) so a run is tied to a specific dataset state.

4. **Make splits deterministic and leakage-free.** Fix the split with a recorded seed/strategy appropriate to the data (group-aware or time-based where needed) so the same split is reproducible and honest.

5. **Add experiment tracking.** Log per run: config/hyperparameters, code version (commit), data version, metrics, and the model artifact — so runs are comparable and traceable.

6. **Make the pipeline a single reproducible command.** One entry point trains, evaluates, logs, and outputs a versioned model artifact from config.

7. **Verify reproducibility.** Run twice from the pinned environment and confirm matching (within stated nondeterminism) metrics; confirm a run can be fully reconstructed from its tracked record.

**Output Format:**

A markdown pipeline guide:
- **Environment Pinning** — how dependencies/runtime are locked.
- **Randomness Control** — seeds set + residual nondeterminism noted.
- **Data Versioning** — how a run is tied to a dataset state.
- **Split Strategy** — deterministic, leakage-aware split.
- **Experiment Tracking** — what's logged per run (config/code/data/metrics/artifact).
- **Run Command** — the single reproducible entry point.
- **Reproducibility Check** — two-run comparison + reconstruct-from-record check.

## Verification

- [ ] Environment is pinned; the pipeline runs the same from a clean setup.
- [ ] Seeds control data/split/init randomness; residual nondeterminism is noted.
- [ ] Data is versioned; a run is tied to a specific dataset state.
- [ ] Splits are deterministic and leakage-aware (group/time as appropriate).
- [ ] Each run logs config, code version, data version, metrics, and artifact; two runs reproduce.

## False-Positive Prevention

❌ **DON'T:**
- Call it reproducible with an unpinned environment, uncontrolled seeds, or unversioned data.
- Use a random split each run (then "compare" incomparable runs).
- Shuffle time-ordered or grouped data and leak across the split.
- Name a specific tracker version/pricing from memory.

✅ **DO:**
- Pin the environment, control seeds, and version the data together — all three.
- Fix a deterministic, leakage-aware split with a recorded seed/strategy.
- Track config/code/data/metrics/artifact per run so results are traceable and comparable.
- Verify by running twice and reconstructing a run from its record.

## Example Output

```markdown
## Reproducible Training Pipeline — tabular classifier

### Environment Pinning
Lockfile + container; Python/runtime + library versions recorded.

### Randomness Control
Seeds for shuffle/split/init set and logged. Residual: GPU nondeterminism ~±0.2 F1, noted.

### Data Versioning
Dataset snapshot hashed; run record stores the hash → run tied to exact data.

### Split Strategy
Group-aware split (no customer appears in both train and test), fixed seed.

### Experiment Tracking
Per run: hyperparameters, git commit, data hash, CV + test metrics, model artifact.

### Run Command
`python -m pkg.train --config configs/baseline.yaml` → trains, evaluates, logs, writes versioned model.

### Reproducibility Check
Two runs from the pinned env match within ±0.2 F1; a logged run fully reconstructs from its record.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** environment → randomness → data → splits → tracking → verify.
- **CM-02 (Constraint Specification):** pinned-env, controlled-seed, versioned-data reproducibility as hard constraints.
- **DS-02 (Metric Specification):** tracked metrics and a stated reproducibility tolerance.
- **QA-01 (Self-Verification):** the two-run + reconstruct-from-record checks verify reproducibility.
- **RT-05 (Evidence-Based Reasoning):** results are traceable to exact code/data/config inputs.

**Related Prompts:**
- `notebook-to-production/mllearn_n2p_01_refactor_notebook_to_package.md` — previous step: the package this pipeline builds on.
- `notebook-to-production/mllearn_n2p_03_package_and_serve_model.md` — next step: package and serve the trained model.
- `mlops_mlflow_experiment_tracking_playbook.md` — a concrete tracking-tool playbook for the tracking step.
