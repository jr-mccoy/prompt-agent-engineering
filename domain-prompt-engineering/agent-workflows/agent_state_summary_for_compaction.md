---
title: "State Summary for Context Compaction"
category: prompt-engineering/agent-workflows
description: "Produce a compact, lossless-where-possible state summary the agent can resume from after context compaction."
techniques:
  - CM-01
  - ST-03
difficulty: advanced
tags:
  - compaction
  - state
  - resume
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/compression-and-cost/compression_lossless_rewrite.md
---

## Objective

Define a structured state-summary format that an agent emits at compaction time, capturing every load-bearing fact needed to resume work without revisiting prior context.

## When to Use

- Long-running agents whose context exceeds the window
- Agents that hand off to a successor session
- Workflows where mid-task pause and resume is expected

## Inputs

1. The agent's task and current progress
2. The list of fact categories that survive compaction (decisions made, files touched, errors encountered, open questions, next action)
3. Token budget for the summary

## Constraints

**Must:**
- Use named sections so a successor can navigate without reading full prose
- Mark each fact as `decision`, `observation`, `assumption`, `pending`, or `risk`
- Preserve any irreversible action taken (file edits, API calls, commits)
- Include `next_action` as the top item

**Must Not:**
- Compress decisions into "various decisions made"
- Drop pending items
- Lose the user's most recent intent

## Instructions

1. Walk the categories: decisions, observations, assumptions, pending, risks.
2. For each, list facts in chronological order with one-line entries.
3. Capture irreversible actions explicitly.
4. End with NEXT_ACTION; this is the resume point.
5. Verify token budget; if over, drop oldest `observation` items first, never `decision` or `pending`.

## Output Format

```
TASK
<one-line restatement>

NEXT_ACTION
<exactly what to do next>

DECISIONS (kept, do not revisit)
  - <id>: <decision>
  - ...

OBSERVATIONS (compress oldest first if over budget)
  - <fact>
  - ...

ASSUMPTIONS (mark each: confirmed | pending)
  - <assumption>: status

IRREVERSIBLE ACTIONS
  - <action>: <when, what was changed>

PENDING
  - <item>: <why pending>

RISKS
  - <risk>: <if-then>

OPEN QUESTIONS
  - <question>: <who can answer>

CONTEXT POINTERS
  - <ref>: <where to look if successor needs detail>
```

## Verification

- NEXT_ACTION is the first non-task line so a successor finds it instantly
- No decision or pending item dropped
- Irreversible actions named
- Token count within budget
