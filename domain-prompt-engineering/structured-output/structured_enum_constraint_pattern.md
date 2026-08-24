---
title: "Enum Constraint Pattern with Rejection on Unknown"
category: prompt-engineering/structured-output
description: "Force a field's value into a closed set, rejecting unknown values with a structured error rather than silently coercing."
techniques:
  - CM-02
  - DP-04
  - ST-03
  - QA-01
difficulty: beginner
tags:
  - enum
  - validation
  - structured_output
  - rejection
  - closed_set
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/structured-output/structured_optional_field_handler.md
  - domain-prompt-engineering/structured-output/structured_output_validator_prompt.md
---

## Objective

For one or more fields with a closed set of valid values, build prompt language that produces an enum value or a typed `enum_violation` error — never a fuzzy near-match.

## When to Use

- A downstream system branches on the field (status, category, severity).
- Past outputs have produced near-matches: `"high "`, `"High"`, `"HIGH_PRIORITY"`, `"high-ish"`.
- Adding new enum values requires deliberate review, not silent acceptance.

## Inputs

```
FIELD_NAME: <string>
ALLOWED_VALUES: <ordered list>
CASE_POLICY: <case_sensitive | lowercase | uppercase>
WHITESPACE_POLICY: <strip | preserve>
SYNONYMS: <optional map: incoming_value → canonical_value>
ON_UNKNOWN: <reject | classify_as_other>
```

## Constraints

### Must
- The model emits the canonical value verbatim (no quotes-with-trailing-space, no case drift).
- If `ON_UNKNOWN=reject`, the model emits `{"<FIELD_NAME>": null, "__enum_violation": {"field": "<FIELD_NAME>", "received": "<raw>", "allowed": [...]}}` and stops processing dependent fields.
- If `ON_UNKNOWN=classify_as_other`, `ALLOWED_VALUES` must contain `"other"` (or its declared synonym); no silent additions.
- SYNONYMS resolve before reject/other branching.

### Must Not
- Add a value to ALLOWED_VALUES at runtime.
- Return a verbose explanation in place of the enum.
- Coerce by lowercasing if `CASE_POLICY=case_sensitive`.

## Instructions

1. Emit the prompt block:
   ```
   The value of <FIELD_NAME> must be exactly one of:
   - <v1>
   - <v2>
   - ...
   Case policy: <CASE_POLICY>. Whitespace policy: <WHITESPACE_POLICY>.
   Synonym map (apply first): <SYNONYMS or "none">.
   If the input does not map to an allowed value, follow ON_UNKNOWN: <reject | classify_as_other>.
   ```
2. Append a 3-line decision procedure: (a) normalize per case/whitespace; (b) lookup in SYNONYMS; (c) check membership.
3. Provide the canonical violation envelope.
4. If the consumer is JSON-strict, also emit a JSON Schema fragment with `enum: [...]`.

## Output Format

```
prompt_block: <text from step 1+2>
violation_envelope: <JSON example>
schema_fragment:
{
  "<FIELD_NAME>": {"type": "string", "enum": [<...>]}
}
test_cases:
- input "High" → output "high" (lowercase policy)
- input "HIGH_PRIORITY" → __enum_violation (no synonym)
- input " medium " → "medium" (whitespace strip)
```

## Verification

- Every entry in `test_cases` is consistent with the chosen CASE_POLICY and WHITESPACE_POLICY.
- `ON_UNKNOWN=classify_as_other` ⇒ `"other" ∈ ALLOWED_VALUES`.
- The `violation_envelope` includes `received` and `allowed`; otherwise reject the design.
