---
title: "Optional Field Policy: null vs Omit vs Empty String"
category: prompt-engineering/structured-output
description: "Pick a single, consumer-aligned policy for absent values across a structured-output schema and document the rules."
techniques:
  - ST-03
  - CM-02
  - DP-04
  - QA-01
difficulty: intermediate
tags:
  - schema
  - optional_fields
  - null_handling
  - structured_output
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/structured-output/structured_json_schema_prompt_builder.md
  - domain-prompt-engineering/structured-output/structured_enum_constraint_pattern.md
---

## Objective

Given a schema and a list of consumers (downstream parsers, UIs, databases, analytics), pick exactly one absence-encoding policy per field type and produce a rule table the prompt and consumers can both reference.

## When to Use

- Different consumers interpret missing/null/empty differently and bugs trace back to that mismatch.
- The schema mixes `nullable: true`, `required: false`, and presence-by-default fields.
- You are migrating an existing schema and don't want to break parsers.

## Inputs

```
SCHEMA: <field list with type, required?, nullable?>
CONSUMERS: <each consumer's tolerance, e.g.,
  api_v1: {null: ok, omit: error, empty_string: ok}
  warehouse: {null: ok, omit: ok, empty_string: distinct_value}
  ui: {null: hidden, omit: hidden, empty_string: shown_as_blank}
>
EXISTING_DATA: <yes|no — does historical data already use one convention?>
```

## Constraints

### Must
- Pick exactly one policy per (type, required?) cell of the table below. Do not split policy by field within a cell.
- The policy must satisfy every consumer or the field is flagged as a `consumer_conflict` requiring a per-consumer adapter.
- For `EXISTING_DATA=yes`, the chosen policy must match historical encoding for required fields, or include a migration note.

### Must Not
- Allow `undefined`, `"null"` (string), or sentinel values like `-1`/`"N/A"` unless a consumer explicitly requires them.
- Use a different policy for the same field across versions of the same consumer.

## Instructions

1. Build the cell table:

   | type \ required | required=true | required=false |
   |---|---|---|
   | string | always present (non-empty)? | <pick: null / omit / empty> |
   | number | always present? | <pick: null / omit> |
   | bool | always present? | <pick: null / omit> |
   | array | always present (may be `[]`)? | <pick: `[]` / omit> |
   | object | always present? | <pick: `{}` / null / omit> |

2. For each cell, intersect consumer tolerances. If the intersection is empty, mark `consumer_conflict` and propose an adapter (e.g., warehouse coerces omit → null on read).
3. Emit a prompt clause the model will see: "When field X has no value, emit `null` / omit the key / emit `\"\"`. Empty array means zero items, not 'unknown'."
4. Add a parser rule per cell (e.g., "consumer A treats omit as null on read").

## Output Format

```
policy_table: <filled cell table>
per_field_rules:
- <field>: <policy with rationale>
consumer_conflicts:
- <field>: <which consumers disagree, proposed adapter>
prompt_clause:
---
<text inserted into producer prompt>
---
parser_rules:
- <consumer>: <rules>
migration_notes: <only if EXISTING_DATA=yes>
```

## Verification

- Every field in SCHEMA appears once in `per_field_rules`.
- For every cell, exactly one of {null, omit, empty, `[]`, `{}`} is chosen.
- No consumer in CONSUMERS has a tolerance violation that is not captured under `consumer_conflicts`.
