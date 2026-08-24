---
title: "Design a Progressive-Disclosure Prompt"
category: prompt-engineering/prompt-creation
description: "Build a prompt that opens minimal, expands on signal, and only loads detailed instructions when triggers fire."
techniques:
  - ST-02
  - CM-01
difficulty: advanced
tags:
  - progressive-disclosure
  - conditional
  - token-budget
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/compression-and-cost/compression_system_prompt_skinnier.md
---

## Objective

Produce a prompt that loads only the instructions needed for the input it receives. Detailed handling for rare cases sits behind triggers, keeping the common path fast and cheap.

## When to Use

- The prompt has many branches, most of which fire rarely
- You are paying for tokens on every call but only some calls need full detail
- A monolithic prompt has become unreadable

## Inputs

1. Current prompt (or instruction set)
2. Frequency estimate per branch (which cases dominate)
3. Acceptable failure rate on cold-path cases

## Constraints

**Must:**
- Define the hot-path prompt (handles the dominant cases)
- Define triggers that route to expanded instructions
- Specify how the expanded block is delivered (in-prompt section, second call, retrieved snippet)
- Keep the hot path under a stated token budget

**Must Not:**
- Use vague triggers like "if needed" — every trigger must be a falsifiable check on input
- Hide safety-critical rules behind triggers
- Allow the cold path to silently degrade hot-path behavior

## Instructions

1. Sort branches by frequency.
2. Place the top 1–3 branches in the hot path inline.
3. For each remaining branch, write a one-line trigger and a separate expansion block.
4. Decide for each cold branch: load inline at trigger, or escalate to a second call.
5. Verify the hot path alone handles the most common case correctly.

## Output Format

```
HOT PATH (always present, target ≤ <n> tokens)
<minimal prompt covering top branches>

TRIGGERS → EXPANSIONS
  - trigger: <falsifiable check>
    expansion: <inline | second-call | retrieve>
    block:
      <expanded instructions>

ALWAYS-ON SAFETY RULES
<rules that must never be gated behind triggers>

BUDGET
  Hot path: <tokens>
  Cold paths: <range>
```

## Verification

- Hot path alone passes the dominant-case test
- No safety rule sits behind a trigger
- Each trigger is a falsifiable input check, not a vibe
- Total tokens for hot path are under the stated budget
