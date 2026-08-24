---
title: "ML Performance Degradation Triage"
category: AI-ML/production-monitoring
description: "Triage a production model whose quality dropped using a decision tree that separates data shift, pipeline/serving bugs, label delay/quality, and genuine concept drift before recommending a fix."
techniques:
  - RT-10
  - RT-09
  - ST-02
  - DS-06
  - QA-12
difficulty: advanced
tags:
  - degradation
  - triage
  - root-cause
  - concept-drift
  - decision-tree
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/production-monitoring/mlmonitor_drift_detection_design.md
  - domain-AI-ML/production-monitoring/mlmonitor_data_pipeline_health_audit.md
  - domain-AI-ML/production-monitoring/mlmonitor_ml_incident_response.md
---

# ML Performance Degradation Triage

**Objective:** Diagnose why a production model's measured quality dropped by walking a decision tree that systematically separates the candidate causes — measurement/label artifacts, data/pipeline bugs (train-serve skew, broken features), input distribution shift, and genuine concept drift — and produce a ranked root-cause hypothesis with the discriminating evidence and the matching remediation, rather than jumping straight to "retrain."

**When to Use:**
- A monitoring alert (accuracy, precision, CTR, calibration) fired and you must find the cause.
- Business metrics tied to the model regressed and the model is a suspect.
- A model that was fine yesterday is materially worse today or this week.

**When NOT to Use:**
- To design the detectors themselves (use `mlmonitor_drift_detection_design.md`).
- To run the full incident lifecycle including comms and rollback (use `mlmonitor_ml_incident_response.md`).
- For an offline model that never shipped (this is a production triage).

## Inputs / Context

Provide what you can; triage degrades gracefully with gaps:
- **The drop** — which metric, by how much, over what window, and against which baseline.
- **Timing** — when it started (sharp step vs gradual slope), and any deploy/config/data changes near that time.
- **Label situation** — how labels arrive (delay, source), and whether the dropped metric uses recent or fully-matured labels.
- **Drift signals** — any data/prediction drift readings for the same window.
- **Pipeline events** — schema changes, upstream source migrations, feature-store updates, retraining, dependency bumps.
- **Segmentation** — is the drop global or concentrated in a region/device/customer segment?

## Constraints

**Must:**
- Separate the four cause families explicitly and rule them in/out with discriminating evidence, not vibes.
- Establish whether the drop is **real** (model output got worse) or a **measurement artifact** (immature/biased labels, metric-window change) before chasing model causes.
- Tie a sudden step-change to deploy/config/data events and a gradual slope to drift, and justify which pattern the data shows.

**Must Not:**
- Recommend retraining before confirming the cause is one retraining can fix (it cannot fix a serving bug or a label artifact).
- Declare "concept drift" while train-serve skew or a broken feature remains unruled-out.
- Treat a metric change driven by label maturation (partial labels) as model degradation.

**Instructions:**

1. **Confirm the drop is real, not a measurement artifact.** Check whether the metric window uses matured labels, whether label volume/source changed, and whether the metric definition or threshold moved. If the labels for the recent window are incomplete, the "drop" may vanish as labels mature — flag and pause.

2. **Characterize the shape and timing.** Is it a sharp step (points to a discrete event: deploy, config, data source, feature break) or a gradual slope (points to drift)? Align the onset against the change log.

3. **Branch on a discrete event near onset (step-change path).** If a deploy/config/feature-store/dependency change coincides, investigate train-serve skew and pipeline bugs first: compare offline vs online feature values for the same entities; check for nulls/defaults silently replacing real values; verify the served model artifact and preprocessing match training.

4. **Check input data health (data-shift path).** Inspect feature null rates, range/schema violations, volume, and data drift vs the reference window. A broken upstream source often masquerades as drift — distinguish "feature distribution shifted in the world" from "feature is now garbage."

5. **Check prediction behavior.** Has the output/score distribution shifted? Compare against the prediction-drift baseline. A flat or collapsed score distribution suggests a serving/feature fault; a shifted-but-healthy distribution is more consistent with real input drift.

6. **Test for concept drift (last, label-gated).** Only after measurement, skew, and data-quality causes are ruled out, evaluate whether P(y|x) genuinely changed: same inputs now yield different outcomes on matured labels. Confirm with a segment where inputs are stable but error rose.

7. **Localize by segment.** Determine whether the drop is global or concentrated. A single-segment drop points to that segment's data source or population change; a global drop points to a shared pipeline/model cause.

8. **Rank causes and map to fixes.** Output the surviving hypothesis (or top 2) with evidence, and the matching action: fix the pipeline/skew, repair the upstream feed, wait for labels to mature, or proceed to retraining/rollback evaluation.

**Output Format:**

A markdown triage report:
- **Drop Summary** — metric, magnitude, window, baseline, shape (step/slope)
- **Decision-Tree Trace** — each branch checked, evidence found, ruled in/out
- **Ranked Root-Cause Hypotheses** — table: Cause Family | Confidence | Key Evidence | Discriminating Test Still Needed
- **Recommended Action** — the fix matching the leading cause (and what NOT to do yet)
- **Open Checks** — fast tests to confirm before acting
- **INSUFFICIENT EVIDENCE** — an available verdict for the leading hypothesis, used where labels have not matured over the affected window. Acting on an unmatured signal is how a pipeline change gets treated as concept drift. Name the unblocking datum: the label maturation window, or a smaller labelled sample that would discriminate earlier.

## Verification

- [ ] Measurement/label-artifact possibility was checked before model causes.
- [ ] The drop's shape (step vs slope) is stated and aligned to the change log.
- [ ] Train-serve skew and broken-feature checks were performed, not skipped.
- [ ] Concept drift was only concluded after other families were ruled out, using matured labels.
- [ ] The drop was localized as global vs segment-specific.
- [ ] The recommended action matches the leading cause; retraining is not the default.
- [ ] Where labels have not matured over the affected window, the leading hypothesis is reported as INSUFFICIENT EVIDENCE with the maturation window or labelled sample named.

## False-Positive Prevention

❌ **DON'T:**
- Call it model degradation when the recent window's labels are still maturing (partial-label bias).
- Diagnose "concept drift" while a feature is silently defaulting to nulls after an upstream change.
- Attribute a sharp step-change to drift when a deploy landed at the same minute.
- Assume a global model cause when the drop is isolated to one region's broken feed.

✅ **DO:**
- Verify label maturity and metric-window definition before chasing the model.
- Compare offline vs online feature values for the same entities to expose train-serve skew.
- Align onset timing to the deploy/config/data change log first.
- Segment the drop to separate a shared pipeline cause from a localized data cause.

## Example Output

```markdown
## Degradation Triage: Churn Model v6 — precision dropped 0.71 → 0.58 (last 9 days)

### Drop Summary
- Metric: precision@top-decile, -13 pts vs trailing-12-week baseline.
- Window: 9 days. Shape: sharp step starting Mar 4 (not a slope).

### Decision-Tree Trace
1. Measurement artifact? Labels mature in ~30d; the 9-day window is partially labeled → precision is computed on a biased early-resolving subset. Partial cause, but step is real on the matured 30-day-prior window too.
2. Shape/timing: step on Mar 4 → deploy log shows feature-store schema change Mar 4 03:12.
3. Train-serve skew: `tenure_days` online now returns 0 for 22% of users (default) after the schema change; offline value is correct. CONFIRMED skew.
4. Data health: `tenure_days` null/default rate jumped 1% → 22% at Mar 4. Other features normal.
5. Prediction behavior: score distribution compressed toward the low end — consistent with a high-importance feature collapsing to 0.
6. Concept drift: ruled out — stable segments (users with valid tenure) show no precision drop.
7. Localization: drop concentrated in users created post-2024 (the cohort hit by the schema change).

### Ranked Root-Cause Hypotheses
| Cause Family | Confidence | Key Evidence | Discriminating Test |
|---|---|---|---|
| Pipeline bug / train-serve skew | High | `tenure_days` defaulting to 0 for 22%; score compression; segment match | Backfill correct tenure, re-score, expect recovery |
| Measurement (partial labels) | Medium | recent window under-labeled | Recompute on matured prior window |
| Concept drift | Ruled out | stable segments unaffected | — |

### Recommended Action
- Fix the feature-store join so `tenure_days` resolves; re-score affected cohort. Do NOT retrain — retraining on skewed serving data would bake in the bug.

### Open Checks
- Confirm precision recovers to ~0.71 on the corrected cohort within 24h of the join fix.
```

**Techniques Used:**
- **RT-10 (Troubleshooting Decision Tree):** the triage is a branching tree across the four cause families.
- **RT-09 (Root Cause Explanation):** each branch resolves to a mechanism, not a symptom.
- **ST-02 (Structured Sequential Instructions):** fixed measurement → shape → skew → data → concept order.
- **DS-06 (Prioritization & Severity Guidance):** causes are ranked by confidence and impact.
- **QA-12 (False Positives Identification):** guards against partial-label bias and skew-as-drift confusion.

**Related Prompts:**
- `mlmonitor_drift_detection_design.md` — the drift signals this triage consumes.
- `mlmonitor_data_pipeline_health_audit.md` — deep-dive when the cause is upstream data.
- `mlmonitor_ml_incident_response.md` — escalate triage into a full incident with rollback and postmortem.
```