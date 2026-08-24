---
title: "ML Incident Response Runbook"
category: AI-ML/production-monitoring
description: "A decision-tree incident runbook for ML production failures — detect, classify severity, diagnose the ML-specific cause, mitigate or roll back, and run an ML-aware postmortem."
techniques:
  - RT-10
  - ST-02
  - DS-06
  - RT-09
  - CM-02
difficulty: advanced
tags:
  - incident-response
  - runbook
  - rollback
  - postmortem
  - on-call
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/production-monitoring/mlmonitor_performance_degradation_triage.md
  - domain-AI-ML/production-monitoring/mlmonitor_rollback_strategy.md
  - domain-AI-ML/production-monitoring/mlmonitor_slo_design_for_ml.md
---

# ML Incident Response Runbook

**Objective:** Produce an incident runbook for a production ML service that takes an on-call responder from alert to resolution along a decision tree — detect and confirm the incident, classify severity against SLOs, diagnose the ML-specific cause (serving fault vs data/pipeline vs model-quality), choose the right mitigation (mitigate-in-place vs rollback), restore service, and run a postmortem that captures ML-specific failure modes — so responses are fast, consistent, and avoid making things worse.

**When to Use:**
- An ML service alert fired (quality, latency, errors, drift) and someone must act now.
- Standing up on-call for a model and you need the runbook before the first incident.
- After a messy incident, to codify a repeatable response.

**When NOT to Use:**
- For deep, non-urgent root-cause of a slow quality slope (use `mlmonitor_performance_degradation_triage.md`).
- To design the rollback mechanism itself (use `mlmonitor_rollback_strategy.md`).
- To set the SLO targets severity is judged against (use `mlmonitor_slo_design_for_ml.md`).

## Inputs / Context

Provide what you can:
- **Service & criticality** — what the model does and the blast radius of failure (user-facing, money, safety).
- **SLOs/SLIs** — the targets and error budgets that define severity (if any exist).
- **Deployment topology** — model versions live, canary/shadow setup, rollback capability and its speed.
- **Signals available** — operational metrics, data/prediction drift, quality (and label latency).
- **Roles** — who is on-call, incident commander, and stakeholders to notify.
- **Mitigation levers** — rollback, feature-flag/fallback heuristic, traffic shed, kill switch.

## Constraints

**Must:**
- Drive the response as a decision tree: confirm → classify severity → diagnose family → mitigate → restore → postmortem.
- Classify the cause family (serving/operational, data/pipeline, model-quality/drift) before choosing a mitigation, because the right fix differs by family.
- For quality incidents, confirm the drop is real (matured labels, correct metric) before declaring an ML-quality incident.

**Must Not:**
- Recommend rollback as the reflexive first action without checking whether the previous version is also affected (a shared upstream data break is not fixed by rollback).
- Skip severity classification — it sets comms, urgency, and who is paged.
- Close an incident without an ML-aware postmortem that distinguishes data, serving, and model causes.

**Instructions:**

1. **Detect and confirm.** Verify the alert is a real incident, not a monitoring artifact: check signal freshness, whether labels are matured (for quality alerts), and whether multiple corroborating signals agree. De-duplicate against existing incidents.

2. **Classify severity against SLOs.** Map the impact to a severity tier (user-facing scope, money/safety, error-budget burn). Severity drives the incident commander assignment, comms cadence, and how aggressive mitigation may be.

3. **Branch on symptom class (decision tree).** Operational symptom (latency/errors/timeouts/saturation) → serving path. Input/data anomaly (nulls, schema, volume, drift) → data/pipeline path. Quality drop on matured labels → model-quality/drift path. Use corroborating signals to pick the branch.

4. **Diagnose within the branch.** Serving: bad deploy, resource saturation, dependency outage. Data: upstream source break, train-serve skew, feature-store fault. Quality: confirmed concept drift vs masked data bug. Identify the proximate cause enough to choose a mitigation (full root-cause can wait for postmortem).

5. **Choose mitigation by cause, restore-first.** Prioritize stopping user/business harm: roll back if the incident is version-specific and a known-good version is unaffected; use a fallback heuristic / feature flag / traffic shed if the cause is shared data or rollback is unsafe; fix-forward only when fast and clearly correct. State the rollback safety check (is the prior version actually unaffected?).

6. **Verify recovery.** Confirm the mitigating action restored the SLI to within budget on real signals, and watch for collateral effects (a rollback that reintroduces an old bug, a fallback that degrades quality differently).

7. **Communicate throughout.** Define status updates by severity tier (channels, cadence, audience) from declaration to resolution to all-clear.

8. **Run an ML-aware postmortem.** Capture timeline, the cause family and mechanism, why detection took as long as it did (monitoring gap), and action items split across data, serving, and model dimensions — including detector/threshold improvements so it is caught earlier next time.

**Output Format:**

A markdown runbook:
- **Incident Decision Tree** — the branch logic from alert to mitigation
- **Severity Matrix** — table: Tier | Criteria | IC role | Comms cadence | Allowed mitigations
- **Diagnosis Checklists by Branch** — serving / data / quality
- **Mitigation Playbook** — lever | when to use | safety check | rollback criteria link
- **Recovery Verification** — what confirms resolved
- **Comms Templates** — declaration / update / resolution
- **Postmortem Template** — timeline, cause family, detection-gap, action items by dimension

## Verification

- [ ] The runbook is a decision tree, not a flat list of tips.
- [ ] Severity is classified before mitigation is chosen.
- [ ] Cause family (serving/data/quality) is identified before picking a mitigation.
- [ ] Rollback includes a check that the prior version is actually unaffected.
- [ ] Quality incidents confirm label maturity before being declared model-quality.
- [ ] The postmortem template separates data, serving, and model causes and includes a detection-gap review.

## False-Positive Prevention

❌ **DON'T:**
- Page everyone over a quality "drop" that is just immature labels in the recent window.
- Roll back automatically when the prior model version shares the broken upstream feature.
- Pick a mitigation before knowing whether the cause is serving, data, or model.
- Close the incident at "service restored" without a postmortem on why detection lagged.

✅ **DO:**
- Confirm with corroborating signals and matured labels before declaring an incident.
- Verify the rollback target is genuinely unaffected before rolling back.
- Branch the diagnosis by symptom class so the mitigation matches the cause.
- Split postmortem actions across data, serving, and model, and fix the monitoring gap.

## Example Output

```markdown
## Incident Runbook (instance): Search Ranker — relevance collapse

### Incident Decision Tree
Alert (NDCG -22% + low-score-collapse) →
  Confirm: corroborated by score-dist collapse + click-through drop; labels (clicks) near-real-time → REAL.
  Severity: SEV-2 (user-facing, no money/safety) → IC = on-call ML, 30-min comms.
  Branch: quality + prediction-dist collapse + coincident deploy 14:02 → serving/deploy path.
  Diagnose: new model artifact loaded with mismatched feature-encoder version → all scores near 0.
  Mitigate: version-specific, prior version healthy → ROLLBACK to v6 (safety check: v6 uses old encoder, unaffected).

### Severity Matrix
| Tier | Criteria | IC | Comms | Mitigations |
|---|---|---|---|---|
| SEV-1 | money/safety or full outage | Eng mgr | 15 min | rollback, kill switch |
| SEV-2 | user-facing quality, no money | On-call ML | 30 min | rollback, fallback heuristic |
| SEV-3 | degraded, contained | On-call ML | daily | fix-forward |

### Mitigation Playbook
| Lever | When | Safety check | 
|---|---|---|
| Rollback | version-specific cause | prior version not sharing the fault |
| Fallback heuristic | shared data break | heuristic quality acceptable |
| Traffic shed | saturation | downstream can absorb |

### Recovery Verification
- NDCG and score distribution back to v6 baseline within 20 min; no v6-era bug recurrence.

### Postmortem (excerpt)
- Cause family: serving (artifact/encoder version mismatch).
- Detection gap: no pre-promotion encoder-compatibility check; score-collapse alert lacked auto-rollback.
- Actions — Data: n/a. Serving: add encoder-version assertion + canary gate. Model: add score-distribution sanity gate pre-promotion.
```

**Techniques Used:**
- **RT-10 (Troubleshooting Decision Tree):** the runbook is an explicit alert-to-mitigation tree.
- **ST-02 (Structured Sequential Instructions):** fixed detect → classify → diagnose → mitigate → postmortem flow.
- **DS-06 (Prioritization & Severity Guidance):** severity matrix governs urgency and allowed actions.
- **RT-09 (Root Cause Explanation):** diagnosis and postmortem resolve to mechanisms by cause family.
- **CM-02 (Constraint Specification):** SLOs and rollback-safety constrain mitigation choices.

**Related Prompts:**
- `mlmonitor_performance_degradation_triage.md` — the deeper diagnosis the quality branch invokes.
- `mlmonitor_rollback_strategy.md` — the rollback mechanism the mitigation playbook depends on.
- `mlmonitor_slo_design_for_ml.md` — the SLOs severity is measured against.
```