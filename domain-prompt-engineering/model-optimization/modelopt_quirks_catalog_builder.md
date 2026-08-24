---
title: "Build a Quirks Catalog for a Model"
category: prompt-engineering/model-optimization
description: "Catalog observed model-specific behaviors (quirks, tics, biases) with reproductions and recommended prompt-side mitigations."
techniques:
  - QA-01
difficulty: intermediate
tags:
  - quirks
  - model-behavior
  - catalog
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/model-behavior/modelbehavior_instruction_deviation_diagnostic.md
---

## Objective

Document observed quirks of a specific model — recurring stylistic tics, output biases, formatting drift, refusal patterns, hallucination shapes — with reproductions and prompt-side mitigations.

## When to Use

- A team uses one model heavily and accumulates "things to know"
- New authors keep running into the same surprises
- Model upgrades may resolve some quirks; tracking helps know what to retest

## Inputs

1. The target model
2. Observations from production or testing
3. Existing prompts that work around quirks

## Constraints

**Must:**
- Document each quirk with: name, description, reproduction prompt, observed behavior, mitigation
- Tag severity (high / medium / low)
- Date the entry; quirks may change with model updates
- Link mitigations to prompts in the library that already apply them

**Must Not:**
- File rare-event observations as confirmed quirks (need ≥3 reproductions)
- Document mitigations that have not been tested
- Mix quirks of different model versions in the same entry

## Instructions

1. For each candidate quirk, get ≥3 reproductions.
2. Write reproduction prompt that reliably triggers it.
3. Write the mitigation: prompt rule, schema choice, structure pattern.
4. Tag severity and date.
5. Add cross-references.

## Output Format

```
QUIRKS CATALOG: <model name + version>

ENTRY 1
  name: <short label>
  description: <one-paragraph>
  severity: high | medium | low
  reproduction_prompt: |
    <prompt that reliably triggers the quirk>
  observed_behavior: |
    <what the model does>
  mitigation:
    pattern: <prompt-side fix>
    example_application: <link to prompt using it>
  date_observed: ...
  date_last_confirmed: ...

ENTRY 2
  ...

REVIEW SCHEDULE
  re-test catalog on every model bump in this family.
```

## Verification

- Each entry has reproduction, observed behavior, and mitigation
- Severity tagged
- Dates included
- Reproductions reproduced ≥3 times
