---
title: "Migrate a Prompt Within a Model Family"
category: prompt-engineering/model-optimization
description: "Move a prompt from one model version to its successor (e.g., Sonnet 4.6 → 4.7) by checking deprecated patterns, new capabilities, and behavior diffs."
techniques:
  - QA-01
difficulty: intermediate
tags:
  - migration
  - within-family
  - upgrade
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/model-optimization/modelopt_retired_model_replacement.md
---

## Objective

Update a prompt for a successor model in the same family: identify behaviors that changed, opportunities to use new capabilities, and patterns that became unnecessary.

## When to Use

- A new model version drops in the family you use
- A team needs a structured upgrade process
- Regression testing on a model bump

## Inputs

1. Current prompt (working on version X)
2. Target version Y (successor)
3. Release notes or known-behavior diffs
4. Regression set

## Constraints

**Must:**
- Read release notes for behavior changes
- Run regression set on the new version
- Identify outputs that changed and decide whether the change is improvement or regression
- For improvements, simplify prompt (remove now-unnecessary scaffolding)
- For regressions, propose targeted fixes (add a rule, sharpen an instruction)

**Must Not:**
- Assume identical behavior across versions
- Remove rules without evidence the new model handles them natively
- Skip refusal-set checks (refusal behavior shifts often)

## Instructions

1. Run regression on Y; compare to X outputs.
2. Categorize each diff: improvement / regression / neutral.
3. For improvements: trim the prompt where possible.
4. For regressions: add targeted rules.
5. Document the bump in changelog.

## Output Format

```
MIGRATION FROM <X> TO <Y>

REGRESSION COMPARISON
  case | X output (digest) | Y output (digest) | classification
  c1   | ...               | ...               | improvement | regression | neutral

PROMPT CHANGES
  - removed: <text> | reason: <Y handles natively>
  - added: <text> | reason: <fixes regression on case c2>

NEW CAPABILITIES TO LEVERAGE
  - <capability>: applied to <section>

CHANGELOG
  - <prompt v>: migrated from <X> to <Y>; <summary>

REMAINING CONCERNS
  - <case>: still differs in <way>; tolerate or address later
```

## Verification

- Every regression case classified
- Trims have evidence
- Added rules trace to specific regressions
- Changelog records the migration
