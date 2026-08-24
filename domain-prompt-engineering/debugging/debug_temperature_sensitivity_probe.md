---
title: "Temperature Sensitivity Probe"
category: prompt-engineering/debugging
description: "Run a fixed prompt at temperatures 0.0, 0.3, 0.7, 1.0 to determine whether a failure is deterministic, variance-driven, or temperature-cliff."
techniques:
  - ST-02
  - QA-01
  - PR-01
  - DC-01
difficulty: beginner
tags:
  - temperature
  - sampling
  - variance
  - probe
  - debugging
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/debugging/debug_minimal_repro_isolator.md
  - domain-prompt-engineering/debugging/debug_input_perturbation_battery.md
  - domain-prompt-engineering/debugging/debug_failure_mode_taxonomy.md
---

## Objective

For a (prompt, input, failure_predicate) triple, run N samples at each of {0.0, 0.3, 0.7, 1.0} temperatures and emit a sensitivity profile that classifies the failure as `DETERMINISTIC`, `VARIANCE_DRIVEN`, `TEMPERATURE_CLIFF`, or `STOCHASTIC_OK`.

## When to Use

- Reported failures are intermittent.
- Choosing a production temperature.
- Before filing a model bug; rule out sampling noise.

## Inputs

- `PROMPT_TEXT`, `INPUT`.
- `FAILURE_PREDICATE`: boolean over output.
- `N`: samples per temperature (default 20).
- `TEMPERATURES`: default `[0.0, 0.3, 0.7, 1.0]`.
- `MODEL_ID`.

## Classification Rules (fixed)

Let `f(t)` = fraction of failing samples at temperature `t`.

| Class | Condition |
|-------|-----------|
| `DETERMINISTIC` | `f(0.0) ≥ 0.95`. The prompt is broken; sampling is irrelevant. |
| `STOCHASTIC_OK` | `f(t) ≤ 0.05` for all t. Failure was not reproduced. |
| `TEMPERATURE_CLIFF` | `f(t)` jumps by ≥ 0.4 between two adjacent t values. |
| `VARIANCE_DRIVEN` | `f(0.0) < 0.5` and `max(f) ≥ 0.5`. Sampling noise alone produces failures. |

If multiple conditions match, choose by row order (top wins).

## Constraints

### Must
- Use the same prompt, input, model, and seed strategy across all temperatures.
- N ≥ 20 per temperature; otherwise abort and request larger N.
- Report `f(t)` to two decimal places.
- Include the per-temperature output diversity score (count of unique outputs / N).

### Must Not
- Use top-p variations within the same probe (vary T only).
- Mix prompt variants between temperatures.
- Classify with N < 20.

## Instructions

1. Run `N` samples at each `t` in `TEMPERATURES` (parallelize when possible).
2. Apply `FAILURE_PREDICATE` to each output.
3. Compute `f(t)` and `unique_outputs(t)` for each.
4. Apply the classification rules in order.
5. Emit profile + recommendation.

## Output Format

```
TEMPERATURE PROFILE
| t   | n  | failures | f(t) | unique_outputs | sample_failure (truncated)            |
|-----|----|----------|------|----------------|----------------------------------------|
| 0.0 | 20 | 19       | 0.95 | 1              | "..."                                 |
| 0.3 | 20 | 17       | 0.85 | 5              | "..."                                 |
| 0.7 | 20 | 8        | 0.40 | 14             | "..."                                 |
| 1.0 | 20 | 4        | 0.20 | 19             | "..."                                 |

CLASSIFICATION: DETERMINISTIC | VARIANCE_DRIVEN | TEMPERATURE_CLIFF | STOCHASTIC_OK
chosen_because: <which rule fired and the values>

RECOMMENDED_NEXT_STEP
- DETERMINISTIC → debug_minimal_repro_isolator.md.
- VARIANCE_DRIVEN → set production T to value with min f(t) AND acceptable diversity; re-test.
- TEMPERATURE_CLIFF → pin T below the cliff; document the cliff value.
- STOCHASTIC_OK → close ticket; note non-reproducible.
```

## Verification

- N ≥ 20 at every t? (yes/no)
- Classification follows the priority order? (yes/no)
- Recompute with N=40 on the most informative t; class must remain stable.

## Examples

A `f(t) = [0.95, 0.95, 0.40, 0.10]` profile shows TEMPERATURE_CLIFF between 0.3 and 0.7. Pin production temperature at 0.7+ if accuracy at high T is acceptable.
