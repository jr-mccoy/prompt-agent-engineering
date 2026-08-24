---
title: "MLflow Experiment Tracking & Model Registry Playbook"
category: AI-ML/mlops-infrastructure
description: "Stand up MLflow for experiment tracking and model-registry promotion on a real stack — tracking server, run/artifact conventions, autologging, registry stages, and reproducibility hooks — without fabricating version-specific API behavior."
techniques:
  - ST-02
  - CM-02
  - RT-10
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - mlflow
  - experiment-tracking
  - model-registry
  - reproducibility
  - mlops
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/mlops-infrastructure/mlops_experiment_tracking_setup.md
  - domain-AI-ML/mlops-infrastructure/mlops_model_registry_design.md
  - domain-AI-ML/mlops-infrastructure/mlops_reproducibility_audit.md
---

# MLflow Experiment Tracking & Model Registry Playbook

**Objective:** Turn a team's "we should track experiments" intent into a concrete MLflow deployment — tracking-server topology, run/experiment naming conventions, what to log (params, metrics, artifacts, signatures), autologging configuration, and a model-registry promotion flow — so runs are reproducible and the path from experiment to registered model is explicit.

**When to Use:**
- You have chosen MLflow (or it is mandated by your platform) and need an opinionated setup walkthrough rather than a tool-selection decision.
- Experiments currently live in notebooks, ad-hoc spreadsheets, or print statements and nothing is reproducible.
- You need to wire a model-registry promotion flow (None → Staging → Production) into an existing training pipeline.

**When NOT to Use:**
- You have not yet decided *whether* MLflow is the right tracker — start with the tool-agnostic `mlops_experiment_tracking_setup.md`.
- You only need registry *design* independent of tooling — use `mlops_model_registry_design.md`.
- You are auditing existing reproducibility gaps rather than building tracking — use `mlops_reproducibility_audit.md`.

## Inputs / Context

Provide what you can; the playbook degrades gracefully if some are missing:
- **MLflow version** and deployment target (local file store, self-hosted tracking server, Databricks-managed, or other managed offering).
- **Backend store & artifact store** — where run metadata lives (filesystem, SQL DB) and where artifacts live (local, S3/GCS/Azure Blob).
- **ML frameworks** in use (and versions) — drives which autolog integrations apply.
- **Team size & access model** — single user vs. team needing auth, RBAC, and shared experiments.
- **Existing pipeline** — how training is launched (notebook, script, orchestrator) and whether CI/CD is involved.

## Constraints

**Must:**
- Ask for the MLflow version and deployment target before giving setup steps; flag any step whose behavior is version-sensitive.
- Specify run/experiment naming and tagging conventions so runs are filterable and comparable, not just stored.
- Tie every registered model to the exact run, code version (git SHA), data version, and environment that produced it.

**Must Not:**
- Invent MLflow API signatures, config flags, default ports, or managed-service pricing — if version-specific, mark "verify against current MLflow docs / your deployment."
- Present autologging as a substitute for logging a model signature, input example, and environment.
- Recommend the local file store for a team setting where concurrent writes or shared access are required.

**Instructions:**

1. **Fix the deployment topology.** From the inputs, state the tracking-server mode (local, remote server, or managed), the backend store (metadata), and the artifact store. Call out the one combination that fits team size and access needs, and why lighter options were rejected.

2. **Define experiment & run structure.** Establish an experiment-naming scheme (e.g., one experiment per project/objective), a run-naming/tagging convention (git SHA tag, data-version tag, owner, intent), and how parent/child runs are used for HPO sweeps.

3. **Specify what gets logged.** Enumerate params, metrics (with step/epoch where relevant), and artifacts. Require a logged model signature, an input example, and the environment (dependencies) for every model run — these are what make a run reproducible.

4. **Configure autologging deliberately.** For each framework in use, state whether autolog is enabled and what it captures vs. what must still be logged manually (signature, custom metrics, data version). Note that autolog defaults change across versions — direct the user to verify.

5. **Design the registry promotion flow.** Define stages (None → Staging → Production → Archived), the gate for each transition (eval thresholds, approval), and how a registered version links back to its source run, code SHA, and data version.

6. **Wire reproducibility hooks.** Specify capture of: git commit, seed(s), dependency lockfile/environment, and data version/lineage reference. Cross-link `mlops_reproducibility_audit.md` for the full checklist.

7. **Set access, retention, and cost guards.** State the auth model (if team), artifact retention/cleanup policy, and storage-cost controls for large artifacts. Avoid unbounded artifact accumulation.

8. **Define the validation path.** Describe how to confirm the setup works end-to-end: a smoke-test run that logs params/metrics/model, appears in the UI, and can be reloaded and promoted.

**Output Format:**

A markdown setup playbook:
- **Deployment Topology** — table: Component (tracking server / backend store / artifact store) | Choice | Why
- **Experiment & Run Conventions** — naming, required tags
- **Logging Contract** — what is logged manually vs. via autolog (table)
- **Registry Promotion Flow** — stages + transition gates
- **Reproducibility Hooks** — captured fields
- **Access / Retention / Cost** — policies
- **Smoke Test** — steps to validate end-to-end
- **Open Questions / Verify-in-Docs** — version-sensitive items flagged

## Verification

- [ ] The deployment topology matches team size and access needs (no file store for concurrent teams).
- [ ] Every model run logs a signature, input example, and environment — not just metrics.
- [ ] Each registry stage has an explicit promotion gate, not just a manual toggle.
- [ ] Registered models trace back to run ID + git SHA + data version.
- [ ] Version-sensitive steps are flagged "verify against current docs" rather than asserted.
- [ ] A concrete smoke test confirms log → view → reload → promote works.

## False-Positive Prevention

❌ **DON'T:**
- Call tracking "set up" because runs appear in the UI, while none capture the code/data/env needed to reproduce them.
- Rely on autolog and assume the model is reproducible — autolog often omits the data version and may omit the signature.
- Promote a model to Production on a metric that was tuned against the same data it's evaluated on (validation overfitting).
- Quote a default port, env var, or API call from memory as if version-stable.

✅ **DO:**
- Treat a run as reproducible only when git SHA, seed, environment, and data version are all logged and linkable.
- State explicitly what autolog captures for each framework and what you must log on top of it.
- Gate Production promotion on a held-out/golden eval set distinct from tuning data.
- Mark every version-sensitive flag, default, or signature as "verify against your MLflow version's docs."

## Example Output

```markdown
## MLflow Playbook: Demand-Forecasting Team (MLflow remote server, S3 artifacts)

### Deployment Topology
| Component | Choice | Why |
|---|---|---|
| Tracking server | Remote MLflow server behind internal auth | 6 ML engineers need shared experiments; file store can't handle concurrent writes |
| Backend store | PostgreSQL | Queryable run metadata; supports model registry (registry requires a DB-backed store) |
| Artifact store | S3 bucket (versioned) | Large model + dataset artifacts; lifecycle rules for retention |

### Experiment & Run Conventions
- Experiment per objective: `demand-forecast/{region}`.
- Required run tags: `git_sha`, `data_version`, `owner`, `intent` (baseline | tuning | candidate).
- HPO sweeps use a parent run with child runs per trial.

### Logging Contract
| Item | Manual | Autolog |
|---|---|---|
| Params (hyperparams) | — | ✅ (framework autolog) |
| Metrics per step | — | ✅ |
| Business metric (WAPE) | ✅ custom | — |
| Model signature + input example | ✅ (verify autolog version behavior) | partial |
| Environment / requirements | ✅ logged with model | partial |
| Data version reference | ✅ tag + artifact pointer | ❌ |

### Registry Promotion Flow
- None → Staging: passes unit + smoke eval, signature present.
- Staging → Production: beats current Production on golden set (WAPE), reviewed + approved.
- Production → Archived: superseded; retained 90 days.
- Each version links: source run ID, git SHA, data_version.

### Reproducibility Hooks
git commit • seed(s) • dependency lockfile • data_version → lineage record. See mlops_reproducibility_audit.md.

### Access / Retention / Cost
- Auth: SSO in front of tracking server.
- Artifact retention: candidates 180d, archived models 90d, sweep trials 30d.
- Cost guard: S3 lifecycle to cold storage after 30d; block artifacts > 2GB without tag.

### Smoke Test
1. Run training script with `intent=baseline`.
2. Confirm run appears with all required tags + logged model.
3. Reload model from the run URI; score the input example.
4. Register, transition to Staging, confirm lineage fields populated.

### Open Questions / Verify-in-Docs
- Confirm autolog signature-capture behavior for your framework + MLflow version.
- Confirm registry stage-transition API vs. alias-based flow in your MLflow version.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** topology → conventions → logging → registry → reproducibility → validation.
- **CM-02 (Constraint Specification):** no-fabrication and reproducibility constraints govern every recommendation.
- **RT-10 (Troubleshooting / Operational Reasoning):** setup is framed around what actually makes runs reproducible and promotable in practice.
- **DS-02 (Metric Specification):** logging contract and promotion gates are defined in terms of concrete metrics on the right data.
- **QA-01 (Self-Verification):** the smoke test and checklist force end-to-end validation, not just "runs appear."

**Related Prompts:**
- `mlops_experiment_tracking_setup.md` — decide *whether* MLflow (vs. alternatives) before this playbook.
- `mlops_model_registry_design.md` — tool-agnostic registry and promotion-gate design.
- `mlops_reproducibility_audit.md` — full reproducibility checklist the hooks here feed into.
