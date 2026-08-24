---
title: "Select Few-Shot Examples From a Corpus"
category: prompt-engineering/few-shot-examples
description: "Pick a small representative set of few-shot examples from a larger corpus, balancing coverage, diversity, difficulty, and prompt budget."
techniques:
  - PR-03
  - CM-01
difficulty: intermediate
tags:
  - few-shot
  - selection
  - coverage
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/few-shot-examples/fewshot_example_ordering.md
  - domain-prompt-engineering/few-shot-examples/fewshot_edge_case_pack_builder.md
---

## Objective

Choose K few-shot examples (typically 3–8) from a corpus of N (typically 50–10000) so they cover the input distribution, span difficulty, include at least one negative or edge case, and fit a token budget.

## When to Use

- A team has a corpus of accepted outputs and wants the most useful 3–8 as in-context examples
- A prompt is plateauing on quality; better example selection is suspected
- You need a defensible selection method (not "the first 5")

## Inputs

1. The corpus (each item: input, output, optional difficulty/label/source)
2. K (target example count)
3. Token budget per example (or total)
4. Coverage axes that matter (e.g., topic, length, intent, language)

## Constraints

**Must:**
- Pick examples that span all named coverage axes at least once
- Include at least one edge / non-canonical case
- Reject examples that exceed the token budget
- Document why each chosen example was picked

**Must Not:**
- Pick K nearest-neighbors of one prototype (collapses diversity)
- Include any example that contradicts the prompt's rules
- Use the same example twice in the K-set

## Instructions

1. Tag each corpus item against the coverage axes.
2. Stratified sampling: ensure at least one item per axis bucket.
3. Within axis buckets, pick by combination of: clarity, length-fit, output quality.
4. Add one deliberate edge or near-rejection example (not pure rejection).
5. Verify: do the K examples together cover all axes? Does the output budget hold?

## Output Format

```
COVERAGE AXES
  axis 1: <buckets and counts in corpus>
  axis 2: ...

CHOSEN EXAMPLES
  1. id <id> | input length: <n> | output length: <n>
     covers axes: [...]
     selection reason: ...
  ...

COVERAGE MAP
  axis × bucket: <count of chosen examples>

EDGE CASE
  example id: <id>
  type: <near-rejection | unusual-input | rare-format>

REJECTED CANDIDATES
  - id <id>: reason (over budget | duplicates axis | contradicts rule)

TOKEN TOTALS
  per-example: ...
  total: <under budget>
```

## Verification

- Every coverage axis has ≥1 example
- Total token cost ≤ budget
- Edge case is present and labeled
- No duplicate axis-cluster overrepresented
