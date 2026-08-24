---
title: "Design a Clarification-Before-Answer Prompt"
category: prompt-engineering/prompt-creation
description: "Author a prompt that asks targeted questions before producing output, with budget caps and a fallback when the user refuses."
techniques:
  - ST-02
  - PR-02
difficulty: intermediate
tags:
  - clarification
  - intake
  - questions-first
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/prompt-creation/creation_input_validation_prompt.md
---

## Objective

Build a prompt that gathers missing information through structured questions before answering, with a strict cap on questions per turn and a graceful fallback if the user declines to answer.

## When to Use

- The task is ambiguous and answering blind produces low-quality output
- The cost of getting it wrong exceeds the cost of asking
- Users supply terse requests in chat-style interfaces

## Inputs

1. The target task
2. The minimum information set required to produce a good answer
3. Maximum questions per turn (default 3)
4. Maximum total turns before the model must answer with caveats

## Constraints

**Must:**
- Ask only questions whose answer changes the output
- Cap questions per turn at the stated number
- After the cap, produce best-effort answer with explicit assumptions listed
- Phrase questions to be answerable in one line each

**Must Not:**
- Ask vague open-ended questions when a closed list would do
- Re-ask questions already answered in earlier turns
- Refuse to answer purely because information is incomplete (must produce caveated answer at the cap)

## Instructions

1. On first turn, list missing inputs against the required set.
2. Choose the top-N highest-value missing inputs.
3. Convert each into a closed-form question (multiple choice when possible).
4. If user answers, integrate and check if minimum set is now met.
5. At cap, produce best-effort output with explicit ASSUMPTIONS block.

## Output Format

```
TURN 1 (clarification mode)
I need <n> things before I can answer well:
  1. <question> [options: A, B, C, other]
  2. <question> [options: ...]
  3. <question> [options: ...]

After your answers I will <produce X>.
If you skip, I will assume <defaults> and proceed with caveats.
```

```
TURN N (cap reached, answer mode)
ASSUMPTIONS
  - <assumed value> (because <reason>)

ANSWER
  <output>

CAVEATS
  - <what would change if assumption is wrong>
```

## Verification

- Question count per turn never exceeds cap
- Every question has options or a clear closed form
- At cap, output is produced (no infinite clarification loop)
- ASSUMPTIONS are listed before ANSWER, not after
