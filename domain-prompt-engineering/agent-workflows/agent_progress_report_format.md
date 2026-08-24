---
title: "Progress Report Format for Long-Running Agents"
category: prompt-engineering/agent-workflows
description: "Define a concise structured progress report an agent emits at intervals so users and orchestrators can track without reading the full trace."
techniques:
  - ST-03
  - CM-01
difficulty: intermediate
tags:
  - progress-report
  - agents
  - status
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/agent-workflows/agent_state_summary_for_compaction.md
---

## Objective

Define the shape of a per-N-iteration progress report an agent emits: what's done, what's next, what's blocking, and a confidence on completion. Concise, parseable, predictable.

## When to Use

- Agents running for minutes-to-hours
- Multi-agent setups where an orchestrator polls status
- User-facing surfaces where a spinner is unacceptable

## Inputs

1. Agent task
2. Reporting interval (every N iterations or every N seconds)
3. Maximum length per report
4. Audience (user / orchestrator / log only)

## Constraints

**Must:**
- Fixed schema across all reports for the same agent
- Include `done`, `next`, `blockers`, `eta_or_unknown`
- Mark progress with a percent or step count, not vibes
- Bound length

**Must Not:**
- Write reports as free prose
- Include reasoning chains in reports
- Hide blockers ("everything's fine" when not)

## Instructions

1. Choose reporting interval and length cap.
2. Define schema fields.
3. Write the prompt addition that triggers the report.
4. Define what triggers an unscheduled report (blocker, milestone, error).

## Output Format

```
PROGRESS REPORT SCHEMA
  iteration: <n>
  elapsed_s: <n>
  step_index: <i> of <total | unknown>
  done: [<list of completed milestones since last report>]
  in_progress: <current micro-step>
  next: <planned next micro-step>
  blockers: [{type, detail}]
  eta_iterations: <n | unknown>
  confidence_will_finish: <high | medium | low>

PROMPT ADDITION (inserted into agent loop)
  Every <interval>, before the next action, emit:
    <REPORT>
      <schema fields>
    </REPORT>

UNSCHEDULED TRIGGERS
  - new blocker
  - error class change
  - external_signal received

LENGTH CAP
  ≤ <n> tokens per report
```

## Verification

- Schema is identical across reports
- `eta_iterations` is `unknown` when truly unknown rather than guessed
- Blockers, when present, are non-empty
- Length cap respected
