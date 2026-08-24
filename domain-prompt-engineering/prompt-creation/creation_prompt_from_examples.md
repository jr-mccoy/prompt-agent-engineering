---
title: "Induce a Prompt From Accepted Outputs"
category: prompt-engineering/prompt-creation
description: "Reverse-engineer a prompt from 5+ accepted outputs by extracting shared structure, vocabulary, and constraints, then writing rules that produce them."
techniques:
  - ST-02
  - PR-03
difficulty: advanced
tags:
  - reverse-engineering
  - induction
  - examples-first
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/few-shot-examples/fewshot_example_selector.md
---

## Objective

Given a set of accepted outputs, derive a prompt that would have produced any of them. The prompt encodes the shared structure and vocabulary, not the specific content of any one example.

## When to Use

- The team has good output examples but no documented prompt
- A prompt was lost or never written down, and outputs need to be reproduced
- You are formalizing a tacit standard

## Inputs

1. 5+ accepted outputs of the target task
2. Optional: 2+ rejected outputs with reasons
3. Optional: known external constraints (compliance, brand)

## Constraints

**Must:**
- Identify structural elements present in ≥4/5 accepted outputs as required
- Identify vocabulary terms present in ≥3/5 as expected register
- Convert ≥3/5 patterns into Must rules; ≤2/5 patterns into Should
- Encode rejected-output patterns into Must Not rules
- Note examples where structural elements vary as `tolerated variance`

**Must Not:**
- Make a feature of one example into a requirement
- Invent constraints unsupported by the example set
- Encode incidental content (specific names, numbers) as part of the rule set

## Instructions

1. Tabulate features across examples (sections, length, headings, vocabulary, formality).
2. Compute frequency. Promote frequent features to Must; rarer to Should.
3. Extract banned patterns from rejected examples.
4. Draft the prompt: role consistent with output style; rules from frequencies.
5. Test by predicting features of held-out examples.

## Output Format

```
FEATURE FREQUENCY TABLE
  feature | freq | role (must|should|tolerated)

PROMPT DRAFT
  Role: ...
  Task: ...
  Constraints:
    Must: ...
    Should: ...
    Must Not: ... (from rejections)
  Output Format: ...
  Verification: ...

TOLERATED VARIANCE
  - <feature>: <observed range>

UNCERTAIN
  - <feature>: too few examples to decide
```

## Verification

- Every Must rule appears in ≥4/5 inputs
- Every Must Not rule traces to a rejection (or is left out)
- Tolerated variance is documented, not silently encoded
- The draft predicts the held-out example's features with stated accuracy
