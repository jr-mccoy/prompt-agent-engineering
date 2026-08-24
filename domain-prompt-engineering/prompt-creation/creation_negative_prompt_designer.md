---
title: "Design the Negative Half of a Prompt"
category: prompt-engineering/prompt-creation
description: "Produce a ranked, falsifiable Must-Not list derived from real rejected outputs and known failure patterns."
techniques:
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - negative-prompt
  - must-not
  - failure-modes
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/style-and-voice/style_anti_voice_designer.md
  - domain-prompt-engineering/evaluation/correctness_pre_mortem.md
---

## Objective

Build the `Must Not` block of a prompt as a first-class artifact: ranked, evidenced by real rejections, and structured so each rule is checkable from output alone.

## When to Use

- The prompt's positive instructions are clear but failures keep happening
- A reviewer rejects on specific patterns the prompt does not name
- You are hardening a prompt before shipping

## Inputs

1. 5+ rejected outputs with reasons
2. The current prompt
3. Brand or compliance lists of forbidden words/topics, if any

## Constraints

**Must:**
- Cluster rejections into pattern groups
- Express each rule as `Do not <verb> <object> when <condition>`
- Pair each rule with a falsifiable check (regex, structural, pairwise, human)
- Rank by severity: safety > legal > correctness > format > style
- Keep the list tight; merge near-duplicates

**Must Not:**
- Write `Must Not` rules that are unfalsifiable ("do not be biased", "do not be unhelpful")
- Add rules that contradict the existing positive instructions
- Inflate the list with rules unsupported by real evidence

## Instructions

1. Read all rejections. Cluster by cause.
2. For each cluster, write one rule with a check method.
3. Rank by severity and group.
4. Cross-check against existing positive instructions for conflicts.
5. Drop any rule with no real evidence.

## Output Format

```
MUST NOT (ranked)

[safety]
  - <rule> | check: <method> | evidence: <rejection ids>

[legal]
  - ...

[correctness]
  - ...

[format]
  - ...

[style]
  - ...

CONFLICTS WITH EXISTING POSITIVE RULES
  - <rule> conflicts with <positive rule>: <resolution>

DROPPED CANDIDATES
  - <candidate> — reason: no evidence
```

## Verification

- Every rule traces to at least one real rejection
- Every rule has a check method
- No two rules contradict each other
- No rule contradicts a kept positive instruction
