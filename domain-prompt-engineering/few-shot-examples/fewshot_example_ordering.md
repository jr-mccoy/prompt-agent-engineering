---
title: "Order Few-Shot Examples"
category: prompt-engineering/few-shot-examples
description: "Decide the order in which few-shot examples appear, considering recency bias, difficulty progression, and primacy/recency effects."
techniques:
  - PR-03
difficulty: intermediate
tags:
  - few-shot
  - ordering
  - recency-bias
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/few-shot-examples/fewshot_example_selector.md
---

## Objective

Given K selected few-shot examples, decide their order in the prompt. Output: an ordering and rationale, plus a small A/B plan to validate.

## When to Use

- You have selected examples and outputs are sensitive to their order
- The model appears to overfit to the last example
- You want a documented, testable ordering policy

## Inputs

1. The K selected examples
2. The known-difficult input distribution
3. Whether the prompt will be cached (affects whether ordering can later change cheaply)

## Ordering Policies (pick one or hybrid)

| Policy | When to use |
|---|---|
| `most-similar-last` | Test input is fresh; placing similar example last anchors style |
| `easy-to-hard` | Want the model to build up reasoning |
| `hard-to-easy` | Want to lead with the strongest signal of expected rigor |
| `diverse-interleave` | No example should dominate; rotate axes |
| `negative-last` | Use when negative example sets the boundary the model should respect |
| `random-stable` | A fixed shuffle to defeat ordering bias on repeat calls |

## Constraints

**Must:**
- Pick a policy from the list (or document a named hybrid)
- Justify the choice using the input distribution
- Place the negative or edge case where it does the most work (often last for boundary anchoring)
- If the prompt is cached, freeze ordering and document that future changes invalidate cache

**Must Not:**
- Sort by accidental properties (length, alphabetical) without justification
- Place the most extreme positive example last if it would cause overfit
- Reorder without invalidating downstream A/B records

## Instructions

1. Look at the K examples and the test input distribution.
2. Choose policy.
3. Apply policy. Tie-break by tokens fitting.
4. Plan a small A/B: alternate ordering vs. policy ordering on 10 inputs.
5. Lock the order with a comment in the prompt.

## Output Format

```
POLICY: <name>
RATIONALE: ...

ORDER
  1. <example id> — role: anchor / progression / boundary / interleave
  2. ...

NEGATIVE/EDGE PLACEMENT
  example <id> at position <p> because ...

A/B PLAN
  arm A: ordering above
  arm B: <comparison ordering>
  test inputs: <count>
  metric: <what to measure>

CACHE NOTE
  ordering frozen at <commit/hash> ; changing breaks <prefix length>
```

## Verification

- Policy named, rationale evidenced
- Each position has a role
- A/B plan has a single metric
- Cache implications stated if applicable
