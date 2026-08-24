---
title: "Produce Terse and Verbose Variants of the Same Prompt"
category: prompt-engineering/prompt-creation
description: "Author two variants of a prompt — minimal and full — that produce equivalent outputs and let callers pick by latency or cost budget."
techniques:
  - ST-02
  - CM-01
difficulty: intermediate
tags:
  - variants
  - terse
  - verbose
  - budget
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/compression-and-cost/compression_lossless_rewrite.md
---

## Objective

Take a working prompt and produce two registered variants — terse and verbose — that share output schema and verification but differ in token footprint. Document when each is preferred.

## When to Use

- Some calls run on cheap models or in tight budgets, others can afford full prompts
- A team wants to standardize on one prompt but accept two physical implementations
- You are A/B testing prompt length effects

## Inputs

1. The working prompt (full version)
2. Output schema (must be identical across variants)
3. Acceptable degradation in quality between variants

## Constraints

**Must:**
- Produce a terse variant under a stated token cap
- Preserve the output schema exactly
- Identify which sentences in the verbose version are load-bearing (kept in terse) vs scaffolding (cut in terse)
- Document the expected quality delta with at least one observable difference

**Must Not:**
- Drop safety rules in the terse variant
- Drop verification in the terse variant (compress it instead)
- Change the output schema to enable terseness

## Instructions

1. Mark each sentence in the verbose prompt as load-bearing or scaffolding.
2. Build the terse variant from load-bearing sentences only.
3. Compress verification to a one-line checklist if needed.
4. Write a one-paragraph "when to use which" guide for callers.
5. Run both on three sample inputs and record observed differences.

## Output Format

```
VERBOSE VARIANT
<full prompt>
  token_estimate: <n>

TERSE VARIANT
<minimal prompt>
  token_estimate: <n>

LOAD-BEARING MAP
  - "<sentence>" → kept (reason)
  - "<sentence>" → cut (reason)

WHEN TO USE WHICH
  Use terse when: ...
  Use verbose when: ...
  Quality delta observed:
    - input class A: <difference>
    - input class B: <difference>

OUTPUT SCHEMA (shared)
<schema>
```

## Verification

- Terse variant fits the stated token cap
- Output schema is byte-identical between variants
- No safety rule was dropped
- Quality-delta documentation cites concrete examples, not adjectives
