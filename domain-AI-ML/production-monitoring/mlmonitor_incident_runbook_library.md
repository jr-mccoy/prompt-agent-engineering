---
title: "ML Incident Runbook Library"
category: AI-ML/production-monitoring
description: "Build an indexed library of ML incident runbooks organized by failure-mode class — drift, pipeline failure/skew, feedback-loop contamination, training-pipeline failure, serving/latency bug, label-delay masking — each with detection signals, triage, ML diagnosis decision points, mitigation, and escalation."
techniques:
  - ST-02
  - RT-10
  - DS-06
  - DS-01
  - QA-12
difficulty: advanced
tags:
  - runbook-library
  - failure-modes
  - on-call
  - drift
  - train-serve-skew
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/production-monitoring/mlmonitor_incident_postmortem_template.md
  - domain-AI-ML/production-monitoring/mlmonitor_ml_incident_response.md
  - domain-AI-ML/production-monitoring/mlmonitor_data_pipeline_health_audit.md
---

# ML Incident Runbook Library

**Objective:** Produce a reusable, indexed catalog of ML incident runbooks — one per ML failure-mode class — so that when an alert fires, a responder routes to the matching runbook and follows class-specific detection signals, first-responder triage, ML diagnosis decision points, mitigation/rollback options, and escalation, rather than improvising from scratch each time and rediscovering the same ML-specific failure modes.

**When to Use:**
- Standing up or maturing on-call for ML services and you need coverage across failure classes, not a single runbook.
- After repeated incidents reveal recurring failure-mode classes worth codifying.
- When responders waste time re-diagnosing because no class-indexed playbooks exist.

**When NOT to Use:**
- To run the generic alert-to-mitigation flow for one live incident (use `mlmonitor_ml_incident_response.md`).
- To write the after-incident review (use `mlmonitor_incident_postmortem_template.md`).
- For a deep data-pipeline health review independent of incidents (use `mlmonitor_data_pipeline_health_audit.md`).

## Inputs / Context

- **Service inventory** — the ML services in scope and their criticality/blast radius.
- **Observed failure history** — past incidents and the classes they fell into (if any).
- **Signals available** — operational metrics, drift detectors, data-quality checks, label latency.
- **Mitigation levers per service** — rollback, fallback heuristic, feature flag, traffic shed, retrain trigger.
- **Escalation map** — on-call, incident commander, data-eng, model owners, stakeholders.

## Constraints

**Must:**
- Cover the ML failure-mode classes as distinct runbooks: data/concept drift; data-pipeline failure or train/serve skew; feedback-loop contamination; training-pipeline failure (bad retrain/artifact); serving/latency bug; label-delay masking.
- Give each runbook the same skeleton — detection signals, first-responder triage, ML diagnosis decision points, mitigation/rollback options, escalation — so they are interchangeable under stress.
- Provide an index that routes from an observed symptom to the right runbook(s).

**Must Not:**
- Invent failure-mode classes, detection thresholds, or metrics not grounded in the service's real signals; mark any value to be tuned as "set from baseline — needs investigation."
- Collapse distinct classes (e.g., concept drift vs train/serve skew) into one runbook, since their diagnosis and fix differ.
- Write generic IT-outage steps that ignore the ML-specific cause (a quality drop is not the same as a 500-error spike).

**Instructions:**

1. **Enumerate the failure-mode classes.** List the ML classes in scope and what each looks like in production; note which apply to which services.

2. **Define a routing index.** Map observable symptoms (quality drop, null surge, latency, prediction-distribution shift, slow self-reinforcing degradation) to the candidate runbook(s) — symptoms can be ambiguous, so allow multiple candidates and a disambiguation step.

3. **For each class, write detection signals.** The leading and confirming signals, and how to tell this class apart from look-alikes (e.g., drift vs immature labels vs skew).

4. **Write first-responder triage.** The first safe steps any responder can take to confirm scope and avoid making it worse (freshness check, label maturity, blast-radius sizing).

5. **Add ML diagnosis decision points.** Class-specific branching: e.g., for a quality drop — matured labels? distribution shift in inputs or outputs? coincident deploy or data change? — leading to a proximate cause.

6. **List mitigation/rollback options.** The levers valid for this class with their safety checks (rollback only if prior version is unaffected; fallback if the cause is shared data; retrain only after confirming drift, not a data bug).

7. **Define escalation.** When to page the model owner vs data-eng, when to declare higher severity, and who decides.

8. **Index and version the library.** Give each runbook an ID, last-reviewed date, and owner; keep the index current as new classes are learned (often from postmortems).

**Output Format:**

A markdown catalog:
- **Routing Index** — table: Symptom → candidate runbook(s) → disambiguation
- **Per-Runbook entries**, each: ID | Class | Detection signals | First-responder triage | ML diagnosis decision points | Mitigation/rollback options | Escalation | Owner / last-reviewed
- **Maintenance** — how runbooks are added/retired (e.g., from postmortem action items)

## Verification

- [ ] All named failure-mode classes have a distinct runbook.
- [ ] Every runbook follows the same five-part skeleton.
- [ ] A routing index maps symptoms to runbooks and handles ambiguous symptoms.
- [ ] Diagnosis steps are ML-specific (label maturity, skew, distribution shift), not generic outage steps.
- [ ] Mitigations state safety checks (rollback target unaffected; retrain only after confirming drift).
- [ ] Each runbook has an owner and last-reviewed date.

## False-Positive Prevention

❌ **DON'T:**
- Merge "concept drift" and "train/serve skew" into one runbook — one needs retrain, the other needs a pipeline fix.
- Route every quality alert to the drift runbook when an immature-label or skew runbook fits better.
- Copy a web-service outage runbook and call it ML coverage (it won't catch silent data corruption).
- Hard-code a drift threshold as universal truth when it must be set per service from baseline.

✅ **DO:**
- Keep each class separate with its own diagnosis and fix path.
- Use the index's disambiguation step to pick among look-alike symptoms.
- Write ML-specific signals (PSI/distribution shift, null-rate, skew, label latency) into detection.
- Mark thresholds "set from baseline — needs investigation" rather than inventing numbers.

## Example Output

```markdown
## ML Incident Runbook Library — Recommendations Platform

### Routing Index
| Symptom | Candidate runbook(s) | Disambiguation |
|---|---|---|
| CTR/quality drop | RB-01 drift, RB-02 skew, RB-06 label-delay | Check label maturity → input vs output dist shift → recent data change |
| Slow self-reinforcing decline | RB-03 feedback-loop | Was a model output later used as its own training label? |
| Latency/timeout spike | RB-05 serving | Coincident deploy? resource saturation? |
| Post-retrain quality drop | RB-04 training-pipeline | New artifact loaded? eval gate passed? |

### RB-02 — Train/Serve Skew
- **Detection signals:** feature distribution differs train vs serve; null surge in a serving feature; quality drop without input concept change.
- **First-responder triage:** confirm labels matured; pull skew dashboard; size affected requests.
- **ML diagnosis decision points:** Which feature skews? Source = pipeline transform mismatch vs upstream feed change vs feature-store staleness?
- **Mitigation/rollback:** fallback rule if cause is shared data (rollback won't help); backfill/fix transform; rollback only if a new serving transform is the cause.
- **Escalation:** page Data Eng if upstream feed; model owner if transform logic.
- Owner: ML Platform · last-reviewed 2026-06-19.

### RB-03 — Feedback-Loop Contamination
- **Detection signals:** slow, self-reinforcing metric drift; training data increasingly reflects model's own past outputs.
- **First-responder triage:** check whether logged labels are model-influenced.
- **Diagnosis:** identify the contamination path (exposure bias, auto-labeled data).
- **Mitigation:** hold-out untreated traffic; debias labels; pause auto-labeling.
- **Escalation:** model owner + data science.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** every runbook shares the same ordered skeleton.
- **RT-10 (Troubleshooting Decision Tree):** routing index + per-class decision points form the trees.
- **DS-06 (Prioritization & Severity Guidance):** escalation and severity guidance per class.
- **DS-01 (Framework Application):** applies a consistent runbook framework across failure modes.
- **QA-12 (False Positives Identification):** prevents merging distinct classes and copying generic outage steps.

**Related Prompts:**
- `mlmonitor_incident_postmortem_template.md` — postmortems feed new runbooks into the library.
- `mlmonitor_ml_incident_response.md` — the live response flow that routes into these runbooks.
- `mlmonitor_data_pipeline_health_audit.md` — proactive pipeline checks behind the skew/pipeline runbooks.
