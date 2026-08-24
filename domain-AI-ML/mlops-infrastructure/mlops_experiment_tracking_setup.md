---
title: "MLOps Experiment Tracking Setup"
category: AI-ML/mlops-infrastructure
description: "Design an experiment-tracking system (params, metrics, artifacts, lineage) and the logging discipline that makes every run reproducible and comparable."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - experiment-tracking
  - reproducibility
  - mlflow
  - lineage
  - logging-discipline
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/mlops-infrastructure/mlops_model_registry_design.md
  - domain-AI-ML/mlops-infrastructure/mlops_reproducibility_audit.md
  - domain-AI-ML/mlops-infrastructure/mlops_training_pipeline_orchestration.md
---

# MLOps Experiment Tracking Setup

**Objective:** Produce a concrete experiment-tracking design — what to log (params, metrics, artifacts, code/data/env versions, lineage), how to structure runs and experiments, and the team logging discipline — so that any past run can be found, compared, and reproduced without tribal knowledge.

**When to Use:**
- Starting a new ML project and choosing how runs will be recorded.
- Results live in notebook cells, spreadsheets, or filenames like `model_final_v2_real.pkl`.
- Two people cannot reconcile "which run produced the model in prod."
- Before standing up a model registry or CI/CD (tracking is the upstream dependency).

**When NOT to Use:**
- For promoting/governing already-tracked models (use `mlops_model_registry_design.md`).
- For a one-off throwaway exploration that will never be revisited or shipped.

## Inputs / Context

Provide what you can; the design adapts to gaps:
- **Platform** — which tracker the team uses or is considering (MLflow / Weights & Biases / SageMaker Experiments / Vertex AI Experiments / Databricks). Ask if unspecified.
- **Team shape** — solo, small team, or multiple teams sharing a tracker; on-prem vs cloud.
- **Workload types** — classical ML, deep learning, LLM fine-tuning; offline-only vs production-bound.
- **Current pain** — what gets lost today (params? data version? the exact code?).
- **Compliance needs** — audit/lineage requirements (regulated domain, model risk).

## Constraints

**Must:**
- Tie every logged item to a reproducibility question it answers ("could I recreate this run?").
- Specify code, data, and environment versioning, not just metrics — metrics alone do not reproduce.
- Define naming/tagging conventions so runs are findable later, not just storable now.

**Must Not:**
- Recommend logging "everything" without a retention and signal-to-noise plan.
- Assume a specific platform API; frame code as illustrative and confirm the tracker first.
- Treat experiment tracking as a substitute for a registry, pipeline orchestrator, or version control.

**Instructions:**

1. **Confirm platform and scope.** Establish the tracker, team size, and whether runs feed production. This sets multi-tenant naming, access, and retention needs.

2. **Define the run unit and hierarchy.** Specify what one "run" is, how runs roll up into experiments/projects, and how grouped runs (HPO sweeps, CV folds, retrains) nest, so comparisons are apples-to-apples.

3. **Specify the logged schema.** Enumerate params (hyperparameters, config), metrics (per-epoch and final, with the eval slice), artifacts (model, plots, sample predictions), and the eval dataset identity. Mark which are required vs optional.

4. **Lock the reproducibility triad.** For every run, capture code version (git SHA + dirty flag), data version (hash/snapshot/DVC pointer), and environment (lockfile/image digest, hardware, seeds). Without all three, a run is not reproducible.

5. **Design lineage links.** Connect run → input dataset version → parent experiment → resulting registered model, so anyone can trace a production model back to its training run and data.

6. **Set naming, tagging, and search conventions.** Define run-name patterns and a small controlled tag vocabulary (owner, stage, model-family, objective) that make filtering and comparison reliable.

7. **Write the logging discipline.** State who logs, when (auto vs manual), the auto-log hooks to enable, and the minimum-bar checklist a run must meet to be considered valid.

8. **Plan retention and access.** Decide what is kept how long, what gets pruned, and who can read/write — balancing audit needs against cost and clutter.

**Output Format:**

A markdown spec:
- **Tracking Architecture** — platform, run/experiment hierarchy, storage layout.
- **Logged Schema Table** — Item | Type (param/metric/artifact/version) | Required? | How captured.
- **Reproducibility Triad** — exactly how code, data, env are versioned per run.
- **Lineage & Naming Conventions** — link graph + naming/tagging rules.
- **Logging Discipline Checklist** — the minimum bar for a valid run.
- **Retention & Access Policy** — keep/prune rules, permissions.

## Verification

- [ ] Every logged item maps to a reproducibility or comparison question it answers.
- [ ] Code, data, and environment versioning are all specified (not just metrics).
- [ ] The run/experiment hierarchy handles sweeps, CV folds, and retrains without ambiguity.
- [ ] Lineage lets a production model be traced back to its run and data version.
- [ ] Naming/tagging conventions make a six-month-old run findable.
- [ ] Platform-specific code (if any) is framed as illustrative, with the tracker confirmed.

## False-Positive Prevention

❌ **DON'T:**
- Call a project "tracked" because metrics are logged while the data version and git SHA are not — that run is not reproducible.
- Treat a tidy metrics dashboard as proof of lineage; dashboards show outcomes, not provenance.
- Assume auto-logging captures the data snapshot — most auto-loggers capture params/metrics, not the dataset identity.
- Conflate experiment tracking with the model registry; tracking records the journey, the registry governs the released artifact.

✅ **DO:**
- Verify the reproducibility triad (code + data + env) is logged before declaring tracking complete.
- Make lineage an explicit link (run → dataset version → registered model), not an inference from timestamps.
- Confirm what the chosen platform auto-logs and fill the gaps manually.
- Define a "valid run" minimum bar and enforce it, so missing-metadata runs are caught at log time, not months later.

## Example Output

```markdown
## Experiment Tracking Spec — Fraud Scoring Team (MLflow, on Databricks)

### Tracking Architecture
- Tracker: MLflow on Databricks; one MLflow Experiment per model project (`/fraud/cardnotpresent`).
- Run hierarchy: parent run = HPO sweep; child runs = trials; nested runs = CV folds.
- Storage: artifacts in S3 under experiment-scoped prefix; metadata in managed MLflow store.

### Logged Schema Table
| Item | Type | Required? | How captured |
|---|---|---|---|
| hyperparameters | param | yes | `mlflow.log_params` from config dataclass |
| AUC / PR-AUC / recall@1%FPR | metric | yes | per-epoch + final, tagged with eval slice |
| git SHA + dirty flag | version | yes | logged via run tag at start |
| dataset snapshot hash | version | yes | DVC pointer logged as param |
| env image digest + seed | version | yes | container digest + `seed` param |
| model artifact + reliability plot | artifact | yes | `mlflow.log_artifact` |
| sample scored predictions | artifact | optional | 1k-row sample for debugging |

### Reproducibility Triad
- Code: git SHA tag `git.sha`, plus `git.dirty=true/false`; CI rejects dirty for promoted runs.
- Data: `data.dvc_rev` + `data.sha256`; eval slice id recorded with each metric.
- Env: `env.image=ecr/...@sha256:...`, `seed=1337`, `gpu=A10G`.

### Lineage & Naming Conventions
- Run name: `{model_family}-{objective}-{yyyymmdd}-{shortsha}`.
- Tags: `owner`, `stage=dev|candidate`, `model_family`, `objective`.
- Lineage: run links dataset version → registered model version on promotion.

### Logging Discipline Checklist (valid-run bar)
- [ ] git SHA + dirty flag, [ ] data hash, [ ] env digest + seed, [ ] eval slice id, [ ] final metric.

### Retention & Access Policy
- Candidate/promoted runs: kept indefinitely. Dev runs: pruned after 90 days unless tagged `keep`.
- Write: project team. Read: org ML guild. Promotion tags: leads only.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** platform → schema → triad → lineage → discipline sequence.
- **RT-02 (Multi-Dimensional Analysis Framework):** balances signal, reproducibility, cost, and findability.
- **CM-02 (Constraint Specification):** reproducibility triad is the governing constraint on every run.
- **DS-02 (Metric Specification):** ties metric logging to eval slice identity, not bare numbers.
- **QA-01 (Self-Verification):** the valid-run checklist enforces the minimum bar at log time.

**Related Prompts:**
- `mlops_model_registry_design.md` — govern the artifacts these runs produce.
- `mlops_reproducibility_audit.md` — find what current tracking is missing.
- `mlops_training_pipeline_orchestration.md` — emit these logs from an orchestrated DAG.
