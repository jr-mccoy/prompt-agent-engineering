---
title: "Generate a Brief for a Subagent"
category: prompt-engineering/agent-workflows
description: "Author a self-contained brief that a sub-agent can run without seeing the parent's context, with explicit scope, return contract, and authority limits."
techniques:
  - DC-01
  - CM-02
difficulty: intermediate
tags:
  - subagent
  - delegation
  - brief
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/delegation/delegation_intent_specification.md
---

## Objective

When a parent agent delegates to a sub-agent, produce the sub-agent's brief: enough context to execute, no parent-only state, explicit return contract, and authority bounds.

## When to Use

- Multi-agent pipelines with sub-task delegation
- Sub-agents that run in parallel and must not depend on parent reasoning
- Cases where the sub-agent has restricted tool access vs the parent

## Inputs

1. The sub-task to delegate
2. What the parent already knows that the sub-agent needs
3. What the parent considers "out of scope" for the sub-agent
4. The return shape the parent will consume

## Constraints

**Must:**
- Restate the sub-task without parent jargon
- Provide every fact the sub-agent needs; assume zero shared memory
- Define exactly what shape the parent expects back
- Specify can-do / ask-first / never authority bounds

**Must Not:**
- Say "based on what we discussed" — the sub-agent did not discuss anything
- Pass a transcript when a digest will do
- Leave authority ambiguous

## Instructions

1. Strip parent-only context; restate the sub-task atomically.
2. List facts the sub-agent needs; bundle them with the brief.
3. Define the return shape with field names and types.
4. State authority bounds: tool whitelist, irreversible actions allowed/forbidden.
5. Set time and token budgets.

## Output Format

```
SUBAGENT BRIEF

TASK
<self-contained restatement>

CONTEXT FACTS
  - <fact>
  - ...

OUT OF SCOPE
  - <item>: do not address
  - ...

AUTHORITY
  can_do: [<tools/actions>]
  ask_first: [<actions requiring confirmation>]
  never: [<absolute prohibitions>]

RETURN CONTRACT
  shape:
    {
      "result": ...,
      "evidence": [...],
      "confidence": <enum>,
      "open_questions": [...]
    }
  failure_shape:
    {
      "status": "failed",
      "reason": ...,
      "partial_progress": ...
    }

BUDGETS
  time: <s>
  tokens: <n>
  tool_calls: <n>
```

## Verification

- Brief is self-contained: a fresh agent can act on it
- Return contract has both success and failure shapes
- Authority is explicit at three levels
- Budgets are numeric, not vibes
