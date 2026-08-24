---
title: "Self-Check Pattern: Answer, Then Verify"
category: prompt-engineering/reasoning-strategies
description: "Add a self-verification pass to a prompt where the model produces an answer, then checks it against named criteria, then revises or confirms."
techniques:
  - QA-01
difficulty: intermediate
tags:
  - self-check
  - verification
  - revision
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/reasoning-strategies/reasoning_premise_check_pattern.md
---

## Objective

Build a prompt that produces a draft answer, runs it against named verification criteria, and either confirms or revises before returning. The verification step is structured, not vibes-based.

## When to Use

- The task has known failure patterns the model can detect after generation
- You want a single-prompt alternative to a planner+critic chain
- Quality gain from self-check exceeds the latency cost

## Inputs

1. The task
2. The verification criteria (3–6 named checks)
3. Maximum revision rounds (default 1)

## Constraints

**Must:**
- Produce DRAFT, then SELF-CHECK, then either CONFIRMED or REVISED
- Express each check as a yes/no question with a one-line rationale
- If any check fails, revise once and re-check
- After max rounds, surface remaining failures honestly rather than hiding

**Must Not:**
- Replace genuine self-check with a generic "I have reviewed this" line
- Skip self-check when checks pass without listing them
- Loop revision indefinitely

## Instructions

1. Define checks. Each must be answerable yes/no from the draft.
2. Cap revision rounds.
3. Specify the final emission format with a `self_check_log`.
4. On unfixable failures, surface them with `unresolved_issues`.

## Output Format

```
DRAFT
<draft answer>

SELF-CHECK
  - check 1: <question> | answer: yes/no | reason: ...
  - check 2: ...
  - ...

DECISION: confirmed | revised

REVISED ANSWER (if revised)
<revised answer>

POST-REVISION SELF-CHECK
  ...

FINAL ANSWER
<final answer>

SELF_CHECK_LOG
  rounds: <n>
  checks_run: <n>
  failures_remaining: [...]

UNRESOLVED_ISSUES (if any)
  - <issue>: <why it persists>
```

## Verification

- All checks are yes/no with rationale
- Revisions are capped
- Final answer is consistent with the post-revision self-check
- Unresolved issues are surfaced, not hidden
