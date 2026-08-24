---
title: "Make an Agent Trace-Friendly"
category: prompt-engineering/agent-workflows
description: "Add prompt rules so the agent emits structured trace events around decisions, tool calls, and errors, enabling observability without log scraping."
techniques:
  - ST-03
difficulty: intermediate
tags:
  - observability
  - traces
  - telemetry
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/evaluation/correctness_production_monitoring_setup.md
---

## Objective

Add explicit emit-event rules to an agent prompt so each decision, tool call, error, and milestone surfaces in a parseable trace event the platform can index without parsing prose.

## When to Use

- An observability platform requires structured events
- A team is debugging agent behavior across many runs
- You want to compute metrics (decision count, tool-call rate, error rate) without ad-hoc parsing

## Inputs

1. The agent prompt
2. The platform's event schema (or a chosen one)
3. Which events matter (decision, tool_call, tool_result, error, milestone)

## Constraints

**Must:**
- Emit events as a fixed JSON shape
- Wrap each event in a known marker (e.g., `<EVENT>...</EVENT>`)
- Include event type, timestamp, iteration, and minimum required fields per type
- Emit events for every named milestone, not just on demand

**Must Not:**
- Mix event JSON into the conversational output
- Skip events to "save tokens" — events are load-bearing for telemetry
- Use freeform fields that can't be aggregated

## Instructions

1. Define event types and required fields.
2. Add prompt rules: when to emit each.
3. Define the emit format (single-line JSON wrapped in markers).
4. Specify what fields are required vs optional per type.

## Output Format

```
EVENT SCHEMA
  base:
    type: <decision | tool_call | tool_result | error | milestone>
    iteration: <n>
    ts: <ISO-8601 or step-relative>
  decision:
    chose: <option>
    among: [...]
    rationale: <≤20 words>
  tool_call:
    tool: <name>
    args: {...}
  tool_result:
    tool: <name>
    ok: <bool>
    summary: <≤50 words>
  error:
    code: <enum>
    detail: <line>
  milestone:
    name: <enum>
    progress: <fraction>

PROMPT ADDITION
  Whenever you make a non-trivial decision, emit:
    <EVENT>{"type":"decision",...}</EVENT>
  Whenever you call a tool, emit decision and tool_call before the call,
  and tool_result after.
  On error, emit error before continuing.
  On milestone, emit milestone.

EXAMPLE EMISSION
  <EVENT>{"type":"decision","iteration":3,"chose":"retry","among":["retry","escalate"],"rationale":"transient 503"}</EVENT>

PARSER REGEX
  /<EVENT>(.+?)<\/EVENT>/g
```

## Verification

- Every named milestone has an emit point
- Events are valid JSON inside markers
- No conversational output overlaps event markers
- Schema fields are required as declared
