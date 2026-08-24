---
title: "Tool Result → User-Facing Answer Interpretation"
category: prompt-engineering/tool-use
description: "Turn raw tool output into a user-facing answer with field grounding, error surfacing, and zero invented numbers."
techniques:
  - ST-03
  - CM-02
  - RT-05
  - QA-01
difficulty: intermediate
tags:
  - tool_use
  - interpretation
  - answer_synthesis
  - grounding
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/tool-use/tooluse_failure_recovery_pattern.md
  - domain-prompt-engineering/structured-output/structured_dual_output_pattern.md
---

## Objective

Take the raw return of a tool call and produce a user-facing answer that (a) is grounded in tool fields, (b) surfaces tool errors faithfully, and (c) never reports a number absent from the result.

## When to Use

- A tool returned JSON or a typed object that needs translation to prose.
- Past answers have rounded numbers, paraphrased status enums, or skipped errors.
- You want a consistent format across many tool types.

## Inputs

```
TOOL_NAME: <name>
TOOL_INPUT: <args sent>
TOOL_OUTPUT: <raw return; may include error envelope>
ANSWER_FORMAT: <single_sentence | bullets | structured_md>
USER_GOAL: <what the user originally asked>
NUMBER_FORMATTING: <preserve | round_to_<n>_decimals>
```

## Constraints

### Must
- Every claim about a value in the answer cites a path in TOOL_OUTPUT (`$.balance`, `$.results[0].id`).
- If TOOL_OUTPUT contains an error envelope (`error`, `__error`, HTTP status ≥ 400), the answer leads with the error and stops; no fallback fabrication.
- Numbers reproduced from TOOL_OUTPUT use the literal value unless `NUMBER_FORMATTING=round_to_<n>_decimals`, in which case the rounding is explicit ("$1,234.57 (rounded)").
- Enum / status values pass through verbatim; do not translate "PENDING" to "in progress".
- If the tool returned an empty list / no match, say so explicitly.

### Must Not
- Add information not in TOOL_OUTPUT or USER_GOAL.
- Hide nulls. If `expiry == null`, say "no expiry on file".
- Editorialize about why the result occurred unless the tool returned a `reason` field.
- Apologize or hedge ("hopefully this helps") — answer the goal.

## Instructions

1. Detect error envelope. If present: render `error.code`, `error.message`, and a one-line "what to try" derived only from `error.code`.
2. Map TOOL_OUTPUT fields to USER_GOAL: which fields answer the goal? List them.
3. Per ANSWER_FORMAT:
   - `single_sentence`: state the headline value or fact.
   - `bullets`: one bullet per goal-relevant field, "Field name: value (path)".
   - `structured_md`: H3 headings per group, table of fields.
4. Append a compact "fields cited" trace block (machine-readable, optional UI display).

## Output Format

```
answer:
<rendered per ANSWER_FORMAT>

fields_cited:
- $.<path> = <value>
- $.<path> = <value>

error_surfaced: <yes|no>
empty_result: <yes|no>
```

## Verification

- Every number, ID, or enum in `answer` appears in `fields_cited`.
- If `error_surfaced=yes`, `answer` does not contain a fabricated success summary.
- Rounding markers (`(rounded)`) appear only when `NUMBER_FORMATTING != preserve`.
- No phrases from the banned set: "hopefully", "I think", "should be", "approximately" (unless paired with a tool field that itself is approximate).
