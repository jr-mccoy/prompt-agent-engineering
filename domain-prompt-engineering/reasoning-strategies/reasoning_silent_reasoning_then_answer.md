---
title: "Silent Reasoning, Visible Answer"
category: prompt-engineering/reasoning-strategies
description: "Have the model reason internally and emit only the conclusion, with reliable separation between hidden reasoning and surfaced answer."
techniques:
  - PR-02
  - ST-03
difficulty: intermediate
tags:
  - hidden-reasoning
  - clean-output
  - parsing
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/reasoning-strategies/reasoning_scratchpad_designer.md
---

## Objective

Direct the model to reason internally (in thinking mode or in a discardable scratchpad) and emit only the final answer in a clean schema. Reasoning never leaks into output.

## When to Use

- The user wants only the answer, not the chain
- Downstream parsers cannot tolerate prose preludes
- Reasoning is an intermediate device, not a deliverable

## Inputs

1. The task
2. Whether the model has thinking-mode (use it) or not (use scratchpad-and-discard pattern)
3. Final answer schema

## Constraints

**Must:**
- Use thinking-mode if available
- Otherwise, use scratchpad with a clear delimiter and instruct the parser to keep only post-delimiter content
- Final answer must match schema exactly
- No "Here is..." or "Let me explain..." preludes

**Must Not:**
- Allow reasoning to bleed into the answer block
- Emit explanations alongside the answer unless the schema includes them
- Skip the delimiter when using scratchpad mode

## Instructions

1. Choose pattern based on model.
2. Write the prompt with a "Reason internally. Emit only the final answer in the schema below." instruction.
3. For scratchpad mode, define delimiter and parser regex.
4. Add a final instruction: "Do not include any text outside the schema."

## Output Format (the final emitted shape)

```
[For thinking-mode models]
<final answer in schema>

[For non-thinking models, with scratchpad]
SCRATCHPAD:
<reasoning>
---END SCRATCHPAD---
FINAL_ANSWER:
<final answer in schema>
```

## Prompt Snippet

```
Reason silently. After your reasoning, emit only the final answer matching this schema. Do not prefix with explanation, do not summarize the reasoning, do not append a sign-off.

SCHEMA:
<schema>
```

## Verification

- Output contains nothing outside the schema (or scratchpad block, in scratchpad mode)
- No "Here is" / "Let me" / "Sure" preludes
- Parser regex extracts the answer cleanly
- Reasoning text not present in the surfaced answer
