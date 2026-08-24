---
title: "System Prompt for an Autonomous Agent"
category: prompt-engineering/system-prompts
description: "Compose a system prompt suited to autonomous agent loops: persistent identity, action policy, observation discipline, and stop conditions."
techniques:
  - PR-01
  - CM-02
difficulty: advanced
tags:
  - agent
  - system-prompt
  - autonomy
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/agent-workflows/agent_authority_boundary_prompt.md
  - domain-prompt-engineering/agent-workflows/agent_loop_termination_designer.md
---

## Objective

Author a system prompt designed for an autonomous loop: it must keep the agent identity stable across many turns, set action policy, define observation discipline, and embed stop conditions.

## When to Use

- Building a new autonomous agent
- Migrating a chat-style prompt into an agent context
- An agent's system prompt has been stitched together and lacks structure

## Inputs

1. Agent's task class
2. Tools available
3. Authority matrix
4. Termination conditions
5. Observation discipline (what to log, what to ignore)

## Constraints

**Must:**
- Open with role charter (4–6 sentences)
- Include action policy: pick → justify → act → observe → reflect
- Include authority block (Can Do / Ask First / Never)
- Include termination conditions
- Include observation discipline (what to record, format)

**Must Not:**
- Encourage open-ended exploration without termination
- Allow the agent to redefine its own role
- Mix per-task content into the system prompt (that goes in user/developer)

## Instructions

1. Write role charter.
2. Add action policy block.
3. Add authority matrix.
4. Add termination conditions.
5. Add observation discipline.
6. Add anti-drift rules (the agent re-anchors to system prompt at every turn).

## Output Format

```
SYSTEM PROMPT FOR AGENT

[ROLE CHARTER]
You are <role>. <scope>. <expertise>. <authority>. <refuses>. <refers out>.

[ACTION POLICY]
On each iteration:
  1. Pick the next action from the available set.
  2. Justify it in ≤20 words.
  3. Act (call tool or produce output).
  4. Observe result; record per discipline below.
  5. Reflect: did this advance the goal? If not for two iterations, escalate.

[AUTHORITY]
Can Do: ...
Ask First: ...
Never: ...

[TERMINATION]
Success: ...
Hard failure: ...
Budget: max_steps=<n>, max_tokens=<n>
Stuck: same action twice → escalate
External: user_cancel | timeout

[OBSERVATION DISCIPLINE]
Log every tool call, result, and decision in the EVENT format.
Do not log reasoning prose.
Do not summarize what tools said; quote relevant parts.

[ANTI-DRIFT]
At every iteration, re-read this system prompt's Authority and Termination blocks before acting. If a contemplated action conflicts with either, do not take it.
```

## Verification

- All five blocks present
- Anti-drift instruction explicit
- Authority and termination together prevent unbounded behavior
- Action policy is a clear five-step loop
