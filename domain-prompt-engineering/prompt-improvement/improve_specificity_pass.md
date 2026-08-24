---
title: "Specificity Pass on an Existing Prompt"
category: prompt-engineering/prompt-improvement
description: "Identify vague verbs, abstract nouns, and unmeasurable adjectives in a prompt and replace them with operational language."
techniques:
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - specificity
  - rewriting
  - operational-language
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/evaluation/correctness_vague_requirements_translator.md
---

## Objective

Take an existing prompt and replace every vague verb, abstract noun, or unmeasurable adjective with a specific, operational form. Output: a diff and the rewritten prompt.

## When to Use

- Outputs are inconsistent across runs of the same prompt
- The prompt uses words like "comprehensive", "appropriate", "high-quality", "thorough"
- A reviewer says "this prompt is fine, the model just isn't following it"

## Inputs

1. The current prompt
2. 2+ outputs that disappointed
3. The disappointment cause for each (in plain language)

## Constraints

**Must:**
- Flag every vague term and propose a replacement
- Replacement must be measurable from output alone
- Preserve the prompt's intent; this is a rewrite, not a redesign
- Show before/after for each change

**Must Not:**
- Add new constraints not implied by the original
- Remove safety or scope rules
- Replace one vague word with another

## Common Vague Terms (replace these)

| Vague | Operational Replacement Examples |
|---|---|
| comprehensive | "covering items A, B, C" |
| appropriate | "matching the register defined in <section>" |
| high-quality | named quality checks (citation present, length cap met) |
| thorough | "checking each input field against <list>" |
| best practices | "following <named standard>" |
| concise | "≤ N words" or "≤ N sentences" |
| professional | "no contractions, no exclamation marks, third-person" |
| user-friendly | "≤ N syllables per word, ≤ M words per sentence" |

## Instructions

1. Highlight every term in the Common Vague Terms table found in the prompt.
2. For each, propose 1–3 operational replacements; pick best fit.
3. Re-run the prompt mentally against the disappointing outputs; would the rewrite have caught them?
4. Emit a diff and the rewritten prompt.

## Output Format

```
DIFF
  - "comprehensive" → "covers customer ID, order ID, refund reason, refund amount"
  - "appropriate tone" → "neutral register; no contractions; no exclamation marks"
  - ...

REWRITTEN PROMPT
<full rewrite>

UNRESOLVED VAGUENESS
  - <term>: <reason it could not be operationalized> | <question for the user>
```

## Verification

- No vague term from the table remains unaddressed
- Every replacement is checkable from the output alone
- Disappointing outputs would now be caught by the rewritten prompt
- No new constraint was silently added
