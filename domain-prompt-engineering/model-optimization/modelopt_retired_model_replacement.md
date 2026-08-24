---
title: "Replace a Retired Model"
category: prompt-engineering/model-optimization
description: "Plan and execute the replacement of a retired model with a successor or alternative, including compatibility checks, prompt edits, and rollback."
techniques:
  - QA-01
difficulty: advanced
tags:
  - retirement
  - replacement
  - deprecation
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/model-optimization/modelopt_within_family_migration.md
---

## Objective

When a model is being retired, produce a replacement plan: candidate successors, prompt edits per candidate, compatibility risks, rollback path, and timeline.

## When to Use

- A model retirement date has been announced
- A workload depends on a deprecated model
- You must move multiple prompts off a single retired model

## Inputs

1. Retired model and retirement date
2. Candidate successors (by family and size)
3. List of prompts using the retired model
4. Production constraints (cost, latency, quality)

## Constraints

**Must:**
- Evaluate ≥2 candidate successors per prompt class
- Edit prompts for each candidate per family-specific patterns
- Run regression set per candidate
- Define rollback: keep an alternative ready in case the chosen one degrades
- Plan timeline: edits, eval, deployment, monitor

**Must Not:**
- Default to the "obvious next model" without comparison
- Skip prompt edits assuming the new model behaves identically
- Cut over without monitoring period

## Instructions

1. Inventory affected prompts.
2. Pick candidate successors.
3. Apply per-candidate prompt edits (within-family migration if same family; cross-family otherwise).
4. Run regression per candidate.
5. Choose primary + fallback.
6. Define rollout: phased percentage, monitoring window, rollback criteria.

## Output Format

```
RETIREMENT PLAN

RETIRED MODEL: <name>
RETIREMENT DATE: <date>
AFFECTED PROMPTS: [<list>]

CANDIDATE EVALUATION
  candidate A:
    family: ...
    quality on regression: <metric>
    cost delta: <value>
    edits required per prompt: <summary>
  candidate B:
    ...

DECISION
  primary: <candidate>
  fallback: <candidate>
  reasoning: ...

PER-PROMPT EDITS
  prompt <id>:
    edits: <summary>
    regression: pass/fail per case

ROLLOUT
  phase 1: <%> traffic on <date>
  phase 2: <%> on <date>
  phase 3: 100% on <date>
  monitoring window: <duration>

ROLLBACK CRITERIA
  - metric drop > <threshold>
  - error rate > <threshold>
  - manual escalation

ROLLBACK PATH
  switch traffic to fallback within <time>
```

## Verification

- ≥2 candidates evaluated per prompt class
- Edits applied per family conventions
- Rollback criteria are quantitative
- Timeline preserves a safety margin before retirement date
