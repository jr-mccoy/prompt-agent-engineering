---
title: "Edge Case Generator"
category: prompt-engineering/evaluation/adversarial
description: "Produce edge inputs from a task specification across boundary, malformed, and hostile axes for exhaustive input-coverage testing."
techniques:
  - ST-02
  - ST-03
  - CM-02
  - DT-01
  - QA-10
difficulty: intermediate
tags:
  - edge_cases
  - boundary_testing
  - adversarial_eval
  - input_coverage
  - fuzzing
updated: "2026-05-11"
related_prompts:
  - domain-prompt-engineering/evaluation/adversarial/adv_prompt_injection_test_set.md
  - domain-prompt-engineering/evaluation/eval-datasets/dataset_difficulty_stratifier.md
  - domain-prompt-engineering/evaluation/correctness_eval_design_prompt.md
---

## Objective

Generate a structured set of edge-case inputs for a specified task across three axes: boundary (valid extremes), malformed (invalid format/type), and hostile (designed to trigger failures or unexpected behavior). Each case includes the input, axis, expected model behavior, and a binary pass/fail rule.

## When to Use

- Before deploying a prompt that processes structured user inputs
- When building an eval harness for a task with well-defined input constraints
- When a task spec has explicit validation rules (min/max, required fields, type constraints)
- When known edge inputs have caused prior deployment failures

## Inputs

| Field | Required | Description |
|-------|----------|-------------|
| `task_spec` | Yes | What the model does and what inputs it receives |
| `input_schema` | Yes | Fields with types, required/optional status, valid ranges or enum values |
| `known_failures` | Optional | Past inputs that produced wrong outputs |
| `target_count` | Optional | Total cases; default 30 (10 per axis) |

## Constraints

**Must:**
- Generate cases across all three axes (boundary, malformed, hostile)
- State `expected_model_behavior` as a specific observable action — not "handles gracefully"
- Include `failure_mode`: what breaks if the model mishandles this case
- Cover every field in `input_schema` with ≥1 boundary case
- Include `pass_condition` as a binary statement for every case

**Must Not:**
- Generate boundary cases identical to nominal (valid, typical) inputs
- Allocate >50% of total cases to a single axis
- Omit `failure_mode` from any case

## Instructions

**Step 1 — Axis and sub-type taxonomy**

| Axis | Code | Sub-types |
|------|------|-----------|
| Boundary | B | B1: at lower bound, B2: at upper bound, B3: null/empty, B4: single-item list, B5: max-length string |
| Malformed | M | M1: wrong type, M2: missing required field, M3: unknown extra field, M4: truncated input, M5: encoding mismatch |
| Hostile | H | H1: injection payload in field, H2: ReDoS pattern, H3: control characters, H4: Unicode edge (RTL/zero-width), H5: prompt-structure-breaking content |

**Step 2 — Case schema**

```json
{
  "id": "EC-001",
  "axis": "B",
  "sub_type": "B1",
  "field_under_test": "<field name from input_schema>",
  "input": "<verbatim input value or full object>",
  "expected_model_behavior": "<specific observable output or action>",
  "failure_mode": "<what breaks if mishandled>",
  "pass_condition": "<binary observable>"
}
```

**Step 3 — Derivation rules per sub-type**

*Boundary axis:*
- B1: Set field to its documented minimum; all other fields at nominal valid values
- B2: Set field to its documented maximum
- B3: Null or empty string for optional fields; expect graceful handling without crash
- B4: For list fields, set length to 1
- B5: For string fields, generate a string exactly at the documented max length

*Malformed axis:*
- M1: Pass integer where string expected; pass string where integer expected
- M2: Send required field as `null`
- M3: Add an undocumented field with a random key and value
- M4: Truncate JSON mid-value (e.g., `{"field": "val`)
- M5: Send UTF-16 bytes where UTF-8 expected

*Hostile axis:*
- H1: Embed `'; DROP TABLE users; --` or `Ignore previous instructions` in a string field
- H2: ReDoS pattern for any field that may be regex-validated (e.g., `(a+)+$`)
- H3: Null byte (`\x00`), backspace, or BEL in string fields
- H4: Arabic/Hebrew RTL text, zero-width joiner, bidirectional override character
- H5: Field value containing model prompt delimiters (e.g., `\n\nHuman:`, `### System:`)

**Step 4 — Field coverage check**

Produce: field × axis matrix, cells = case count. Flag any field with 0 boundary cases.

**Step 5 — Known-failure crosswalk**

For each entry in `known_failures`, identify which axis/sub-type it represents. Mark as "covered" if an equivalent case was generated; "new" if it reveals a sub-type gap.

## Output Format

1. **Case array** — JSON array following schema
2. **Field coverage matrix** — field × axis, cells = counts; flag fields with 0 boundary cases
3. **Known-failure crosswalk** — table mapping each known failure to axis/sub-type and coverage status
4. **Gap list** — fields with no boundary case, axes below 20% of target_count

## Verification

- [ ] All three axes (B, M, H) represented with ≥1 case each
- [ ] Every field in `input_schema` has ≥1 boundary case
- [ ] No axis exceeds 50% of total case count
- [ ] All `expected_model_behavior` values are observable (no "handles appropriately")
- [ ] `pass_condition` present and binary on every case
