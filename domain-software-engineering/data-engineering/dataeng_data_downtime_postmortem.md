---
title: "Data Downtime Triage and Postmortem — Containing Bad or Late Data, Mapping the Blast Radius Through Lineage, Repairing, and Learning Why Detection Failed"
category: software-engineering/data-engineering
description: "Handle a data pipeline incident — data that is missing, late, duplicated, or wrong — from first report to closed postmortem: confirm and classify the failure, stop bad data spreading, find every downstream table, dashboard, and sync it reached through lineage, choose fix-forward or restore-and-backfill, tell affected consumers what was wrong and for which dates, then write a blameless postmortem that measures time-to-detect and asks why a consumer noticed before the checks did."
techniques:
  - RT-07
  - RT-09
  - DS-06
  - DS-40
difficulty: intermediate
tags:
  - data-incident
  - data-downtime
  - data-lineage
  - postmortem
  - root-cause-analysis
  - time-to-detect
  - dashboard-showed-wrong-numbers
  - report-data-is-late
  - who-used-the-bad-data
updated: "2026-10-03"
related_prompts:
  - domain-AI-ML/production-monitoring/mlmonitor_incident_postmortem_template.md
  - domain-engineering-workflows/workflows/engineering_postmortem_blueprint.md
  - domain-data-analytics/analysis-and-sql/analytics_metric_movement_investigation.md
---

# Data Downtime Triage and Postmortem

**Objective:** Run a data incident in two parts — a triage that limits how far bad data
travels and repairs it with every affected consumer told, and a postmortem that explains
the failure, its detection delay, and the owned actions that prevent a repeat.

**When to Use:**
- A stakeholder reports that a dashboard, export, or customer-facing number is wrong,
  stale, or doubled.
- A data quality check fired on a Tier 1 dataset and the data may already be published.
- A pipeline silently skipped days, or a source changed format and loads "succeeded" empty.
- The incident is fixed and you need the write-up.
- **Not this prompt if** a business metric moved and you do not yet know whether the data
  is wrong — start with `domain-data-analytics/analysis-and-sql/analytics_metric_movement_investigation.md`,
  which rules data problems in or out. If the failure is a model's behaviour (drift, skew),
  use `domain-AI-ML/production-monitoring/mlmonitor_incident_postmortem_template.md`. For a
  facilitated, general engineering postmortem on a service outage, use
  `domain-engineering-workflows/workflows/engineering_postmortem_blueprint.md` or the
  `domain-agentic-resources/skills/devops/postmortem-writing/` skill; this prompt adds
  the data-specific parts — lineage blast radius, restatement, and detection gaps.

## Inputs / Context

1. **Report or alert**: who noticed, what they saw, when.
2. **Affected dataset(s)** and the pipeline runs around the first bad interval.
3. **Lineage**: upstream sources and downstream models, dashboards, reverse-ETL syncs,
   exports, ML features (from a catalogue or the transformation DAG).
4. **Check results** around the incident window (what fired, what did not).
5. **Recent changes**: deploys, source-system releases, schema changes, credential rotations.

## Method

**Triage (hours)**

1. **Confirm and classify.** Compare against an independent source (system of record,
   raw layer). Classify: *missing* (gap), *late* (freshness), *duplicated*, *wrong values*,
   *schema break*. Record the first bad interval and whether it is still growing.
2. **Severity (DS-06).** Sev 1: wrong data reached customers, money movement, regulators,
   or external reporting. Sev 2: internal decision-critical dashboards or finance close.
   Sev 3: exploratory or self-correcting within the next run.
3. **Contain.** Pause downstream publication and syncs that propagate the bad data
   (reverse-ETL to CRM, customer exports) — stopping a sync is cheaper than undoing what it
   wrote. Pin dashboards to last good data or add a visible banner.
4. **Map the blast radius (RT-07).** Walk lineage forward from the first bad table: first
   order (direct models), second order (marts, aggregates), third order (dashboards,
   syncs, extracts, features). For each: affected dates, whether it was read in the window
   (query logs), and by whom.
5. **Repair.** *Fix forward* when the bad interval is short and the pipeline is
   idempotent per partition: fix the cause, re-run affected partitions, rebuild
   dependents in order. *Restore and backfill* when values were overwritten or merges
   corrupted history: restore from snapshot/time travel, then re-run. Verify by the same
   independent comparison used to confirm.
6. **Tell consumers what changed.** For each affected asset: what was wrong, which dates,
   corrected values (or magnitude), and any decisions or customer communications that used
   the bad numbers.

**Postmortem (days)**

7. **Timeline with four timestamps**: failure started, first detectable, detected (and
   by whom — a check or a human consumer), resolved. Time-to-detect and time-to-resolve
   together are the data downtime.
8. **Root cause and contributing factors (RT-09).** Cause → symptoms → why it produced
   those symptoms → fix. Separate the trigger (e.g. source added a currency) from the
   conditions that let it through (no accepted-values check, merge silently coerced).
9. **Detection review.** If a consumer found it first, which check would have caught it,
   at which layer, how much earlier? Treat "a human noticed" as a detection failure.
10. **Actions (DS-40).** Each with an owner, due date, and type: prevent (stop the cause),
    detect (catch it sooner), mitigate (reduce blast radius, e.g. circuit breaker on a
    sync). Blameless: describe decisions in the context people had at the time.

## Output Format

```
# Data incident [id] — [dataset], Sev [n]

## Triage log
Classified as: [missing/late/duplicated/wrong/schema] · first bad interval: [...] · growing? [...]
Containment: [syncs paused, dashboards bannered] at [time]

## Blast radius
| Order | Asset | Type | Dates affected | Read during window? | By whom | Action |

## Repair
Approach: fix-forward / restore + backfill · steps · verification against [source]

## Consumer notice
[asset · what was wrong · dates · corrected magnitude · decisions possibly affected]

## Postmortem
Timeline: started · first detectable · detected (by) · resolved
Data downtime: TTD [..] + TTR [..]
Root cause · contributing factors
Detection gap: [check that would have caught it, layer, time saved]
| Action | Type (prevent/detect/mitigate) | Owner | Due |
```

## Verification

- [ ] The failure was confirmed against an independent source before repair.
- [ ] Every downstream asset in lineage has been listed with dates and read status.
- [ ] Syncs and exports carrying bad data were paused before repair began.
- [ ] Repair was verified with the same comparison used to confirm the problem.
- [ ] Consumers received what was wrong, which dates, and the corrected magnitude.
- [ ] The timeline separates first-detectable from detected and names who detected it.
- [ ] Every action has an owner, a due date, and a type.

## False-Positive Prevention

1. **"Job succeeded" as "data correct".** Many data incidents are green runs over empty or
   wrong input; confirm with the data, not the orchestrator status.
2. **Root cause = the upstream team.** The trigger may be upstream; the conditions that let
   it reach a dashboard are usually yours.
3. **Fixing the table, forgetting the copies.** Extracts, caches, reverse-ETL destinations
   and spreadsheets keep the bad values after the warehouse is fixed.
4. **Over-declaring.** A one-run freshness delay on a Tier 3 dataset that self-corrected is
   a log entry, not a Sev 2 with a postmortem.
5. **Blame in the timeline.** "Engineer X pushed a bad change" teaches nothing; "the change
   passed review because the test suite had no fixture with a non-USD currency" does.
6. **Actions without owners.** "Improve monitoring" is not an action.

## Example Output

```
# Data incident DI-2026-031 — fct_invoices (revenue), Sev 2

## Triage log
Reported 2026-09-08 09:40 by FP&A: August revenue in dashboard 6.2% above ledger.
Confirmed vs ledger at 10:15. Classified: wrong values. First bad interval: 2026-08-19 →
ongoing. Containment 10:30: finance dashboard bannered "under review"; month-end export
to ERP paused.

## Blast radius
| 1 | stg_invoices            | model     | 08-19 → 09-07 | — | — | rebuild |
| 2 | fct_invoices, mart_revenue_monthly | models | same | yes | FP&A, CFO deck draft | rebuild |
| 3 | Revenue dashboard       | BI        | same | 46 views | exec team | banner, refresh |
| 3 | ERP month-end export    | file sync | Aug | not yet sent | — | held |
| 3 | Board pre-read v1       | slide     | Aug | yes | CFO | correct before send |

## Repair
Fix forward: from 08-19 the source emitted CAD invoices as a native-currency row plus a
USD-converted row; the merge key (invoice_id, currency) kept both, so each CAD invoice
counted twice. Fixed key to invoice_id (USD row kept); re-ran 20 daily partitions; rebuilt 2 marts. Verified August
total = ledger ±0.01% at 15:20.

## Consumer notice (sent 15:45)
Revenue dashboard and mart_revenue_monthly overstated 2026-08-19 → 09-07 by $412k (6.2% of
Aug). Corrected. Board pre-read v1 used the wrong figure; v2 corrected before distribution.

## Postmortem
Timeline: started 08-19 02:10 · first detectable 08-19 (duplicate invoice_id) · detected
09-08 09:40 by FP&A · resolved 09-08 15:20. Data downtime: TTD 20 d 7 h, TTR 5 h 40 m.
Root cause: merge key (invoice_id, currency) allowed two rows per invoice when a currency
was first introduced. Contributing: no uniqueness test on invoice_id alone; reconciliation
to ledger only ran at quarter end.
Detection gap: staging uniqueness on invoice_id would have blocked on 08-19 (20 days sooner).
| Uniqueness test on invoice_id (blocking)        | detect   | Analytics Eng (R. Osei) | 09-12 |
| Monthly-to-date ledger reconciliation, daily    | detect   | Finance Systems (M. Ito) | 09-30 |
| Circuit breaker on ERP export when recon fails  | mitigate | Data Platform (J. Park) | 10-15 |
| Multi-currency fixture in test data             | prevent  | Analytics Eng (R. Osei) | 09-19 |
```

## Techniques Used

- **RT-07 Cascade Effect Analysis** — blast radius walked through first-, second-, and third-order consumers.
- **RT-09 Root Cause Explanation Pattern** — cause → symptoms → explanation → fix, with trigger separated from enabling conditions.
- **DS-06 Prioritization and Severity Guidance** — severity by who and what the bad data reached.
- **DS-40 Follow-Up Action Extraction** — prevent/detect/mitigate actions with owners and dates.

## Related Prompts

- `domain-AI-ML/production-monitoring/mlmonitor_incident_postmortem_template.md` — the ML-model equivalent.
- `domain-engineering-workflows/workflows/engineering_postmortem_blueprint.md` — a facilitated, general engineering postmortem.
- `domain-data-analytics/analysis-and-sql/analytics_metric_movement_investigation.md` — deciding whether a moved number is a data problem at all.
