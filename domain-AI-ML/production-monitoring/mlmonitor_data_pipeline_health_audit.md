---
title: "ML Data Pipeline Health Audit"
category: AI-ML/production-monitoring
description: "Audit the production data pipeline feeding a model for silent failures and train-serve skew — nulls, schema drift, stale joins, default-substitution, and timing mismatches that degrade quality without raising errors."
techniques:
  - ST-02
  - RT-09
  - DS-06
  - RT-05
  - QA-12
difficulty: advanced
tags:
  - data-pipeline
  - train-serve-skew
  - data-quality
  - silent-failures
  - audit
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/production-monitoring/mlmonitor_performance_degradation_triage.md
  - domain-AI-ML/production-monitoring/mlmonitor_drift_detection_design.md
  - domain-AI-ML/production-monitoring/mlmonitor_monitoring_dashboard_design.md
---

# ML Data Pipeline Health Audit

**Objective:** Audit the production data pipeline that feeds a deployed model for *silent* failures — data that flows without raising errors but is wrong, stale, default-substituted, or computed differently than at training time — and for train-serve skew, producing a ranked list of evidenced issues with their model-quality impact and the checks that should be instrumented so these failures surface as alerts rather than as a mysterious accuracy drop weeks later.

**When to Use:**
- Suspecting that degraded model quality has an upstream data cause.
- Onboarding a model whose feature pipeline you did not build and want to harden.
- After an incident traced to a silent data failure, to find the others lurking.

**When NOT to Use:**
- To triage a confirmed live degradation end-to-end (use `mlmonitor_performance_degradation_triage.md`).
- To design distribution-shift detectors (use `mlmonitor_drift_detection_design.md`).
- For leakage in the training data specifically (use the data-for-ml leakage detector).

## Inputs / Context

Provide what you can; the audit degrades gracefully with gaps:
- **Pipeline topology** — sources, transforms, joins, feature store, and the serving path that computes features at inference.
- **Feature definitions** — how each feature is computed offline (training) vs online (serving), and by what code.
- **Freshness expectations** — how current each source/feature should be, and update cadences.
- **Schema/contracts** — declared types, ranges, allowed categories, nullability.
- **Recent changes** — source migrations, schema edits, feature-store updates, dependency bumps.
- **Symptoms** — any quality drop, drift readings, or anomalies, with timing.

## Constraints

**Must:**
- Distinguish *silent* failures (no error, wrong data) from *loud* failures (errors/timeouts) — the audit's value is in the silent ones.
- Check train-serve skew explicitly: compare how each feature is computed offline vs online, including timing and code path.
- Anchor each finding to a specific feature/source/transform with evidence (rate, example, or comparison), not a generic warning.

**Must Not:**
- Treat a successful pipeline run as evidence of healthy data — a job can succeed while emitting defaults/nulls.
- Conflate legitimate real-world distribution shift with a broken feed; distinguish "the world changed" from "the feature is now garbage."
- Recommend fixes without stating the model-quality impact and how to verify the fix.

**Instructions:**

1. **Map the dual computation paths.** For each feature, lay out the offline (training) and online (serving) computation. Differences in source table, aggregation window, timing, or code are skew candidates — the leading cause of silent degradation.

2. **Hunt default/null substitution.** Find features that, on lookup miss or upstream gap, silently return a default (0, mean, "unknown") instead of failing. Quantify the substitution rate and flag spikes — a feature defaulting for 20% of requests looks "fine" but is corrupting predictions.

3. **Check freshness and staleness.** Verify each source/feature is as current as required. A stale join (yesterday's feature served as today's, a frozen batch table) degrades silently. Compare last-update timestamps against cadence expectations.

4. **Validate schema and ranges in production.** Check live data against the declared contract: type changes, new/disappeared categories, out-of-range values, unit changes (cents vs dollars), encoding shifts. These pass through without errors but mislead the model.

5. **Check joins and key integrity.** Look for join fan-out/collapse, duplicate keys, and orphaned rows that change feature semantics. A broken join can null a whole feature group quietly.

6. **Distinguish broken-feed from real drift.** For each anomalous feature, decide whether the distribution shifted because the world changed (real drift) or because the pipeline broke (garbage). Use range/validity checks and the substitution rate to tell them apart.

7. **Rank by quality impact.** Order findings by (feature importance × corruption severity × prevalence). A high-importance feature defaulting for many requests outranks a cosmetic schema nit.

8. **Specify instrumentation.** For each class of silent failure, recommend the monitor that would have caught it (null/default-rate alert, freshness SLA, schema-contract check, skew comparison job) so the pipeline self-reports next time.

**Output Format:**

A markdown audit:
- **Pipeline Map (offline vs online)** — per-feature dual-path summary
- **Findings Table** — Finding | Type (skew / default-sub / staleness / schema / join) | Evidence | Feature Importance | Quality Impact | Confidence
- **Train-Serve Skew Detail** — features computed differently and how
- **Broken-Feed vs Real-Drift Calls** — which anomalies are which, and why
- **Ranked Remediations** — fix + verification per finding
- **Recommended Instrumentation** — monitors to add so these fail loudly
- **INSUFFICIENT EVIDENCE** — the verdict for the skew question when offline and online feature values have not been compared on the same entities. Reading both code paths shows they *look* equivalent; it does not show they *compute* equivalently. Name the unblocking datum: paired offline/online values for a sample of entity-timestamps.

## Verification

- [ ] Each feature's offline vs online computation was compared (skew check), not assumed identical.
- [ ] Default/null substitution rates were quantified, not just noted.
- [ ] Freshness/staleness checked against explicit cadence expectations.
- [ ] Live data validated against the declared schema/range contract.
- [ ] Each anomalous feature is classified as broken-feed vs real drift with reasoning.
- [ ] Findings are ranked by quality impact and each has recommended instrumentation.
- [ ] Train-serve skew is reported as INSUFFICIENT EVIDENCE unless paired offline/online values for the same entities were compared — code inspection alone does not settle it.

## False-Positive Prevention

❌ **DON'T:**
- Conclude the pipeline is healthy because the job exited 0 — silent failures emit data, just wrong data.
- Flag a feature's shifted distribution as "broken" when the world legitimately changed.
- Ignore default-substitution because individual rows look plausible (a 0 is a valid number).
- Assume offline and online compute a feature identically without checking the code paths.

✅ **DO:**
- Compare offline vs online feature values for the same entities to expose skew.
- Quantify default/null rates and alert on spikes, not just presence.
- Separate broken-feed (out-of-range/garbage) from real drift (valid but shifted) with validity checks.
- Recommend a loud monitor (rate/freshness/schema/skew) for every silent failure class found.

## Example Output

```markdown
## Data Pipeline Health Audit: Ad CTR Model

### Pipeline Map (offline vs online)
- `user_7d_clicks`: offline = batch aggregate over event table; online = feature-store lookup. Paths differ → skew candidate.
- `hour_of_day`: offline = event timestamp; online = server clock at request (UTC vs local) → timing skew candidate.

### Findings Table
| Finding | Type | Evidence | Importance | Quality Impact | Confidence |
|---|---|---|---|---|---|
| `user_7d_clicks` defaults to 0 on store miss | Default-sub | miss rate 18% (was 2%) since Apr 9 store migration | High | Under-scores active users | High |
| `hour_of_day` UTC online vs local offline | Skew | values offset by tz; offline used local | Medium | Time-pattern features misaligned | High |
| `campaign_table` stale | Staleness | last_update 3d old; cadence is hourly | Medium | New campaigns scored on missing features | Medium |
| `device_type` new category "ctv" | Schema | unseen at train → encoded as unknown | Low | Minor | Medium |

### Train-Serve Skew Detail
- `user_7d_clicks`: online store missing recent backfill → 0 default; offline always populated. Same-entity comparison shows mean 4.2 offline vs 1.1 online.
- `hour_of_day`: standardize both to UTC.

### Broken-Feed vs Real-Drift Calls
- `user_7d_clicks` = broken feed (default spike, not a real activity drop — event table is healthy).
- `device_type` ctv = real drift (legitimate new device), handle via retrain, not a bug.

### Ranked Remediations
1. Fix store backfill for `user_7d_clicks`; verify online mean matches offline; expect CTR-AUC recovery.
2. Align `hour_of_day` timezone; re-score.
3. Restore hourly `campaign_table` refresh + freshness SLA.

### Recommended Instrumentation
- Default/null-rate alert per feature (page if >2x baseline). Freshness SLA per source. Offline-vs-online skew job nightly. Schema-contract check on ingest.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** dual-path map → silent-failure hunts → classify → rank flow.
- **RT-09 (Root Cause Explanation):** each finding resolves to a mechanism (skew, default-sub, staleness).
- **DS-06 (Prioritization & Severity Guidance):** findings ranked by importance × severity × prevalence.
- **RT-05 (Evidence-Based Reasoning):** every finding cites a rate, example, or offline/online comparison.
- **QA-12 (False Positives Identification):** separates broken-feed from real drift and job-success from data-health.

**Related Prompts:**
- `mlmonitor_performance_degradation_triage.md` — when a quality drop points upstream to this audit.
- `mlmonitor_drift_detection_design.md` — distinguish real distribution drift from pipeline breakage.
- `mlmonitor_monitoring_dashboard_design.md` — surface the recommended pipeline-health monitors.
```