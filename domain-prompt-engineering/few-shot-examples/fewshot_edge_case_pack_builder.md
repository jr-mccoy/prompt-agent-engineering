---
title: "Build an Edge-Case Few-Shot Pack"
category: prompt-engineering/few-shot-examples
description: "Curate few-shot examples that cover edge cases (boundary inputs, malformed inputs, refusal-worthy inputs) instead of typical inputs."
techniques:
  - PR-03
  - QA-01
difficulty: advanced
tags:
  - edge-cases
  - boundary
  - few-shot
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/few-shot-examples/fewshot_example_selector.md
  - domain-prompt-engineering/prompt-improvement/improve_brittleness_audit.md
---

## Objective

Assemble a few-shot pack focused on edge cases — the inputs that production handles poorly — so the model sees the boundary behavior, not just the easy middle.

## When to Use

- The prompt handles common inputs well but fails on edges
- A separate "edge pack" can be loaded conditionally for risky inputs
- You are stress-testing a prompt before release

## Edge Categories (target each)

- Empty / minimal inputs
- Maximum-length / overflow inputs
- Wrong-type inputs
- Refusal-worthy inputs
- Multi-language or code-switched inputs
- Self-contradictory inputs
- Ambiguous inputs that map to multiple valid outputs
- Inputs requiring an "I don't know" response

## Constraints

**Must:**
- Cover at least 5 of the 8 categories above
- Include the desired model behavior for each, even if it is "refuse" or "ask for clarification"
- Mark each example with its category
- Keep the pack within a token budget; this is supplementary to the main few-shot set

**Must Not:**
- Treat edge inputs as if they were typical
- Show only the bad behavior; always show the desired behavior
- Use synthetic edge cases without marking them synthetic

## Instructions

1. Walk the categories; for each, draft or curate one example.
2. For each, write the desired output (which may be a refusal or clarification request).
3. Tag examples with category.
4. Decide loading strategy: always-on, or triggered when input matches a category check.
5. Document budget impact.

## Output Format

```
EDGE PACK

[empty/minimal]
  input: <minimal example>
  desired output: ...

[max-length]
  input: <truncated indicator>
  desired output: ...

[wrong-type]
  ...

[refusal-worthy]
  input: ...
  desired output: refusal text matching policy

[multi-language]
  ...

[self-contradictory]
  ...

[ambiguous]
  ...

[idk]
  ...

LOADING
  strategy: always-on | triggered by <input check>
  trigger checks (if triggered): ...

BUDGET
  pack tokens: <n>
  always-on cost: <n>
  triggered cost: <n>
```

## Verification

- ≥5 categories covered
- Every example has a desired output
- Refusal/idk examples align with policy language
- Loading strategy is named and budgeted
