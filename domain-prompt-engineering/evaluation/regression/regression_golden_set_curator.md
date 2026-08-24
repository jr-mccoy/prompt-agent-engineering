---
title: "Golden Set Curator"
category: prompt-engineering/evaluation/regression
description: "Build and maintain a stable golden test set with provenance tracking, freeze protocol, and update criteria for long-term regression testing."
techniques:
  - ST-02
  - ST-03
  - CM-02
  - QA-01
  - RT-05
difficulty: intermediate
tags:
  - golden_set
  - regression_testing
  - test_management
  - provenance
  - eval_infrastructure
updated: "2026-05-11"
related_prompts:
  - domain-prompt-engineering/evaluation/regression/regression_canary_set_designer.md
  - domain-prompt-engineering/evaluation/regression/regression_change_impact_estimator.md
  - domain-prompt-engineering/evaluation/correctness_eval_design_prompt.md
---

## Objective

Produce a versioned golden test set — a stable collection of (input, expected output, acceptance criterion) triples — with provenance metadata, a freeze protocol, and explicit rules for adding, removing, or updating cases. The golden set is the ground truth that regression tests compare against.

## When to Use

- Establishing a baseline before the first prompt deployment
- Formalizing informal "this should always work" knowledge into a versioned artifact
- After a regression incident: curate cases from failures to prevent recurrence
- When multiple team members need to agree on what "correct" means for a task

## Inputs

| Field | Required | Description |
|-------|----------|-------------|
| `task_description` | Yes | What the prompt does; the success criteria in natural language |
| `existing_cases` | Optional | Informal test cases, chat examples, or accepted past outputs |
| `failure_history` | Optional | Past regressions (input + wrong output) to include as anchors |
| `owner` | Yes | Name or team responsible for maintaining the set |
| `target_set_size` | Optional | Total cases; default 20, min 10 |

## Constraints

**Must:**
- Assign every case a unique stable ID (format: `GS-NNN`)
- Record `provenance` for every case: source (human-authored / sampled-from-log / failure-derived), author, date
- State `acceptance_criterion` as an observable pass/fail rule — not "output is good"
- Specify `freeze_status` per case: `frozen` (never auto-updated) or `live` (can be updated)
- Document the version of the set (`v1.0`, `v1.1`, etc.) and change log

**Must Not:**
- Include cases whose `acceptance_criterion` requires subjective judgment without anchors
- Mark a case `frozen` without a written justification for why it must never change
- Add or remove cases without incrementing the set version

## Instructions

**Step 1 — Case structure**

```json
{
  "id": "GS-001",
  "version_added": "v1.0",
  "freeze_status": "frozen",
  "freeze_justification": "<why this case must never be modified>",
  "provenance": {
    "source": "failure-derived",
    "author": "Jane Smith",
    "date": "2026-05-11",
    "original_context": "<link or description of the failure event>"
  },
  "input": "<verbatim prompt input>",
  "expected_output": "<canonical accepted output or output property>",
  "acceptance_criterion": "<binary observable rule>",
  "tags": ["<category>", "<behavior>"]
}
```

**Step 2 — Case selection criteria**

Prioritize cases that:
1. Represent the most common production inputs (high-frequency, low-variance)
2. Cover behaviors that failed in production (failure-derived anchors)
3. Test boundary conditions that the task spec explicitly names
4. Test behaviors that are easy to accidentally break during prompt edits

Deprioritize:
- Edge cases with no production history
- Cases whose acceptance criterion requires a human to read the full output carefully

**Step 3 — Coverage audit**

After drafting the set, produce a coverage table:
| Behavior cluster | Case count | Frozen count | Risk if uncovered |
|-----------------|------------|--------------|-------------------|

Behavior clusters are derived from the task description (e.g., "format compliance", "refusal handling", "edge inputs", "core functionality").

**Step 4 — Freeze protocol**

| Event | Action |
|-------|--------|
| Prompt changes a constraint the case tests | Re-run case; if accepted output changes, evaluate: update case or revert prompt |
| Case fails on a new model version | Do not automatically update; hold for human review |
| Case is obsolete (behavior intentionally removed) | Archive with reason; never delete |
| New failure discovered | Add new case; set `freeze_status: live` until stable for 30 days |

**Step 5 — Version control**

Golden set version schema: `v{major}.{minor}`
- Major bump: any frozen case changes, or ≥20% of cases change
- Minor bump: new cases added or live cases updated
- Maintain a `CHANGELOG.md` alongside the set: date, version, change, author

## Output Format

1. **Case array** — JSON array following schema
2. **Coverage table** — behavior cluster × count × frozen count × risk
3. **Freeze protocol** — decision table (Step 4)
4. **Version header** — set version, case count, owner, date, change log entry

## Verification

- [ ] Every case has a unique `GS-NNN` ID
- [ ] Every `acceptance_criterion` is a binary observable rule
- [ ] Every frozen case has a written `freeze_justification`
- [ ] Coverage table has no behavior cluster with 0 cases and "high" risk
- [ ] Version header and change log entry present
