---
title: "JSON Schema → Prompt Builder"
category: prompt-engineering/structured-output
description: "Convert a JSON Schema into a prompt that produces conforming output, choosing schema-in-prompt vs response_format vs tool-use strategy."
techniques:
  - ST-02
  - ST-03
  - OC-02
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - json
  - schema
  - structured_output
  - response_format
  - validation
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/structured-output/structured_json_repair_pattern.md
  - domain-prompt-engineering/structured-output/structured_output_validator_prompt.md
  - domain-prompt-engineering/structured-output/structured_dual_output_pattern.md
---

## Objective

Given a JSON Schema (Draft 7+), produce (a) a prompt that emits conforming JSON, and (b) a justified choice between three enforcement strategies: schema-in-prompt, native `response_format`/Structured Outputs, or tool-use forcing.

## When to Use

- A downstream consumer parses model output as JSON.
- The schema contains required fields, enums, nested objects, or arrays of typed objects.
- Past outputs have failed parse, missed fields, or invented keys.

## Inputs

```
SCHEMA: <paste JSON Schema>
TARGET_MODEL: <claude-* | gpt-* | open-source>
PROVIDER_FEATURES: <native_structured_outputs: yes/no, tool_use: yes/no>
LATENCY_BUDGET_MS: <number>
EXAMPLE_INPUT: <one realistic input the prompt will receive>
```

## Constraints

### Must
- Pick exactly one strategy and name it: `schema-in-prompt` | `response_format` | `tool-use-forced`.
- Justify the choice with two facts from inputs (e.g., "GPT-4o + native Structured Outputs available → response_format").
- Emit the final prompt as a single fenced block labeled `final_prompt`.
- Include every `required` field name verbatim in the final prompt.
- Reject the user task if `additionalProperties: false` conflicts with a strategy that cannot enforce it; state the conflict.

### Must Not
- Output the schema reformatted as prose.
- Add fields not in the schema.
- Use the word "appropriate" or "as needed" anywhere in the final prompt.

## Instructions

1. Parse the schema. List every `required` path (`$.user.id`, `$.items[].sku`, etc.).
2. Score each strategy 0–3 on: enforcement strength, token cost, latency, model support. Pick the highest; tiebreak toward `response_format` when available.
3. Build the prompt body with these sections in order:
   - Role line (1 sentence).
   - Task (1–3 sentences).
   - Input placeholder.
   - Output contract: paste the schema verbatim if `schema-in-prompt`; otherwise reference field list.
   - Field-level rules: enums → "must be one of [...]"; integers with bounds → range; date-time → ISO 8601 UTC; nullable → emit `null` not omit.
   - Failure clause: "If a required field cannot be determined, emit `\"__error\": \"<reason>\"` at top level and stop."
4. Add a 4-line self-check the model runs before emitting.

## Output Format

```
strategy: <name>
rationale: <2 facts>
required_paths: [<list>]
schema_conflicts: [<list or "none">]

final_prompt:
---
<the prompt>
---

self_check_block:
- All required paths present? Y/N
- All enums in allowed set? Y/N
- No extra keys? Y/N
- Types match (string/number/bool/null)? Y/N
```

## Verification

- Run final_prompt against EXAMPLE_INPUT mentally; list which `required_paths` would be filled and which would trigger `__error`.
- If any `required_path` cannot be filled from EXAMPLE_INPUT, the prompt must show how `__error` is emitted, not invent a value.
- Confirm zero occurrences of "appropriate", "as needed", "etc." in `final_prompt`.
