---
title: "Argument Extraction From Messy User Text"
category: prompt-engineering/tool-use
description: "Extract typed tool arguments from natural-language input with explicit confidence, source spans, and missing-field handling."
techniques:
  - ST-02
  - ST-03
  - CM-02
  - QA-01
  - RT-05
difficulty: intermediate
tags:
  - tool_use
  - argument_extraction
  - entity_extraction
  - source_grounding
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/tool-use/tooluse_when_to_call_decision_prompt.md
  - domain-prompt-engineering/tool-use/tooluse_disambiguation_pattern.md
  - domain-prompt-engineering/structured-output/structured_json_schema_prompt_builder.md
---

## Objective

Given a tool's parameter schema and a natural-language user message, extract args with `value`, `confidence`, `evidence_span`, and a `__missing[]` list — never invented, never near-matched silently.

## When to Use

- Args come from messy chat, transcripts, or emails.
- Past calls failed because of fabricated args (wrong dates, wrong IDs).
- You want a typed gate to ask for missing fields before invoking.

## Inputs

```
USER_TEXT: <the message; preserve casing>
PARAMETER_SCHEMA: <name, type, required, format e.g., date, uuid, enum>
DEFAULTS: <optional: param → default with provenance "user_profile" | "session" | "config">
RESOLUTION_RULES: <e.g., "today" → ISO TODAY; "tomorrow" → TODAY+1>
TODAY: <ISO date>
```

## Constraints

### Must
- For each parameter, emit one of:
  - `{"value": <typed>, "confidence": "high|medium|low", "evidence_span": "<exact substring of USER_TEXT>", "source": "user_text"}`
  - `{"value": <typed>, "confidence": "high", "evidence_span": null, "source": "default:<provenance>"}`
  - `{"missing": true, "reason": "<one of: not_mentioned | ambiguous | type_conflict>"}`
- `evidence_span` must be a literal substring of USER_TEXT (verbatim, including case). If derived (e.g., "tomorrow" → date), set `evidence_span` to the trigger word and add `derived_via: <rule>`.
- For relative dates/times, apply RESOLUTION_RULES with TODAY; do not assume a timezone — pass `timezone: "unknown"` if absent.
- `confidence=low` ⇒ also emit `clarification_question` for that param.

### Must Not
- Invent values. If the schema has `format: uuid` and no UUID appears, mark `missing` (not zeros, not a placeholder).
- Pick one of multiple candidates without flagging ambiguity. If two candidates exist, emit `confidence=low` + `candidates: [...]`.
- Extract from a quoted segment that is being cited or refused (e.g., "I don't want to do X" — X is not consent).

## Instructions

1. Tokenize USER_TEXT into spans. Mark which spans are quoted, negated, or in conditional clauses.
2. For each parameter, search non-negated spans for type-matching candidates.
3. Apply DEFAULTS only after USER_TEXT search returns nothing.
4. Apply RESOLUTION_RULES last (relative time, person references like "me" → caller_id from session).
5. Emit `__missing[]` listing every required parameter that ended `missing`.
6. If `__missing` is non-empty, emit `next_action: "ask_user"` with a single combined question.

## Output Format

```json
{
  "args": {
    "<param>": {"value": "...", "confidence": "high", "evidence_span": "...", "source": "user_text"},
    "<param>": {"missing": true, "reason": "ambiguous", "candidates": ["a","b"]}
  },
  "__missing": ["<param>"],
  "next_action": "call_tool | ask_user",
  "ask_user_question": "<single sentence, only if next_action=ask_user>"
}
```

## Verification

- Every required parameter appears in `args`.
- Every `evidence_span` (non-null) is a substring of USER_TEXT.
- No `value` of `null` paired with `confidence != null`.
- `next_action=call_tool` ⇒ `__missing == []` AND no `confidence=low`.
