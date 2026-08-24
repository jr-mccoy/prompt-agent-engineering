---
title: "Audit Few-Shot Examples for Contamination and Overfit"
category: prompt-engineering/few-shot-examples
description: "Detect when few-shot examples are causing the prompt to overfit to surface features that do not generalize."
techniques:
  - QA-01
  - PR-03
difficulty: advanced
tags:
  - contamination
  - overfit
  - few-shot
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/few-shot-examples/fewshot_example_selector.md
---

## Objective

Identify whether the chosen few-shot examples are leaking incidental properties (specific names, numbers, lengths, phrasing) into outputs in ways that fail on real inputs.

## When to Use

- New inputs produce outputs that copy phrases or numbers from few-shot examples
- The prompt scores well on test inputs that resemble examples but poorly elsewhere
- A reviewer notices the model "is just imitating example 3"

## Inputs

1. The current few-shot pack
2. 5+ recent outputs on real inputs
3. The list of example outputs

## Contamination Symptoms

- Direct quotation of example text in non-example outputs
- Same numeric values appearing across unrelated outputs
- Output length tracking example length more than input demands
- Style anomalies (idiom, punctuation) shared across outputs
- Refusal language matching one example's specific phrasing

## Constraints

**Must:**
- For each symptom, count occurrences across recent outputs
- Tag confirmed contamination with the example responsible
- Propose a fix: rewrite example to be less specific, swap with a more diverse one, or convert to a rule

**Must Not:**
- Conclude contamination from a single occurrence
- Remove examples without checking if they are also load-bearing
- Confuse desired imitation (output schema) with contamination (incidental detail)

## Instructions

1. Diff recent outputs against example outputs at sentence and entity level.
2. Cluster recurring leakage by which example seeds it.
3. For each cluster, classify as `desired imitation` or `contamination`.
4. Propose example rewrites that keep structure but anonymize incidentals.
5. Re-run mentally on real inputs to confirm contamination decreases.

## Output Format

```
LEAKAGE CLUSTERS
  cluster 1:
    pattern: "<phrase | entity | length pattern>"
    seed example: <id>
    occurrences in 5 recent outputs: <count>
    classification: contamination | desired imitation

REWRITES
  example <id>:
    before: ...
    after: ...
    incidentals removed: [...]

REPLACEMENTS
  - example <id> → swap with <new id>: <reason>

EXAMPLES KEPT AS-IS
  - <id>: leakage is desired imitation (output schema)
```

## Verification

- Each contamination cluster has ≥2 occurrences across outputs
- Rewrites preserve structural lessons while removing incidentals
- Desired-imitation clusters are documented and not "fixed"
- Predicted contamination drop is stated for each rewrite
