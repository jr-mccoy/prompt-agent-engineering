---
title: "Design Agent Loop Termination Conditions"
category: prompt-engineering/agent-workflows
description: "Define explicit, falsifiable termination conditions for an agent's main loop so it stops cleanly on success, failure, or budget exhaustion."
techniques:
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - agents
  - termination
  - loops
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/agent-workflows/agent_self_correction_loop.md
---

## Objective

Define a complete set of termination conditions for an agent: success conditions, failure conditions, budget caps, and stuck-detection signals. Each must be falsifiable from the agent's state.

## When to Use

- Agents are running indefinitely or exiting prematurely
- A new agent is being designed
- Cost or latency overruns trace to bad termination logic

## Termination Categories

1. **Success**: task done, gates passed
2. **Hard failure**: unrecoverable error, refused tool, contradiction
3. **Budget**: max steps, max tokens, max wall-clock, max tool calls
4. **Stuck detection**: same action twice, no progress N steps, oscillating between states
5. **External signal**: user cancellation, timeout, escalation requested

## Constraints

**Must:**
- Provide ≥1 condition per category (or document why category does not apply)
- Each condition must be a check on agent state (no "feels done")
- Conditions are evaluated each loop iteration in a defined priority order
- On termination, emit a structured exit reason

**Must Not:**
- Use vague exit cues ("when reasonable")
- Let any single category go unbounded
- Allow the agent to define its own success without a check

## Instructions

1. Walk the categories; define ≥1 condition for each.
2. Order: hard failure > external signal > stuck > success > budget.
3. Define the per-iteration check pseudocode.
4. Define the exit-reason structure.

## Output Format

```
TERMINATION CONDITIONS

[success]
  - <condition>: <state check>

[hard failure]
  - <condition>: ...

[budget]
  - max_steps: <n>
  - max_tokens: <n>
  - max_wall_clock_s: <n>
  - max_tool_calls: <n>

[stuck]
  - same action two consecutive iterations
  - no state change for <n> iterations
  - tool error rate > <threshold>

[external]
  - user_cancel signal received
  - parent timeout
  - escalation requested

EVALUATION ORDER
  hard_failure > external > stuck > success > budget

EXIT STRUCTURE
  {
    "category": "...",
    "condition": "...",
    "iteration": <n>,
    "tokens_used": <n>,
    "last_state": <summary>,
    "next_action": "<resume_path | report_to_user | escalate>"
  }
```

## Verification

- Each category has at least one condition or a documented exception
- Each condition is a state check, not vibes
- Evaluation order is named and prevents two conditions firing simultaneously
- Exit structure is parseable
