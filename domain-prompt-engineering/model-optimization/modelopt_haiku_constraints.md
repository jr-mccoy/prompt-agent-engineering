---
title: "Haiku-Class Model Constraints and Patterns"
category: prompt-engineering/model-optimization
description: "Adapt prompts to small/fast models (Haiku, mini, flash) by simplifying instructions, reducing reasoning, and tightening schemas."
techniques:
  - CM-01
  - ST-03
difficulty: intermediate
tags:
  - haiku
  - small-model
  - mini
  - flash
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/compression-and-cost/cost_model_downsize_decision.md
---

## Objective

Adjust a prompt to perform well on a small fast model: simpler instructions, fewer simultaneous concerns, tighter schemas, and explicit limits where the model would otherwise over-think.

## When to Use

- Routing simple tasks to a smaller model for cost/latency
- A migrated prompt over-performs on bigger models but under-performs on smaller
- A workload has narrow scope and does not need a frontier model

## Patterns That Help Small Models

| Pattern | Why |
|---|---|
| Single concern per prompt | Small models stretch thin across many concerns |
| No chain-of-thought when answer is direct | They produce noisy CoT |
| Strict JSON schema or enums | Reduces freeform errors |
| Smaller output schemas (fewer fields) | Reliability per field is higher |
| Fewer few-shot examples (1–2) | More can confuse, not help |
| Explicit "respond with only the value" | Cuts preamble |
| Pre-baked refusal text | Smaller models may refuse with awkward phrasing |
| Hard length caps | Prevent rambling |

## Patterns That Hurt Small Models

| Pattern | Why |
|---|---|
| Multi-step reasoning prompts | They struggle with self-consistency |
| Tree-of-thought | They cannot evaluate branches well |
| Long abstract instructions | They lose the thread |
| Unbounded creative tasks | They produce generic output |

## Constraints

**Must:**
- Tag prompt with target small model
- Apply at least 3 small-model-friendly patterns
- Avoid all small-model-hurting patterns
- Add an escalation rule for inputs that exceed small model's reach

**Must Not:**
- Expect parity with large-model output without measurement
- Stack reasoning techniques on a small model
- Use the large-model prompt verbatim

## Instructions

1. Identify single concern of the prompt; trim others.
2. Tighten schema; remove optional fields.
3. Add hard caps and "respond with only..." rules.
4. Define escalation: which inputs require the larger model.
5. Measure on stratified test set.

## Output Format

```
SMALL-MODEL PROMPT
<prompt with applied patterns>

PATTERNS APPLIED
  - single concern
  - tight schema
  - hard length cap
  - explicit "only the value"

PATTERNS REMOVED
  - chain-of-thought
  - tree-of-thought
  - long instructions

ESCALATION RULE
  trigger: <input feature suggesting hard case>
  action: route to <larger model>

MEASUREMENT
  per-stratum metric: ...

FRONTMATTER ADDITION
  model: haiku-class | gpt-mini-class | flash-class
  techniques: + CM-01 (compression), TS-01 (tight schema)
```

## Verification

- Prompt tagged with target small model
- ≥3 helpful patterns applied
- No hurting patterns remain
- Escalation rule defined
