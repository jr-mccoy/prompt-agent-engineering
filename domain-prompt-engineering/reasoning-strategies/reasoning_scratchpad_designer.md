---
title: "Design a Structured Scratchpad"
category: prompt-engineering/reasoning-strategies
description: "Add a bounded scratchpad to a prompt so the model can think out loud in a fixed structure before producing the final answer."
techniques:
  - ST-03
  - PR-02
difficulty: intermediate
tags:
  - scratchpad
  - structured-thinking
  - reasoning
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/reasoning-strategies/reasoning_silent_reasoning_then_answer.md
---

## Objective

Define a scratchpad section the model fills before its final answer, with named slots and a hard length cap, so reasoning is structured and downstream parsing is reliable.

## When to Use

- The task benefits from intermediate reasoning but free-form CoT is too noisy
- You want the reasoning visible for audit but bounded
- You will parse the final answer programmatically and need a reliable separator

## Inputs

1. The task and its known reasoning steps
2. Whether the user will see the scratchpad
3. Length cap for the scratchpad

## Constraints

**Must:**
- Define scratchpad slots by name (e.g., `inputs_received`, `assumptions`, `key_decision`, `risk_flags`)
- Cap each slot's length
- Put scratchpad before the final answer with an explicit separator
- Make the final-answer block parseable independently

**Must Not:**
- Allow free-form scratchpad content; every slot has a name
- Mix scratchpad reasoning into the final answer
- Use scratchpads as a place to hide unsupported claims

## Instructions

1. Decompose the task's reasoning into 3–6 named slots.
2. Set length cap per slot.
3. Choose a separator between scratchpad and final answer.
4. Add a rule: "If scratchpad would exceed cap, summarize, do not extend."
5. Document parser regex for extracting the final answer.

## Output Format

```
SCRATCHPAD CONTRACT
  slots:
    - <slot_name>: <≤ N words> — <what goes here>
    - ...
  separator: "---END SCRATCHPAD---"
  cap: total ≤ <n> words

PROMPT ADDITION
  Before answering, fill the scratchpad below using only the named slots.
  After "---END SCRATCHPAD---", produce the final answer in the declared schema.

  SCRATCHPAD:
    <slot_name>: ...
    ...

  ---END SCRATCHPAD---

  FINAL ANSWER:
    <schema>

PARSER
  regex: ".*?---END SCRATCHPAD---\\s*FINAL ANSWER:\\s*(?<answer>.*)"
```

## Verification

- Every slot has a length cap
- Separator string is unambiguous (does not appear in normal answers)
- Parser regex extracts the final answer cleanly on sample outputs
- No slot allows unstructured "thoughts" without a topic
