---
title: "Databricks MLOps Stack Playbook"
category: AI-ML/mlops-infrastructure
description: "Design an end-to-end MLOps workflow on Databricks — managed MLflow tracking, Unity Catalog model registry, Model Serving endpoints, Workflows/Jobs CI/CD, and the deploy-code promotion pattern across dev/staging/prod — without inventing pricing or version-specific API behavior."
techniques:
  - ST-02
  - CM-02
  - RT-02
  - DS-06
  - QA-01
difficulty: advanced
tags:
  - databricks
  - mlflow
  - unity-catalog
  - model-serving
  - mlops
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/mlops-infrastructure/mlops_mlflow_experiment_tracking_playbook.md
  - domain-AI-ML/mlops-infrastructure/mlops_ml_cicd_pipeline_design.md
  - domain-AI-ML/mlops-infrastructure/mlops_model_registry_design.md
---

# Databricks MLOps Stack Playbook

**Objective:** Turn a Databricks-platform decision into a concrete end-to-end MLOps workflow — managed MLflow tracking, Unity Catalog as the model registry and governance layer, Model Serving endpoints, and Workflows/Jobs for CI/CD across dev → staging → prod using the deploy-code promotion pattern — so experiments, governance, and serving form one reproducible pipeline.

**When to Use:**
- Databricks is your platform and you want an opinionated stack walkthrough spanning tracking, registry, serving, and CI/CD.
- You need to set up environment promotion (dev/staging/prod) and decide between deploy-code vs. deploy-model patterns.
- You are governing models through Unity Catalog and wiring serving endpoints.

**When NOT to Use:**
- You only need the MLflow tracking layer (any host) — use `mlops_mlflow_experiment_tracking_playbook.md`.
- You need tool-agnostic CI/CD design — use `mlops_ml_cicd_pipeline_design.md`.
- You need registry/promotion design independent of platform — use `mlops_model_registry_design.md`.

## Inputs / Context

Provide what you can:
- **Databricks runtime (DBR / ML runtime) version** and whether Unity Catalog is enabled.
- **Workspace topology** — single workspace with environments vs. separate dev/staging/prod workspaces.
- **Catalog/schema structure** in Unity Catalog and existing governance rules.
- **Serving needs** — real-time endpoint vs. batch scoring; latency SLO and traffic profile.
- **CI/CD tooling** — Databricks Asset Bundles, Repos, and an external CI (GitHub Actions, Azure DevOps, etc.).

## Constraints

**Must:**
- Ask whether Unity Catalog is enabled and the runtime version before giving registry/serving steps; flag version-sensitive behavior.
- Choose and justify a promotion pattern (deploy-code vs. deploy-model) for the team's setup.
- Tie each registered model (Unity Catalog) to its source run, code version, and data version (Delta table version / lineage).

**Must Not:**
- Quote DBU/compute pricing, runtime defaults, or API signatures from memory — mark "verify in current Databricks docs and your account pricing."
- Conflate the legacy Workspace Model Registry with Unity Catalog registry — confirm which the workspace uses.
- Recommend manual notebook-run promotions to production without a Jobs/Workflows + CI gate.

**Instructions:**

1. **Confirm the platform baseline.** Establish runtime version, Unity Catalog status, and workspace topology (single-workspace environments vs. multi-workspace). This determines registry mechanics and promotion design.

2. **Set tracking conventions.** Use managed MLflow: experiment-per-objective, required run tags (git SHA, data/Delta version, intent). Reuse `mlops_mlflow_experiment_tracking_playbook.md` for the logging contract.

3. **Model the Unity Catalog registry.** Define catalog.schema.model naming, who can register/promote, and how aliases/versions represent staging vs. production. Link versions to source run + code + Delta table version for lineage.

4. **Choose the promotion pattern.** Decide deploy-code (promote the training code across environments; retrain in each) vs. deploy-model (promote the model artifact). Justify against reproducibility, data access per environment, and regulatory needs.

5. **Design Model Serving.** For real-time, specify a serving endpoint, compute sizing, scale-to-zero where supported, and traffic split for canary; for batch, specify a scheduled Job scoring against Delta. Decide from the traffic/latency profile.

6. **Wire CI/CD with Workflows + Asset Bundles.** Describe how merges trigger Jobs/Workflows (train → evaluate → register → conditional promote) defined as Asset Bundles in Repos, with the promotion gate enforced in the pipeline. Cross-link `mlops_ml_cicd_pipeline_design.md`.

7. **Set governance, cost, and monitoring.** Use Unity Catalog permissions/lineage for governance; enable Lakehouse Monitoring (or equivalent) for inference tables/drift; right-size clusters and use scale-to-zero/job clusters to control DBU spend.

8. **Define validation.** Provide a smoke test: run training in dev, register to Unity Catalog, promote to staging via the Job, deploy to a serving endpoint at low traffic, confirm scoring + lineage, then promote to prod.

**Output Format:**

A markdown stack playbook:
- **Platform Baseline** — runtime, UC status, workspace topology
- **Tracking Conventions** — experiments, required tags
- **Unity Catalog Registry Model** — naming, permissions, aliases/versions, lineage
- **Promotion Pattern** — deploy-code vs. deploy-model + rationale
- **Model Serving Design** — real-time/batch, sizing, canary
- **CI/CD (Workflows + Asset Bundles)** — stages + enforced gate
- **Governance, Cost, Monitoring** — controls
- **Smoke Test** — validation steps
- **Verify-in-Docs** — pricing/version/API items flagged

## Verification

- [ ] Unity Catalog status and runtime version are confirmed before registry/serving steps.
- [ ] A promotion pattern (deploy-code vs. deploy-model) is chosen with explicit rationale.
- [ ] Each registered model links to source run + code version + Delta/data version.
- [ ] Production promotion runs through Workflows/Jobs + CI gate, not manual notebook runs.
- [ ] Serving design (real-time/batch + sizing + canary) matches the traffic/latency profile.
- [ ] DBU/pricing, runtime defaults, and API calls are flagged "verify," not asserted.

## False-Positive Prevention

❌ **DON'T:**
- Assume the legacy Workspace Model Registry behaves like the Unity Catalog registry — promotion and permissions differ.
- Promote a model to production by manually re-running a notebook, bypassing the Jobs/CI gate.
- Quote DBU rates or cluster pricing from memory.
- Default to deploy-model when each environment lacks access to consistent data for the deploy-code pattern (or vice versa) without justifying the choice.

✅ **DO:**
- Confirm which registry the workspace uses and design promotion to match it.
- Enforce production promotion through Workflows/Jobs + a CI gate on a golden eval.
- Direct the user to current Databricks pricing/runtime docs for any figure or default.
- Choose deploy-code vs. deploy-model based on reproducibility, per-env data access, and governance — and state why.

## Example Output

```markdown
## Databricks MLOps Playbook: Churn Model (UC enabled, multi-workspace)

### Platform Baseline
- ML runtime (verify version); Unity Catalog enabled; separate dev/staging/prod workspaces sharing one metastore.

### Tracking Conventions
- Managed MLflow; experiment `/churn/training`; tags: git_sha, delta_version, intent.

### Unity Catalog Registry Model
- Model `prod_catalog.ml.churn_model`; register from dev; aliases: `@staging`, `@champion`.
- Each version links source run + git_sha + Delta table version (lineage via UC).

### Promotion Pattern
Deploy-code: training code promoted dev→staging→prod via bundles; model retrained against each env's governed data (regulatory traceability). Rationale: reproducibility + per-env data isolation.

### Model Serving Design
Real-time endpoint (p99 < 150ms), scale-to-zero off-peak, canary 10%→100%. Batch fallback Job scores Delta nightly.

### CI/CD (Workflows + Asset Bundles)
Repo merge → Asset Bundle deploys Job: train → evaluate → register to UC → ConditionalPromote(@staging if golden AUC ≥ threshold) → manual approval → @champion + endpoint update.

### Governance, Cost, Monitoring
UC permissions + lineage; Lakehouse Monitoring on inference table for drift; job clusters + scale-to-zero to control DBU.

### Smoke Test
Train in dev → register UC version → promote @staging via Job → deploy endpoint at 10% → confirm scoring + lineage → promote @champion.

### Verify-in-Docs
- DBU/compute pricing; runtime version capabilities.
- UC registry alias API, serving endpoint config, Lakehouse Monitoring setup.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** baseline → tracking → registry → promotion → serving → CI/CD → validation.
- **CM-02 (Constraint Specification):** no-fabrication, UC-vs-legacy correctness, and gated-promotion constraints govern the design.
- **RT-02 (Multi-Dimensional Analysis):** the promotion pattern and serving choice weigh reproducibility, data access, latency, and cost together.
- **DS-06 (Prioritization & Severity Guidance):** deploy-code vs. deploy-model is a ranked decision against weighted criteria.
- **QA-01 (Self-Verification):** the smoke test and checklist confirm the pipeline and lineage end-to-end.

**Related Prompts:**
- `mlops_mlflow_experiment_tracking_playbook.md` — the managed-MLflow tracking layer this stack builds on.
- `mlops_ml_cicd_pipeline_design.md` — tool-agnostic CI/CD design the Workflows wiring implements.
- `mlops_model_registry_design.md` — registry/promotion design independent of Unity Catalog specifics.
