---
title: "Minimal-Change Pass: Fix One Failure Without Regressing Others"
category: prompt-engineering/prompt-improvement
description: "Diagnose a specific failure in a prompt and propose the smallest possible change that fixes it while passing a regression set."
techniques:
  - QA-01
difficulty: advanced
tags:
  - minimal-change
  - regression-safe
  - surgical-edit
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/evaluation/regression/regression_change_impact_estimator.md
---

## Objective

When a prompt fails on one input class, propose the smallest change that fixes it without altering behavior on the regression set. Optimize for low blast radius.

## When to Use

- A prompt is in production and one failure mode needs fixing fast
- Larger refactors are blocked or risky
- You have a regression set you cannot regress

## Inputs

1. The current prompt
2. The failing input(s) and the desired behavior
3. The regression set (5+ inputs the current prompt handles correctly)
4. Constraints on what cannot change (e.g., output schema, refusal language)

## Constraints

**Must:**
- Propose ≤3 candidate changes ranked by blast radius
- Choose the smallest viable change
- For each candidate, predict its effect on each regression item
- Reject any candidate that risks regression unless evidence shows otherwise

**Must Not:**
- Refactor unrelated sections
- Rename variables, sections, or schema fields
- Change refusal language or safety rules

## Instructions

1. Localize the failure: which rule(s) caused it?
2. Generate up to 3 candidate fixes:
   - add a clause
   - add a `Must Not`
   - tighten an existing rule
3. For each candidate, walk the regression set mentally; mark each item `pass / risk / regress`.
4. Choose the candidate with no regressions and smallest token delta.
5. Emit a unified diff and the patched prompt.

## Output Format

```
LOCALIZATION
  failing rule(s): ...
  why current rule fails: ...

CANDIDATES
  candidate 1:
    change: <text>
    blast radius: <small | medium | large>
    regression effect:
      case 1: pass
      case 2: pass
      ...
    token delta: +<n> | -<n>

CHOSEN CANDIDATE: <id>

DIFF
  + <added line>
  - <removed line>

PATCHED PROMPT
<full prompt>

UNTESTED RISKS
  - <input class not in regression set that may now behave differently>
```

## Verification

- Chosen candidate has zero `regress` marks
- Token delta is minimal
- Untested risks are listed (not silently ignored)
- Refusal/safety language unchanged
