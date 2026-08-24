---
title: "ML Model Rollback Strategy"
category: AI-ML/production-monitoring
description: "Design safe model rollback — version pinning, rollback criteria, automation, and data/feature consistency — so reverting to a prior model is fast, deterministic, and does not reintroduce a worse state."
techniques:
  - ST-02
  - CM-02
  - DS-06
  - RT-09
  - QA-12
difficulty: advanced
tags:
  - rollback
  - versioning
  - release-safety
  - automation
  - data-consistency
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/production-monitoring/mlmonitor_canary_shadow_deployment.md
  - domain-AI-ML/production-monitoring/mlmonitor_ml_incident_response.md
  - domain-AI-ML/production-monitoring/mlmonitor_data_pipeline_health_audit.md
---

# ML Model Rollback Strategy

**Objective:** Design a rollback strategy for a production model that makes reverting to a known-good version fast, deterministic, and safe — covering version pinning of the model artifact *and* its preprocessing/feature dependencies, explicit rollback criteria, automation vs human gate, and the data-consistency concerns that make ML rollback harder than rolling back ordinary code — so a rollback restores service without reintroducing an old bug or causing train-serve skew.

**When to Use:**
- Establishing the rollback capability for a model before its first incident.
- A prior rollback failed, was slow, or reintroduced a different problem.
- Designing the automated revert that a failed canary or incident triggers.

**When NOT to Use:**
- To run the live incident itself (use `mlmonitor_ml_incident_response.md`).
- To design the forward rollout that may invoke rollback (use `mlmonitor_canary_shadow_deployment.md`).
- For diagnosing the failure (use `mlmonitor_performance_degradation_triage.md`).

## Inputs / Context

Provide what you can:
- **Model packaging** — how the model + preprocessing/feature transforms + dependencies are versioned and deployed.
- **Feature dependencies** — feature-store schemas/transforms tied to a model version, and whether old/new can coexist.
- **State coupling** — does the model write to state (caches, feature stores, downstream tables) that a rollback must reconcile?
- **Traffic & criticality** — request volume and blast radius, which set how fast rollback must be.
- **Detection signals** — what indicates a release is bad and should be reverted.
- **Rollback infra** — blue/green, canary infra, model registry, ability to pin a prior version atomically.

## Constraints

**Must:**
- Treat the rollback unit as the *full bundle* — model artifact + preprocessing + feature-schema/version + dependency set — not just the model weights.
- Define explicit, measurable rollback criteria (what conditions trigger a revert) and whether each is automated or human-gated.
- Verify the rollback target is genuinely a known-good state for *current* conditions before reverting, and that reverting does not create train-serve skew.

**Must Not:**
- Roll back the model weights while leaving an incompatible new feature schema in place (recreates skew/incompatibility).
- Auto-roll-back on a cause the previous version also has (shared upstream data break) — that wastes time and changes nothing.
- Leave data/state written by the bad version unreconciled if downstream training or features depend on it.

**Instructions:**

1. **Define the rollback bundle.** Enumerate everything pinned to a model version: weights/artifact, preprocessing code, feature definitions/schema, dependency versions, config. Rollback must restore the whole bundle atomically or it risks skew.

2. **Set rollback criteria and ownership.** List the conditions that warrant rollback (operational SLO breach, guardrail/quality regression beyond tolerance, score-distribution collapse) and tier them: which are automated, which require a human decision, and who decides.

3. **Verify the rollback target's validity.** Before reverting, confirm the prior version is (a) compatible with the *current* feature schema and data, and (b) not subject to the same upstream cause. Specify this pre-revert check so rollback isn't a no-op or a new break.

4. **Design the revert mechanism.** Specify the technical path (blue/green swap, registry version pin, traffic re-route) and target time-to-revert proportional to blast radius. Prefer atomic, deterministic switches over manual redeploys.

5. **Handle data and state consistency.** Identify any state the bad version wrote (caches, feature-store updates, logged predictions used for training) and define reconciliation: invalidate poisoned caches, quarantine bad-version predictions from training data, and reconcile downstream tables.

6. **Preserve forensics.** Ensure the bad version, its config, and the failing inputs/outputs are captured before revert so postmortem and fix-forward are possible — rollback must not destroy the evidence.

7. **Define the post-rollback verification.** Specify the signals that confirm the rollback restored a healthy state (SLIs back in budget, no recurrence of an old bug the prior version had) and the watch window.

8. **Plan the path forward.** State how the team exits the rolled-back state: re-fix and re-canary the new version, and how long the rollback target is kept warm.

**Output Format:**

A markdown rollback design:
- **Rollback Bundle Definition** — everything pinned per version
- **Rollback Criteria & Ownership** — table: Condition | Threshold | Automated/Human | Decider
- **Pre-Revert Validity Check** — target-version compatibility + shared-cause check
- **Revert Mechanism & TTR** — technical path and target time-to-revert
- **Data/State Reconciliation** — caches, feature store, training-data quarantine
- **Forensics Capture** — what is preserved before revert
- **Post-Rollback Verification & Path Forward** — confirmation signals and exit plan

## Verification

- [ ] The rollback unit is the full bundle (model + preprocessing + feature schema + deps), not weights alone.
- [ ] Rollback criteria are explicit and tiered into automated vs human-gated.
- [ ] A pre-revert check confirms the target is compatible and not subject to the same cause.
- [ ] Data/state written by the bad version has a reconciliation plan (caches, training quarantine).
- [ ] Forensics are preserved before revert.
- [ ] Post-rollback verification signals and a path forward are defined.

## False-Positive Prevention

❌ **DON'T:**
- Swap model weights back while keeping the new, incompatible feature schema — recreating skew.
- Auto-roll-back when the prior version shares the broken upstream feature (no improvement).
- Leave the bad version's predictions in the training pool to poison the next retrain.
- Wipe the failing version and its inputs in the revert, destroying postmortem evidence.

✅ **DO:**
- Roll back the whole bundle atomically so model and features stay consistent.
- Pre-check that the target version is compatible with current data and not subject to the same cause.
- Quarantine bad-version predictions and invalidate poisoned caches/feature-store writes.
- Snapshot the failing version, config, and example inputs before reverting.

## Example Output

```markdown
## Rollback Strategy: Credit Risk Model v9 → v8

### Rollback Bundle Definition
- Pinned per version: model artifact, preprocessing pipeline hash, feature-store schema vN, scoring config, runtime deps lockfile. Registry stores the tuple; deploy is the tuple, not the weights alone.

### Rollback Criteria & Ownership
| Condition | Threshold | Mode | Decider |
|---|---|---|---|
| Score-dist collapse | mean score Δ>0.2, 5 min | Automated | system |
| p99 latency | >500ms, 5 min | Automated | system |
| Approval-rate anomaly | ±5% vs control, 30 min | Human-gated | on-call risk lead |
| Quality regression (matured) | KS on default-rate, CI | Human-gated | ML lead |

### Pre-Revert Validity Check
- Confirm v8's preprocessing hash is compatible with current feature-store schema (v8 used schema v(N-1); ensure v(N-1) still served or dual-served). Confirm incident is v9-specific (v8 not subject to the upstream `bureau_score` feed break).

### Revert Mechanism & TTR
- Blue/green: registry pin flips traffic to v8 deployment held warm. Target TTR < 2 min (money-impacting → SEV-1).

### Data/State Reconciliation
- Quarantine all v9 predictions from the training/calibration pool (tag by version). Invalidate the per-applicant score cache written by v9. Reconcile the downstream `decisions` table with a corrected re-score batch.

### Forensics Capture
- Snapshot v9 artifact + config + 1k failing input/output pairs to incident bucket before flip.

### Post-Rollback Verification & Path Forward
- Confirm score distribution + approval rate match v8 baseline within 15 min; verify no v8-era calibration bug recurs. Keep v8 warm 14 days; v9 re-enters via shadow + canary after fix.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** bundle → criteria → validity → revert → reconcile → verify sequence.
- **CM-02 (Constraint Specification):** bundle atomicity and compatibility are the governing constraints.
- **DS-06 (Prioritization & Severity Guidance):** criteria tiered by automation and blast radius.
- **RT-09 (Root Cause Explanation):** pre-revert shared-cause check ties rollback validity to the actual mechanism.
- **QA-12 (False Positives Identification):** prevents partial-bundle reverts and same-cause no-op rollbacks.

**Related Prompts:**
- `mlmonitor_canary_shadow_deployment.md` — the rollout whose abort criteria trigger this rollback.
- `mlmonitor_ml_incident_response.md` — the incident flow that invokes rollback as a mitigation.
- `mlmonitor_data_pipeline_health_audit.md` — confirm a shared upstream cause before reverting.
```