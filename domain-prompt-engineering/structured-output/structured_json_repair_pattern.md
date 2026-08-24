---
title: "JSON Repair Pattern"
category: prompt-engineering/structured-output
description: "Detect and repair malformed JSON from a model without dropping fields, hallucinating values, or silently coercing types."
techniques:
  - ST-02
  - CM-02
  - QA-01
  - DP-04
difficulty: intermediate
tags:
  - json
  - repair
  - parsing
  - structured_output
  - error_handling
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/structured-output/structured_json_schema_prompt_builder.md
  - domain-prompt-engineering/structured-output/structured_output_validator_prompt.md
---

## Objective

Take a malformed JSON blob plus the target schema, and emit a repaired JSON object that (1) parses, (2) preserves every field the broken output intended to carry, (3) marks anything that had to be inferred.

## When to Use

- A producer model returned text that does not parse as JSON.
- Re-running the producer is more expensive than running a small repair pass.
- You need an audit trail of what was changed.

## Inputs

```
RAW_OUTPUT: <the broken text, verbatim>
TARGET_SCHEMA: <JSON Schema or field list with types>
ALLOW_FIELD_DROP: <true|false>   # if false, every field must be preserved or marked
```

## Constraints

### Must
- Repair only syntactic and minor structural errors. Categories you may fix: trailing commas, unquoted keys, single quotes, unescaped newlines in strings, smart quotes, leading/trailing prose, duplicate keys (keep last), unterminated strings (close at next plausible boundary).
- For every change, append an entry to `__repairs[]` with `path`, `before`, `after`, `category`.
- If a value is missing and required, set it to `null` and add a `__repairs[]` entry with `category: "missing_required_filled_null"`. Do not invent values.
- Output must parse with `JSON.parse` / `json.loads` on first try.

### Must Not
- Translate, summarize, or rephrase string values.
- Change number precision or coerce strings ↔ numbers without logging it.
- Add fields not in TARGET_SCHEMA.
- Drop fields when `ALLOW_FIELD_DROP=false`; instead mark them under `__repairs[]` with `category: "preserved_off_schema"` inside an `__extra` object.

## Instructions

1. Strip non-JSON prose around the blob (markdown fences, "Here's the JSON:" prefix). Log as `category: "stripped_wrapper"`.
2. Tokenize and identify the first parse error. Apply the smallest fix in the allowed category list.
3. Re-parse. Repeat until parse succeeds or 10 iterations are reached.
4. Validate against TARGET_SCHEMA. For type mismatches, attempt one safe coercion: `"42"` → `42` if schema says integer; `"true"` → `true` if boolean. Log every coercion.
5. Emit final object with `__repairs` array.

## Output Format

```json
{
  "<repaired payload, schema-conforming>": "...",
  "__repairs": [
    {"path": "$.user.age", "before": "\"42\"", "after": 42, "category": "type_coercion"},
    {"path": "$.items[2]", "before": "missing", "after": null, "category": "missing_required_filled_null"}
  ],
  "__extra": { /* only if ALLOW_FIELD_DROP=false and off-schema fields existed */ }
}
```

## Verification

- Confirm output parses cleanly. If not, return the input unchanged with `__repairs: [{"category": "unrepairable", "reason": "<...>"}]`.
- Confirm every repair category is in the allowed list.
- If `__repairs` contains an entry not traceable to the input, reject and restart.
