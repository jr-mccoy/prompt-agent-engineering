---
title: "Weights & Biases Experiment Tracking Playbook"
category: AI-ML/mlops-infrastructure
description: "Stand up Weights & Biases for experiment tracking, sweeps, and artifact lineage on a real stack — project/entity structure, run conventions, what to log, sweep configuration, and reproducibility hooks — without inventing version-specific API behavior."
techniques:
  - ST-02
  - CM-02
  - RT-10
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - wandb
  - experiment-tracking
  - hyperparameter-sweeps
  - reproducibility
  - mlops
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/mlops-infrastructure/mlops_experiment_tracking_setup.md
  - domain-AI-ML/mlops-infrastructure/mlops_reproducibility_audit.md
  - domain-AI-ML/deep-learning/dl_training_not_converging_debug.md
---

# Weights & Biases Experiment Tracking Playbook

**Objective:** Turn a team's intent to track experiments with Weights & Biases (W&B) into a concrete setup — entity/project/group structure, run naming and config conventions, what to log (config, metrics, media, artifacts), sweep configuration for HPO, and artifact-based lineage — so experiments are comparable and reproducible.

**When to Use:**
- You have chosen W&B and need an opinionated setup walkthrough, not a tool-selection decision.
- You run many training runs (especially deep-learning) and need systematic comparison, sweeps, and media logging.
- You need artifact lineage (datasets → models) tied to runs.

**When NOT to Use:**
- You have not decided *whether* W&B fits — start with `mlops_experiment_tracking_setup.md`.
- Your problem is unstable training itself (NaNs, divergence) rather than tracking — use `dl_training_not_converging_debug.md`.
- You need a tool-agnostic reproducibility audit — use `mlops_reproducibility_audit.md`.

## Inputs / Context

Provide what you can:
- **W&B mode** — SaaS cloud vs. self-hosted/dedicated; **W&B SDK version**.
- **ML frameworks** + versions — drives integration/autolog hooks.
- **Team structure** — entity (team) and how projects map to objectives.
- **Compute environment** — local, cluster, cloud, or CI; whether runs are launched in parallel.
- **Data/artifact needs** — do you need versioned dataset/model artifacts and lineage?

## Constraints

**Must:**
- Ask for W&B mode and SDK version before setup steps; flag version-sensitive behavior.
- Define a project/group/tag convention so runs are filterable and sweeps are comparable.
- Capture config, code version (git SHA), seed, environment, and data/artifact version for every run.

**Must Not:**
- Invent W&B API calls, config keys, sweep YAML fields, or pricing/seat behavior — mark version-specific items "verify against current W&B docs."
- Treat logging loss curves as sufficient reproducibility — config + code + data version are required.
- Log secrets, PII, or raw sensitive data as artifacts/media without a redaction policy.

**Instructions:**

1. **Fix mode and access.** State SaaS vs. self-hosted, the entity (team), and how API-key/auth is handled in each environment (local, cluster, CI). Note offline-mode + later sync if runs execute without network.

2. **Design project & grouping structure.** Map projects to objectives; define `group` (e.g., per sweep or experiment cohort), `job_type`, and `tags`. This is what makes runs comparable rather than a flat pile.

3. **Define the run config contract.** Require `config` to capture all hyperparameters plus git SHA, seed, and data/artifact version. The config is the primary axis for filtering and sweep analysis.

4. **Specify what to log.** Enumerate metrics (with explicit step), system metrics, media/tables where useful (predictions, confusion matrices), and the final model as an artifact. Keep high-frequency logging bounded to control cost and noise.

5. **Configure sweeps for HPO.** Define the sweep method (grid/random/Bayes), the search space, the metric + goal, and early-termination policy. Tie sweep runs into a `group` so results aggregate. Flag that sweep config schema is version-sensitive.

6. **Set up artifact lineage.** Version input datasets and output models as artifacts; declare `use_artifact`/`log_artifact` relationships so the dataset→run→model lineage is queryable. Mark exact API as verify-in-docs.

7. **Wire reproducibility + environment capture.** Ensure code (git SHA or code artifact), environment/requirements, and seed are captured per run. Cross-link `mlops_reproducibility_audit.md`.

8. **Define validation + governance.** Provide a smoke test (a run that logs config/metrics/artifact and appears grouped correctly), plus retention and privacy policies for media/artifacts.

**Output Format:**

A markdown setup playbook:
- **Mode & Access** — SaaS/self-hosted, entity, auth per environment
- **Project / Group / Tag Convention** — table
- **Run Config Contract** — required config fields
- **Logging Plan** — metrics / media / artifacts (table) + cost guards
- **Sweep Configuration** — method, space, metric, early-stop
- **Artifact Lineage** — dataset → run → model relationships
- **Reproducibility & Privacy** — captured fields + redaction policy
- **Smoke Test** — validation steps
- **Verify-in-Docs** — version-sensitive items flagged

## Verification

- [ ] Project/group/tag convention makes runs and sweeps filterable, not a flat list.
- [ ] Every run's `config` includes hyperparameters + git SHA + seed + data/artifact version.
- [ ] Sweeps define method, space, target metric+goal, and an early-termination policy.
- [ ] Dataset → run → model lineage is expressed via artifacts, not implied.
- [ ] Media/artifact logging has a privacy/redaction policy (no raw PII/secrets).
- [ ] A smoke test confirms a run logs and groups correctly end-to-end.

## False-Positive Prevention

❌ **DON'T:**
- Declare tracking complete because loss curves render in the dashboard while config omits data version and seed.
- Compare runs across a sweep when they lack a shared `group`/`config` schema — the comparison is meaningless.
- Log full prediction tables or sample images containing PII as media without redaction.
- Quote sweep-YAML keys or SDK calls from memory as version-stable.

✅ **DO:**
- Treat a run as reproducible only when config + code + environment + data version are all captured.
- Standardize `group`/`job_type`/`tags` so sweep and cohort analysis aggregate correctly.
- Apply a redaction/retention policy to media and dataset artifacts.
- Flag every SDK call, config key, and sweep field as "verify against your W&B SDK version."

## Example Output

```markdown
## W&B Playbook: Image-Classification Team (SaaS, team entity)

### Mode & Access
- SaaS cloud, entity `acme-vision`. API key via secret manager; CI uses a service key.
- Cluster jobs may run offline → `WANDB_MODE=offline` then sync (verify env var for your SDK version).

### Project / Group / Tag Convention
| Field | Convention |
|---|---|
| project | `defect-classifier` |
| group | one per sweep / experiment cohort |
| job_type | `train` | `eval` | `sweep` |
| tags | git_sha, data_version, backbone name |

### Run Config Contract
config = {all hyperparameters, git_sha, seed, data_version, backbone, image_size}

### Logging Plan
| Item | Logged | Notes |
|---|---|---|
| train/val loss, accuracy, F1 | per epoch (step) | — |
| system metrics (GPU util) | auto | watch cost |
| confusion matrix, sample preds | per eval | redact any PII in images |
| final model | artifact | versioned |
Cost guard: cap image/media logging to N samples per eval.

### Sweep Configuration
method=bayes; metric={name: val/f1, goal: maximize}; space={lr, weight_decay, backbone}; early_terminate=hyperband (verify schema for your version). All sweep runs share group.

### Artifact Lineage
dataset artifact (v3) --use--> training run --log--> model artifact (v7).

### Reproducibility & Privacy
git_sha + requirements + seed per run. Media redaction policy on customer images; artifact retention 120d.

### Smoke Test
Launch one `train` run → confirm config complete, metrics stepping, model artifact logged, run appears under correct group.

### Verify-in-Docs
- Offline-mode env var + sync command for your SDK version.
- Sweep early-termination schema; artifact API signatures.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** mode → structure → config → logging → sweeps → lineage → validation.
- **CM-02 (Constraint Specification):** no-fabrication, reproducibility, and privacy constraints bound every step.
- **RT-10 (Troubleshooting / Operational Reasoning):** setup is organized around making runs comparable and reproducible in real compute environments.
- **DS-02 (Metric Specification):** sweeps and logging are defined around explicit target metrics and goals.
- **QA-01 (Self-Verification):** the smoke test and checklist validate the setup end-to-end.

**Related Prompts:**
- `mlops_experiment_tracking_setup.md` — choose W&B vs. alternatives before this playbook.
- `mlops_reproducibility_audit.md` — full reproducibility checklist the config/artifact hooks feed.
- `dl_training_not_converging_debug.md` — when the issue is training stability, not tracking.
