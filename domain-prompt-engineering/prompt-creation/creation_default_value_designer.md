---
title: "Decide What the Prompt Assumes When Input Is Silent"
category: prompt-engineering/prompt-creation
description: "Define explicit default values and silence-handling rules for every optional input so behavior is predictable."
techniques:
  - CM-02
difficulty: intermediate
tags:
  - defaults
  - silence-handling
  - determinism
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/prompt-creation/creation_input_validation_prompt.md
---

## Objective

For each optional input, decide what the prompt assumes when the caller is silent, and surface those assumptions in the output so callers can detect drift.

## When to Use

- A prompt has many optional inputs and behavior varies by what callers omit
- Outputs differ unpredictably between callers using the same prompt
- You are documenting a prompt for a new team

## Inputs

1. List of optional inputs the prompt accepts
2. For each, the realistic distribution of values seen in practice
3. The cost of a wrong assumption per input (low / medium / high)

## Constraints

**Must:**
- Assign a default to every optional input
- Choose defaults that match the dominant real distribution, not the theoretical center
- Surface defaults used in the output (e.g., `defaults_applied: [...]`)
- For high-cost inputs, refuse silence rather than defaulting

**Must Not:**
- Use silent defaults for high-cost inputs
- Default to "none" or empty when a domain default exists
- Hide the default-handling logic from the output

## Instructions

1. List optional inputs with their cost-of-wrong-assumption.
2. For low/medium cost, pick a default that matches dominant real usage.
3. For high cost, set policy to ASK or REFUSE rather than DEFAULT.
4. Add a `defaults_applied` field to the output schema.
5. Document the rationale for each default.

## Output Format

```
DEFAULTS TABLE
  field | cost | policy (default | ask | refuse) | default_value | rationale
  ...

PROMPT ADDITION
  When <field> is absent:
    - if policy=default: use <value>; record in defaults_applied
    - if policy=ask: ask the caller before proceeding
    - if policy=refuse: return error code "missing_required_high_cost"

OUTPUT SCHEMA ADDITION
  defaults_applied: [
    {"field": "...", "value": "...", "rationale": "..."}
  ]
```

## Verification

- Every optional input has a row in DEFAULTS TABLE
- No high-cost field has policy=default
- Defaults match observed distribution, not theoretical defaults
- Output schema surfaces defaults; nothing is silent
