---
title: "MLOps ML CI/CD Pipeline Design"
category: AI-ML/mlops-infrastructure
description: "Design CI/CD for ML — code, data, and model tests, training-pipeline triggers, and deployment gates — so changes ship automatically only when quality is proven."
techniques:
  - ST-02
  - CM-02
  - QA-02
  - DS-06
  - RT-10
difficulty: advanced
tags:
  - ci-cd
  - ml-testing
  - deployment-gates
  - automation
  - continuous-training
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/mlops-infrastructure/mlops_model_registry_design.md
  - domain-AI-ML/mlops-infrastructure/mlops_training_pipeline_orchestration.md
  - domain-software-engineering/devops/devops_cicd_pipeline_analysis.md
---

# MLOps ML CI/CD Pipeline Design

**Objective:** Design a CI/CD pipeline for an ML system that tests three things software CI ignores — code, *data*, and the *model* — and that triggers training and gates deployment on objective, baseline-relative criteria, so a model reaches production only when its quality is demonstrated, not assumed.

**When to Use:**
- Models are trained and deployed by hand, with no automated tests between commit and prod.
- You have software CI but it tests only code, while data and model regressions slip through.
- You need to define when retraining triggers (schedule, data volume, drift) and what blocks a release.

**When NOT to Use:**
- Generic application CI/CD with no model artifact (use `domain-software-engineering/devops/devops_cicd_pipeline_analysis.md`).
- Designing the registry governance itself (use `mlops_model_registry_design.md` — this consumes its gates).

## Inputs / Context

Provide what you can; the design adapts to gaps:
- **CI/CD platform** — GitHub Actions / GitLab CI / Jenkins, plus the ML platform (SageMaker Pipelines / Vertex / Databricks / MLflow). Ask if unspecified.
- **What changes trigger a build** — code, config, data, schedule, drift signal — and how often.
- **Existing tests** — unit tests, data validation, eval suite, golden set; whether a baseline/prior model exists.
- **Deployment target & strategy** — online/batch serving; shadow/canary/blue-green availability.
- **Risk profile** — manual approval required? regulated? rollback SLA?

## Constraints

**Must:**
- Test code, data, and model as three distinct stages — passing code tests must not be mistaken for a passing model.
- Gate deployment on a baseline-relative result (vs prior model / heuristic), not an absolute metric.
- Make every gate a binary, automatically evaluated condition with a defined failure action.

**Must Not:**
- Auto-promote on a single offline metric improvement without checking for leakage, slice regressions, or noise.
- Invent platform pipeline APIs; confirm the platform and frame any YAML/config as illustrative.
- Couple training and deployment into one un-gated step — training success is not deployment readiness.

**Instructions:**

1. **Map the change-to-prod path.** Enumerate what can change (code, config, data, retrain schedule, drift trigger) and trace each to the stages it must pass before production.

2. **Design the code stage.** Specify unit/integration tests, linting, and pipeline-component tests (does each step run on a tiny fixture?). This is standard CI plus ML-pipeline smoke tests.

3. **Design the data stage.** Specify data validation gates: schema conformance, range/null checks, distribution checks against a reference, and a freshness/volume check before training is allowed to consume the data.

4. **Design the model stage.** Specify the eval suite that runs post-training: metric vs baseline, per-slice regression checks, calibration if probabilities are consumed, and a behavioral/golden-set test. Define the leakage cross-check.

5. **Define training triggers.** State exactly when retraining fires (push to main, schedule, new-data threshold, drift alert) and the idempotency/concurrency rules so two triggers do not collide.

6. **Define deployment gates.** List the binary conditions to advance to each environment (staging → shadow → prod), the packaging/contract test, and the deployment strategy (canary %, rollback trigger).

7. **Wire registry + lineage handoff.** Specify how a passing build registers the model with full lineage and how serving pins to the registered version (not "latest").

8. **Define failure handling.** For each gate, state the action on failure (block, alert, open issue, auto-rollback) and who is notified.

**Output Format:**

A markdown design doc:
- **Pipeline Overview** — change triggers → stages → environments diagram (as text/ASCII).
- **Stage Specs** — Code / Data / Model: tests in each, pass criteria, failure action.
- **Training Triggers** — table: Trigger | Condition | Concurrency rule.
- **Deployment Gates** — per environment: binary conditions + strategy.
- **Registry & Lineage Handoff** — what registers on pass, how serving resolves the version.
- **Failure & Rollback Matrix** — gate | failure action | notify | rollback.

## Verification

- [ ] Code, data, and model are tested as three separate, named stages.
- [ ] At least one deployment gate is baseline-relative, not absolute.
- [ ] The model stage includes a per-slice regression check and a leakage cross-check.
- [ ] Training triggers have explicit concurrency/idempotency rules.
- [ ] Every gate has a defined failure action and notification path.
- [ ] Serving pins to a registered version; "latest" is never the deploy target.

## False-Positive Prevention

❌ **DON'T:**
- Treat green code CI as a green model — code can pass while the model regressed.
- Promote because aggregate accuracy rose while a key slice silently regressed.
- Skip the leakage cross-check in CI; an inflated metric will sail through an absolute-threshold gate.
- Let a schedule-triggered retrain and a push-triggered retrain run concurrently against the same artifact.

✅ **DO:**
- Run an eval suite that compares to the *current prod model*, and block on slice regressions, not just the headline.
- Validate data (schema, distribution, freshness) *before* training consumes it, so garbage-in is caught at the gate.
- Make the deployment gate refuse a model whose improvement is within the metric's confidence interval.
- Enforce concurrency control on training triggers and pin serving to an explicit version for clean rollback.

## Example Output

```markdown
## ML CI/CD Design — Churn Model (GitHub Actions + SageMaker Pipelines)

### Pipeline Overview
push/schedule/drift → [Code stage] → [Data stage] → [Train] → [Model stage] → register → [staging → shadow → prod]

### Stage Specs
- **Code:** pytest unit + pipeline-component smoke on 200-row fixture; ruff lint. Fail → block PR.
- **Data:** Great-Expectations-style suite — schema, null bounds, PSI vs last-month reference < 0.2, ≥ 30 days of rows. Fail → block train, alert data-owner.
- **Model:** PR-AUC ≥ prod model (CI lower bound) AND ≥ heuristic + 3 pts; recall regression on each region slice < 1 pt; ECE < 0.05; golden-set 50 cases pass; leakage cross-check (drop top feature → metric must not collapse to baseline). Fail → block, open issue.

### Training Triggers
| Trigger | Condition | Concurrency rule |
|---|---|---|
| push to main | code/config change | cancel-in-progress per branch |
| schedule | weekly Mon 02:00 | skip if a run is active |
| drift alert | PSI > 0.25 on key feature | debounce 24h; one run max |

### Deployment Gates
- staging: model stage green + packaging contract test green.
- shadow: 24h, p99 < 120ms, 0 schema errors.
- prod: shadow parity + manual sign-off (lead). Canary 10% → 100% over 1h; auto-rollback if error rate +2%.

### Registry & Lineage Handoff
- On model-stage pass: register version with run uri, data hash, code SHA. Serving resolves alias `prod` → version.

### Failure & Rollback Matrix
| Gate | Failure action | Notify | Rollback |
|---|---|---|---|
| Data | block train | data-owner | n/a |
| Model | block + issue | ML team | n/a |
| Canary | auto-rollback alias | SRE + lead | repoint `prod` to last-good |
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** code → data → model → triggers → gates → failure flow.
- **CM-02 (Constraint Specification):** gates are binding, binary constraints on promotion.
- **QA-02 (Error Detection):** the model and data stages exist to catch regressions software CI misses.
- **DS-06 (Prioritization & Severity Guidance):** the failure matrix ranks actions by severity.
- **RT-10 (Troubleshooting Decision Tree):** failure actions form a decision tree per gate.

**Related Prompts:**
- `mlops_model_registry_design.md` — the registry these gates promote into.
- `mlops_training_pipeline_orchestration.md` — the DAG the train stage invokes.
- `domain-software-engineering/devops/devops_cicd_pipeline_analysis.md` — general (non-ML) CI/CD analysis.
