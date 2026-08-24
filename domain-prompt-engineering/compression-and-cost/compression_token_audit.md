---
title: "Token Audit of an Existing Prompt"
category: prompt-engineering/compression-and-cost
description: "Find the highest-cost low-value sections of a prompt and rank them for compression based on observed token weight."
techniques:
  - CM-01
difficulty: intermediate
tags:
  - tokens
  - audit
  - compression
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/compression-and-cost/compression_lossless_rewrite.md
---

## Objective

Decompose a prompt into measurable sections, count tokens per section, and rank sections by compression candidate score (high tokens × low load-bearing).

## When to Use

- A prompt is over budget or paying noticeable inference cost
- A team wants targets for the next compression pass
- You need a defensible audit for a review

## Inputs

1. The prompt
2. Token counter (tiktoken / model tokenizer)
3. Section labels (Role, Constraints, Output Format, Examples, Verification, etc.)

## Constraints

**Must:**
- Count tokens per labeled section
- Rate each section's load-bearing on a 1–5 scale with rationale
- Compute candidate score = tokens × (6 − load_bearing)
- Rank sections by candidate score
- Surface the top 3 candidates for compression

**Must Not:**
- Recommend deleting safety or refusal sections regardless of score
- Use heuristic byte counts when a real tokenizer is available
- Compress without naming what behavior could regress

## Instructions

1. Split the prompt into labeled sections.
2. Token-count each.
3. Rate load-bearing per section.
4. Compute candidate score and rank.
5. For top 3, name the specific compression strategy and the regression risk.

## Output Format

```
SECTION TABLE
  section | tokens | load_bearing (1-5) | candidate_score | notes

TOP CANDIDATES
  1. <section> | tokens=<n> | load=<n> | score=<n>
     strategy: <lossless | lossy with test | restructure>
     regression risk: <named risk>
  2. ...
  3. ...

EXCLUDED
  - safety/refusal: not eligible regardless of score

TOTAL
  current tokens: <n>
  potential reduction: <n> (if all top candidates compressed at projected ratios)
```

## Verification

- Token counts come from a real tokenizer
- Load-bearing rationale per section
- Top-3 candidates have named strategy and risk
- Safety/refusal excluded
