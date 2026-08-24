---
title: "Decide Whether to Downsize the Model"
category: prompt-engineering/compression-and-cost
description: "Diagnose whether a smaller model can serve the same prompt acceptably, with measurement-based gates and a fallback escalation rule."
techniques:
  - QA-01
  - CM-01
difficulty: advanced
tags:
  - model-size
  - downsize
  - cost
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/model-optimization/modelopt_haiku_constraints.md
---

## Objective

Decide whether to move a workload from a large model (e.g., Opus / GPT-4-class) to a smaller one (Sonnet / Haiku / mini), with a measurement plan and an escalation rule for hard cases.

## When to Use

- Cost or latency optimization
- Workloads with mixed difficulty where simple cases waste big-model capacity
- Routing strategy decisions

## Inputs

1. Current model and cost
2. Candidate smaller model and cost
3. Test set stratified by difficulty
4. Acceptable quality bar per stratum
5. Fallback path: escalate to larger model on detected uncertainty

## Constraints

**Must:**
- Measure each model on the same test set, same prompt
- Stratify results by difficulty
- Define escalation rule (when to fall back to larger model) with a check on smaller-model output
- Compute net cost: smaller-model cost + escalation rate × larger-model cost

**Must Not:**
- Switch on a vibes claim that smaller is "good enough"
- Skip stratification (averages hide failures on hard cases)
- Use the larger model's outputs as ground truth without independent validation

## Instructions

1. Run smaller model on stratified test set.
2. Score each stratum.
3. Identify where smaller-model is below quality bar.
4. Define escalation triggers (low confidence, schema fail, contradictory output).
5. Project net cost across realistic input mix.

## Output Format

```
SETUP
  baseline model: <name>, cost/call: $<x>
  candidate model: <name>, cost/call: $<y>
  test set: stratified into <list>

PER-STRATUM RESULTS
  stratum | baseline metric | candidate metric | within bar?
  easy   | ...             | ...              | yes
  medium | ...             | ...              | yes/no
  hard   | ...             | ...              | no

ESCALATION RULE
  trigger: <falsifiable check on candidate output>
  fallback model: <baseline>
  expected escalation rate: <fraction>

NET COST PROJECTION
  candidate × (1 − escalation_rate) + baseline × escalation_rate = $<n>
  vs current: $<n>
  savings: <fraction>

DECISION
  - downsize: yes | no | partial (route by stratum)

ROLLBACK
  trigger: <metric drop> in production
  action: route 100% to baseline within <duration>
```

## Verification

- Stratified results, not averages
- Escalation trigger is falsifiable
- Net cost is computed, not estimated by feel
- Rollback rule predefined
