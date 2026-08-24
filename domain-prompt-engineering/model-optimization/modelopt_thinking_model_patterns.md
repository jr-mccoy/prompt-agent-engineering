---
title: "Patterns for Thinking-Mode (Reasoning) Models"
category: prompt-engineering/model-optimization
description: "Adapt a prompt for reasoning-mode models (Claude extended thinking, o-series) by simplifying instructions, removing CoT scaffolding, and tuning thinking budget."
techniques:
  - PR-02
  - CM-01
difficulty: advanced
tags:
  - thinking-mode
  - reasoning-model
  - extended-thinking
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/reasoning-strategies/reasoning_extended_thinking_budget.md
---

## Objective

Adjust prompts for reasoning-mode models so they leverage native thinking instead of fighting it: drop CoT scaffolding, simplify instructions, tune thinking budgets, and trust the model with the harder reasoning.

## When to Use

- Migrating a non-thinking prompt to a thinking model
- A thinking-mode model is being used but the prompt still includes "let's think step by step"
- Performance tuning on reasoning-heavy tasks

## Patterns to Apply

| Pattern | Why |
|---|---|
| Remove "Let's think step by step" trailers | Native thinking handles this; trailer is redundant |
| Remove explicit scratchpad scaffolding | The model's hidden thinking is the scratchpad |
| Tune thinking budget per input class | Hard cases need more; easy cases waste tokens |
| State the goal clearly; trust derivation | Don't over-instruct the reasoning path |
| Move final-answer formatting to clear schema | Thinking emits the answer cleanly given schema |
| Verification block stays | Thinking does not replace explicit checks |

## Patterns to Avoid

| Pattern | Why |
|---|---|
| Asking the model to "show its work" outside thinking | Doubles cost and clutters |
| Tree-of-thought meta-prompts | The model's native thinking already explores |
| Step-by-step over-prescription | Limits the search the model would otherwise do |
| Self-consistency with N=large on thinking models | Cost compounds; usually not needed |

## Constraints

**Must:**
- Strip CoT scaffolding
- Define thinking budget (or accept default and document why)
- Keep verification block (thinking doesn't validate by itself)
- Tag prompt with `model: <thinking-class>`

**Must Not:**
- Ask the model to produce visible step-by-step reasoning when thinking is hidden
- Use thinking models on cheap tasks where direct-answer suffices

## Instructions

1. Identify CoT and over-prescription in the current prompt; remove.
2. Set thinking budget; document default vs custom.
3. Add or keep verification block.
4. Test on hard cases; adjust budget.

## Output Format

```
PROMPT (thinking-model adapted)
<role>
<task>
<output schema>
<verification block>

REMOVED FROM ORIGINAL
  - "Let's think step by step"
  - "Show your reasoning before answering"
  - <other scaffolding>

THINKING BUDGET
  default: <n>
  triggers for higher: <input features>
  cap: <n>

FRONTMATTER ADDITION
  model: claude-extended-thinking | o-series | <other>
  techniques: + ET-01 (extended thinking)
```

## Verification

- No CoT scaffolding remains
- Thinking budget named
- Verification block present
- Frontmatter targets thinking model
