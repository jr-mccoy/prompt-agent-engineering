---
title: "One-Sentence Answer Pattern"
category: prompt-engineering/output-formatting
description: "Enforce extreme brevity: one sentence for answerable questions, with a defined fallback structure when one sentence is impossible."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - QA-08
  - DC-01
difficulty: beginner
tags:
  - brevity
  - conciseness
  - output_format
  - one_sentence
  - constraint
updated: "2026-05-11"
related_prompts:
  - domain-prompt-engineering/output-formatting/format_no_preamble_no_postamble.md
  - domain-prompt-engineering/output-formatting/format_length_budget_designer.md
  - domain-prompt-engineering/style-and-voice/style_length_and_density_control.md
---

## Objective

Design a one-sentence answer contract for a prompt: specify what makes a one-sentence answer sufficient, define the fallback structure when it is genuinely impossible, and produce the system prompt enforcement block.

## When to Use

- Chatbot or assistant responses must be scannable in under 5 seconds.
- API response is parsed by a downstream system that expects minimal prose.
- You want to force model to commit to a direct answer before elaborating.
- **Not for:** outputs that require multi-step reasoning by design (use reasoning-strategies/). Not for tasks that produce artifacts (code, documents, lists).

## One-Sentence Sufficiency Conditions

A one-sentence answer is sufficient when:
1. The question has a single-claim answer (factual, definitional, or comparative).
2. The answer does not require prerequisite context the user is confirmed to lack.
3. No mandatory caveat changes the answer's interpretation.

A one-sentence answer is **insufficient** (use fallback) when:
- The answer requires ≥ 2 distinct claims that cannot be conjoined without ambiguity.
- A mandatory caveat would exceed 15 words if appended to the answer sentence.
- The answer is "it depends" — a follow-up question is required before answering.

## Fallback Structures

| Situation | Fallback | Max length |
|-----------|---------|-----------|
| Two-claim answer | Two sentences, no connector | 2 sentences |
| Answer with mandatory caveat | Answer sentence + "Note: [caveat]." | 2 sentences |
| "It depends" | "[Condition A]: [answer A]. [Condition B]: [answer B]." | 3 sentences |
| Multi-step answer | Numbered list of ≤ 5 items, each ≤ 10 words | 5 items |
| Definitional answer | "[Term]: [definition under 20 words]." | 1 sentence |

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Question or task type | Yes | What kind of queries this prompt handles |
| Permitted fallbacks | Yes | Select from the table above which fallback types are allowed |
| Hard word ceiling | Optional | Default: 40 words per response |
| Excluded fallbacks | Optional | e.g., "never use numbered list fallback" |

## Constraints

**Must:**
- Begin every response with the answer, not a premise.
- Apply sufficiency check before emitting: confirm one sentence is sufficient or select a fallback.
- Declare which fallback was used if not one-sentence (e.g., append `[fallback: two-claim]` on a new line, or omit if the caller doesn't need it).
- Never exceed the hard word ceiling.

**Must Not:**
- Use "it depends" as an answer without immediately resolving the dependency.
- Append an unsolicited elaboration paragraph after a one-sentence answer.
- Use a fallback for a question that genuinely has a one-sentence answer (unnecessary elaboration is a violation, not a fallback).

## Instructions

1. **Define the scope.** What question types will this contract govern? (List 3–5 representative question patterns.)

2. **Select permitted fallbacks** from the table. Exclude any that are inappropriate for the context.

3. **Set word ceiling.** Default 40 words. Increase only for contexts requiring precision (e.g., technical definitions).

4. **Write sufficiency test** — a decision checklist the model applies to every answer candidate.

5. **Write the system prompt block.**

## Output Format

```
## One-Sentence Answer Contract — [Context Name]

### Scope: Representative question patterns
- [Pattern 1]
- [Pattern 2]
...

### Sufficiency Decision Checklist
Before answering, check:
☐ Single-claim answer? If no → use fallback.
☐ No missing prerequisite context? If no → ask clarifying question instead of answering.
☐ No mandatory caveat >15 words? If no → use "answer + Note:" fallback.
If all ☐ checked: answer in one sentence.

### Permitted Fallbacks
| Situation | Structure | Max words |
|-----------|---------|-----------|
[Selected rows from fallback table]

### System Prompt Block (copy-paste ready)
Answer in one sentence. Hard limit: [N] words.
If one sentence is insufficient, use: [list permitted fallbacks].
Do not elaborate beyond the fallback structure.
Start with the answer, not a premise.

### Examples
✓ Q: "What does HTTP 429 mean?" A: "The server is rate-limiting your requests."
✗ Q: "What does HTTP 429 mean?" A: "HTTP 429 is a status code that means Too Many Requests, which indicates that the user has sent too many requests in a given amount of time."
```

## Verification

- [ ] Sufficiency checklist has exactly 3 binary conditions (not more), each independently testable.
- [ ] Every permitted fallback has a named structure and max word count.
- [ ] Example section shows one correct and one incorrect response for the same question.
- [ ] System prompt block contains the hard word ceiling as a number, not a descriptor.
- [ ] "It depends" is a prohibited answer unless the "it depends" fallback is in the permitted list.
