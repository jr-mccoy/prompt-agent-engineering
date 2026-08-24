---
title: "Instruction Negation Audit"
category: prompt-engineering/instruction-design
description: "Find every 'do not X' rule in a prompt that risks priming the model toward X, and rewrite it into a positive-form replacement."
techniques:
  - ST-02
  - ST-03
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - negation
  - priming
  - rule_rewriting
  - audit
  - language_model_quirks
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/instruction-design/instruction_imperative_vs_declarative.md
  - domain-prompt-engineering/instruction-design/instruction_anchor_phrase_library.md
  - domain-prompt-engineering/debugging/debug_failure_mode_taxonomy.md
---

## Objective

Audit a prompt for negation patterns ("do not", "never", "avoid X") that empirically increase the probability of the forbidden token sequence appearing. Output a rewrite table with a positive-form substitute for each risky rule.

## When to Use

- The model produces the exact thing the prompt says to avoid (forbidden phrases, banned formatting, restricted topics).
- After observing leakage of a denied output type.
- During a polish pass on long system prompts with many "Don't" rules.

## Inputs

- `PROMPT_TEXT`: the prompt to audit.
- `OBSERVED_LEAKS_OPTIONAL`: list of strings the model is currently producing that the prompt forbids.

## Risk Levels (fixed)

| Level | Definition |
|-------|------------|
| `HIGH` | Negation rule names a specific phrase / format / token. ("Do not say 'I'm sorry'.") |
| `MED`  | Negation rule names a category but no concrete tokens. ("Avoid medical advice.") |
| `LOW`  | Negation rule restricts a structural property. ("Do not exceed 200 words.") |

`HIGH` carries the highest priming risk and is mandatory to rewrite. `MED` is rewritten if the category is producible. `LOW` is left unchanged unless duplicated.

## Constraints

### Must
- Quote each negation rule verbatim with its rule ID.
- Assign each one of `HIGH | MED | LOW`.
- For every `HIGH` and every `MED` rule, produce a `positive_rewrite` that:
  - Uses no negation word from `{ not, never, don't, avoid, refrain, must not, cannot }`.
  - Specifies what to do instead with at least one concrete output behavior.
- If `OBSERVED_LEAKS_OPTIONAL` contains a string named in a `HIGH` rule, mark that rule as `confirmed_leak: true`.

### Must Not
- Rewrite `LOW` rules unless duplicated.
- Replace a negation with a softer hedge ("try to avoid…").
- Drop information from the original rule.

## Instructions

1. Tokenize prompt into rules.
2. Tag every rule containing a negation word with risk level using the table above.
3. For each `HIGH` rule, identify the named forbidden item; write a positive rewrite that redirects to a desired alternative ("Open replies with the user's question restated.").
4. For each `MED` rule, write a positive rewrite that names the allowed scope ("Reply to medical questions with: 'Direct that to a clinician,' then stop.").
5. Cross-check `OBSERVED_LEAKS_OPTIONAL` and flag matches.
6. Emit the table; append a summary count.

## Output Format

```
| rule_id | original (verbatim)         | risk | confirmed_leak | positive_rewrite                      |
|---------|------------------------------|------|----------------|----------------------------------------|
| D4      | "Do not say 'as an AI'."     | HIGH | true           | "Open replies with the verb of action." |
| D7      | "Avoid making promises."     | MED  | false          | "Phrase commitments as 'I will attempt …'." |
| D9      | "Do not exceed 200 words."   | LOW  | false          | (unchanged)                            |

SUMMARY
high_count: <n>
med_count: <n>
confirmed_leaks: <n>
rules_rewritten: <n>
```

## Verification

- Every `HIGH` rule has a rewrite? (yes/no)
- Zero rewrites contain banned negation tokens? (grep check)
- For one rewritten rule, run a 5-shot test before/after the rewrite; report leak rate Δ.
- Confirm no rule's intent was changed (semantic check by re-reading).

## Examples

Bad: "Do not mention competitor names." → primes competitor recall.
Good: "When asked about competitors, reply with 'I cover only this product.' Then stop."
