---
title: "Google Vertex AI Training & Deployment Playbook"
category: AI-ML/mlops-infrastructure
description: "Design a training-to-serving workflow on Google Vertex AI — custom/AutoML training, Model Registry, online vs. batch prediction endpoints, Vertex Pipelines CI/CD, cost controls, and rollback — without inventing pricing or version-specific API behavior."
techniques:
  - ST-02
  - CM-02
  - RT-02
  - DS-06
  - QA-01
difficulty: advanced
tags:
  - vertex-ai
  - gcp
  - model-serving
  - deployment
  - mlops
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/mlops-infrastructure/mlops_model_serving_architecture.md
  - domain-AI-ML/mlops-infrastructure/mlops_ml_cicd_pipeline_design.md
  - domain-AI-ML/mlops-infrastructure/mlops_infra_cost_optimization.md
---

# Google Vertex AI Training & Deployment Playbook

**Objective:** Turn a trained-model goal into a concrete Google Vertex AI workflow — custom or AutoML training, Model Registry, the right prediction surface (online endpoint vs. batch prediction), Vertex Pipelines CI/CD, and cost/rollback controls — so the path from training to served model is explicit and reversible on GCP.

**When to Use:**
- GCP is your platform and you need an opinionated Vertex AI walkthrough rather than a tool-agnostic serving design.
- You must choose between online endpoints and batch prediction for a specific workload.
- You are wiring Vertex training + deployment into Vertex Pipelines with promotion gates.

**When NOT to Use:**
- You are still choosing a serving approach in the abstract — start with `mlops_model_serving_architecture.md`.
- You need the tool-agnostic CI/CD design first — use `mlops_ml_cicd_pipeline_design.md`.
- The task is purely cost tuning of existing infra — use `mlops_infra_cost_optimization.md`.

## Inputs / Context

Provide what you can:
- **Model type & size**, framework + version; custom container vs. prebuilt vs. AutoML.
- **Traffic profile** — request rate, latency SLO, burstiness; online vs. batch.
- **Project, region, and IAM** constraints; VPC Service Controls / private endpoints if required.
- **Existing GCP footprint** — GCS layout, Artifact Registry, Vertex Pipelines, Cloud Build.
- **Budget ceiling** and tolerance for always-on node cost vs. batch latency.

## Constraints

**Must:**
- Ask for the traffic profile and latency SLO before recommending online vs. batch; justify against them.
- Tie every deployed model to a Model Registry version, training run, code SHA, and data version.
- Define a rollout strategy (traffic splitting across deployed models) and an explicit rollback.

**Must Not:**
- Quote machine-type specs, accelerator pricing, quotas, or API signatures from memory — mark "verify in current Google Cloud / Vertex AI docs and your project's pricing/quotas."
- Recommend an always-on online endpoint with provisioned nodes for low-volume or scheduled workloads without comparing batch prediction.
- Use broad IAM roles; specify least-privilege service accounts per stage.

**Instructions:**

1. **State serving requirements.** Capture latency SLO, request rate/burstiness, payload size, and whether predictions are online or batch/scheduled. This drives the endpoint decision.

2. **Design the training step.** Choose custom training (custom container in Artifact Registry) vs. AutoML; specify inputs from GCS, hyperparameters, output artifact location, and machine/accelerator type. Record git SHA + data version.

3. **Choose the prediction surface with a decision matrix.** Compare online endpoint (with node autoscaling) vs. batch prediction against latency, throughput, payload, and cost/idle-node considerations. Recommend one; state why the other was rejected.

4. **Wire Model Registry promotion.** Register model versions; define the gate from candidate → default/production (eval thresholds + approval) and link each version to its training run, code SHA, and data version.

5. **Design rollout & rollback.** Use traffic splitting across deployed model versions on an endpoint (e.g., canary %), health checks, node autoscaling (min/max), and an explicit rollback (shift traffic to prior version) with a defined trigger.

6. **Integrate CI/CD with Vertex Pipelines.** Describe merge → pipeline (preprocess → train → evaluate → register → conditional deploy) with the promotion gate enforced as a pipeline condition, not a manual step. Cross-link `mlops_ml_cicd_pipeline_design.md`.

7. **Set cost & monitoring controls.** Right-size machine/accelerator types, enable model monitoring (skew/drift) on the endpoint, set min-nodes appropriately (avoid idle GPUs), and define alerts. Cross-link `mlops_infra_cost_optimization.md` and production-monitoring prompts.

8. **Define validation.** Provide a smoke test: deploy to an endpoint with low traffic split, send a representative request, confirm latency within SLO and monitoring capturing, then shift full traffic.

**Output Format:**

A markdown deployment playbook:
- **Serving Requirements** — SLO, rate, payload, online/batch
- **Training Step Spec** — custom/AutoML, inputs, machine type, artifacts
- **Prediction-Surface Decision Matrix** — table: Option | Fit | Cost | Verdict
- **Registry Promotion Flow** — stages + gates + lineage
- **Rollout & Rollback** — traffic split, autoscaling, rollback trigger
- **CI/CD (Vertex Pipelines)** — stages + enforced condition
- **Cost & Monitoring** — controls + alerts
- **Smoke Test** — validation steps
- **Verify-in-Docs** — pricing/quota/API items flagged

## Verification

- [ ] Online vs. batch is justified against the latency SLO and traffic profile.
- [ ] Each deployed model links to a registry version + training run + code SHA + data version.
- [ ] Traffic splitting and an explicit rollback trigger are defined before production.
- [ ] The promotion gate is a pipeline condition, not a manual click.
- [ ] Least-privilege service accounts are specified per stage.
- [ ] Machine specs, accelerator pricing, and quotas are flagged "verify," not asserted.

## False-Positive Prevention

❌ **DON'T:**
- Stand up an always-on online endpoint with provisioned GPUs for a workload that runs on a schedule — batch prediction may be far cheaper.
- Call a deployment done without traffic-split rollout and a rollback trigger.
- Quote accelerator hourly cost or regional quotas from memory.
- Promote on a metric computed on tuning data rather than a held-out/golden set.

✅ **DO:**
- Select online vs. batch from a matrix scored on latency, throughput, payload, and idle-cost.
- Roll out via traffic splitting with a health-based rollback to the prior version.
- Point the user to current Vertex AI pricing/quota pages for any figure.
- Gate promotion on a golden eval distinct from tuning data; enable skew/drift monitoring.

## Example Output

```markdown
## Vertex AI Playbook: Product-Recommendation Reranker

### Serving Requirements
- p99 < 120ms online during peak; ~150 req/s with daily peaks; medium payload.

### Training Step Spec
- Custom training, container in Artifact Registry; inputs from gs://.../features/v8.
- Machine type with 1 accelerator (verify type/availability); git_sha + data_version=v8 recorded.

### Prediction-Surface Decision Matrix
| Option | Fit | Cost | Verdict |
|---|---|---|---|
| Online endpoint + autoscaling | Meets p99, handles peaks | Min-node baseline cost | ✅ Chosen |
| Batch prediction | Adds unacceptable latency | Cheaper, no idle nodes | ❌ Online need |

### Registry Promotion Flow
Register version → candidate → (beats golden-set NDCG + approval) → set as endpoint default. Links training run + git_sha + data_version.

### Rollout & Rollback
Deploy new version at 10% traffic split → ramp to 100% if healthy; autoscale min 2 / max 10; rollback trigger: latency/error breach → revert split to prior version.

### CI/CD (Vertex Pipelines)
Merge → pipeline: preprocess → train → evaluate → register → ConditionalDeploy(if golden NDCG ≥ threshold). Gate is a pipeline condition.

### Cost & Monitoring
Right-size machine; min-nodes tuned to avoid idle GPU; enable model monitoring for feature skew/drift; alert on drift + latency. See mlops_infra_cost_optimization.md.

### Smoke Test
Deploy at low split → send representative request → confirm p99 < 120ms warm → confirm monitoring active → ramp traffic.

### Verify-in-Docs
- Machine/accelerator types, regional pricing, quotas.
- Current Model Registry + traffic-split API and monitoring config.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** requirements → training → surface choice → registry → rollout → CI/CD → validation.
- **CM-02 (Constraint Specification):** no-fabrication (pricing/quota/API), least-privilege, and rollback constraints govern the design.
- **RT-02 (Multi-Dimensional Analysis):** online vs. batch weighs latency, throughput, payload, and idle cost together.
- **DS-06 (Prioritization & Severity Guidance):** the decision matrix ranks prediction surfaces against weighted requirements.
- **QA-01 (Self-Verification):** the smoke test and checklist confirm SLO compliance and rollback readiness.

**Related Prompts:**
- `mlops_model_serving_architecture.md` — tool-agnostic serving design before committing to Vertex AI.
- `mlops_ml_cicd_pipeline_design.md` — the CI/CD backbone this playbook plugs into.
- `mlops_infra_cost_optimization.md` — deeper cost controls for the chosen machines/endpoints.
