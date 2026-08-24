---
title: "Dual Output Pattern: Human Prose + Machine JSON"
category: prompt-engineering/structured-output
description: "Emit a user-facing message and a machine-readable payload in one call without the two contradicting each other."
techniques:
  - ST-03
  - CM-02
  - QA-01
  - DC-01
difficulty: intermediate
tags:
  - dual_output
  - human_machine
  - structured_output
  - consistency
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/structured-output/structured_xml_tag_pattern.md
  - domain-prompt-engineering/structured-output/structured_markdown_section_contract.md
  - domain-prompt-engineering/structured-output/structured_output_validator_prompt.md
---

## Objective

Define a single output shape that contains both a prose answer for users and a JSON payload for code, with explicit consistency rules so the prose never disagrees with the payload.

## When to Use

- One model call needs to satisfy a UI display and a backend pipeline.
- You cannot afford a second call for prose summarization.
- Mismatch between displayed message and stored data has caused bugs (e.g., UI says "approved", DB says "pending").

## Inputs

```
PAYLOAD_SCHEMA: <JSON Schema or field list>
USER_FACING_TONE: <neutral | warm | terse>
DECISION_FIELDS: <fields the prose must reflect, e.g., status, severity, next_action>
TRANSPORT: <xml-tagged | fenced-json-after-prose | json-with-message-field>
```

## Constraints

### Must
- Choose exactly one TRANSPORT and use it consistently.
  - `xml-tagged`: `<message>...</message>` then `<payload>JSON</payload>`.
  - `fenced-json-after-prose`: prose paragraph, blank line, then ```` ```json ```` fence.
  - `json-with-message-field`: payload JSON contains a top-level `message` string.
- Prose must reference every value in DECISION_FIELDS by its canonical form (no synonyms, no rounding for numbers shown to ≤ 1 decimal).
- Generate the payload first, then the prose from the payload — never the reverse.
- Add a `consistency_check` self-step that compares prose mentions of DECISION_FIELDS to payload values before final emit.

### Must Not
- Repeat the entire payload as prose.
- Hide payload-only fields in prose (omit from prose is fine).
- Allow the prose to contain numbers absent from the payload.
- Emit prose that hedges ("approximately", "around") about a number that the payload states exactly.

## Instructions

1. Order: produce payload → run internal `consistency_check` → produce prose using payload values → emit per TRANSPORT.
2. For `fenced-json-after-prose`, the JSON fence must be the LAST block; no prose after.
3. For `xml-tagged`, both tags appear; `<message>` first, `<payload>` second; no nesting.
4. Build a decision-field reference table the model uses while drafting prose:
   ```
   field=status, value=approved → say "approved"
   field=severity, value=3 → say "severity 3" (not "moderate")
   ```
5. On consistency_check failure: regenerate prose, do not edit payload.

## Output Format

```
transport: <choice>
ordering_rule: payload_first

shape_template:
---
<verbatim template with placeholders {message}, {payload_json}>
---

consistency_check:
- for field in DECISION_FIELDS: payload[field] appears in message text? Y/N
- numbers in message ⊆ numbers in payload? Y/N

failure_recovery: regenerate message; payload is canonical
```

## Verification

- Eye-grep the template for two copies of any decision-field value (one in message, one in payload). Both must use the same canonical form.
- For `json-with-message-field`, confirm `message` is `string`, ≤ a chosen char limit, contains no markdown that breaks downstream renderers.
- If the model would emit prose-only or payload-only, fail closed and retry.
