---
title: "Change Impact Estimator"
category: prompt-engineering/evaluation/regression
description: "Predict which test cases a specific prompt change is likely to affect before running them, to prioritize test execution and reduce evaluation cost."
techniques:
  - ST-02
  - ST-03
  - CM-02
  - RT-05
  - DT-01
difficulty: intermediate
tags:
  - change_impact
  - regression_testing
  - test_prioritization
  - prompt_diff
  - eval_efficiency
updated: "2026-05-11"
related_prompts:
  - domain-prompt-engineering/evaluation/regression/regression_golden_set_curator.md
  - domain-prompt-engineering/evaluation/regression/regression_ab_test_runner_prompt.md
  - domain-prompt-engineering/evaluation/correctness_prompt_specification_audit.md
---

## Objective

Given a prompt diff (before → after) and a test case inventory, predict which cases the change is likely to affect, rank them by impact probability, and produce a prioritized run order. Reduces evaluation cost by running high-risk cases first and deferring low-risk cases.

## When to Use

- Before running a full regression suite after a prompt change
- When the full eval suite is expensive (>10 min or >$1) and you need a fast signal
- When validating that a "safe" edit (e.g., formatting change) truly has no behavioral impact
- During iterative prompt development to tighten the feedback loop

## Inputs

| Field | Required | Description |
|-------|----------|-------------|
| `prompt_before` | Yes | Full text of the prompt before the change |
| `prompt_after` | Yes | Full text of the prompt after the change |
| `test_case_inventory` | Yes | List of test cases with IDs, input descriptions, and behavior tags |
| `change_description` | Optional | Human-readable description of intent behind the change |

## Constraints

**Must:**
- Classify the change by type (see taxonomy) before predicting impact
- Assign every test case an `impact_probability`: `high` / `medium` / `low` / `none`
- Provide a written rationale for every `high` classification
- Output a ranked run order: high first, then medium, then low, skip none
- Estimate the expected number of affected cases as a count, not a %

**Must Not:**
- Classify all cases as `high` — must apply discriminating criteria
- Assign `none` to cases whose behavior cluster directly corresponds to the changed section
- Skip the change-type classification step

## Instructions

**Step 1 — Diff classification**

Classify the change using the taxonomy:

| Code | Change type | Typical impact |
|------|-------------|----------------|
| C1 | Instruction added | Cases testing the new behavior: high; others: low |
| C2 | Instruction removed | Cases relying on removed behavior: high; others: low |
| C3 | Instruction reworded (same intent) | Cases exercising exact phrasing: medium; others: low |
| C4 | Constraint changed (tightened) | Cases near the constraint boundary: high; others: low |
| C5 | Constraint changed (loosened) | Cases testing the old boundary: high; others: medium |
| C6 | Output format changed | Cases checking output structure: high; content cases: low |
| C7 | Role/persona changed | All persona-dependent cases: high |
| C8 | Example added/changed | Cases similar to the example: medium; dissimilar: low |
| C9 | Multi-section compound | Classify each section independently; take max per case |

**Step 2 — Case impact scoring**

For each test case:
1. Extract its `behavior_tags` from the inventory
2. Map those tags against the changed section using the taxonomy
3. Assign impact probability:

| Assignment rule | Probability |
|-----------------|-------------|
| Changed section directly governs this behavior | `high` |
| Changed section has side-effects on this behavior | `medium` |
| Changed section is semantically adjacent | `low` |
| Changed section has no logical connection | `none` |

**Step 3 — Prioritized run order**

Output a ranked list:
```
Priority 1 (high impact, run first):
  GS-007: <behavior description> — rationale: <why this is high>
  GS-012: <behavior description> — rationale: <why this is high>
  ...

Priority 2 (medium impact):
  GS-003: ...
  ...

Priority 3 (low impact, run if time permits):
  ...

Skip (estimated none):
  GS-002, GS-005, ...
```

**Step 4 — Impact summary**

| Priority | Case count | Estimated run time | Notes |
|----------|------------|-------------------|-------|
| High | N | X min | Must run before shipping |
| Medium | N | X min | Run if high passes |
| Low | N | X min | Run on full regression only |
| Skip | N | 0 | Document rationale |

**Step 5 — Calibration note**

After running, record actual failures per priority tier. Track over time:
- `high` tier actual failure rate (target: ≥60%)
- `none` tier actual failure rate (target: 0%)

If either target is missed consistently, revise the impact-scoring criteria.

## Output Format

1. **Change classification** — type code(s) and description
2. **Case impact table** — case ID, behavior tags, impact probability, rationale
3. **Prioritized run order** — grouped list as shown in Step 3
4. **Impact summary table** — counts and estimated time per tier
5. **Calibration row** — empty columns for actual failure rates, filled post-run

## Verification

- [ ] Change classified by type code before impact assignments
- [ ] Every `high` classification has a written rationale
- [ ] No behavior cluster directly corresponding to the changed section assigned `none`
- [ ] `none` tier documented with brief rationale for each case
- [ ] Impact summary includes estimated run time per tier
