---
title: "Data Pipeline Design Review — Idempotency, Safe Retries, Backfills, Late Data, and Exactly-Once Claims"
category: software-engineering/data-engineering
description: "Review a batch or streaming data pipeline design for correctness under failure: whether every task can be re-run without duplicating or losing rows, whether retries are safe end to end, whether the pipeline can be backfilled for any past interval, how late-arriving and out-of-order data are handled, and whether any 'exactly-once' claim holds across the source, the processor, and the sink — with each risk traced to a concrete failure scenario."
techniques:
  - DP-07
  - QA-09
  - IPC-09
  - QA-24
difficulty: advanced
tags:
  - data-pipeline
  - idempotency
  - exactly-once
  - late-arriving-data
  - backfill
  - stream-processing
  - batch-etl
  - pipeline-duplicates-rows
  - safe-to-rerun-job
  - numbers-change-after-rerun
updated: "2026-10-03"
related_prompts:
  - domain-software-engineering/data-engineering/dataeng_incremental_load_backfill_plan.md
  - domain-software-engineering/data-engineering/dataeng_data_quality_test_strategy.md
  - domain-AI-ML/production-monitoring/mlmonitor_data_pipeline_health_audit.md
---

# Data Pipeline Design Review

**Objective:** Decide whether a pipeline design (proposed or running) produces the same,
correct output no matter how often its tasks fail, retry, or are re-run — and list the
specific scenarios where it would not, with the smallest design change that fixes each.

**When to Use:**
- A design doc for a new ingestion or transformation pipeline is up for review.
- A rerun after a failure produced duplicate or missing rows and nobody is sure why.
- A streaming job claims "exactly-once" and downstream teams are relying on it.
- You are about to backfill a year of history through a pipeline that was only ever run
  forward.
- **Not this prompt if** you want a new pipeline architecture and code generated —
  `domain-agentic-resources/commands/architecture/data_pipeline.md` builds; this prompt
  judges. For orchestrator or engine how-to (DAG structure, Spark tuning) use the skills in
  `domain-agentic-resources/skills/data-engineering/` (`airflow-dag-patterns`,
  `spark-optimization`). A pipeline feeding a model, where the concern is train/serve skew,
  is `domain-AI-ML/production-monitoring/mlmonitor_data_pipeline_health_audit.md`. Planning
  one specific backfill is `dataeng_incremental_load_backfill_plan.md`.

## Inputs / Context

1. **Topology**: sources, ingestion mechanism (API pull, CDC, file drop, event stream),
   transforms, sinks, and orchestrator.
2. **Per task**: input selection (how it decides which data to read), write mode (append,
   overwrite partition, merge/upsert, delete-insert), and the keys it writes on.
3. **Time semantics**: event time vs processing/ingestion time, partitioning column,
   expected lateness, watermark or lookback settings.
4. **Retry and failure behaviour**: orchestrator retries, consumer offset commits,
   checkpointing, dead-letter handling.
5. **Delivery claims** made to consumers (freshness SLA, completeness, exactly-once).
6. **Incidents** to date involving duplicates, gaps, or reruns.

## Method

1. **Trace each task's determinism.** A task is re-runnable only if its output depends on
   its parameters (logical date/interval, input snapshot), not on wall-clock time. Flag any
   `now()`, `current_date`, "last 24 hours from run time", or reading "latest" without a
   pinned version — these make reruns and backfills compute a different answer.
2. **Classify each write (QA-09).** For each sink write, ask "what happens if this runs
   twice?" Append without a key → duplicates. Overwrite of the exact partition the task owns
   → idempotent. Merge on a stable business key with a deterministic tie-break (e.g. latest
   `updated_at`, then source sequence) → idempotent. Delete-insert in two transactions →
   a window where readers see nothing. Record reversibility: can a bad run be undone by
   re-running, or does it need a restore?
3. **Walk failure scenarios (DP-07).** For each task: fails before write, fails mid-write,
   fails after write but before marking success (orchestrator retries a completed write),
   succeeds twice concurrently (overlapping schedules or manual trigger). State the outcome
   in each case.
4. **Test the exactly-once claim end to end.** "Exactly-once" inside a stream processor
   (e.g. transactional producers, checkpointed state) does not extend to an external sink
   unless the sink write is transactional with the checkpoint (two-phase commit) or
   idempotent on a key. The honest default is *at-least-once delivery + idempotent sink =
   effectively-once results*; anything stronger must show the mechanism at every hop.
5. **Late and out-of-order data.** Determine the partitioning time. If partitions are by
   event time, how long are they reopened (lookback window, allowed lateness)? What happens
   to data later than that — dropped, routed to a correction path, or silently landed in
   the wrong partition? Quantify from history: % of events arriving > N hours late.
6. **Backfill-ability.** Can any past interval be re-run with parameters alone, without
   code changes, at a controlled rate against the source? Does it rebuild downstream
   dependents in order?
7. **Failure visibility (IPC-09).** A partial input must fail loudly: empty upstream
   partitions, schema changes, and row counts outside expected bounds stop the task rather
   than produce a "successful" empty or partial output.
8. **List what was checked and is sound (QA-24)** so the review distinguishes "safe" from
   "not examined".

## Output Format

```
# Pipeline design review — [pipeline], [date]
Mode: batch / micro-batch / streaming · Orchestrator: [...] · Consumers: [...]

## Task-by-task correctness
| Task | Input selection | Deterministic? | Write mode | Key | Run-twice outcome | Reversible by rerun? |

## Failure scenarios
| Task | Fails before write | Mid-write | After write, before success | Concurrent double run |

## Delivery semantics
Claimed: [...] · Actual per hop: source → processor → sink · Verdict: [...]

## Late / out-of-order data
Partition time: [...] · Lateness observed: [p50/p95/p99] · Lookback: [...] · Beyond lookback: [...]

## Backfill readiness
## Fail-loud checks present / missing
## Findings (severity, scenario, smallest fix)
## Checked and sound
```

## Verification

- [ ] Every task's input selection is checked for wall-clock dependence.
- [ ] Every write has a stated run-twice outcome.
- [ ] Each "exactly-once" statement names the mechanism at the sink.
- [ ] Lateness is quantified from data, not assumed.
- [ ] Each finding names the concrete scenario that triggers it and the smallest fix.
- [ ] Sound areas are listed, not just problems.

## False-Positive Prevention

1. **Append flagged as always wrong.** Append is safe when the task owns an immutable
   partition it overwrites as a unit, or when a downstream dedup on a key is guaranteed.
2. **Orchestrator retries assumed safe.** A retry re-executes the whole task, including a
   write that already succeeded; safety comes from the write, not the scheduler.
3. **"Exactly-once" accepted from a framework feature name.** Check the sink.
4. **Every late event treated as a defect.** Some lateness is normal (mobile clients
   offline); the question is whether the design has a stated policy for it.
5. **Theoretical races given equal weight.** A concurrent double run that the orchestrator
   prevents by a max-active-runs limit is low severity; say why.
6. **Recommending streaming to fix batch correctness.** Most correctness bugs are write-mode
   and key bugs that exist in both.

## Example Output

```
# Pipeline design review — orders_daily (Postgres → lake → warehouse), 2026-10-02
Mode: daily batch · Orchestrator: Airflow · Consumers: finance revenue mart, ops dashboard

## Task-by-task correctness
| extract_orders  | updated_at > max(updated_at) in target | no — depends on target state | append to raw | none | duplicates on retry after write | no |
| stage_orders    | raw partition ds={{ds}}                | yes | overwrite partition | ds | identical | yes |
| fct_orders      | stage where ds between ds-3 and ds     | yes | merge | order_id | identical | yes |
| revenue_rollup  | fct where order_date = current_date-1  | no — wall clock | overwrite | date | rerun on 10-05 rebuilds 10-04, not 10-01 | no |

## Failure scenarios (extract_orders)
Fails after S3 write, before success → retry re-reads from same watermark (target not yet
loaded) → second file with same rows → stage reads both files → duplicate orders.

## Delivery semantics
Claimed: "exactly-once to warehouse". Actual: extract at-least-once; fct merge on order_id
makes fct effectively-once *only* because stage duplicates collapse on merge — but
revenue_rollup reads stage counts for a "new orders" metric → double counts on retry days.

## Late / out-of-order data
Partition time: ingestion date. 0.8% of order updates arrive > 3 days late (refund edits) →
fct merge lookback of 3 days misses them; refunds land but rollups are never recomputed.

## Findings
H1 extract: pin interval to [data_interval_start, data_interval_end) on updated_at; write
   file named by interval so a retry overwrites. 
H2 revenue_rollup: parameterise by {{ds}}, not current_date.
M1 Extend lookback to 7 days (covers 99.6% of late updates); route older edits to a
   weekly correction run that recomputes affected dates.
M2 Add fail-loud check: stage row count within ±40% of 28-day same-weekday median.

## Checked and sound
stage_orders overwrite semantics; fct_orders merge tie-break (updated_at, then xmin).
```

## Techniques Used

- **DP-07 Failure Mode Prediction** — each task walked through four failure scenarios before judging it safe.
- **QA-09 Reversibility Assessment** — every write classified by whether a rerun repairs it or a restore is needed.
- **IPC-09 Error Propagation over Absorption** — partial or empty inputs must fail the task, not produce quiet partial output.
- **QA-24 Dismissed-Candidates Coverage Table** — sound areas listed so the review shows what was examined.

## Related Prompts

- `dataeng_incremental_load_backfill_plan.md` — planning the load strategy and a specific backfill once the design is sound.
- `dataeng_data_quality_test_strategy.md` — where the fail-loud checks live and who owns them.
- `domain-AI-ML/production-monitoring/mlmonitor_data_pipeline_health_audit.md` — the ML-feeding variant focused on train/serve skew.
