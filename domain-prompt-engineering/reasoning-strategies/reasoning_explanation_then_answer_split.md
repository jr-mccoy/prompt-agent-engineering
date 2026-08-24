---
title: "Explanation-Then-Answer Split for Auditable Outputs"
category: prompt-engineering/reasoning-strategies
description: "Produce an answer plus a separate, parseable explanation block when both are needed by different consumers (UI vs API vs reviewer)."
techniques:
  - ST-03
  - PR-02
difficulty: intermediate
tags:
  - explanation
  - dual-output
  - audit
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/structured-output/structured_dual_output_pattern.md
  - domain-prompt-engineering/reasoning-strategies/reasoning_silent_reasoning_then_answer.md
---

## Objective

Build a prompt that returns both a structured answer and an explanation, in separate parseable blocks, so a UI can render the answer, an API can consume the answer field, and a reviewer can audit the explanation.

## When to Use

- The same output serves multiple consumers (display, downstream system, audit)
- A single concatenated text answer cannot be split reliably
- Compliance or reviewability requires explanation that is not optional

## Inputs

1. The task and final-answer schema
2. Whether the explanation is mandatory or optional
3. Length cap for explanation
4. Audience: who reads the explanation

## Constraints

**Must:**
- Emit two named blocks: `ANSWER` and `EXPLANATION`
- Make `ANSWER` parseable as a standalone unit (matching the schema)
- Cap `EXPLANATION` length
- Tailor explanation register to the named audience

**Must Not:**
- Mix explanation prose into the answer schema
- Allow the explanation to contradict the answer
- Skip explanation when policy says it is mandatory

## Instructions

1. Define the answer schema.
2. Define explanation length and audience.
3. Order in output: answer first (so streaming consumers get it early) or explanation first (audit-first surfaces).
4. Add a consistency rule: if explanation contradicts answer, refuse and emit a diagnostic.

## Output Format

```
ANSWER
<answer matching schema>

EXPLANATION
<≤ N words; audience: <who>; covers: why this answer over alternatives>

CONSISTENCY CHECK
  ANSWER and EXPLANATION must agree.
  If they disagree, output:
    {
      "status": "internal_inconsistency",
      "answer": ...,
      "explanation": ...,
      "diagnostic": "<which contradicts which>"
    }
```

## Verification

- Two distinct, parseable blocks
- Explanation length within cap
- Explanation written to the named audience
- Consistency check is part of the prompt and triggers on disagreement
