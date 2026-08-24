---
title: "Tree-of-Thought Template"
category: prompt-engineering/reasoning-strategies
description: "Prompt the model to branch on candidate approaches, evaluate each, prune, and proceed with the best — within a bounded budget."
techniques:
  - PR-02
  - DC-01
difficulty: advanced
tags:
  - tree-of-thought
  - branching
  - search
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/reasoning-strategies/reasoning_self_consistency_runner.md
---

## Objective

Author a prompt that explicitly enumerates B candidate approaches, scores each on stated criteria, prunes to the top T, and proceeds along the best — with a hard budget on branches and depth.

## When to Use

- The task has multiple valid approaches with non-obvious tradeoffs
- You want the model to consider alternatives before committing
- Mistakes from picking the first plausible approach are expensive

## Inputs

1. The task
2. Branching factor B (default 3)
3. Top-T to keep at each level (default 1–2)
4. Maximum depth D
5. Scoring criteria (3–5 named, weighted)

## Constraints

**Must:**
- Enumerate exactly B candidates per branching step
- Score each on every named criterion with a brief justification
- Prune to top T explicitly with reason
- Bound total branches at B^D worst case; refuse to expand past D

**Must Not:**
- Add candidates beyond B per level to "be thorough"
- Skip scoring on a criterion to save tokens
- Pursue more than T branches past a pruning step

## Instructions

1. State criteria and their weights.
2. At depth 0, generate B candidate approaches.
3. Score each; prune to T.
4. For each kept branch, expand if needed (depth+1).
5. Stop at depth D or when one branch dominates.
6. Emit chosen path with reasoning.

## Output Format

```
CRITERIA
  - <name>: weight <w> | description

DEPTH 0
  candidate 1: <description>
    scores: c1=<s>, c2=<s>, ... | weighted total: <t>
  candidate 2: ...
  candidate 3: ...
  pruned to top <T>: [c1, c2]

DEPTH 1 (per kept branch)
  branch c1:
    sub-candidates: ...
    scored ...
    pruned ...
  branch c2:
    ...

CHOSEN PATH
  c1 → c1.sub-X → ...

FINAL ANSWER (along chosen path)
<answer>

BUDGET
  branches_explored: <n>
  max_depth_reached: <d>
```

## Verification

- B and T limits respected at every level
- Every candidate scored on every criterion
- Pruning rationale stated
- Final answer flows from chosen path, not from a discarded branch
