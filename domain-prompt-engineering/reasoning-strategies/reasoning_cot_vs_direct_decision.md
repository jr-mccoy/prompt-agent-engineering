---
title: "Decide Whether to Use Chain-of-Thought"
category: prompt-engineering/reasoning-strategies
description: "Diagnose whether a task benefits from explicit reasoning steps or whether direct-answer mode performs better."
techniques:
  - PR-02
  - QA-01
difficulty: intermediate
tags:
  - cot
  - reasoning
  - decision
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/reasoning-strategies/reasoning_extended_thinking_budget.md
  - domain-prompt-engineering/reasoning-strategies/reasoning_silent_reasoning_then_answer.md
---

## Objective

Decide whether a prompt should request explicit step-by-step reasoning, hidden internal reasoning, or direct answers. Output: a decision with rationale and a small comparison plan.

## When to Use

- Designing a new prompt and unsure which mode to use
- An existing CoT prompt is verbose, slow, or noisy without quality gain
- A direct-answer prompt is failing on tasks that need structured reasoning

## Decision Inputs

1. Task type: classification / extraction / planning / multi-hop / generation / refusal
2. Whether the model used has thinking-mode support
3. Whether reasoning needs to be visible to users
4. Latency / token budget

## Modes

| Mode | Best for | Cost |
|---|---|---|
| Direct answer | classification, extraction, single-fact retrieval | low |
| Visible CoT | math, multi-hop reasoning where users want to audit | high |
| Hidden / extended thinking | complex reasoning where users only need the answer | medium-high |
| Scratchpad before answer | tasks needing structure but where chain length is bounded | medium |
| Plan-then-execute | tasks with multiple steps where intermediate verification helps | medium-high |

## Constraints

**Must:**
- Pick one mode, not "depends"
- Justify with the task type and at least one observed failure (or expected failure)
- For visible-CoT, declare an end-of-reasoning marker so post-processing can isolate the answer
- For hidden thinking, name the budget

**Must Not:**
- Default to "let's think step by step" without diagnosis
- Ask for reasoning that the user will never read or use
- Use visible CoT in latency-sensitive surfaces without justification

## Instructions

1. Classify task type.
2. Apply the table; note candidates that fit.
3. If multiple fit, A/B them on 5–10 inputs with the chosen evaluation metric.
4. Lock the mode with a comment in the prompt.

## Output Format

```
TASK TYPE: ...
MODE CHOSEN: ...
RATIONALE: ...

PROMPT ADDITION
  <text inserted into prompt to enable mode>

A/B PLAN (if uncertain)
  arms: <mode A vs mode B>
  inputs: <count>
  metric: <accuracy | latency | clarity>

POST-PROCESSING
  <how to extract final answer from output, if mode emits reasoning>

LOCK NOTE
  "Mode <X> chosen on <date> because <reason>. Change requires re-evaluation."
```

## Verification

- One mode chosen, rationale given
- Visible-CoT prompts have an end-of-reasoning marker
- Hidden-thinking prompts have a budget
- A/B plan exists if mode was uncertain
