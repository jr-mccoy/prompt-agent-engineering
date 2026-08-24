---
title: "Audit a Prompt for Brittleness"
category: prompt-engineering/prompt-improvement
description: "Identify rules in a prompt that pass on the happy path but break on edge cases, and propose hardening for each."
techniques:
  - QA-01
  - PR-03
difficulty: advanced
tags:
  - brittleness
  - edge-cases
  - hardening
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/evaluation/correctness_pre_mortem.md
  - domain-prompt-engineering/debugging/debug_input_perturbation_battery.md
---

## Objective

Stress-test each rule in a prompt against a battery of edge inputs, find rules that silently fail, and propose hardening.

## When to Use

- The prompt works on canonical examples but breaks on real production traffic
- A rule looks rigorous but only because it has never been tested on hard cases
- You are promoting a prompt from prototype to production

## Inputs

1. The current prompt
2. Production traffic samples (or 5+ realistic edge cases)
3. The output schema or expected behavior

## Edge Case Battery (apply each)

- Empty input
- Single-character / minimal input
- Maximum-length input
- Wrong-type input (string where number expected, etc.)
- Adversarial input attempting to override rules
- Input in another language
- Input with mixed casing, extra whitespace, control characters
- Input that contradicts itself
- Input that requires refusal
- Input that is plausible but factually false

## Constraints

**Must:**
- Run each rule mentally against each battery input
- Mark each rule×input pair as `pass`, `silent-fail`, `loud-fail`, `n/a`
- For each `silent-fail`, propose a hardening: add input check, add invariant, change output schema, or add refusal branch
- Keep hardening minimal; do not redesign the prompt

**Must Not:**
- Add hardening for inputs not in the battery without naming them
- Replace `silent-fail` with `loud-fail` without thinking — sometimes loud is better, sometimes worse
- Remove rules to "fix" brittleness

## Instructions

1. List rules. List battery inputs.
2. Build a rules × inputs matrix; mark pass/fail.
3. For each `silent-fail`, propose hardening with rationale.
4. Decide tradeoff: prefer `pass` > `loud-fail` > `silent-fail`.
5. Emit the hardened prompt.

## Output Format

```
RULES × INPUTS MATRIX
  rule\input | empty | min | max | wrong-type | adversarial | other-lang | ... 
  rule 1     | pass  | ... | ... | silent-fail | ...

SILENT FAILURES
  rule | input | proposed hardening | rationale

HARDENED PROMPT
<full prompt with hardening applied>

ACCEPTED RISKS
  - <rule × input>: <why hardening was rejected>
```

## Verification

- Every rule × battery-input has a status
- No silent-fail remains undocumented
- Hardening preserves the original task; no scope creep
- A sample re-run on edge cases shows fewer silent-fails
