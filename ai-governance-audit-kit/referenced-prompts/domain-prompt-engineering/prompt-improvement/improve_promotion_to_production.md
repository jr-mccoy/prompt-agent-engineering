---
title: "Promote a Prompt From Prototype to Production"
category: prompt-engineering/prompt-improvement
description: "Run a prototype prompt through a fixed promotion checklist that adds validation, monitoring hooks, and refusal handling."
techniques:
  - QA-01
  - CM-02
difficulty: advanced
tags:
  - promotion
  - production
  - hardening
  - tier
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/evaluation/correctness_production_monitoring_setup.md
  - domain-prompt-engineering/prompt-improvement/improve_brittleness_audit.md
---

## Objective

Apply a fixed checklist to a prompt that has been working in development and produce a production-ready version with monitoring hooks, refusal cases, and rollback notes.

## When to Use

- A prompt has passed dev evaluation and is going live
- A team is standardizing what "production-grade" means
- You need a reproducible promotion process for many prompts

## Inputs

1. The prototype prompt
2. The deployment surface (chat, API, agent step)
3. Telemetry available downstream (response time, error rate, schema compliance)
4. SLA or quality bar

## Promotion Checklist

```
[ ] Inputs declared with types and bounds
[ ] Output schema declared and parseable
[ ] Refusal cases enumerated with exit message
[ ] At least one rule per known failure mode
[ ] Verification block present and falsifiable
[ ] Token estimate within budget
[ ] Cache prefix maximized (stable text first)
[ ] Versioned (`version: x.y.z`) with changelog
[ ] Owner named in frontmatter
[ ] Rollback prompt or previous version reference present
[ ] Monitoring hooks: which fields/events the system logs
[ ] At least 5 eval cases (3 happy, 1 edge, 1 refusal)
```

## Constraints

**Must:**
- Apply every checklist item
- Mark items `done`, `n/a (reason)`, or `gap (action)`
- Refuse to promote if any safety-related item is `gap`
- Add a `version` and `changelog` to the prompt frontmatter

**Must Not:**
- Mark an item `n/a` without a reason
- Remove checklist items to fit time pressure
- Promote without the rollback path

## Instructions

1. Walk the checklist top to bottom.
2. For each gap, write the smallest action that closes it.
3. Apply the actions; re-walk the checklist.
4. Emit the production-ready prompt with version + changelog.
5. Output the eval case set (5 cases minimum).

## Output Format

```
CHECKLIST RESULT
  [x] inputs declared
  [ ] refusal cases — gap: missing for input class X | action: add
  ...

ACTIONS APPLIED
  - <action>

PRODUCTION PROMPT
  ---
  version: 1.0.0
  owner: ...
  changelog:
    - 1.0.0 (2026-05-09): initial production version
  ---
  <prompt body>

EVAL CASE SET
  1. <case>
  ...

ROLLBACK
  previous: <ref> | rollback condition: <when to revert>
```

## Verification

- No checklist item left unaddressed
- Frontmatter has version, owner, changelog
- Refusal cases cover known sensitive inputs
- Eval set has 3 happy + 1 edge + 1 refusal at minimum
