---
title: "Silent Failure Detector"
category: prompt-engineering/debugging
description: "Detect outputs that look fluent and well-formed but are wrong — where surface validators pass and only deeper checks fail."
techniques:
  - ST-02
  - QA-01
  - PR-01
  - PR-03
  - DC-01
difficulty: advanced
tags:
  - silent_failure
  - looks_correct
  - second_pass_validation
  - hallucination
  - debugging
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/debugging/debug_failure_mode_taxonomy.md
  - domain-prompt-engineering/hallucination-control/
  - domain-prompt-engineering/evaluation/
---

## Objective

Build and apply a layered validator stack that catches outputs that pass syntactic checks but fail semantic ones (the "looks fine but wrong" class).

## When to Use

- A prompt's outputs are 100% valid JSON, well-typed, fluent — and downstream users keep finding errors.
- High-stakes outputs (financial, clinical, legal) where surface QA is insufficient.
- After surface validators stop catching anything but issues persist.

## Validator Layers (run all in order)

| Layer | Check | Detects |
|-------|-------|---------|
| L1 Syntax | Parses, schema-valid, expected encoding | Format breaks |
| L2 Type | Each field has correct type, unit, range | Wrong-type values that parse |
| L3 Provenance | Every named entity / number is grounded in input or whitelist | Hallucinated entities |
| L4 Internal Consistency | Cross-field invariants hold (sum = total; date_a < date_b) | Contradictions |
| L5 External Consistency | Comparison vs ground-truth or oracle on a labeled subset | Wrong-but-plausible answers |
| L6 Calibration | Stated confidence matches empirical accuracy | Overconfident wrongness |

## Inputs

- `PROMPT_TEXT`, sample of `(INPUT, OUTPUT)` pairs (≥ 50).
- `GROUND_TRUTH_SUBSET`: at least 20 of those pairs labeled with the correct answer.
- `SCHEMA`, `INVARIANTS` (list of cross-field expressions), `ENTITY_WHITELIST` (list or query).

## Constraints

### Must
- Implement all 6 layers; mark layers without inputs as `SKIPPED` not `PASSED`.
- For each output, emit a per-layer result: `PASS | FAIL | SKIPPED`.
- Aggregate metrics: per-layer fail-rate, plus `silent_failure_rate = (passed L1+L2 but failed L3+) / total`.
- Persist failing outputs with the layer that caught them.

### Must Not
- Combine layers into a single check.
- Treat `SKIPPED` as `PASSED`.
- Use the same model that generated the output as L4/L5 judge unless it is explicitly given the ground truth.

## Instructions

1. Generate or load the `(INPUT, OUTPUT)` sample.
2. For each layer:
   - L1: validate against `SCHEMA`.
   - L2: type/range/unit check (e.g., a `price` field must be ≥0 and currency-prefixed).
   - L3: extract entities, numbers, dates from output; require each to appear in `INPUT` or `ENTITY_WHITELIST`.
   - L4: evaluate every expression in `INVARIANTS`.
   - L5: compare against `GROUND_TRUTH_SUBSET`; report exact-match and approximate-match scores.
   - L6: compare any model-stated confidence against empirical correctness; report Brier score.
3. Emit table.

## Output Format

```
SAMPLE_SIZE: <n>
GROUND_TRUTH_SIZE: <m>

| layer | description           | fail_rate | example_failure_id | failed_field        |
|-------|-----------------------|-----------|---------------------|---------------------|
| L1    | schema                | 0.00      | -                   | -                   |
| L2    | type/range            | 0.02      | s007                | price < 0           |
| L3    | entity provenance     | 0.18      | s011                | "Acme Corp" not in input |
| L4    | invariants            | 0.07      | s022                | sum(line_items) != total |
| L5    | external truth (n=20) | 0.30      | s033                | answer != truth      |
| L6    | calibration            | brier=0.21| -                   | -                   |

silent_failure_rate: 0.36   # passed L1+L2, failed at L3 or deeper
top_layer_to_address_first: L3  # highest fail layer that is not L5/L6

ACTIONS
- L3 failure → add a grounding contract in prompt; require entity citations.
- L4 failure → add a self-check second-pass that recomputes invariants.
```

## Verification

- All 6 layers reported (PASS/FAIL/SKIPPED)? (yes/no)
- `silent_failure_rate` arithmetic checks out against per-layer counts? (yes/no)
- For one L3 failure, manually confirm the entity is genuinely not in input.
- After remediation, rerun on same sample; silent_failure_rate must drop.

## Examples

A pricing assistant returns valid JSON with sensible types (L1+L2 pass) but invents a SKU code that never appeared in the input catalog (L3 fails). Surface monitoring would have shipped it.
