---
title: "Set an Extended-Thinking Budget"
category: prompt-engineering/reasoning-strategies
description: "Decide and document the thinking-token budget for reasoning models, with rules for adjusting it per input class."
techniques:
  - CM-01
  - PR-02
difficulty: advanced
tags:
  - extended-thinking
  - reasoning-budget
  - latency
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/reasoning-strategies/reasoning_cot_vs_direct_decision.md
  - domain-prompt-engineering/compression-and-cost/cost_model_downsize_decision.md
---

## Objective

Choose a thinking-token budget for a reasoning-mode prompt, justify it with measurements, and define rules for raising or lowering the budget per input class.

## When to Use

- Using a model with explicit thinking-mode budget (e.g., Claude extended thinking)
- A flat budget is overkill on easy inputs and starves hard ones
- Latency or cost matters and "max thinking" is too expensive

## Inputs

1. Task description
2. Latency / cost ceiling
3. 5+ representative inputs across difficulty
4. Quality metric to evaluate against

## Constraints

**Must:**
- Measure quality vs budget on the 5+ inputs at 3+ budget levels
- Find the smallest budget that hits the quality bar
- Define input-class triggers that raise the budget
- Cap the budget at a hard maximum

**Must Not:**
- Set the budget by feel
- Use the same budget for trivially easy and known-hard inputs
- Allow the budget to scale with no upper bound

## Instructions

1. Sweep budget levels (e.g., 1k / 4k / 16k tokens).
2. Score each input at each level.
3. Pick the smallest level where quality plateaus.
4. Identify input features that correlate with needing more budget.
5. Define triggers: "if input matches X, increase budget to Y."

## Output Format

```
SWEEP RESULTS
  budget | input 1 | input 2 | ... | aggregate score
  1k     | ...     | ...     | ... | ...
  4k     | ...     | ...     | ... | ...
  16k    | ...     | ...     | ... | ...

CHOSEN DEFAULT BUDGET: <n>
PLATEAU NOTE: quality stops improving past <m>

ESCALATION TRIGGERS
  - if <input feature>: budget = <higher>
  - if <input feature>: budget = <max>

HARD CAP: <n>

ROLLBACK
  if quality drops on <metric>: revert to budget <n_prev>
```

## Verification

- Sweep covers ≥3 budget levels and ≥5 inputs
- Plateau identified empirically, not assumed
- Triggers are falsifiable input checks
- Hard cap is named
