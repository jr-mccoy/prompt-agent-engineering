---
title: "Restructure for Prompt-Cache Hits"
category: prompt-engineering/compression-and-cost
description: "Reorder a prompt so the longest stable prefix is at the front, maximizing cache hit length and amortizing token cost."
techniques:
  - CM-01
difficulty: intermediate
tags:
  - prompt-caching
  - prefix
  - latency
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/prompt-creation/creation_user_prompt_template_designer.md
---

## Objective

Increase the stable prefix length of a prompt by moving variable content as late as possible, so prompt caching reuses the maximum byte-identical prefix on subsequent calls.

## When to Use

- Using a model/provider that supports prompt caching
- A prompt is called many times with small variations near the top
- Latency or cost wins from cache hits are large

## Inputs

1. The current prompt
2. List of variable elements (per-call) and stable elements
3. Caching minimum prefix length the provider requires

## Constraints

**Must:**
- Identify every variable element and its position
- Reorder to push variables as late as feasible without breaking semantics
- Keep system rules and refusal policy in the stable prefix
- Verify behavior unchanged on regression set

**Must Not:**
- Move safety/refusal content out of the stable prefix
- Reorder if it degrades comprehension materially
- Misorder examples in a way that changes their effect

## Instructions

1. Tag elements as STABLE or VARIABLE.
2. Build the new order: STABLE first, VARIABLE last.
3. Within STABLE, preserve semantic ordering (Role → Rules → Format → Examples).
4. Within VARIABLE, place the most-likely-to-change last.
5. Compute stable prefix length; verify ≥ provider minimum.
6. Run regression set.

## Output Format

```
STABLE / VARIABLE TAGGING
  - <element>: STABLE
  - <element>: VARIABLE

REORDERED PROMPT
<full prompt with stable first, variable last>

STABLE PREFIX
  length: <chars / tokens>
  exceeds provider minimum: yes | no

CACHING ESTIMATE
  expected hit rate: <fraction> (based on variable distribution)
  cost saved per hit: <tokens × rate>

REGRESSION RESULTS
  - all cases match: yes | no
```

## Verification

- Variables sit after the stable prefix
- Safety/refusal in stable prefix
- Prefix exceeds provider minimum
- Regression set passes
