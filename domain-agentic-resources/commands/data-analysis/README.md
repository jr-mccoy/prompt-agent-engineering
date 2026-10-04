# Data Analysis Commands

> Quick operational commands for checking data and numbers before they are used. They run checks and report evidence; interpretation, metric definitions, and full query reviews live in `domain-data-analytics/`.

## Commands

| Command | Syntax | Description |
|---------|--------|-------------|
| [dataset_profile.md](./dataset_profile.md) | `/dataset_profile` | Profile one tabular dataset: shape, types, nulls vs empty strings vs sentinels, distinct counts, candidate keys, duplicates, ranges, date coverage; PII masked; ends in flags and owner questions |
| [metric_sanity_check.md](./metric_sanity_check.md) | `/metric_sanity_check` | Pre-publish smoke test for one computed metric: definition, grain, join fan-out, nulls, totals reconciliation, time window, ratio bounds, step change; PASS / WARN / FAIL with diagnostics |
| [process_financials.md](./process_financials.md) | `/process_financials` | Full financial-records pipeline over bank/credit-card statements: extract, verify, categorize, flag for attorney review |

## Routing

| If you need to… | Use |
|-----------------|-----|
| See what is actually in an unfamiliar file or table | `/dataset_profile` |
| Check a number before it goes in a deck or dashboard | `/metric_sanity_check` |
| Write the definition two analysts will compute the same way | `domain-data-analytics/framing-and-metrics/analytics_metric_definition_spec.md` |
| Fully review a query for correctness | `domain-data-analytics/analysis-and-sql/analytics_sql_query_correctness_review.md` |
| Validate an ML training dataset | `skills/ml-ai/dataset-validation/` |

## Usage

These commands are invoked using slash syntax: `/command-name [arguments]`

## Related Resources

- [Commands Index](../README.md)
- [Agents Index](../../agents/README.md)
