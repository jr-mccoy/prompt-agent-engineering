---
title: "Imperative vs Declarative Instruction Converter"
category: prompt-engineering/instruction-design
description: "Decide whether each rule should be an imperative ('Do X') or a declarative spec ('Output is X'), and convert it into the better form."
techniques:
  - ST-02
  - ST-03
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - imperative
  - declarative
  - rule_form
  - rewriting
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/instruction-design/instruction_negation_audit.md
  - domain-prompt-engineering/instruction-design/instruction_must_should_may_classifier.md
  - domain-prompt-engineering/instruction-design/instruction_anchor_phrase_library.md
---

## Objective

For each rule in a prompt, decide whether it is best expressed as an imperative ("Do X.") or a declarative specification ("Output contains X."), and rewrite mismatched rules.

## When to Use

- A prompt mixes "Return JSON" with "JSON shape: {...}" inconsistently.
- The model sometimes follows process rules but ignores output rules (or vice versa).
- Standardizing prompt style across a team library.

## Decision Rule (apply in order)

1. If the rule constrains the **artifact** (shape, schema, length, allowed tokens) → DECLARATIVE.
2. If the rule constrains the **process** (order of operations, when to ask, when to stop, what to do on error) → IMPERATIVE.
3. If the rule expresses a **policy/value** (refuse, escalate, cite) → IMPERATIVE.
4. If unclear, default to DECLARATIVE; it is easier to validate.

## Inputs

- `PROMPT_TEXT`: the prompt to convert.
- `RULE_IDS_OPTIONAL`.

## Constraints

### Must
- Classify every rule as `IMP` or `DEC`.
- For each rule whose original form does not match its target class, produce a `rewrite`.
- DECLARATIVE rewrites use the form: `Output[<field>] = <constraint>` or "The reply is/contains/matches …".
- IMPERATIVE rewrites use a single verb-first sentence ≤ 20 words.
- Preserve every constraint from the original; nothing dropped, nothing added.

### Must Not
- Mix forms in one rule (e.g., "Do X (must be ≤200 chars)").
- Use future-tense ("will produce…").
- Use first-person ("I will…").

## Instructions

1. Number rules.
2. Apply the decision rule to set `target_class`.
3. Detect `original_class` from the rule's grammatical form (verb-first → IMP; predicate/spec → DEC).
4. If `original_class != target_class`, write the `rewrite`.
5. Add an `applies_at` tag for IMP rules: `pre_response | mid_response | error | tool_call | end_of_turn`.
6. For DEC rules, add a `validator` field: a single check expression that an external script could run (regex / json-schema reference / length check).

## Output Format

```
| rule_id | original (verbatim) | original_class | target_class | rewrite                                         | applies_at | validator                  |
|---------|---------------------|----------------|--------------|--------------------------------------------------|------------|----------------------------|
| R3      | "Output JSON only." | IMP            | DEC          | "Output is a single JSON object, no prose."     |            | starts_with(`{`) AND parses_json |
| R5      | "Schema: { id, name }" | DEC          | DEC          | (unchanged)                                      |            | json_schema(R5_schema)     |
| R7      | "On tool error, retry once then escalate." | IMP | IMP   | (unchanged)                                      | error      |                            |

SUMMARY
imp_count: <n>
dec_count: <n>
rewrites: <n>
unvalidated_dec_rules: <list of IDs>  # should be empty
```

## Verification

- Every rule has `target_class` ∈ {IMP, DEC}? (yes/no)
- Every DEC rule has a non-empty `validator`? (yes/no)
- Every IMP rule has `applies_at`? (yes/no)
- Pick one DEC rule; run its validator against the model's output. Pass/fail recorded.

## Examples

Imperative (process):
- "Ask one clarifying question if `user_age` is missing."
Declarative (artifact):
- "Output is a markdown table with columns: name, score, reason."
