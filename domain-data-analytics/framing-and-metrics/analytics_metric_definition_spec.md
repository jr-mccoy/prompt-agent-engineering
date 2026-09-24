---
title: "Metric Definition Spec — Grain, Numerator, Denominator, Filters, Window, Edge Cases, Owner"
category: data-analytics/framing-and-metrics
description: "Write an unambiguous spec for one business metric: its grain, numerator and denominator in words and in SQL-shaped logic, inclusion and exclusion filters, time window and time zone, the edge cases that change the number, how it can be gamed, and a named owner — so two analysts computing it independently get the same value."
techniques:
  - DS-02
  - CM-02
  - MP-04
  - QA-21
  - OC-03
difficulty: intermediate
tags:
  - metric-definition
  - business-metrics
  - data-dictionary
  - semantic-layer
  - metric-governance
  - business-analytics
updated: "2026-09-24"
related_prompts:
  - domain-data-analytics/framing-and-metrics/analytics_kpi_tree_decomposition.md
  - domain-data-analytics/analysis-and-sql/analytics_sql_query_correctness_review.md
  - domain-product-management/prompts/product_north_star_metric_definition.md
---

# Metric Definition Spec

**Objective:** Produce a spec for one metric that is precise enough that two analysts,
working separately from the same tables, compute the same number — and that says
who decides when they don't.

**When to Use:**
- Two dashboards show different values for what everyone calls the same metric.
- A metric is about to go into a board pack, an OKR, or a compensation plan.
- You are migrating a metric into a semantic layer or dbt metric and need the logic
  written down before the code.
- A new analyst asked "which active-user number is the real one?"

**When NOT to use:**
- You are choosing *which* metric should be the product's north star —
  `domain-product-management/prompts/product_north_star_metric_definition.md` picks the
  metric; this prompt specifies it once picked.
- You need a finance KPI pack with GAAP/non-GAAP treatment and budget variance —
  `domain-finance/accounting-controllership/finance_management_reporting_kpi_pack.md`.
- You are choosing an ML evaluation metric — `domain-AI-ML/model-evaluation-validation/mleval_metric_selection_guide.md`.
- You need event instrumentation — `domain-agentic-resources/skills/marketing/analytics-tracking/`.

## Inputs / Context

1. **The metric name as people currently say it**, and every variant in use.
2. **What decision or report it feeds.**
3. **Source tables** and their grain (one row per what?).
4. **Any existing SQL or dashboard logic** for it, including conflicting versions.
5. **Known incidents** — times the number was wrong or disputed.

## Method

1. **Fix the grain first (DS-02).** State what one unit of the metric is: per user-day,
   per account-month, per order. Mixing grains between numerator and denominator is
   the most common source of silent error.

2. **Write numerator and denominator in words, then in logic.** Each gets:
   - a plain-English sentence a stakeholder can check;
   - SQL-shaped pseudo-logic naming tables, join keys, and aggregation;
   - its own filters. A ratio whose numerator and denominator apply different
     filters must say so explicitly and justify it.

3. **Pin the constraints (CM-02).**
   - **Inclusions and exclusions**: test accounts, internal users, bots, refunds,
     free vs paid, deleted records.
   - **Time window**: calendar vs rolling, inclusive/exclusive boundaries, and the
     **time zone** the day boundary uses.
   - **Attribution date**: which timestamp assigns an event to a period (created,
     paid, shipped, recognised).
   - **Late-arriving data**: when the number is considered final, and whether past
     periods restate.

4. **Enumerate edge cases with worked examples (MP-04).** For each, state the input
   and what the metric does:
   - a user active in two time zones on the same UTC day;
   - an order refunded in a later period;
   - an account that downgrades mid-month;
   - a record with a null in the join key;
   - a zero denominator — report as null, zero, or excluded?

5. **List how it can be gamed (QA-21).** Name at least three ways the number could
   rise without the underlying outcome improving (redefining "active", cleaning the
   denominator, shifting dates), and a counter-metric that would expose each.

6. **Assign ownership.** One named owner who decides disputes, a change process, and a
   version history. A spec without an owner drifts back into three definitions.

7. **Reconcile against what exists.** Compute the new spec alongside each existing
   version for one recent period and explain every difference above 1%.

## Output Format

```
# Metric spec — [name]   v[n]   Owner: [role/name]   Status: [draft | approved]

## Definition (one sentence)
## Grain
## Numerator — words / logic / filters
## Denominator — words / logic / filters
## Window, time zone, attribution date, finality
## Inclusions / exclusions
## Edge cases
| Case | Input | Metric behaviour |
|---|---|---|
## Gaming vectors and counter-metrics
| Vector | How the number rises | Counter-metric |
|---|---|---|
## Reconciliation against existing versions
| Version | Value (period) | Diff vs spec | Explained by |
|---|---|---|---|
## Change log
```

## Verification

- [ ] Numerator and denominator are at the same grain, or the difference is explained.
- [ ] The day boundary names a time zone.
- [ ] The attribution date and the finality rule are stated.
- [ ] At least five edge cases, each with a stated behaviour.
- [ ] The zero-denominator case is decided.
- [ ] At least three gaming vectors, each with a counter-metric.
- [ ] Every existing version has been reconciled, or listed as unreconciled.
- [ ] One named owner.

## False-Positive Prevention

1. **A formula is not a spec.** "Active users ÷ total users" leaves grain, window,
   time zone, and exclusions to whoever writes the SQL — which is how you got three
   versions.
2. **Silent filter asymmetry.** Excluding test accounts from the numerator but not
   the denominator makes the rate look worse and nobody notices. Write filters for
   each side separately.
3. **UTC by default is still a choice.** A UTC day boundary splits a US evening into
   two days. State it on purpose.
4. **"Final" is not "loaded".** Revenue metrics that restate after refunds must say
   when a period closes, or month-over-month comparisons mix final and provisional numbers.
5. **Reconciling by rounding.** A 3% gap between versions is not a rounding issue.
   Trace it to a filter, a join, or a date before calling the spec done.
6. **Picking the owner by committee.** "Data team" is not an owner. Name the person
   who breaks ties.
7. **Presenting the reconciled value as measured when a source was estimated.** If
   any input was backfilled or imputed, mark it `[estimated]` in the reconciliation.

## Example Output

```
# Metric spec — Weekly Active Accounts (WAA)   v2   Owner: Head of Analytics   Status: draft

## Definition
Share of paying accounts with ≥1 qualifying action by any seat in a Mon–Sun week (America/New_York).

## Grain
Account-week.

## Numerator
Words: paying accounts where at least one non-internal seat performed a qualifying action
(create, edit, share — not login or view) during the week.
Logic:
  SELECT DISTINCT a.account_id, DATE_TRUNC('week', e.event_ts AT TIME ZONE 'America/New_York') AS wk
  FROM fct_events e JOIN dim_seat s ON e.seat_id = s.seat_id
  JOIN dim_account a ON s.account_id = a.account_id
  WHERE e.event_name IN ('doc_create','doc_edit','doc_share')
    AND s.is_internal = FALSE AND a.is_test = FALSE
Filters: same as denominator, plus qualifying event list.

## Denominator
Words: accounts with an active paid contract on the Monday of the week.
Logic: dim_contract where start_date <= wk AND (end_date IS NULL OR end_date > wk), is_test = FALSE.

## Window, time zone, attribution date, finality
Mon–Sun, America/New_York; attributed by event_ts; final 3 days after week end (late events).

## Inclusions / exclusions
Excludes test accounts, internal seats, and accounts in a trial. Includes accounts in dunning.

## Edge cases
| Case | Input | Metric behaviour |
|---|---|---|
| Contract starts Wednesday | New account | Not in denominator that week; counts next week |
| Only logins, no edits | Seat logs in daily | Not active |
| Seat moved between accounts | Mid-week transfer | Credits account at event time |
| Null seat_id on event | 0.4% of events [measure] | Dropped; tracked as DQ metric |
| Zero paying accounts in segment | Small region | Report null, not 0% |

## Gaming vectors and counter-metrics
| Vector | How the number rises | Counter-metric |
|---|---|---|
| Add 'view' to qualifying events | Passive visits count | Median actions per active account |
| Auto-share on doc create | One action becomes two | Share-to-create ratio |
| Churn inactive accounts early | Denominator shrinks | Gross revenue retention |

## Reconciliation (week of 2026-09-14)
| Version | Value | Diff vs spec | Explained by |
|---|---|---|---|
| Exec dashboard | 71.2% | +6.1 pts | counts logins as active |
| CS health score | 63.8% | −1.3 pts | UTC week boundary |
| Spec v2 | 65.1% | — | — |

## Change log
v1 (2025-11): login-based. v2 (2026-09-24): action-based, NY time zone — pending owner approval.
```

## Techniques Used

- **DS-02 Metric Specification** — grain, numerator, and denominator defined measurably.
- **CM-02 Constraint Specification** — filters, window, time zone, and finality stated as constraints.
- **MP-04 Strategic Edge Case Calibration** — edge cases carry concrete inputs and behaviours.
- **QA-21 Metric Gaming Vector Enumeration** — ways the number can rise without the outcome improving, each with a counter-metric.
- **OC-03 Markdown Table Specification** — edge cases, gaming, and reconciliation in fixed tables.

## Related Prompts

- `domain-data-analytics/framing-and-metrics/analytics_kpi_tree_decomposition.md` — place the metric in its driver tree.
- `domain-data-analytics/analysis-and-sql/analytics_sql_query_correctness_review.md` — review the SQL that implements the spec.
- `domain-product-management/prompts/product_north_star_metric_definition.md` — choosing which metric matters.
