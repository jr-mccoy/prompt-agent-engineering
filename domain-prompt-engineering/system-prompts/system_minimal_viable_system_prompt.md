---
title: "Build the Minimal Viable System Prompt"
category: prompt-engineering/system-prompts
description: "Write the smallest possible system prompt that still produces acceptable outputs on a target task, then justify each surviving sentence."
techniques:
  - CM-01
  - QA-01
difficulty: intermediate
tags:
  - minimal
  - system-prompt
  - skinny
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/compression-and-cost/compression_system_prompt_skinnier.md
---

## Objective

Author the smallest system prompt that still passes a stated quality bar on representative inputs. Every surviving sentence is justified by a specific failure mode it prevents.

## When to Use

- A bloated system prompt has accreted over time
- Token cost on system messages is a meaningful share
- You want a defensible baseline before adding bells

## Inputs

1. The task and quality bar
2. 5+ representative inputs and expected behaviors
3. Maximum allowed token count for system prompt

## Constraints

**Must:**
- Start from a single role sentence
- Add only sentences that prevent a specific failure observed in iteration
- Test after each addition; stop when quality bar met
- Annotate each sentence with the failure it prevents

**Must Not:**
- Pre-load defensive language ("be helpful, be honest")
- Add formatting rules unless format is observably wrong
- Keep accreted text whose purpose is unclear

## Instructions

1. Start with `You are <role>` only.
2. Run on 5 inputs. Note failures.
3. Add the smallest sentence that fixes the most-impactful failure.
4. Re-run. Repeat.
5. Stop at quality bar or token cap.
6. Annotate each kept sentence.

## Output Format

```
ITERATION LOG
  v0: "<role only>" → failures: [...]
  v1: + "<added>" → failures: [...]
  v2: + "<added>" → failures: [...]
  ...
  vK: stable, quality bar met

FINAL MINIMAL PROMPT
<final sentences>

ANNOTATIONS
  s1: prevents <failure mode X>
  s2: prevents <failure mode Y>
  ...

DEFERRED
  - <sentence considered but rejected>: reason

TOKEN COUNT
  final: <n> ≤ cap
```

## Verification

- Every sentence is annotated with a failure it prevents
- The iteration log shows real evidence of each addition's value
- Token count under cap
- A held-out input passes with the final minimal prompt
