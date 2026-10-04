# Domain: Data Analytics

The working analyst's craft: turning a business question into an analysis, a metric
into a definition two people compute the same way, a query into a number you can
defend, and an experiment or dashboard into a decision. This is the domain for work
whose **object is a business metric, an analysis query, a dashboard, or an experiment
readout.**

Users are product, business, growth, and operations analysts, analytics engineers
answering stakeholder questions, and the managers who have to act on what those
analysts report.

> **Guard — measured vs inferred.** Every prompt here keeps three things apart: what
> was **queried**, what was **estimated** from queried facts, and what was **assumed**.
> Never present an inferred number (a projection, an imputed value, a share of a move
> worked out from an assumption) as a measured one. Tag it `[estimate]` or
> `[verify]`. State the uncertainty (an interval, a confidence level, an unexplained
> residual) rather than rounding it away. If a value is not in the data, use a
> `[measure]` placeholder rather than making one up.

---

## When to use this domain

- A stakeholder asked a vague question and you need a plan before writing SQL.
- A metric has more than one definition in use, or is about to go into a board pack.
- A number moved and someone wants to know why.
- A query feeds a decision and nobody has checked whether it double counts.
- An experiment finished and needs a ship / no-ship readout.
- A dashboard exists and nobody trusts or uses it.

## Subdirectory map

| Subdirectory | What it covers | Prompts |
|---|---|---|
| `framing-and-metrics/` | Before the query: request triage, the analysis plan, the metric spec, the driver tree, the data dictionary | 5 |
| `analysis-and-sql/` | Doing the analysis: query correctness, spreadsheet audit, metric-movement investigation, cohort retention | 4 |
| `experiments-and-reporting/` | Turning results into decisions: experiment readouts, dashboard critique, operational volume forecasts | 3 |

**File naming:** `analytics_{specific_function}.md`, one prefix across all subdirectories.

## Prompts in this domain

### `framing-and-metrics/`

| File | Purpose |
|---|---|
| `analytics_request_intake_triage.md` | Queue of inbound asks → real question and decision per ask, redirects and merges first, effort bands, anchored value score, ranked schedule, a reply to every requester |
| `analytics_question_to_analysis_plan.md` | Vague stakeholder ask → decision, answerable question, decision rule written before data, capped cut list, stop rule |
| `analytics_metric_definition_spec.md` | Grain, numerator/denominator, filters, window and time zone, edge cases, gaming vectors, owner, reconciliation |
| `analytics_kpi_tree_decomposition.md` | Outcome → additive/multiplicative driver tree that reconciles, log-decomposed attribution, dominant driver |
| `analytics_data_dictionary_writer.md` | Warehouse table cards (grain, key, layer, refresh), column meaning in business terms, value lists flagged closed/open, time columns, known traps, joins, metrics fed; unconfirmed = `[verify]` |

### `analysis-and-sql/`

| File | Purpose |
|---|---|
| `analytics_sql_query_correctness_review.md` | Does the query return the right number? Grain, fan-out, nulls, time zones, dedup, survivorship, each proved by a diagnostic |
| `analytics_spreadsheet_model_audit.md` | Any operating workbook: model map, inconsistent formulas, hard-codes, short ranges, lookup and unit errors, links and circularity, independent reproduction, severity vs. tolerance |
| `analytics_metric_movement_investigation.md` | "Why did X drop?" in fixed order: noise, data, calendar, mix vs rate, segments, events; residual stated |
| `analytics_cohort_retention_analysis.md` | Cohort key, return event, clock; triangle with censoring; read down columns, rows, diagonals; mix check |

### `experiments-and-reporting/`

| File | Purpose |
|---|---|
| `analytics_ab_test_readout.md` | Gated readout: SRM, integrity, primary with CI vs MDE, guardrail margins, novelty, multiplicity, decision memo |
| `analytics_dashboard_critique.md` | Tile-by-tile: question, definition, trust, form, context; Keep/Fix/Merge/Cut; ranked change list |
| `analytics_business_forecast_for_planners.md` | Operational volumes (orders, tickets, calls): cleaned history, baseline and damped trend, seasonal indices, owned event lines, back-tested range, plan percentile, bias/WMAPE tracking |

## Routing within the domain

| If you need to… | Start with |
|---|---|
| Rank a pile of incoming data requests | `framing-and-metrics/analytics_request_intake_triage.md` |
| Scope a request before doing it | `framing-and-metrics/analytics_question_to_analysis_plan.md` |
| Document what tables and columns mean | `framing-and-metrics/analytics_data_dictionary_writer.md` |
| Settle "which number is right" | `framing-and-metrics/analytics_metric_definition_spec.md` |
| See which lever moves a top-line KPI | `framing-and-metrics/analytics_kpi_tree_decomposition.md` |
| Check a query before trusting its output | `analysis-and-sql/analytics_sql_query_correctness_review.md` |
| Check a spreadsheet before trusting its output | `analysis-and-sql/analytics_spreadsheet_model_audit.md` |
| Explain a metric that moved | `analysis-and-sql/analytics_metric_movement_investigation.md` (often after the KPI tree) |
| Tell whether retention is improving | `analysis-and-sql/analytics_cohort_retention_analysis.md` |
| Call a finished experiment | `experiments-and-reporting/analytics_ab_test_readout.md` |
| Fix a dashboard nobody trusts | `experiments-and-reporting/analytics_dashboard_critique.md` |
| Forecast orders, tickets, or calls for staffing | `experiments-and-reporting/analytics_business_forecast_for_planners.md` |

A typical chain: **triage → plan → spec → query review → analysis → readout or dashboard.**

## Not here (negative boundaries)

| If the work is… | It lives in |
|---|---|
| Research statistical inference: SAPs, test selection, survival models, meta-analysis | `domain-science/statistics/` |
| Models, datasets, ML evaluation, online model A/B tests | `domain-AI-ML/` (e.g. `model-evaluation-validation/mleval_ab_test_design_for_models.md`) |
| Rendering a chart or slide for a board deck | `domain-presentations/board-decks/` (e.g. `boarddeck_cohort_retention_heatmap.md`, `boarddeck_funnel_diagnostic.md`) |
| Designing a KPI dashboard from scratch | `domain-agentic-resources/skills/data-engineering/kpi-dashboard-design/` |
| Presenting findings as a narrative | `domain-agentic-resources/skills/data-engineering/data-storytelling/` |
| dbt models, data contracts, data-quality pipelines | `domain-agentic-resources/skills/data-engineering/dbt-transformation-patterns/`, `data-quality-frameworks/` |
| Query **performance**: indexes, EXPLAIN, slow queries | `domain-agentic-resources/skills/developer-tools/sql-optimization-patterns/` |
| Planning and sizing an A/B test before launch | `domain-agentic-resources/skills/marketing/ab-test-setup/` |
| Event tracking, GA4, tag manager, UTM setup | `domain-agentic-resources/skills/marketing/analytics-tracking/` |
| Choosing a product north-star metric | `domain-product-management/prompts/product_north_star_metric_definition.md` |
| Finance KPI packs, budget variance, unit economics | `domain-finance/` (`accounting-controllership/`, `corporate-finance-fpa/`) |
| DCF / valuation model methodology review | `domain-finance/valuation/finance_dcf_model_auditor.md` |
| P&L rolling forecast process; ML forecasting model choice | `domain-finance/corporate-finance-fpa/finance_rolling_forecast_designer.md`; `domain-AI-ML/specialized-ml/time-series/` |
| Research-dataset codebooks (variable-level, FAIR) | `domain-science/computational/science_data_dictionary_designer.md` |

## Related

- Coverage context: `../meta/COVERAGE_ROADMAP.md` (Wave 1, business analytics).
- Roadmap for this domain: `EXPANSION_ROADMAP.md`.
