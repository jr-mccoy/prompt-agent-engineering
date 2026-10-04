---
title: "Dimensional Model Review — Declared Grain, Fact Types, Slowly Changing Dimensions, Conformed Dimensions, and the Joins That Double-Count"
category: software-engineering/data-engineering
description: "Review a warehouse dimensional model (star schema or wide marts built from one) before analysts build on it: is each fact table's grain declared and enforced, are measures typed as additive, semi-additive or non-additive, does each dimension attribute use the right slowly-changing-dimension type for how history must be reported, are shared dimensions conformed across facts, and which joins fan out or drop rows — each finding backed by a check query."
techniques:
  - DT-05
  - QA-18
  - IPC-04
  - RT-05
difficulty: advanced
tags:
  - dimensional-modeling
  - star-schema
  - fact-table-grain
  - slowly-changing-dimensions
  - conformed-dimensions
  - data-warehouse
  - reports-disagree-on-totals
  - double-counted-numbers
  - history-changed-in-old-reports
updated: "2026-10-03"
related_prompts:
  - domain-data-analytics/analysis-and-sql/analytics_sql_query_correctness_review.md
  - domain-software-engineering/analysis/database/database_data_modeling_review.md
  - domain-software-engineering/data-engineering/dataeng_data_quality_test_strategy.md
---

# Dimensional Model Review

**Objective:** Determine whether a warehouse model will give every analyst the same, correct
answer to the same question — and where it will not, show the query that proves it and the
modelling change that fixes it.

**When to Use:**
- A new mart or star schema is about to be published to BI users.
- Two dashboards report different totals for "the same" metric from the same warehouse.
- Last year's numbers changed after a customer moved region or a product was re-categorised.
- Several teams built their own `dim_customer` and you are deciding which is canonical.
- **Not this prompt if** the model is an application (OLTP) schema — normalisation and
  integrity are `domain-software-engineering/analysis/database/database_schema_design_normalization.md`
  and `domain-software-engineering/analysis/database/database_data_modeling_review.md`. If one analysis query returns a wrong number on a
  sound model, use `domain-data-analytics/analysis-and-sql/analytics_sql_query_correctness_review.md`.
  For how to *build* models in dbt (materialisations, snapshots syntax), use
  `domain-agentic-resources/skills/data-engineering/dbt-transformation-patterns/`.

## Inputs / Context

1. **Model DDL or dbt models** for facts and dimensions, with keys.
2. **Business processes** the facts represent (orders, shipments, subscriptions, sessions).
3. **Reporting requirements for history**: "report revenue by the customer's region *at the
   time of sale*" vs "*as of today*" — per attribute that changes.
4. **Row counts** of each table and of the source systems of record for reconciliation.
5. **Known disputes**: metrics that disagree, and the queries behind each version.

## Method

1. **Fact-by-fact matrix (DT-05).** For each fact table record: business process; declared
   grain in one sentence ("one row per order line per shipment"); fact type (transaction,
   periodic snapshot, accumulating snapshot, factless); dimension keys; measures with
   additivity — additive (sum across all dimensions), semi-additive (balances: sum across
   accounts, not across time), non-additive (ratios, distinct counts: store numerator and
   denominator instead).
2. **Enforce grain with checks (QA-18).** Run a uniqueness query on the declared grain
   columns: `select grain_cols, count(*) from fact group by grain_cols having count(*) > 1`.
   Any rows returned mean the grain sentence is false. Mixed grain (order header totals and
   line items in one table) is the most common double-count source.
3. **Reconcile counts and sums (IPC-04).** Fact row count and a control total (e.g. sum of
   net amount) against the source of record for a closed period; a model that loses or
   gains 0.3% of rows silently is a correctness finding, not rounding.
4. **Dimension history review.** For each changing attribute, match the SCD type to the
   reporting requirement: Type 0 (never changes), Type 1 (overwrite — history restated),
   Type 2 (new row with effective dates and current flag — history preserved), Type 3
   (prior-value column — one level of history), mixed/Type 6 where both "as was" and "as is"
   are needed. Check Type 2 integrity: no overlapping effective ranges per natural key,
   exactly one current row, facts join on the surrogate key valid at the event time.
5. **Conformance across facts.** Shared dimensions (date, customer, product) must have one
   definition and key so drill-across works; build or check a bus matrix (processes ×
   dimensions). Two `dim_customer` tables with different de-duplication rules will never
   reconcile.
6. **Join behaviour.** Fact → dimension joins must be many-to-one; test each for fan-out
   (row count after join = before) and orphans (facts with no matching dimension → map to
   an explicit "unknown" member, key −1, not dropped by an inner join). Late-arriving
   dimensions need an inferred-member pattern.
7. **Evidence for each finding (RT-05).** Every finding cites the check query and its
   result; opinions on naming style are kept separate and low priority.

## Output Format

```
# Dimensional model review — [mart/schema], [date]

## Fact matrix
| Fact | Process | Declared grain | Type | Grain check | Measures (additivity) | Reconciles to source? |

## Dimension history
| Dimension.attribute | Changes how often | Reporting need (as-was / as-is / both) | Current SCD | Correct SCD | Type 2 integrity |

## Bus matrix (conformance)
| Process \ Dimension | Date | Customer | Product | ... |

## Join checks
| Fact → Dimension | Fan-out? | Orphans (n, %) | Unknown member? |

## Findings
| # | Severity | Finding | Evidence (query + result) | Fix |

## Style notes (non-blocking)
```

## Verification

- [ ] Every fact has a one-sentence grain and a uniqueness check result.
- [ ] Every measure is labelled with its additivity.
- [ ] SCD type is justified by a stated reporting requirement, not by habit.
- [ ] Type 2 dimensions are checked for overlaps and single current rows.
- [ ] Every fact→dimension join is tested for fan-out and orphans.
- [ ] At least one closed period reconciles to the source of record, or the gap is quantified.

## False-Positive Prevention

1. **Type 2 everywhere.** Type 2 on attributes nobody reports historically adds joins and
   storage for no reader; Type 1 is correct when restating history is the requirement.
2. **Denormalised = wrong.** A wide one-big-table mart can be sound if built from a sound
   star with a single declared grain; judge grain and additivity, not shape.
3. **Snowflaking flagged as a defect.** Normalised dimension hierarchies are a performance
   and usability trade-off, not a correctness bug.
4. **Small reconciliation gaps waved through.** 0.3% fewer rows can be all orders from one
   channel; find which rows before calling it noise.
5. **Distinct counts summed.** Unique customers per day do not add to unique customers per
   month; that is a modelling finding (non-additive measure exposed as additive).
6. **Naming preferences ranked with correctness.** Keep `dim_`/`fct_` style comments
   separate from grain and history findings.

## Example Output

```
# Dimensional model review — analytics.sales mart, 2026-09-29

## Fact matrix
| fct_orders       | order placement | "one row per order" | transaction | FAIL: 4,212 order_ids with 2–6 rows | net_amount (additive), discount_pct (non-additive!) | −0.0% rows, +3.1% net_amount |
| fct_order_lines  | order placement | one row per order line | transaction | pass | qty, net_amount (additive) | ✓ |
| fct_inventory_daily | stock position | one row per sku per warehouse per day | periodic snapshot | pass | on_hand (semi-additive) | ✓ |

## Dimension history
| dim_customer.region   | ~2%/yr move | as-was for revenue reporting | Type 1 | Type 2 | n/a |
| dim_customer.email    | frequent    | as-is only                   | Type 2 | Type 1 | 31k rows of churn for no reader |
| dim_product.category  | yearly re-cat | both (finance as-was, merch as-is) | Type 1 | Type 6 (Type 2 + current_category) | — |

## Join checks
| fct_order_lines → dim_product | none | 1,904 (0.06%) dropped by inner join | no unknown member |
| fct_orders → dim_promotion    | FAN-OUT ×1.08 (orders with 2 promos) | — | — |

## Findings
1 High  fct_orders is mixed grain: split-shipment orders repeat header net_amount per shipment
        → +3.1% revenue. Fix: declare grain = order; move shipments to fct_shipments.
2 High  Promotion join fans out; revenue by promotion overstated. Fix: bridge table with
        allocation weight, or grain = order × promotion with allocated amount.
3 High  Region restated on customer move; Q1 EMEA revenue fell 4% in reports run in Sept.
        Fix: Type 2 on region; fact joins customer_sk valid at order_ts.
4 Med   discount_pct summed in BI. Fix: store discount_amount and gross_amount; compute ratio.
5 Med   Orphan product keys dropped. Fix: unknown member −1, inferred members for late SKUs.

## Style notes: mixed `dim_`/`d_` prefixes (non-blocking).
```

## Techniques Used

- **DT-05 Element-by-Element Assessment Matrix** — every fact and changing attribute assessed on the same columns.
- **QA-18 Domain-Specific Smell Tests** — grain uniqueness, fan-out, orphan, and Type 2 overlap checks.
- **IPC-04 Count-and-Sequence Checksums** — row counts and control totals reconciled to the source of record.
- **RT-05 Evidence-Based Reasoning** — each finding carries its check query and result.

## Related Prompts

- `domain-data-analytics/analysis-and-sql/analytics_sql_query_correctness_review.md` — reviewing a single analysis query once the model is sound.
- `domain-software-engineering/analysis/database/database_data_modeling_review.md` — application data models rather than warehouse marts.
- `dataeng_data_quality_test_strategy.md` — turning the grain, orphan, and reconciliation checks into owned, alerting tests.
