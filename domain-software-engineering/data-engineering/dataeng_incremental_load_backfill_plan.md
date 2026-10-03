---
title: "Incremental Load and Backfill Plan — Choosing the Change-Capture Method, Handling Deletes and Late Updates, and Running a Backfill You Can Verify and Undo"
category: software-engineering/data-engineering
description: "Choose how a table loads incrementally (append by key, timestamp watermark with overlap, log-based change data capture, or periodic full snapshot) given how the source changes, deletes, and corrects records; then plan a backfill as an operation — scope, chunking, rate limits on the source, cost and duration estimate, a pilot chunk, per-chunk reconciliation, downstream rebuild order, and a rollback that does not depend on luck."
techniques:
  - QA-09
  - DP-11
  - GT-06
  - GT-11
  - NE-11
difficulty: advanced
tags:
  - incremental-load
  - backfill
  - change-data-capture
  - watermark
  - merge-upsert
  - partition-overwrite
  - reload-historical-data
  - fix-past-data
  - pipeline-missed-days
updated: "2026-10-03"
related_prompts:
  - domain-software-engineering/data-engineering/dataeng_pipeline_design_review.md
  - domain-software-engineering/analysis/database/database_migration_strategy.md
  - domain-AI-ML/data-for-ml/mldata_schema_evolution_strategy.md
---

# Incremental Load and Backfill Plan

**Objective:** Produce two things: a load-strategy decision for a table that keeps the
target correct as the source inserts, updates, and deletes rows; and an executable backfill
runbook — chunked, rate-limited, verified chunk by chunk, and reversible.

**When to Use:**
- A table is fully reloaded every night and the job no longer fits its window.
- An incremental load is missing updates or deletes and the warehouse drifts from source.
- A logic fix or new column must be applied to two years of history.
- The pipeline was down for nine days and the gap must be filled without double-loading.
- **Not this prompt if** you are reviewing a whole pipeline's failure behaviour — use
  `dataeng_pipeline_design_review.md` first; this prompt plans one table's load and one
  backfill. Changing an application database's schema in production is
  `domain-software-engineering/analysis/database/database_migration_strategy.md`. How a
  schema may evolve without breaking consumers is
  `domain-AI-ML/data-for-ml/mldata_schema_evolution_strategy.md`. dbt incremental
  materialisation syntax is in `domain-agentic-resources/skills/data-engineering/dbt-transformation-patterns/`.

## Inputs / Context

1. **Source table behaviour**: insert-only or updated in place; is there a reliable
   `updated_at` (set by the database or by application code?); hard or soft deletes;
   primary key stability; volume per day and total.
2. **Access options**: read replica, CDC/log access, API with rate limits, file exports.
3. **Target**: warehouse/lakehouse engine, partitioning, merge support, time travel or
   snapshot retention.
4. **Backfill scope**: date range, reason (gap, logic fix, new column), downstream models.
5. **Constraints**: source load limits, warehouse cost budget, deadline, consumer freeze windows.

## Method

1. **Pick the change-capture method from source behaviour.**
   - *Append by monotonic key*: insert-only sources with an increasing id; misses updates.
   - *Timestamp watermark*: `updated_at > last_watermark − overlap`; needs an `updated_at`
     the database maintains (application-set timestamps miss bulk updates); overlap (e.g.
     1–2 h) covers clock skew and long transactions; misses hard deletes.
   - *Log-based CDC*: captures inserts, updates, and deletes in commit order; costs
     connector operations and replication-slot management.
   - *Snapshot diff*: full extract compared to the previous snapshot; simplest and catches
     deletes; viable while the full extract fits the window.
   Write the target with merge on the primary key (deterministic tie-break on source
   commit sequence or `updated_at`) or overwrite of owned partitions; record how deletes
   propagate (soft-delete flag vs physical delete).
2. **Estimate the backfill (NE-11).** Rows = days × rows/day; chunks = days ÷ chunk size;
   duration = chunks × time/chunk ÷ parallelism; source load = parallel reads × rows/s vs
   the source's safe ceiling; warehouse cost = bytes scanned/written × price. Pick chunk size
   so one chunk fails cheaply (minutes to an hour) and parallelism so the source stays
   under its ceiling.
3. **Make it reversible before you start (QA-09).** Write to a shadow table or new
   partitions, or confirm time-travel retention exceeds backfill duration plus validation
   time. State exactly how to restore the prior state, and test that restore on one chunk.
4. **Pilot one chunk (DP-11).** Pick a chunk with known edge cases (month-end, a known
   correction, a DST change). Validate fully before scaling.
5. **Re-check before each swap (GT-06).** Immediately before promoting chunks or swapping
   tables, re-verify the target set: no concurrent regular load wrote into the same
   partitions, the source has not been re-corrected since extraction. Pause the regular
   incremental job for overlapping partitions or make both write idempotently.
6. **Reconcile per chunk and report the discrepancy first (GT-11).** For each chunk:
   row count and control totals vs source, key uniqueness, null-rate of new columns, and a
   diff against the old values (how many rows changed and why). Report mismatches before
   successes.
7. **Rebuild downstream in dependency order** and notify consumers of restated history,
   with the before/after on metrics they watch.

## Output Format

```
# Load strategy and backfill plan — [table], [date]

## Source behaviour
Inserts/updates/deletes · updated_at maintained by [db/app] · PK stability · volume

## Load strategy decision
Method: [...] · Overlap/lookback: [...] · Write: [merge key / partition overwrite] · Deletes: [...]
Rejected alternatives and why

## Backfill estimate
| Scope | Rows | Chunk size | Chunks | Parallelism | Source load vs ceiling | Duration | Cost |

## Reversibility
Prior-state preservation: [...] · Restore procedure (tested on chunk [..]): [...]

## Runbook
1. Pilot chunk [..] → validation → go/no-go
2. Pause/guard regular load for overlapping partitions
3. Chunk loop: extract → load to shadow → reconcile → promote (with pre-promote recheck)
4. Downstream rebuild order
5. Consumer notice

## Per-chunk reconciliation template
| Chunk | Src rows | Tgt rows | Control total Δ | Dupes | Rows changed vs old | Status |
```

## Verification

- [ ] The method matches how the source updates and deletes; its blind spots are stated.
- [ ] Watermark loads have an overlap and use a database-maintained timestamp, or the risk is named.
- [ ] Backfill duration, source load, and cost are computed, not guessed.
- [ ] The restore path is tested before the backfill starts.
- [ ] Regular loads cannot write into partitions being backfilled.
- [ ] Each chunk reports discrepancies before declaring success.

## False-Positive Prevention

1. **`updated_at` trusted blindly.** Application-set timestamps miss bulk SQL fixes and
   migrations; verify with a sample comparison before relying on it.
2. **CDC as the default.** For a 2 GB table, a nightly snapshot diff is simpler and catches
   deletes; CDC earns its operational cost on large, frequently updated tables.
3. **"Rows changed" read as bugs.** A logic-fix backfill is supposed to change rows; the
   check is whether the changed rows are the ones the fix targets.
4. **Biggest chunk that fits.** Large chunks make each failure expensive and each retry
   long; size for cheap failure.
5. **Time travel as a rollback plan without checking retention.** A 7-day retention on a
   12-day backfill is no rollback for the first chunks.
6. **Backfilling the target but not its dependents.** Aggregates built on the old values
   stay wrong until rebuilt.

## Example Output

```
# Load strategy and backfill plan — warehouse.subscriptions, 2026-10-02

## Source behaviour
Postgres `subscriptions`, 41 M rows, ~120 k inserts + ~300 k updates/day; status changes
in place; hard deletes on GDPR erasure (~200/day); updated_at set by trigger (verified:
0 mismatches in 10 k-row sample vs WAL timestamps).

## Load strategy decision
Method: watermark on updated_at with 2 h overlap, merge on subscription_id (tie-break
updated_at, then xmin); deletes via nightly key-only snapshot diff → soft-delete flag.
Rejected: log CDC (replication slot ownership unresolved with DB team); full reload
(3 h 40 m, exceeds 2 h window).

## Backfill estimate (logic fix: MRR excluded paused periods; 2024-01-01 → 2026-09-30)
| 1,004 days | ~41 M current + 380 M history rows | 7 days | 144 | 4 | 4 × 9 k rows/s = 36 k vs replica ceiling 60 k | 144 × 18 min ÷ 4 ≈ 11 h | ~$85 |

## Reversibility
New partitions written to subscriptions_v2; v1 kept read-only 30 days. Restore = repoint
view to v1 (tested on pilot: 40 s).

## Runbook
1. Pilot: 2025-03-24 → 03-30 (DST change + known March price migration). Go if Δ control
   total explained by paused-period exclusion only.
2. Regular load writes to v1 and v2 (dual-write) for the duration.
3. Chunks oldest → newest; before each promote, recheck no correction ticket touched chunk dates.
4. Rebuild fct_mrr_daily → mart_revenue_monthly → exec dashboard extracts.
5. Finance notified: Q2-2025 MRR restates −1.8% (paused accounts), signed off by Revenue Ops.

## Pilot result
| 2025-03-24..30 | 2,861,204 | 2,861,204 | MRR −1.6% | 0 | 48,113 rows (all paused=true) | pass |
```

## Techniques Used

- **QA-09 Reversibility Assessment** — prior state preserved and restore tested before any chunk runs.
- **DP-11 Safe Experiment Design** — a pilot chunk chosen for its edge cases gates the full run.
- **GT-06 Pre-Commit Recheck** — target partitions and source corrections re-verified before each promote.
- **GT-11 Post-Action Reconciliation & Disclosure** — each chunk reports discrepancies first.
- **NE-11 Embedded Calculation Formulas** — duration, source load, and cost computed from chunk arithmetic.

## Related Prompts

- `dataeng_pipeline_design_review.md` — whole-pipeline idempotency and late-data review.
- `domain-software-engineering/analysis/database/database_migration_strategy.md` — production schema changes on the source side.
- `domain-AI-ML/data-for-ml/mldata_schema_evolution_strategy.md` — compatibility rules when a backfill adds or changes columns.
