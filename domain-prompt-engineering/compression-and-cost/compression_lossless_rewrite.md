---
title: "Lossless Compression Rewrite"
category: prompt-engineering/compression-and-cost
description: "Rewrite a prompt to reduce tokens while preserving identical behavior on the regression set."
techniques:
  - CM-01
  - QA-01
difficulty: intermediate
tags:
  - lossless
  - compression
  - tokens
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/prompt-improvement/improve_idempotent_rewrite.md
  - domain-prompt-engineering/compression-and-cost/compression_lossy_with_test_set.md
---

## Objective

Reduce a prompt's token count without changing its behavior on a stated regression set. Output: rewritten prompt + token delta + behavior verification.

## When to Use

- Token budget is the binding constraint
- A prompt has verbose phrasings that can shorten without losing meaning
- You want a safe baseline before considering lossy compression

## Inputs

1. The current prompt
2. Regression set with expected outputs
3. Equivalence tolerance (exact, semantic, structural)

## Lossless Techniques

- Replace long phrases with shorter equivalents ("In order to" → "To")
- Convert repeated paragraphs into single rules
- Replace examples that demonstrate the same lesson
- Convert prose lists into tight bullets
- Remove polite scaffolding ("Please ensure that you...")
- Use tags / placeholders instead of repeated literal sections

## Constraints

**Must:**
- Preserve every load-bearing instruction
- Keep refusal/safety language verbatim where operative
- Validate against regression set; all outputs must equivalence-match
- Report token delta

**Must Not:**
- Drop any rule
- Change vocabulary in safety rules
- Cross from lossless into lossy without explicit consent

## Instructions

1. Apply each technique in turn; record token savings.
2. After each technique, mentally re-run regression set; abort change on any deviation.
3. Combine accepted changes.
4. Final-check: token count, equivalence on regression set.

## Output Format

```
TECHNIQUE LOG
  technique 1 (phrase shortening):
    examples:
      - "In order to" → "To"
      - "It is important that" → "Must"
    tokens saved: <n>
  technique 2 (rule consolidation):
    ...
  ...

REWRITTEN PROMPT
<full rewrite>

TOKEN DELTA
  before: <n>
  after: <n>
  reduction: <n> (<percent>%)

REGRESSION RESULTS
  case 1: <expected> | actual: <actual> | match: yes
  ...
```

## Verification

- Token reduction is real (real tokenizer used)
- Every regression case matches
- No technique logged without saved tokens
- Refusal language preserved verbatim
