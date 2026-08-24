---
title: "MLOps Model Registry Design"
category: AI-ML/mlops-infrastructure
description: "Design a model registry with lifecycle stages, approval gates, required metadata, and promotion criteria so only governed, traceable models reach production."
techniques:
  - ST-02
  - DS-01
  - CM-02
  - DS-06
  - QA-01
difficulty: intermediate
tags:
  - model-registry
  - governance
  - promotion-gates
  - model-card
  - lineage
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/mlops-infrastructure/mlops_experiment_tracking_setup.md
  - domain-AI-ML/mlops-infrastructure/mlops_ml_cicd_pipeline_design.md
  - domain-AI-ML/mlops-infrastructure/mlops_model_packaging_strategy.md
---

# MLOps Model Registry Design

**Objective:** Design a model registry — lifecycle stages, required metadata per version, approval gates, and promotion criteria — so that every production model is versioned, traceable to its training run and data, and can only advance through stages that have been explicitly satisfied.

**When to Use:**
- Models are deployed straight from notebooks or ad-hoc artifact buckets with no gate.
- Nobody can answer "what's in prod right now, who approved it, and how do we roll back?"
- Setting up CI/CD for ML and need a governed handoff between training and deployment.
- Operating in a regulated domain needing model lineage and sign-off records.

**When NOT to Use:**
- For recording exploratory runs (use `mlops_experiment_tracking_setup.md`).
- For the deployment mechanics themselves (use `mlops_model_serving_architecture.md`).

## Inputs / Context

Provide what you can:
- **Platform** — MLflow Model Registry / W&B / SageMaker Model Registry / Vertex AI Model Registry / Databricks Unity Catalog. Ask if unspecified.
- **Org context** — team count, regulatory regime, who is allowed to approve promotions.
- **Lifecycle reality** — how models go from trained → tested → prod today (even if informal).
- **Existing tracking** — whether runs already carry lineage the registry can link to.
- **Rollback needs** — how fast a bad model must be reverted; whether shadow/canary is used.

## Constraints

**Must:**
- Define explicit stages and the *gate criteria* required to move between them — a stage with no gate is just a label.
- Require lineage from each registered version back to its training run, data version, and code SHA.
- Separate the person who proposes a promotion from the person who approves it where governance demands it.

**Must Not:**
- Allow promotion based on a single offline metric without a baseline comparison and a passing eval suite.
- Assume registry features by platform; confirm the platform and frame APIs as illustrative.
- Conflate "registered" with "deployed" — registration is a governed record, not a rollout.

**Instructions:**

1. **Confirm platform and authority model.** Establish the registry tool and who may propose vs approve promotions; this drives stage permissions.

2. **Define the lifecycle stages.** Lay out stages (e.g., None → Staging/Candidate → Production → Archived) and what each means operationally — what traffic, if any, a model in that stage serves.

3. **Specify required metadata per version.** Enumerate the model card fields: training run link, data version, code SHA, metrics + eval slice, intended use, known limitations, owner, and dependencies.

4. **Set promotion gate criteria.** For each transition, list objective, checkable conditions (passes eval suite vs baseline, fairness slices within bounds, packaging/contract test green, sign-off recorded).

5. **Design approval and audit flow.** Define who approves each gate, what is recorded (who/when/why), and how the record is retained for audit.

6. **Plan rollback and version pinning.** Specify how the previous Production version is retained, how a rollback is triggered, and how serving pins to a specific version, not "latest."

7. **Wire lineage and discoverability.** Ensure each version links upstream to its run/data and downstream to its deployments; define tags/aliases so consumers can resolve "current prod" deterministically.

8. **Define deprecation and archival.** State when a version is archived, retention duration, and how superseded models are kept for reproducibility and audit.

**Output Format:**

A markdown spec:
- **Registry Architecture & Authority Model** — platform, who proposes/approves.
- **Lifecycle Stages** — table: Stage | Meaning | Serves traffic? | Entry gate.
- **Required Metadata (Model Card) Schema** — field | required? | source.
- **Promotion Gate Criteria** — per transition, the checkable conditions.
- **Rollback & Version Pinning** — retention + revert procedure.
- **Lineage, Tags & Archival Policy** — upstream/downstream links, deprecation rules.

## Verification

- [ ] Every stage transition has explicit, checkable gate criteria — no ungated stage.
- [ ] Each registered version links to training run, data version, and code SHA.
- [ ] Promotion requires a baseline comparison and a passing eval suite, not one bare metric.
- [ ] Propose/approve separation is defined where governance requires it.
- [ ] Rollback retains the prior Production version and serving pins by version, not "latest."
- [ ] Platform-specific APIs (if shown) are framed as illustrative with the platform confirmed.

## False-Positive Prevention

❌ **DON'T:**
- Treat a registry with stage labels but no gate criteria as "governance" — labels without checks gate nothing.
- Promote on a higher offline metric alone; without a baseline and eval suite it may be noise or leakage.
- Equate "registered as Production" with "deployed and serving" — they can diverge.
- Resolve "current prod" by latest-timestamp; use an explicit alias/tag or a version will silently change under consumers.

✅ **DO:**
- Require each gate to enumerate objective pass/fail conditions before a model can advance.
- Tie promotion to a baseline-relative result plus a passing eval and packaging contract test.
- Keep registration and deployment as distinct, separately recorded events.
- Pin serving to a specific version and retain the prior Production version for instant rollback.

## Example Output

```markdown
## Model Registry Spec — Recommendations Platform (SageMaker Model Registry)

### Registry Architecture & Authority Model
- Platform: SageMaker Model Registry, one Model Package Group per use case.
- Authority: ML engineers propose; the use-case lead + on-call SRE jointly approve Production.

### Lifecycle Stages
| Stage | Meaning | Serves traffic? | Entry gate |
|---|---|---|---|
| Candidate | passed offline eval | no | eval suite green vs baseline |
| Shadow | scoring live, not served | mirror only | latency p99 < 80ms in shadow |
| Production | serving users | yes | shadow parity + sign-off recorded |
| Archived | retired | no | superseded or deprecated |

### Required Metadata (Model Card) Schema
| Field | Required? | Source |
|---|---|---|
| training_run_uri | yes | tracker run link |
| data_version (snapshot hash) | yes | feature pipeline |
| code_sha | yes | CI build |
| metrics + eval slice | yes | eval job |
| intended_use / limitations | yes | author |
| owner / on-call | yes | team config |

### Promotion Gate Criteria (Candidate → Production)
1. Offline NDCG@10 ≥ prior prod and ≥ popularity baseline + 3 pts (CI excludes overlap).
2. Fairness: exposure parity across top creator tiers within ±5%.
3. Packaging contract test green; model loads behind serving interface.
4. Shadow run 24h: p99 latency < 80ms, no schema errors.
5. Sign-off recorded (lead + SRE), with reason.

### Rollback & Version Pinning
- Serving resolves alias `prod` → explicit version. Prior `prod` version retained 90 days.
- Rollback = repoint `prod` alias to last-good version; < 2 min, no rebuild.

### Lineage, Tags & Archival Policy
- Each version links upstream (run/data) and downstream (deployment id).
- Archive on supersession; retain archived versions 1 year for audit/reproducibility.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** stages → metadata → gates → rollback → lineage flow.
- **DS-01 (Framework Application):** applies a lifecycle/governance framework to the registry.
- **CM-02 (Constraint Specification):** gate criteria are the binding constraints on promotion.
- **DS-06 (Prioritization & Severity Guidance):** orders gate conditions and rollback urgency.
- **QA-01 (Self-Verification):** the gate checklists enforce checkable promotion conditions.

**Related Prompts:**
- `mlops_experiment_tracking_setup.md` — supplies the lineage the registry links to.
- `mlops_ml_cicd_pipeline_design.md` — automates the gates that drive promotion.
- `mlops_model_packaging_strategy.md` — defines the artifact the registry governs.
