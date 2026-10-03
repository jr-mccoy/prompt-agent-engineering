---
title: "Analytics Data Dictionary Writer — Table Grain, Column Meaning in Business Terms, Known Gotchas, and the Metrics Each Table Feeds"
category: data-analytics/framing-and-metrics
description: "Write analyst-facing documentation for warehouse tables and the business metrics built on them: one table card stating grain, primary key, refresh, and source system; one row per column with its business meaning, allowed values marked closed or open, null meaning, and known traps; join paths; and the metrics each table feeds — with every definition the writer could not confirm marked for the owner rather than invented."
techniques:
  - OC-03
  - IPC-12
  - QA-26
  - DS-02
difficulty: intermediate
tags:
  - data-dictionary
  - data-documentation
  - data-warehouse
  - table-grain
  - business-glossary
  - analytics-engineering
  - what-does-this-column-mean
  - document-our-tables
  - new-analyst-onboarding
updated: "2026-10-02"
related_prompts:
  - domain-data-analytics/framing-and-metrics/analytics_metric_definition_spec.md
  - domain-science/computational/science_data_dictionary_designer.md
  - domain-agentic-resources/skills/data-engineering/dbt-transformation-patterns/SKILL.md
---

# Analytics Data Dictionary Writer

**Objective:** Produce documentation that lets an analyst who has never seen a table
query it correctly the first time — what one row is, what each column means in the
business's words, which values are possible, what a null means, how it joins, and
which traps have burned people before.

**When to Use:**
- New analysts keep asking the same questions about the same tables.
- Two people query the same table and get different answers because they read a
  column differently (`status`, `created_at`, `amount`).
- A warehouse migration, new source system, or reorganisation of models needs the
  meaning carried across.
- You are preparing tables for self-serve use by non-analysts.

**When NOT to use:**
- You are documenting a **research dataset** variable by variable for deposit or
  sharing (units, missingness codes, instruments, FAIR) —
  `domain-science/computational/science_data_dictionary_designer.md`. This prompt is
  for business warehouse tables and the metrics on them.
- You need the definition of **one metric** settled (numerator, denominator, edge
  cases, owner) — `domain-data-analytics/framing-and-metrics/analytics_metric_definition_spec.md`.
  This prompt links each table to its metric specs; it does not replace them.
- You want the dbt YAML syntax, tests, and `docs generate` mechanics —
  `domain-agentic-resources/skills/data-engineering/dbt-transformation-patterns/SKILL.md`.
  The content written here can be pasted into dbt `description:` fields.

## Inputs / Context

1. **Schema**: table names, column names and types (`information_schema` export or
   DDL).
2. **Sample rows** (10–50, de-identified) and simple profiles: row count, distinct
   counts, null rates, min/max for key columns. Profiles are `queried`; anything else
   is `assumed` until confirmed.
3. **Lineage**: the source system and the transformation (dbt model SQL, ETL job)
   for each table.
4. **Existing fragments**: old wiki pages, Slack answers, comments in SQL.
5. **Owners** to confirm meanings: the data engineer for mechanics, the business
   owner for meaning.
6. **Metric specs** that use these tables, if any exist.

## Method

1. **Table card first.** For each table: purpose in one sentence; **grain** ("one row
   per order line per day of status change", not "orders"); primary key, verified by
   a uniqueness check; refresh schedule and latency; source system; owner; whether it
   is a source, staging, or reporting table and which to use.
2. **Column rows (OC-03).** For each column: name, type, business meaning in plain
   words, example value, null meaning (unknown vs. not applicable vs. not yet
   happened), and the source field it came from.
3. **Allowed values with exhaustiveness flags (IPC-12).** For coded columns, list the
   observed values with counts and mark the list **closed** (the system cannot
   produce others) or **open** (new values can appear — handle the default). This
   is what tells an analyst whether `CASE WHEN status IN (...)` is safe.
4. **Time columns explicitly.** For every timestamp: what event it records, time zone,
   whether it can change after the fact (updated in place vs. append-only), and which
   one to use for which question (`ordered_at` vs. `paid_at` vs. `shipped_at`).
5. **Known traps.** Fan-out joins, soft deletes, test accounts, backfilled history,
   currency mixing, columns whose meaning changed on a date. Each trap with the date
   or condition and the safe query pattern.
6. **Join paths and metrics (DS-02).** How the table joins to others (key, cardinality)
   and which governed metrics are computed from it, linked to their specs.
7. **Mark what you could not confirm (QA-26).** The first column meaning you would
   have to guess is a gap: write `[verify — owner]` and the specific question, never a
   plausible definition. Report the count of verified vs. unverified columns.

## Output Format

```
# Data dictionary — [schema / domain]   Version: [..]   Verified with: [owners, date]

## Table: [name]
Purpose: [..]
Grain: one row per [..]   Primary key: [..] (uniqueness checked [date])
Layer: [source | staging | reporting] — use for: [..]   Refresh: [..]   Latency: [..]
Source: [system]   Owner: [mechanics] / [meaning]

### Columns
| Column | Type | Business meaning | Example | Null means | Source field | Status |

### Allowed values
| Column | Values (count) | Closed / open | Default handling |

### Time columns
| Column | Event | Time zone | Mutable? | Use for |

### Known traps
| Trap | Condition / since | Safe pattern |

### Joins and metrics
| Joins to | On | Cardinality |   Metrics fed: [links to specs]

## Coverage
Columns verified: [n] / [N]   Open questions: [list with owner]
```

## Verification

- [ ] Every table states grain as "one row per …" and the key was checked for uniqueness.
- [ ] Every column has a business meaning or an explicit `[verify — owner]`.
- [ ] Every coded column's value list is marked closed or open.
- [ ] Every timestamp has event, time zone, and mutability.
- [ ] Traps include the date or condition they apply from.
- [ ] Profiles are labelled queried; meanings not confirmed by an owner are labelled.
- [ ] Coverage count is reported.

## False-Positive Prevention

1. **Restating the column name.** "`customer_status`: the status of the customer"
   documents nothing. Say what each value means and when it changes.
2. **Inventing plausible meanings.** A confident wrong definition is worse than a
   gap. Unconfirmed is `[verify]`.
3. **Grain from the table name.** `orders` is often one row per order *line* or per
   status change. Check the key.
4. **Observed values as the full set.** A value not in this month's sample can still
   appear. Mark lists open unless the source system constrains them.
5. **Documenting staging tables for end users.** Point users to the reporting layer
   and mark staging tables "internal".
6. **A dictionary with no owner.** Without a named owner and a review date, it goes
   stale within a quarter.

## Example Output

```
# Data dictionary — Commerce reporting schema   v1.0   Verified with: D. Ruiz (DE), A. Shah (Finance), 2026-10-01

## Table: rpt_order_lines
Purpose: Line-level sales for revenue, units, and product mix reporting.
Grain: one row per order line (order_id + line_number). Primary key: order_line_id
(uniqueness checked 2026-09-30: 4,812,330 rows, 4,812,330 distinct).
Layer: reporting — use this, not stg_shop_orders. Refresh: hourly at :15. Latency ~40 min.
Source: Shopify via Fivetran → dbt. Owner: D. Ruiz / A. Shah.

### Columns (excerpt)
| order_line_id | string | surrogate key for a line | ol_88213_2 | never null | dbt-generated | verified |
| ordered_at    | timestamp | when the customer placed the order | 2026-09-14 18:02:11 | never null | created_at | verified |
| net_amount    | numeric(12,2) | line price after line discounts, before tax and shipping, in order currency | 42.50 | never null | computed | verified |
| refund_amount | numeric(12,2) | refunded on this line to date | 0.00 | null = no refund record (treat as 0) | refunds.amount | verified |
| fulfillment_status | string | warehouse status of the line | shipped | null = not yet sent to warehouse | fulfillments.status | verified |
| channel       | string | sales channel | web | null before 2025-03-01 | source_name | [verify — A. Shah: are 'pos' lines in revenue?] |

### Allowed values
| fulfillment_status | unfulfilled 41,220; partial 3,105; shipped 4,701,880; cancelled 66,125 | open (Shopify adds statuses) | ELSE → 'other', alert |
| channel | web 3.9M; app 0.7M; pos 0.2M | open | ELSE → 'other' |

### Time columns
| ordered_at   | order placed  | UTC | immutable | revenue by order date |
| refunded_at  | latest refund | UTC | updated in place | refunds by refund date |

### Known traps
| Currency mixing | multi-currency since 2026-04-01 | sum net_amount_usd, not net_amount |
| Test orders     | email ends @ourco.com            | filter is_test = false (exposed column) |
| Join fan-out    | joining rpt_shipments on order_id | join on order_line_id |

### Joins and metrics
| dim_product | product_id | many-to-one |  | rpt_orders | order_id | many-to-one |
Metrics fed: Net revenue (spec: metrics/net_revenue.md), Units sold, AOV.

## Coverage
Columns verified: 23 / 24. Open: channel 'pos' revenue treatment — A. Shah, due 10-08.
```

## Techniques Used

- **OC-03 Markdown Table Specification** — fixed table card and column table shapes.
- **IPC-12 Exhaustiveness Flags on Enumerations** — every value list marked closed or open with default handling.
- **QA-26 First-Invented-Fact Test** — any meaning that would have to be guessed becomes a `[verify]` gap with an owner.
- **DS-02 Metric Specification** — each table linked to the governed metrics it feeds.

## Related Prompts

- `domain-data-analytics/framing-and-metrics/analytics_metric_definition_spec.md` — the spec for each metric the tables feed.
- `domain-science/computational/science_data_dictionary_designer.md` — variable-level codebooks for research datasets.
- `domain-agentic-resources/skills/data-engineering/dbt-transformation-patterns/SKILL.md` — putting these descriptions into dbt YAML and tests.
