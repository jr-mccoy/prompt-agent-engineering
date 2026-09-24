# Expansion Roadmap — `domain-data-analytics/`

**Status as of 2026-09-24:** Wave 1 shipped (coverage roadmap). Eight prompts in
three subdirectories, created to fill the business-analytics gap recorded in
[`meta/COVERAGE_ROADMAP.md`](../meta/COVERAGE_ROADMAP.md). Before this domain existed,
the work was split across ML evaluation, finance, and board-deck rendering.

**Filing convention:** `analytics_{specific_function}.md`, one prefix across all
subdirectories.

**Scope discipline.** The domain's object is a business metric, analysis query,
dashboard, or experiment readout. Anything whose object is a model (`domain-AI-ML/`),
research inference (`domain-science/statistics/`), a rendered slide
(`domain-presentations/board-decks/`), or a data pipeline, query performance or
tracking setup (`domain-agentic-resources/skills/`) stays where it is. The
authoritative list is the **Not here** table in `README.md`.

---

## Shipped — Wave 1

```
domain-data-analytics/                       8 prompts
├── framing-and-metrics/        3   plan, metric spec, KPI tree
├── analysis-and-sql/           3   query correctness, movement investigation, cohort retention
└── experiments-and-reporting/  2   A/B test readout, dashboard critique
```

## Wave 2 candidates (not built)

| Candidate | Subdirectory | Scope note |
|---|---|---|
| `analytics_spreadsheet_model_audit.md` | `analysis-and-sql/` | Formula errors, hard-codes, broken ranges, circularity in an operating spreadsheet. Distinct from finance model review in `domain-finance/`: this is about the mechanics of the sheet, not the valuation. |
| `analytics_request_intake_triage.md` | `framing-and-metrics/` | Triage a queue of analysis requests by decision value and effort, before any one gets a plan. Sits upstream of `analytics_question_to_analysis_plan.md`. |
| `analytics_data_dictionary_writer.md` | `framing-and-metrics/` | Table- and column-level documentation for analysts. Must not duplicate dbt docs patterns in `skills/data-engineering/dbt-transformation-patterns/`. |
| `analytics_business_forecast_for_planners.md` | `experiments-and-reporting/` | Simple, explainable forecasts for business planning (seasonal baseline, driver-based). Distinct from `domain-AI-ML/specialized-ml/time-series/` model design. |

Each candidate needs a duplicate sweep (`pae search`) before it is built.
