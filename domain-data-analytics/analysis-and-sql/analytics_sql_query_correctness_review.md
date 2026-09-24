---
title: "SQL Query Correctness Review — Grain, Join Fan-Out, Nulls, Time Zones, Dedup, Survivorship"
category: data-analytics/analysis-and-sql
description: "Review an analysis query for whether it returns the right number, not whether it runs fast: output grain, join fan-out and double counting, null handling in joins, filters and aggregates, time-zone and date-boundary errors, deduplication, survivorship and look-ahead bias — each finding backed by a diagnostic query and a severity."
techniques:
  - QA-18
  - DT-05
  - RT-05
  - DS-06
  - QA-12
difficulty: advanced
tags:
  - sql-review
  - query-correctness
  - join-fan-out
  - data-validation
  - business-analytics
  - analysis-queries
  - number-looks-wrong
  - double-counting
  - reports-disagree
updated: "2026-09-24"
related_prompts:
  - domain-data-analytics/framing-and-metrics/analytics_metric_definition_spec.md
  - domain-data-analytics/analysis-and-sql/analytics_metric_movement_investigation.md
  - domain-agentic-resources/skills/developer-tools/sql-optimization-patterns/SKILL.md
---

# SQL Query Correctness Review

**Objective:** Find every way an analysis query could return a plausible but wrong
number, prove each suspected defect with a diagnostic query, and rank the defects by
how much they move the answer.

**When to Use:**
- A query feeds a decision, a board number, or a dashboard tile, and nobody else has read it.
- A number "looks off" and you want to rule out the query before blaming the data.
- You inherited a query and are about to reuse it for a different question.
- Two queries that should agree do not.

**When NOT to use:**
- The query is slow — `domain-agentic-resources/skills/developer-tools/sql-optimization-patterns/`
  covers indexing, EXPLAIN, and performance. This prompt ignores speed.
- You are reviewing application SQL for injection — `domain-software-engineering/analysis/security/security_sql_injection_analysis.md`.
- You are designing dbt models or tests — `domain-agentic-resources/skills/data-engineering/dbt-transformation-patterns/`
  and `data-quality-frameworks/`.

## Inputs / Context

1. **The query**, in full, including CTEs.
2. **The question it is meant to answer**, in one sentence, and the metric spec if one exists.
3. **Table grains** — one row per what, for every table referenced — and primary keys.
4. **The warehouse dialect** (NULL semantics, time-zone functions, and `DATE_TRUNC`
   behaviour differ).
5. **The result** it currently returns, if run.

If table grains are unknown, the first finding is "grain unverified" and the first
diagnostic is a uniqueness check on each claimed key.

## Method

Walk the query clause by clause (DT-05), applying the analytics smell tests (QA-18).
For each suspected defect, write a diagnostic query that proves or disproves it (RT-05).

1. **Output grain.** State what one output row should represent. Check that the
   `GROUP BY` produces exactly that, and that every non-aggregated column is at that grain.

2. **Join fan-out.** For each join, name the cardinality (1:1, 1:N, N:M). A 1:N join
   followed by `SUM` or `COUNT(*)` of a parent-level column double counts.
   Diagnostic: `SELECT key, COUNT(*) FROM right_table GROUP BY key HAVING COUNT(*) > 1`.

3. **Join type and silent row loss.** An `INNER JOIN` drops unmatched rows; a
   `LEFT JOIN` followed by a `WHERE right.col = ...` filter turns back into an inner join.
   Diagnostic: row counts before and after each join.

4. **Nulls.**
   - `NULL` join keys never match.
   - `col <> 'x'` excludes nulls.
   - `COUNT(col)` ignores nulls; `AVG` ignores them in numerator and denominator.
   - `NOT IN (subquery)` returns nothing if the subquery contains a null.

5. **Time.** Time zone of the stored timestamp vs the day boundary the spec requires;
   `BETWEEN` on timestamps including or excluding the end day; `DATE_TRUNC('week')`
   start day; daylight-saving gaps; comparing a partial current period to full prior ones.

6. **Deduplication.** Duplicate events from retries or replays; `DISTINCT` hiding a
   fan-out instead of fixing it; `ROW_NUMBER()` dedup with a non-deterministic `ORDER BY`.

7. **Population bias.** Survivorship (joining to a current-state table such as
   `dim_customer WHERE status = 'active'` when measuring the past); look-ahead (using
   attributes known only after the period); slowly changing dimensions joined on the
   current row rather than the row valid at event time.

8. **Ratios.** Numerator and denominator filtered identically; average of ratios vs
   ratio of sums chosen on purpose; integer division.

9. **Rank findings (DS-06)** by estimated impact on the answer, not by how unusual
   they are. Run the diagnostic and state the magnitude where possible.

10. **Note what was checked and cleared (QA-12)**, so a clean review is distinguishable
    from a skipped one.

## Output Format

```
# SQL correctness review — [query name]
Question it answers: [...]    Intended output grain: [...]

## Table grains
| Table | Claimed grain / key | Verified? |
|---|---|---|

## Findings (ranked by impact)
| # | Clause | Defect | Severity | Diagnostic | Result | Impact on answer | Fix | Confidence |
|---|---|---|---|---|---|---|---|---|

Severity: Blocking (answer wrong) | Material (> [x]% change) | Minor | Style

## Checked and cleared
- [check] — [how cleared]

## Corrected query (or diff)
## Before / after
| Metric | Original | Corrected |
|---|---|---|
```

## Verification

- [ ] Output grain is stated and matches the `GROUP BY`.
- [ ] Every join has a stated cardinality, and every 1:N join has a fan-out diagnostic.
- [ ] Every `LEFT JOIN` has been checked for a `WHERE` filter on the right table.
- [ ] Null behaviour has been checked in joins, filters, `NOT IN`, and aggregates.
- [ ] Day boundary and time zone match the metric spec.
- [ ] Each Blocking or Material finding has a diagnostic that was run, or is marked `[not run]`.
- [ ] A "checked and cleared" list exists.

## False-Positive Prevention

1. **`DISTINCT` is not a fix.** It can hide a fan-out on the columns you selected while
   the `SUM` beside it is still inflated. Find the join that fans out.
2. **Not every 1:N join is a bug.** Fan-out only matters if you aggregate a parent-level
   column afterwards. Check what is summed before flagging.
3. **Don't claim a defect you haven't demonstrated.** "This might double count" without
   a diagnostic is a hypothesis. Mark it Low confidence until the query runs.
4. **Dialect assumptions.** `DATE_TRUNC('week')` starts Monday in some warehouses and
   Sunday in others; string comparison with trailing spaces differs. Confirm the dialect.
5. **Style is not correctness.** CTE naming and formatting go in a Style bucket at the
   bottom and do not dilute Blocking findings.
6. **Performance is out of scope.** A slow correct query passes this review. Route
   speed concerns to `sql-optimization-patterns`.
7. **A corrected number is still a measured number only if you ran it.** If the
   impact is estimated from row counts, label it `[estimated]`.

## Example Output

```
# SQL correctness review — q3_revenue_by_region
Question it answers: Q3 2026 net revenue by customer region.   Intended grain: region.

## Table grains
| Table | Claimed grain / key | Verified? |
|---|---|---|
| fct_orders | order_id | Yes — unique |
| fct_order_items | order_item_id | Yes |
| dim_customer | customer_id (current row) | No — SCD2, customer_id repeats |

## Findings (ranked by impact)
| # | Clause | Defect | Severity | Diagnostic | Result | Impact | Fix | Confidence |
|---|---|---|---|---|---|---|---|---|
| 1 | JOIN fct_order_items | SUM(o.order_total) after 1:N join to items | Blocking | count items per order | mean 2.3 items/order | revenue ×2.3 | sum item_amount, or aggregate items first | High |
| 2 | JOIN dim_customer | SCD2 joined without valid_from/valid_to | Material | customer_id dup count | 4.1% of customers have 2+ rows | region double-assigned [measured: +3.8%] | join on event date within validity | High |
| 3 | WHERE | order_ts BETWEEN '2026-07-01' AND '2026-09-30' | Material | count orders on 09-30 | Sep 30 after 00:00 excluded | −1.1% | order_ts >= '07-01' AND < '10-01' | High |
| 4 | WHERE | `status <> 'test'` also drops rows where status is NULL | Minor | null status count | 212 rows null status excluded | −0.2% | COALESCE(status,'') <> 'test' | Medium |

## Checked and cleared
- Time zone: order_ts stored in UTC; spec uses UTC — cleared.
- Refund netting: refunds joined 1:1 on order_id — verified unique.

## Corrected query (diff)
- SUM(o.order_total)
+ SUM(i.item_amount - COALESCE(i.item_refund, 0))
- JOIN dim_customer c ON c.customer_id = o.customer_id
+ JOIN dim_customer c ON c.customer_id = o.customer_id
+   AND o.order_ts >= c.valid_from AND o.order_ts < COALESCE(c.valid_to, '9999-12-31')
- WHERE o.order_ts BETWEEN '2026-07-01' AND '2026-09-30'
+ WHERE o.order_ts >= '2026-07-01' AND o.order_ts < '2026-10-01'

## Before / after
| Metric | Original | Corrected |
|---|---|---|
| Q3 net revenue, all regions | $9.84M | $4.12M |
| EMEA share | 31% | 27% |
```

## Techniques Used

- **QA-18 Domain-Specific Smell Tests** — the analytics-specific failure list: fan-out, null joins, SCD joins, date boundaries, survivorship.
- **DT-05 Element-by-Element Assessment Matrix** — clause-by-clause walk with a finding row per defect.
- **RT-05 Evidence-Based Reasoning** — each finding carries a diagnostic query and its result.
- **DS-06 Prioritization and Severity Guidance** — findings ranked by impact on the answer.
- **QA-12 False Positives Identification** — a "checked and cleared" list and a Style bucket keep non-defects out of the findings.

## Related Prompts

- `domain-data-analytics/framing-and-metrics/analytics_metric_definition_spec.md` — the spec the query is checked against.
- `domain-data-analytics/analysis-and-sql/analytics_metric_movement_investigation.md` — when the number moved and the query is a suspect.
- `domain-agentic-resources/skills/developer-tools/sql-optimization-patterns/SKILL.md` — query performance, which this review ignores.
