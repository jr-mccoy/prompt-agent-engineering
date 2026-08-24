---
title: "Second-Pass Schema Compliance Validator"
category: prompt-engineering/structured-output
description: "Grade a producer's structured output against a schema with a typed verdict, per-field findings, and a single retry instruction."
techniques:
  - QA-01
  - CM-02
  - ST-03
  - DD-07
difficulty: intermediate
tags:
  - validator
  - schema_compliance
  - structured_output
  - second_pass
  - retry
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/structured-output/structured_json_schema_prompt_builder.md
  - domain-prompt-engineering/structured-output/structured_json_repair_pattern.md
  - domain-prompt-engineering/structured-output/structured_enum_constraint_pattern.md
---

## Objective

Grade a producer's structured output against a schema and emit `{verdict, findings[], retry_instruction}` so an orchestrator can pass/fail/retry without re-running the schema.

## When to Use

- Producer is expensive; validator should be a smaller/cheaper model.
- You want a typed reason for failure (not "looks bad").
- You retry once with targeted feedback before falling back to a human.

## Inputs

```
PRODUCER_OUTPUT: <raw text returned by producer>
TARGET_SCHEMA: <JSON Schema or field list>
STRICTNESS: <strict | lenient>   # lenient allows extra fields
RETRY_BUDGET: <number of remaining retries>
```

## Constraints

### Must
- Emit exactly one verdict from {`pass`, `fail_recoverable`, `fail_unrecoverable`}.
- Each finding has: `path`, `rule`, `severity` ∈ {`error`,`warn`}, `evidence` (≤ 200 chars from output), `fix_hint`.
- `fail_recoverable` is only chosen when `RETRY_BUDGET > 0` and at least one `fix_hint` is mechanical (rename field, fix enum, fill missing).
- `retry_instruction` is ≤ 6 lines and references findings by index.
- For `pass`, findings list is empty AND `retry_instruction = null`.

### Must Not
- Modify or rewrite PRODUCER_OUTPUT.
- Speculate on intent ("I think the model meant...").
- Emit prose narrative outside the response shape.
- Mark `pass` when any required field is missing, even if the rest is great.

## Instructions

1. Parse PRODUCER_OUTPUT. If parse fails, the first finding is `{path: "$", rule: "parse", severity: "error", fix_hint: "Emit valid JSON; common cause: trailing comma / unquoted key"}` and verdict is `fail_recoverable` (if budget) or `fail_unrecoverable`.
2. Walk the schema. For each `required` path absent → finding (`error`).
3. For each present path, check type, enum membership, format (date-time, uuid), and bounds.
4. If `STRICTNESS=strict`, flag any extra path as `error`. If `lenient`, flag as `warn`.
5. Decide verdict:
   - All severities `warn` only → `pass` (lenient) or `fail_recoverable` (strict).
   - Any `error` with mechanical fix and budget > 0 → `fail_recoverable`.
   - Errors without mechanical fix (semantic, e.g., contradictory values) → `fail_unrecoverable`.
6. Compose `retry_instruction` listing only the errors the producer can fix; reference finding indices.

## Output Format

```json
{
  "verdict": "pass | fail_recoverable | fail_unrecoverable",
  "findings": [
    {"path": "$.user.id", "rule": "required_missing", "severity": "error",
     "evidence": "<excerpt or 'absent'>", "fix_hint": "Add string id from input."}
  ],
  "retry_instruction": "Fix findings [0,1]: …"
}
```

## Verification

- `pass` ⇒ `findings == []` ⇒ `retry_instruction == null`. Otherwise reject and recompute.
- Every finding has all five keys.
- `fail_recoverable` with `RETRY_BUDGET=0` is illegal — downgrade to `fail_unrecoverable`.
- `retry_instruction` length ≤ 6 lines; references each finding index it asks the producer to fix.
