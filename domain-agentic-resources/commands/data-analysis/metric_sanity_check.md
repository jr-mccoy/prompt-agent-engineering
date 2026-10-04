---
name: metric_sanity_check
description: Ten-to-fifteen-minute pre-publish smoke test for one computed business metric — confirms the definition being used, tests the output grain for duplicates, checks join fan-out, null handling in numerator and denominator, totals reconciliation (segments sum to total; total matches an independent source within a stated tolerance), time window and time zone, ratio bounds, and an abrupt step versus recent periods. Each check returns PASS / WARN / FAIL with the diagnostic query and its result. Escalates to the full SQL correctness review on any FAIL. Distinct from the metric-definition spec (writes the definition) and the SQL correctness review (deep adversarial review).
version: "1.0.0"
category: data-analysis
tags: [data-analysis, metrics, sanity-check, reconciliation, grain, nulls, sql, kpi, data-quality]
agents_used: []
---

# Metric Sanity Check

Before a number goes into a deck, a dashboard, or a decision, run a short battery
of diagnostics that catch the errors that most often make a metric wrong. You
run the checks (or hand over the exact diagnostic queries when you cannot run
them), report results with evidence, and keep **measured**, **estimated**, and
**assumed** values visibly separate.

[Extended thinking: Most wrong metrics are wrong for a handful of mechanical
reasons — duplicated rows from a join, nulls dropped or counted inconsistently,
a time-zone boundary, a partial current period, a numerator that is not a
subset of its denominator. These are cheap to test and expensive to miss. This
command is the quick pre-flight; it does not replace a full review of the query
or a written metric definition, and it routes to both when needed.]

## Requirements
$ARGUMENTS

Expected: the metric name, the query or code that computes it, the value(s) it
produced, and where it will be used. Helpful: the written metric definition, the
intended grain ("one row per account per month"), an independent reference total
(finance system, source-system count, prior published figure), and the
tolerance the audience will accept. If the computing query or code is missing,
ask for it and stop.

## When NOT to use

- No agreed definition exists and people disagree on what the metric means →
  `domain-data-analytics/framing-and-metrics/analytics_metric_definition_spec.md` first
- A full correctness review of a complex query (survivorship, look-ahead bias,
  dedup logic, every join) → `domain-data-analytics/analysis-and-sql/analytics_sql_query_correctness_review.md`
- "Why did this metric move?" → `domain-data-analytics/analysis-and-sql/analytics_metric_movement_investigation.md`
- Profiling an unfamiliar input table → `/dataset_profile`
  (`commands/data-analysis/dataset_profile.md`)

## Instructions

### Phase 1 — Pin the definition
State, in one block, the definition actually implemented by the query: grain,
numerator, denominator (if a ratio), filters, time window, time zone. If a
written definition was supplied, list every difference between it and the
implementation. If none was supplied, label the block `[assumed from query]`.

### Phase 2 — Run the checks
Run each check; record PASS / WARN / FAIL, the diagnostic, and the result.
If you cannot execute queries in this environment, output the diagnostic and
mark the check **UNRUN** — never mark an unrun check PASS.

| # | Check | Diagnostic (adapt to the SQL dialect) | FAIL when |
|---|-------|---------------------------------------|-----------|
| 1 | **Grain** | `SELECT <grain cols>, COUNT(*) FROM (<metric query>) q GROUP BY <grain cols> HAVING COUNT(*) > 1` | any rows returned |
| 2 | **Join fan-out** | Row count of the base table vs after each join | count grows where the join should be 1:1 or many:1 |
| 3 | **Nulls** | Null rate of key, numerator, and denominator fields; rows dropped by inner joins on nullable keys; `COUNT(col)` vs `COUNT(*)`; `AVG` silently ignoring nulls | nulls change the result and the definition does not say how to treat them |
| 4 | **Totals reconcile (internal)** | Sum of segment values vs the stated total (for additive metrics) | segments do not sum to total and the metric is supposed to be additive |
| 5 | **Totals reconcile (external)** | Metric total vs the independent reference | difference exceeds the stated tolerance; report the residual either way |
| 6 | **Time window** | Min/max event timestamp included; time zone of the boundary; is the latest period complete? | boundary in the wrong time zone, or a partial period presented as complete |
| 7 | **Ratio bounds** | Denominator zero/negative count; numerator ⊆ denominator; rate within 0–100% where it must be | impossible values present |
| 8 | **Step change** | Value for the last several comparable periods | abrupt jump/drop with no known cause → WARN, not FAIL (route to movement investigation) |

Non-additive metrics (distinct counts, medians, ratios): check 4 is N/A — say
so rather than summing them.

### Phase 3 — Verdict and routing
- Any FAIL → **DO NOT PUBLISH**; list the fix or route to the SQL correctness review.
- WARN only → **PUBLISH WITH CAVEAT**; write the one-line caveat the audience should see.
- All PASS (none UNRUN) → **PASS**, with the residual from check 5 stated.
- Any UNRUN on checks 1, 3, or 5 → verdict is at best **PASS PENDING** those checks.

## Output

```markdown
# Metric Sanity Check: <metric> = <value> (<period>)
Use: <where it will appear> · Tolerance: <stated | none given>

## Definition implemented  [given | assumed from query]
Grain: ... · Numerator: ... · Denominator: ... · Filters: ... · Window/TZ: ...
Differences from written definition: <list or none>

## Checks
| # | Check | Status | Evidence |
|---|-------|--------|----------|

## Verdict: DO NOT PUBLISH | PUBLISH WITH CAVEAT | PASS PENDING | PASS
Caveat (if any): "<one line for the audience>"
Reconciliation residual: <value and %> vs <reference>  [measured]
Next step: <fix | route to analytics_sql_query_correctness_review | none>
```

## Success Criteria

- Every check has a status and evidence; none is skipped silently
- Unrun checks are labelled UNRUN, never PASS
- The external reconciliation residual is reported even when within tolerance
- Inferred or assumed values are tagged `[estimate]`, `[assumed]`, or `[verify]`

## Constraints

- NEVER adjust the metric, filters, or tolerance to make a check pass
- NEVER present an estimate or a sample-based figure as measured
- Read-only: run `SELECT` diagnostics only; never write to the warehouse
