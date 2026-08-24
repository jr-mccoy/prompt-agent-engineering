---
title: "ML Incident Postmortem Template"
category: AI-ML/production-monitoring
description: "A blameless postmortem framework for a resolved ML production incident — reconstructed timeline, quantified impact, ML-specific root cause split across model/data/pipeline/serving, contributing factors, and owned, dated corrective + preventive actions."
techniques:
  - ST-02
  - RT-09
  - DS-06
  - QA-12
  - CM-02
difficulty: advanced
tags:
  - postmortem
  - blameless
  - root-cause-analysis
  - capa
  - incident-review
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/production-monitoring/mlmonitor_ml_incident_response.md
  - domain-AI-ML/production-monitoring/mlmonitor_performance_degradation_triage.md
  - domain-AI-ML/production-monitoring/mlmonitor_rollback_strategy.md
---

# ML Incident Postmortem Template

**Objective:** Produce a blameless postmortem for a resolved ML production incident that reconstructs the timeline from evidence, quantifies impact, isolates the ML-specific root cause across the model / data / pipeline / serving dimensions, captures contributing factors and what went well, and converts learning into concrete, owned, dated corrective and preventive actions (CAPA) — without blaming individuals, oversimplifying to a single cause, or inventing facts the logs do not support.

**When to Use:**
- After an ML incident is resolved and you need a durable, structured review.
- When an ML quality/behavior failure (drift, skew, silent data break, feedback loop) needs a cause analysis deeper than the on-call notes.
- To turn a messy incident into preventive actions that get owned and tracked.

**When NOT to Use:**
- During an active incident — drive the live response with `mlmonitor_ml_incident_response.md` first.
- For non-urgent diagnosis of a slow quality slope that never became an incident (use `mlmonitor_performance_degradation_triage.md`).
- To design the rollback mechanism the incident relied on (use `mlmonitor_rollback_strategy.md`).

## Inputs / Context

- **Incident record** — alerts that fired, timestamps, severity, who responded.
- **Evidence trail** — monitoring graphs, deploy/CI logs, data-pipeline run logs, feature-store snapshots, model versions live, sample predictions.
- **Impact data** — affected users/requests, duration, money/safety/SLA consequences, error-budget burn.
- **Mitigation taken** — rollback, fallback, traffic shed, data backfill, and when each happened.
- **Label timing** — whether quality was confirmed on matured labels or estimated.

## Constraints

**Must:**
- Reconstruct the timeline strictly from timestamped evidence (logs, graphs, deploys); mark any inferred gap as inferred.
- Classify the root cause across four dimensions — model, data, pipeline, serving — and allow more than one.
- Frame causes as systems/process failures (missing gate, absent detector, fragile contract), not individual error.
- Produce CAPA items each with an owner, a due date, and a verification of "done."

**Must Not:**
- Invent timeline events, root causes, or metrics; reconstruct only from evidence and mark missing facts "unknown / needs investigation."
- Collapse a multi-factor incident into a single root cause when evidence shows several contributing factors.
- Apply hindsight bias — judge responder decisions by what was knowable at the time, not what is obvious now.
- Name an individual as the cause or assign blame; the unit of analysis is the system and process.

**Instructions:**

1. **Summarize the incident.** One paragraph: what failed, severity, duration, and impact in plain terms.

2. **Reconstruct the timeline from evidence.** Order detection → diagnosis → mitigation → resolution with timestamps tied to specific logs/graphs. Mark inferred or missing entries as "unknown / needs investigation."

3. **Quantify impact.** Affected requests/users, duration, money/safety/SLA effects, error-budget burned — with the source of each figure. No estimated number presented as measured.

4. **Isolate the ML root cause by dimension.** Determine whether the proximate cause sits in the model (drift, stale model, miscalibration), data (train/serve skew, silent pipeline corruption, label delay masking the drop, leakage discovered late), pipeline (orchestration/feature-store fault), or serving (artifact mismatch, latency, dependency). Allow multiple dimensions; state the mechanism for each.

5. **Surface contributing factors.** Missing or mis-tuned detectors, absent pre-promotion gates, fragile data contracts, alerting gaps, and why detection took as long as it did — as systemic conditions, not personal fault.

6. **Record what went well.** Detectors that fired correctly, mitigations that worked, decisions that limited blast radius — so good practice is reinforced, not lost.

7. **Write CAPA.** Corrective (close this incident's gap) and preventive (stop the class recurring), each with owner, due date, and how "done" is verified. Include detector/threshold improvements so it is caught earlier next time.

8. **Capture lessons and follow-up.** Note where the model of the system was wrong, and schedule a review to confirm actions landed.

**Output Format:**

A markdown postmortem with sections:
- **Summary** (what/severity/duration/impact)
- **Timeline** (evidence-tied; gaps marked unknown)
- **Impact** (quantified, with sources)
- **Root Cause by Dimension** (model / data / pipeline / serving — mechanism each)
- **Contributing Factors** (systemic, blameless)
- **What Went Well**
- **Corrective & Preventive Actions** (table: action | owner | due | done-when)
- **Lessons & Follow-up Review**

## Verification

- [ ] Every timeline entry is tied to evidence or explicitly marked unknown.
- [ ] Root cause is mapped across model/data/pipeline/serving, not forced to one.
- [ ] Contributing factors are systemic; no individual is named as the cause.
- [ ] Decisions are judged on what was knowable at the time (no hindsight bias).
- [ ] Every CAPA item has an owner, due date, and a "done-when" check.
- [ ] Impact figures cite their source; no estimate is presented as measured.

## False-Positive Prevention

❌ **DON'T:**
- Write "Engineer X pushed a bad model" — that is blame, not a cause; the cause is "no pre-promotion compatibility gate."
- Declare a single root cause when a silent data break AND a missing detector both had to occur.
- Reconstruct "the team should have known by 14:10" using metrics that only matured hours later.
- Fill timeline gaps with plausible-sounding events that no log supports.
- Quote an impact number ("~5k users") as if measured when it was eyeballed.

✅ **DO:**
- State the systemic gap (missing gate, absent detector, fragile contract) as the cause.
- List all contributing factors and how they combined.
- Judge responder actions by signals available at the time; flag the detection lag as a monitoring action item.
- Mark unreconstructable steps "unknown / needs investigation" and make investigating one an action.

## Example Output

```markdown
## Postmortem: Fraud Scorer — recall collapse (SEV-2)

### Summary
Fraud-model recall fell ~30% for 9h after an upstream merchant-category feed silently
started emitting nulls. Auto-approve let fraudulent transactions through. Resolved by
backfill + fallback rule.

### Timeline (evidence-tied)
- 02:14 — feed vendor changed schema (vendor changelog).
- 02:15 — feature `merchant_cat` 88% null (pipeline log). No alert configured.
- 06:40 — fraud-ops flagged chargeback spike (ticket #4471).
- 07:05 — train/serve skew confirmed on `merchant_cat` (skew dashboard).
- 07:30 — fallback rule enabled; 09:50 backfill complete; recall recovered.
- Gap: 02:15–06:40 detection lag — unknown why null-rate monitor was absent (needs investigation).

### Impact
~$? loss under reconciliation (finance, pending — not yet measured); 9h exposure; SLA n/a.

### Root Cause by Dimension
- Data: upstream schema change → silent nulls → train/serve skew (primary).
- Pipeline: feature job had no null-rate contract/assertion (contributing).
- Model: behaved correctly given corrupted input — not a model cause.
- Serving: no fault.

### Contributing Factors
No data-contract test on the feed; no null-rate detector; drift dashboard not paged.

### What Went Well
Skew dashboard pinpointed the feature in 25 min once someone looked; fallback rule existed.

### Corrective & Preventive Actions
| Action | Owner | Due | Done-when |
|---|---|---|---|
| Add null-rate + schema contract on feed | Data Eng (A. Rao) | 2026-06-30 | contract fails CI on injected nulls |
| Page on `merchant_cat` skew > threshold | ML Platform (J. Lee) | 2026-06-26 | test alert fires |
| Finance reconciles true loss | Finance (M. Diaz) | 2026-06-25 | figure recorded |

### Lessons & Follow-up Review
We trusted an external feed without a contract. Review actions 2026-07-15.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** fixed summary → timeline → impact → root cause → CAPA flow.
- **RT-09 (Root Cause Explanation):** resolves the failure to mechanisms across four ML dimensions.
- **DS-06 (Prioritization & Severity Guidance):** severity and impact frame the depth of the review.
- **QA-12 (False Positives Identification):** blocks blame, hindsight bias, and single-cause oversimplification.
- **CM-02 (Constraint Specification):** evidence-only reconstruction and owned/dated CAPA constrain the output.

**Related Prompts:**
- `mlmonitor_ml_incident_response.md` — the live runbook this postmortem reviews after the fact.
- `mlmonitor_performance_degradation_triage.md` — the deeper quality diagnosis a quality cause may invoke.
- `mlmonitor_rollback_strategy.md` — the rollback mechanism whose use the postmortem evaluates.
