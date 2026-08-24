---
title: "Eliminate Redundancy in a Prompt"
category: prompt-engineering/prompt-improvement
description: "Find duplicated instructions in a prompt, classify each as harmless / redundant / conflicting, and consolidate without losing intent."
techniques:
  - CM-01
difficulty: intermediate
tags:
  - redundancy
  - cleanup
  - rewriting
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/prompt-improvement/improve_conflict_resolver.md
  - domain-prompt-engineering/compression-and-cost/compression_lossless_rewrite.md
---

## Objective

Identify rules and statements that repeat across a prompt, classify each repetition, and consolidate while preserving any intentionally redundant safety or robustness duplications.

## When to Use

- A prompt has grown by accretion and exceeds what it needs to say
- You suspect rules are being said three different ways with subtle drift
- You want to compress before fixing other issues

## Inputs

1. The current prompt
2. Notes on which (if any) duplications are intentional (e.g., "say 'no PII' twice for emphasis")

## Constraints

**Must:**
- Cluster near-duplicate rules
- Classify each cluster: `harmless` (delete extras), `redundant-but-intended` (keep), `conflicting` (escalate to conflict-resolver)
- For `harmless` deletions, choose the canonical statement based on specificity
- Track every deletion

**Must Not:**
- Delete an intentional duplication without confirming it is harmless
- Merge two rules that have different scope, even if wording is similar
- Silently rewrite kept statements

## Instructions

1. Scan the prompt sentence by sentence. Cluster sentences that say roughly the same thing.
2. For each cluster, mark intent (harmless / intended / conflicting).
3. For harmless clusters, pick the canonical (most specific, most operational) statement.
4. For conflicting clusters, do not resolve here — flag for conflict-resolver.
5. Emit the cleaned prompt and the deletion log.

## Output Format

```
CLUSTERS
  cluster 1:
    sentences: [...]
    classification: harmless | intended | conflicting
    canonical (if harmless): "<chosen sentence>"
    rationale: ...

DELETIONS
  - line <n>: "<text>" (duplicate of line <m>)
  - ...

KEPT REDUNDANCIES
  - line <n> + line <m>: <reason>

ESCALATED TO CONFLICT-RESOLVER
  - cluster <id>: <why conflicting>

CLEANED PROMPT
<full prompt with deletions applied>

TOKEN DELTA
  before: <n>
  after: <n>
```

## Verification

- No `conflicting` cluster was silently merged
- Every deletion is logged with the duplicate it replaces
- Kept redundancies have a stated reason
- The cleaned prompt produces equivalent behavior on a sample input
