---
title: "Canary Set Designer"
category: prompt-engineering/evaluation/regression
description: "Design a small, fast-running canary test set (5–15 cases) that catches major regressions early, with run-time targets, sensitivity requirements, and triage protocol."
techniques:
  - ST-02
  - ST-03
  - CM-02
  - QA-10
  - QA-11
difficulty: intermediate
tags:
  - canary_set
  - regression_testing
  - fast_eval
  - ci_cd
  - test_prioritization
updated: "2026-05-11"
related_prompts:
  - domain-prompt-engineering/evaluation/regression/regression_golden_set_curator.md
  - domain-prompt-engineering/evaluation/regression/regression_change_impact_estimator.md
  - domain-prompt-engineering/evaluation/correctness_eval_design_prompt.md
---

## Objective

Design a minimal canary test set — 5 to 15 cases — that is fast enough to run on every prompt change (target: <60 seconds or <$0.10) while sensitive enough to catch major regressions before they reach the full suite or production. Output is a prioritized set with run-time estimates, failure thresholds, and a triage protocol for canary failures.

## When to Use

- Setting up CI/CD gates for prompt changes
- When the full regression suite is too slow or expensive to run on every commit
- As the first check in a tiered eval pipeline (canary → partial suite → full suite)
- When you need a fast signal during iterative prompt development

## Inputs

| Field | Required | Description |
|-------|----------|-------------|
| `task_description` | Yes | What the prompt does |
| `full_test_inventory` | Yes | Full test case inventory (IDs, behavior tags, historical failure rate) |
| `full_suite_run_time` | Yes | How long the full suite takes (minutes) and costs ($) |
| `canary_budget` | Optional | Max run time (seconds) and cost ($); defaults: 60s / $0.10 |
| `past_regressions` | Optional | Historical regression events with causing change type |

## Constraints

**Must:**
- Limit the canary set to 5–15 cases
- Estimate run time per case; total must fit within `canary_budget`
- Assign each case a `sensitivity_justification`: why this case catches regressions early
- Cover ≥3 distinct behavior clusters
- Define the failure threshold: how many canary cases must fail before blocking a change
- Document the triage protocol for canary failures

**Must Not:**
- Include cases with high cost variance (e.g., cases that trigger long model outputs unpredictably)
- Include cases that require human review to score — canary must be fully automated
- Select cases solely because they are easy; they must be sensitive to regression-causing changes

## Instructions

**Step 1 — Case selection criteria (ranked)**

Score each candidate case on:

| Criterion | Weight | Scoring |
|-----------|--------|---------|
| Historical failure rate | High | Cases that have failed before: preferred |
| Behavior cluster coverage | High | Select at least 1 case per critical cluster |
| Automation compatibility | Required | Must pass/fail without human review |
| Run time predictability | High | Output length variance <50% |
| Sensitivity to common change types | High | Covers C1–C8 change types most likely in this task |
| Uniqueness | Medium | No two cases testing identical behavior |

**Step 2 — Case schema**

```json
{
  "id": "CS-001",
  "source_case_id": "GS-007",
  "behavior_cluster": "<cluster name>",
  "estimated_run_time_sec": 3.5,
  "estimated_cost_usd": 0.002,
  "sensitivity_justification": "<why this case catches regressions early>",
  "pass_condition": "<binary observable>",
  "failure_weight": 1
}
```

`failure_weight`: some cases are more critical than others; use 1 (normal) or 2 (critical blocker).

**Step 3 — Failure threshold**

Define the threshold:
```
Canary fails if:
  SUM(failure_weight of failed cases) >= THRESHOLD

Recommended threshold: 1 for most deployments; 2 if any failure_weight=2 case is present.
```

Rationale: a single unweighted failure blocks; two low-weight failures block.

**Step 4 — Triage protocol**

| Canary result | Action |
|---------------|--------|
| 0 failures | Proceed to full suite (or deploy if canary-only policy) |
| 1 failure (weight=1) | Review failing case before proceeding; if deterministic, block |
| 1 failure (weight=2) | Block immediately; escalate to prompt owner |
| 2+ failures | Block; run change impact estimator to scope the damage |
| All cases fail | Revert the change; investigate whether model itself changed |

**Step 5 — Canary budget breakdown**

| Case ID | Behavior cluster | Estimated time (s) | Estimated cost ($) | Failure weight |
|---------|-----------------|-------------------|-------------------|----------------|
| CS-001 | | | | |
| … | | | | |
| **TOTAL** | | **< budget** | **< budget** | |

**Step 6 — Refresh protocol**

Refresh the canary set when:
- A regression is caught by the full suite but missed by the canary → add a case targeting that behavior
- A canary case consistently passes for 90+ days with no changes to that behavior → candidate for replacement with a higher-sensitivity case
- The task spec adds a new critical behavior cluster → add ≥1 case for it

## Output Format

1. **Canary case array** — JSON following schema, sorted by behavior cluster
2. **Budget breakdown table** — Step 5 table with totals
3. **Failure threshold** — formula and threshold value
4. **Triage protocol** — decision table from Step 4
5. **Refresh trigger list** — conditions that require canary set update

## Verification

- [ ] Set contains 5–15 cases
- [ ] Total estimated run time ≤ `canary_budget` time limit
- [ ] Total estimated cost ≤ `canary_budget` cost limit
- [ ] ≥3 distinct behavior clusters covered
- [ ] Every case has `pass_condition` automatable without human review
- [ ] Failure threshold and triage protocol documented
