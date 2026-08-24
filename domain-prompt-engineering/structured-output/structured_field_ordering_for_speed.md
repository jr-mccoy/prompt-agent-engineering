---
title: "Field Ordering for Streaming and Short-Circuit Speed"
category: prompt-engineering/structured-output
description: "Order schema fields so consumers can short-circuit on early signals and streamed output becomes useful before completion."
techniques:
  - ST-03
  - OC-02
  - CM-02
difficulty: intermediate
tags:
  - streaming
  - latency
  - schema_design
  - structured_output
  - performance
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/structured-output/structured_json_schema_prompt_builder.md
  - domain-prompt-engineering/structured-output/structured_table_row_emitter.md
  - domain-prompt-engineering/compression-and-cost/
---

## Objective

Reorder fields in a structured-output schema so (a) the consumer can decide to abort early, (b) streamed tokens become user-visible before the response completes, and (c) cheap classification fields precede expensive generated fields.

## When to Use

- Token-by-token streaming is enabled.
- A "no-op" or "reject" verdict can save downstream work.
- One field's value gates whether other fields matter (e.g., `is_relevant` gates `analysis`).
- Latency is user-visible.

## Inputs

```
CURRENT_SCHEMA: <ordered list of fields with type and est. tokens>
SHORT_CIRCUIT_FIELDS: <fields whose value can cause the consumer to stop reading>
USER_VISIBLE_FIELDS: <fields the user sees while streaming>
DEPENDENCIES: <field A's value depends on field B; list pairs>
```

## Constraints

### Must
- Place every short-circuit field in the first 3 positions.
- Place fields with `enum` or `boolean` type before any `string` (long-form) field.
- Resolve dependencies: if A depends on B's value, B must precede A.
- Keep arrays of objects toward the end unless they themselves are short-circuit signals.
- Output a reordered schema and a one-line justification per moved field.

### Must Not
- Change field names or types.
- Remove fields.
- Reorder in a way that breaks a stated dependency (the prompt must reject the request and list the conflict).

## Instructions

1. Build a directed graph from DEPENDENCIES (edge B → A means B must come before A).
2. Topologically sort. Within a topological tier, sort by: short-circuit (yes first), type cheapness (bool/enum < number < short string < long string < array < object), tokens ascending.
3. If the sort places a long-string field before all short-circuit fields, escalate: "schema cannot stream usefully — consider splitting into two calls."
4. For each moved field, emit `from_index → to_index: reason`.
5. Emit a streaming-consumer note: which field, when seen, lets the consumer cancel.

## Output Format

```
new_order:
1. <field> (<type>, ~<tokens>t)
2. ...

moves:
- <field>: 5 → 1 (short_circuit + enum)
- <field>: 2 → 4 (depends on field X)

streaming_consumer_hooks:
- after seeing <field>=<value>: cancel remaining stream
- after seeing <field>: render to user

conflicts:
- <list dependency or short-circuit conflicts, or "none">
```

## Verification

- Run dependency check: for every pair B→A, B's index < A's index.
- Confirm every short-circuit field has index ≤ 3 OR a conflict is logged.
- Confirm token estimate for fields 1–3 sums to ≤ 30 tokens (early-cancel budget).
