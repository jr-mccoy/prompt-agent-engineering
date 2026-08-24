---
title: "Self-Consistency Runner"
category: prompt-engineering/reasoning-strategies
description: "Sample N independent answers at temperature > 0, vote or aggregate, and emit the majority answer with disagreement signal."
techniques:
  - PR-02
  - QA-01
difficulty: advanced
tags:
  - self-consistency
  - sampling
  - voting
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/reasoning-strategies/reasoning_tree_of_thought_template.md
  - domain-prompt-engineering/hallucination-control/hallucination_self_consistency_check.md
---

## Objective

Run a single prompt N times at non-zero temperature, then aggregate by voting or summarization to produce a final answer plus a disagreement metric the caller can act on.

## When to Use

- The task has a small canonical answer set (numeric, classification, short string)
- A single sample's variance is too high
- Disagreement itself is signal (low confidence triggers human review)

## Inputs

1. The base prompt
2. N samples (typical 5–10)
3. Temperature for sampling
4. Aggregation rule: majority vote, weighted vote, semantic cluster, or summarize-and-pick

## Constraints

**Must:**
- Use identical prompt across samples; vary only sampling
- Define how to canonicalize answers before voting (trim whitespace, lowercase, normalize numbers)
- Emit majority answer plus a disagreement metric (entropy, top-2 share, or pairwise similarity for free-form)
- Surface disagreement when over a threshold

**Must Not:**
- Use this pattern for tasks with continuous-space answers without semantic clustering
- Hide disagreement when the caller might act differently if they knew
- Drop the disagreement signal in the final output

## Instructions

1. Define the canonicalizer for raw outputs.
2. Run N samples; collect canonicalized answers.
3. Vote (or cluster).
4. Compute disagreement metric.
5. Emit final answer + metric + sample count + threshold-flag.

## Output Format

```
SETUP
  prompt: <ref>
  N: <n>
  temperature: <t>
  aggregation: majority | weighted | semantic-cluster | summarize

SAMPLES (canonicalized)
  1. ...
  2. ...
  ...

AGGREGATION
  votes / clusters: ...
  winner: <answer>
  disagreement: <metric value>
  threshold: <t>
  flag: <below/above threshold>

FINAL ANSWER
<answer>

CONFIDENCE
  agreement_rate: <fraction>
  alternative_answers: [...]
  recommend_human_review: yes | no
```

## Verification

- Canonicalization is defined and applied identically
- Aggregation rule is named
- Disagreement is reported, not omitted
- Threshold-based flag is present so callers can route low-confidence cases
