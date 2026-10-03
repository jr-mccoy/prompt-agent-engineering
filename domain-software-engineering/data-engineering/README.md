# Data Engineering

Prompts for judging the design and operation of data pipelines and warehouses — whether a
pipeline survives retries and reruns, whether a dimensional model gives one right answer,
where data quality checks belong and who owns them, how to load incrementally and backfill
safely, and how to run a data incident from first report to postmortem.

The object of every prompt here is a **data system** (pipeline, table, model, load job).
That is why they live in `domain-software-engineering/`.

## Prompts

| Prompt | Use When |
|--------|----------|
| [`dataeng_pipeline_design_review.md`](dataeng_pipeline_design_review.md) | Review a batch or streaming pipeline for idempotency, safe retries, backfill-ability, late data, and whether an "exactly-once" claim holds at the sink. |
| [`dataeng_dimensional_model_review.md`](dataeng_dimensional_model_review.md) | Review a star schema or mart for declared and enforced grain, measure additivity, SCD types matched to reporting needs, conformed dimensions, and fan-out joins. |
| [`dataeng_data_quality_test_strategy.md`](dataeng_data_quality_test_strategy.md) | Decide which checks run at ingestion, staging, and marts; which block publication vs warn; who owns each alert; and how to prune a noisy suite. |
| [`dataeng_incremental_load_backfill_plan.md`](dataeng_incremental_load_backfill_plan.md) | Choose a change-capture method (key, watermark, CDC, snapshot diff) and plan a chunked, rate-limited, verified, reversible backfill. |
| [`dataeng_data_downtime_postmortem.md`](dataeng_data_downtime_postmortem.md) | Contain bad or late data, map its blast radius through lineage, repair and notify consumers, then write a postmortem that measures time-to-detect. |

## Typical Sequence

1. Designing or inheriting a pipeline → `dataeng_pipeline_design_review.md`.
2. Publishing a mart to analysts → `dataeng_dimensional_model_review.md`.
3. Before anyone relies on it → `dataeng_data_quality_test_strategy.md`.
4. Moving off full reloads, or fixing history → `dataeng_incremental_load_backfill_plan.md`.
5. When something gets through → `dataeng_data_downtime_postmortem.md`, whose detection
   gaps feed back into step 3.

## Boundaries — What Lives Elsewhere

**Prompts here = design and review judgement. Skills = tool how-to.** These prompts decide
*what* a correct pipeline, model, or test suite looks like and *why*; they do not teach a
tool's syntax. For implementation in a specific tool, use:

| Need | Go to |
|------|-------|
| Airflow DAG structure, operators, sensors | `../../domain-agentic-resources/skills/data-engineering/airflow-dag-patterns/` |
| dbt models, incremental materialisations, snapshots | `../../domain-agentic-resources/skills/data-engineering/dbt-transformation-patterns/` |
| Great Expectations / dbt test syntax, contract tooling | `../../domain-agentic-resources/skills/data-engineering/data-quality-frameworks/` |
| Spark partitioning, shuffle, memory tuning | `../../domain-agentic-resources/skills/data-engineering/spark-optimization/` |
| An agent that builds pipelines end to end | `../../domain-agentic-resources/agents/backend/data_engineer.md` |
| Generating a new pipeline architecture and code | `../../domain-agentic-resources/commands/architecture/data_pipeline.md` |

Other neighbours:

- **Data feeding ML models** — data contracts, schema evolution, contract enforcement in CI,
  train/serve skew: `../../domain-AI-ML/data-for-ml/` and `../../domain-AI-ML/production-monitoring/`.
  `dataeng_data_quality_test_strategy.md` places checks across a warehouse; the contract
  itself is designed with `../../domain-AI-ML/data-for-ml/mldata_data_contract_design.md`.
- **Analysis on top of the warehouse** — whether a query returns the right number, why a
  metric moved, dashboard critique: `../../domain-data-analytics/`.
- **Application (OLTP) databases** — normalisation, indexing, production schema migration:
  `../analysis/database/`.
- **General service-outage postmortems** — `../../domain-engineering-workflows/workflows/engineering_postmortem_blueprint.md`.

## Related Resources

- [Software Engineering Domain](../README.md) - Full domain index
- [Database Analysis](../analysis/database/README.md) - Application database prompts
- [Cloud](../cloud/README.md) - Including FinOps for warehouse and pipeline spend
