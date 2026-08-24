---
title: "Generate Synthetic Few-Shot Examples"
category: prompt-engineering/few-shot-examples
description: "Build few-shot examples when no corpus exists, with explicit diversity targets and a quality gate."
techniques:
  - PR-03
  - QA-01
difficulty: advanced
tags:
  - synthetic
  - few-shot
  - bootstrapping
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/few-shot-examples/fewshot_example_selector.md
  - domain-prompt-engineering/evaluation/eval-datasets/dataset_synthetic_case_generator.md
---

## Objective

When real examples are unavailable, generate synthetic input/output pairs that the team will validate, with explicit diversity coverage and a quality gate before any are used in production prompts.

## When to Use

- Greenfield prompt with no corpus yet
- Sensitive domain where real examples cannot be exposed
- Pilot phase before production logs accumulate

## Inputs

1. Task description and output schema
2. Coverage axes (topic, intent, length, style, language)
3. Quality gate: who validates each candidate, against what rubric
4. Target K examples and overprovision factor (e.g., generate 3K, keep best K)

## Constraints

**Must:**
- Generate against named coverage axes; each candidate is tagged on creation
- Generate in batches of ≤10 to avoid mode collapse within a single call
- Vary surface form (sentence structure, vocabulary, register) within each batch
- Pass every candidate through the quality gate; only keep gate-pass examples
- Mark every example as `synthetic` in metadata so it never gets used as ground-truth eval

**Must Not:**
- Use synthetic examples as eval ground truth without separate human approval
- Mix real and synthetic without provenance tags
- Generate examples that copy verbatim from any source

## Instructions

1. Define K and 3K (overprovisioning).
2. For each coverage bucket, request batch generation with explicit constraints.
3. Tag each candidate with axis bucket and surface-form variation.
4. Apply quality gate; record each candidate's pass/fail.
5. Pick K from gate-pass set, balancing axes.

## Output Format

```
COVERAGE PLAN
  axis × bucket → target candidates

GENERATED CANDIDATES
  id | bucket | surface variation | gate result | notes

KEPT EXAMPLES (K)
  id | bucket | input | output | metadata.synthetic: true

REJECTED
  id | reason (gate fail | duplicate | over-budget)

PROVENANCE
  source: synthetic
  generator: <model + version>
  date: ...
  validator: ...
```

## Verification

- Every kept example has metadata.synthetic = true
- Coverage map has ≥1 example per bucket
- Quality gate was applied to every candidate
- No verbatim copies from external sources
