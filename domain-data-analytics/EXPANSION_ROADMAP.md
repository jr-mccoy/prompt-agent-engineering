# Expansion Roadmap — `domain-data-analytics/`

**Status as of 2026-10-02:** Waves 1 and 2 shipped — twelve prompts in three
subdirectories. Wave 1 (eight prompts) was created to fill the business-analytics gap recorded in
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

## Shipped — Wave 2 (2026-10-02, coverage Wave 6)

```
domain-data-analytics/                       12 prompts
├── framing-and-metrics/        5   + request intake triage, data dictionary writer
├── analysis-and-sql/           4   + spreadsheet model audit
└── experiments-and-reporting/  3   + operational volume forecast for planners
```

| Candidate | Status | Boundary kept |
|---|---|---|
| `analysis-and-sql/analytics_spreadsheet_model_audit.md` | **Shipped** | Mechanics of any operating workbook; `domain-finance/valuation/finance_dcf_model_auditor.md` keeps valuation methodology and assumptions. |
| `framing-and-metrics/analytics_request_intake_triage.md` | **Shipped** | One triage pass over an analytics queue, upstream of `analytics_question_to_analysis_plan.md`; designing an intake system stays in `skills/non-coding/cross-domain/intake-triage-pattern/`. |
| `framing-and-metrics/analytics_data_dictionary_writer.md` | **Shipped** | Business warehouse tables and the metrics they feed; research codebooks stay in `domain-science/computational/science_data_dictionary_designer.md`, dbt YAML mechanics in `skills/data-engineering/dbt-transformation-patterns/`. |
| `experiments-and-reporting/analytics_business_forecast_for_planners.md` | **Shipped (narrowed scope)** | Narrowed to operational volume forecasts (orders, tickets, calls → staffing/stock) with baseline, seasonality, event lines, and error tracking. P&L forecasting stays in `domain-finance/corporate-finance-fpa/finance_rolling_forecast_designer.md`; model selection in `domain-AI-ML/specialized-ml/time-series/`. Duplicate sweep found no operational-volume prompt. |
