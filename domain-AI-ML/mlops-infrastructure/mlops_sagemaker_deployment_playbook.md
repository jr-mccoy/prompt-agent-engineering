---
title: "Amazon SageMaker Training & Deployment Playbook"
category: AI-ML/mlops-infrastructure
description: "Design a training-to-serving workflow on Amazon SageMaker — training jobs, model registry, real-time vs. batch vs. async endpoints, CI/CD wiring, cost controls, and rollback — without inventing instance pricing or version-specific API behavior."
techniques:
  - ST-02
  - CM-02
  - RT-02
  - DS-06
  - QA-01
difficulty: advanced
tags:
  - sagemaker
  - aws
  - model-serving
  - deployment
  - mlops
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/mlops-infrastructure/mlops_model_serving_architecture.md
  - domain-AI-ML/mlops-infrastructure/mlops_ml_cicd_pipeline_design.md
  - domain-AI-ML/mlops-infrastructure/mlops_infra_cost_optimization.md
---

# Amazon SageMaker Training & Deployment Playbook

**Objective:** Turn a trained-model goal into a concrete Amazon SageMaker workflow — training jobs and their artifacts, model-registry promotion, the right endpoint type (real-time, serverless, asynchronous, or batch transform), CI/CD wiring, and cost/rollback controls — so the path from training to production serving is explicit and reversible.

**When to Use:**
- AWS is your platform and you need an opinionated SageMaker walkthrough rather than a tool-agnostic serving design.
- You must choose among SageMaker endpoint types for a specific latency/throughput/cost profile.
- You are wiring SageMaker training + deployment into a CI/CD pipeline with promotion gates.

**When NOT to Use:**
- You are still choosing a serving approach in the abstract — start with `mlops_model_serving_architecture.md`.
- You need the tool-agnostic CI/CD design first — use `mlops_ml_cicd_pipeline_design.md`.
- The problem is purely cost optimization of existing infra — use `mlops_infra_cost_optimization.md`.

## Inputs / Context

Provide what you can:
- **Model type & size**, framework + version, and whether a prebuilt or custom container is needed.
- **Traffic profile** — request rate, latency SLO, burstiness, and whether traffic is online or batch.
- **Region, account structure, and IAM** constraints; VPC/private-networking requirements.
- **Existing AWS footprint** — S3 layout, ECR, Step Functions / SageMaker Pipelines, CodePipeline, etc.
- **Budget ceiling** and tolerance for cold starts vs. always-on cost.

## Constraints

**Must:**
- Ask for traffic profile and latency SLO before recommending an endpoint type; justify the choice against them.
- Tie every deployed model to a Model Registry version, training job, code SHA, and data version.
- Define rollback and a safe deployment strategy (e.g., blue/green or canary) before going to production.

**Must Not:**
- Quote instance pricing, instance-type specs, quotas, or API signatures from memory — mark "verify in current AWS/SageMaker docs and your account's pricing/quotas."
- Recommend an always-on real-time endpoint for spiky or low-volume traffic without comparing serverless/async.
- Grant broad IAM permissions; specify least-privilege roles for training, registry, and endpoints.

**Instructions:**

1. **State the serving requirements.** Capture latency SLO, request rate/burstiness, payload size, and online-vs-batch nature. These determine the endpoint decision more than anything else.

2. **Design the training job.** Specify container (prebuilt vs. custom/BYOC), input channels from S3, hyperparameters, output artifact path, and spot vs. on-demand for cost. Capture git SHA + data version as job tags/metadata.

3. **Choose the endpoint type with a decision matrix.** Compare real-time, serverless inference, asynchronous inference, and batch transform against the requirements (latency, throughput, payload, cost, cold-start tolerance). Recommend one and state why others were rejected.

4. **Wire the Model Registry promotion flow.** Register model versions with approval status; define the gate from PendingManualApproval/Staging → Approved/Production (eval thresholds + review). Link each version to training job + code + data version.

5. **Design the deployment strategy.** Specify blue/green or canary rollout, health checks, autoscaling policy (target metric + min/max), and the explicit rollback trigger and procedure.

6. **Integrate CI/CD.** Describe how a merge triggers train → evaluate → register → deploy through SageMaker Pipelines + CodePipeline (or your orchestrator), with the promotion gate enforced in the pipeline, not by hand. Cross-link `mlops_ml_cicd_pipeline_design.md`.

7. **Set cost and observability controls.** Specify autoscaling-to-zero where supported (serverless), instance right-sizing, data-capture for monitoring, and alarms. Cross-link `mlops_infra_cost_optimization.md` and production-monitoring prompts.

8. **Define the validation path.** Provide a smoke test: deploy to a test endpoint, invoke with a representative payload, verify latency within SLO, confirm data capture, then promote.

**Output Format:**

A markdown deployment playbook:
- **Serving Requirements** — SLO, rate, payload, online/batch
- **Training Job Spec** — container, channels, artifacts, cost mode
- **Endpoint Decision Matrix** — table: Option | Fit vs. requirements | Cost | Verdict
- **Registry Promotion Flow** — stages + gates + lineage
- **Deployment Strategy** — rollout, autoscaling, rollback trigger
- **CI/CD Wiring** — pipeline stages + enforced gate
- **Cost & Observability** — controls + alarms
- **Smoke Test** — validation steps
- **Verify-in-Docs** — pricing/quota/API items flagged

## Verification

- [ ] The endpoint type is justified against the stated latency SLO and traffic profile.
- [ ] Each deployed model links to a registry version + training job + code SHA + data version.
- [ ] A rollback trigger and procedure exist before any production deploy.
- [ ] The promotion gate is enforced in the pipeline, not applied manually.
- [ ] IAM roles are least-privilege per stage (train / register / serve).
- [ ] Pricing, instance specs, and quotas are flagged "verify," not asserted.

## False-Positive Prevention

❌ **DON'T:**
- Default to an always-on real-time endpoint because it's the familiar option, ignoring serverless/async/batch for the actual traffic shape.
- Call a deployment "production-ready" with no rollback path or health-based autoscaling.
- State instance hourly costs or quotas from memory — they vary by region and change over time.
- Approve a model version on a metric measured against tuning data rather than a held-out set.

✅ **DO:**
- Pick the endpoint type from a decision matrix scored against latency, throughput, payload, and cost.
- Require a tested rollback (blue/green or previous-version) before promotion.
- Direct the user to current AWS pricing/quota pages for any cost or limit figure.
- Gate promotion on a golden/held-out eval distinct from tuning data.

## Example Output

```markdown
## SageMaker Playbook: Fraud-Scoring Model (real-time, strict latency)

### Serving Requirements
- p99 latency < 80ms; ~300 req/s steady, 3x bursts; small JSON payloads; online.

### Training Job Spec
- Prebuilt framework container; input channels: train/val from s3://.../v12.
- Spot instances with checkpointing for cost; tags: git_sha, data_version=v12.
- Artifact → s3://.../models/fraud/{job-name}/.

### Endpoint Decision Matrix
| Option | Fit | Cost | Verdict |
|---|---|---|---|
| Real-time endpoint + autoscaling | Meets p99, handles bursts | Always-on baseline | ✅ Chosen |
| Serverless inference | Cold starts risk p99 breach | Scales to zero | ❌ Latency risk |
| Async inference | Not for sync scoring | Cheap for large/batch | ❌ Wrong shape |
| Batch transform | Offline only | Cheapest | ❌ Online need |

### Registry Promotion Flow
Register version → PendingManualApproval → (beats golden-set AUPRC + review) → Approved → deploy. Version links job + git_sha + data_version.

### Deployment Strategy
Blue/green with canary %; autoscale on invocations-per-instance, min 2 / max 12; rollback trigger: p99 > SLO or error rate > threshold for N min → shift traffic back to prior version.

### CI/CD Wiring
Merge → SageMaker Pipeline: process → train → evaluate → register; CodePipeline gate enforces golden-set threshold; approved → deploy stage. No manual prod toggles.

### Cost & Observability
Right-size instance family; enable data capture for monitoring; CloudWatch alarms on latency/error/instance count. See mlops_infra_cost_optimization.md.

### Smoke Test
Deploy to test endpoint → invoke representative payload → confirm p99 < 80ms on warm path → confirm data capture writing → promote.

### Verify-in-Docs
- Instance type specs, regional pricing, account quotas.
- Current endpoint-type capabilities and registry approval API.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** requirements → training → endpoint choice → registry → rollout → CI/CD → validation.
- **CM-02 (Constraint Specification):** no-fabrication (pricing/quota/API), least-privilege, and rollback constraints govern the design.
- **RT-02 (Multi-Dimensional Analysis):** endpoint choice weighs latency, throughput, payload, and cost together.
- **DS-06 (Prioritization & Severity Guidance):** the decision matrix ranks endpoint options against weighted requirements.
- **QA-01 (Self-Verification):** the smoke test and checklist confirm SLO compliance and rollback readiness.

**Related Prompts:**
- `mlops_model_serving_architecture.md` — tool-agnostic serving design before committing to SageMaker.
- `mlops_ml_cicd_pipeline_design.md` — the CI/CD backbone this playbook plugs into.
- `mlops_infra_cost_optimization.md` — deeper cost controls for the chosen instances/endpoints.
