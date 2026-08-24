---
title: "Call-Tool vs Answer-From-Knowledge Decision Prompt"
category: prompt-engineering/tool-use
description: "Force a typed decision on whether to invoke a tool or answer directly, with declared confidence and freshness checks."
techniques:
  - ST-02
  - CM-02
  - QA-01
  - DP-04
difficulty: intermediate
tags:
  - tool_use
  - decision
  - knowledge_cutoff
  - freshness
  - over_calling
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/tool-use/tooluse_tool_description_writer.md
  - domain-prompt-engineering/tool-use/tooluse_disambiguation_pattern.md
  - domain-prompt-engineering/tool-use/tooluse_tool_set_minimization.md
---

## Objective

Before any tool call, force the model to emit a routing decision: `call_tool` (which one, why), `answer_directly` (with confidence), or `ask_user` (specific question). Eliminates over-calling and under-calling.

## When to Use

- Tool calls are expensive, rate-limited, or destructive.
- The model is over-calling (every prompt fetches state) or under-calling (answers stale facts from training).
- You need an audit trail of when a tool was used vs not.

## Inputs

```
USER_MESSAGE: <verbatim>
TOOL_REGISTRY: <list of name + 1-line purpose + freshness_class>
KNOWLEDGE_CUTOFF: <ISO date>
TODAY: <ISO date>
COST_PER_CALL: <relative: low | medium | high>
DESTRUCTIVE_TOOLS: <subset of TOOL_REGISTRY>
```

## Constraints

### Must
- Emit one of three routes: `call_tool` | `answer_directly` | `ask_user`.
- For `answer_directly`, declare `confidence` ∈ {high, medium, low} and `freshness_required` ∈ {real_time, recent_30d, stable_facts}.
  - If `freshness_required=real_time` AND a tool exists with `freshness_class=real_time`, route MUST be `call_tool`.
  - If `confidence=low`, route MUST NOT be `answer_directly`.
- For `call_tool`, name the tool, list the args (or `unknown` with source-of-args), and state the expected return shape in ≤ 1 line.
- For destructive tools, emit `ask_user` first with the planned call quoted, unless USER_MESSAGE explicitly authorizes.

### Must Not
- Call multiple tools in this decision; that's a separate orchestration step.
- Hide the route under a wrapper; the route is the first line of output.
- Use `answer_directly` for any factual claim with a date strictly after KNOWLEDGE_CUTOFF when a tool exists.

## Instructions

1. Classify USER_MESSAGE on three axes:
   - Time sensitivity: real_time / recent_30d / stable_facts.
   - State change: read / write.
   - Specificity: enough args to call a tool? (yes/no).
2. Apply the decision table:
   | time | state | args? | route |
   |---|---|---|---|
   | real_time | read | yes | call_tool |
   | real_time | * | no | ask_user |
   | recent_30d | read | yes | call_tool if cost ≠ high; else ask_user |
   | stable_facts | read | * | answer_directly (confidence ≥ medium) |
   | * | write | yes | ask_user (if destructive) or call_tool |
   | * | write | no | ask_user |
3. Emit the chosen route with required fields.

## Output Format

```
route: call_tool | answer_directly | ask_user
- if call_tool: tool=<name> args=<json> expected_return=<one line>
- if answer_directly: confidence=<h|m|l> freshness_required=<class> rationale=<≤1 line>
- if ask_user: question=<specific, ≤ 1 sentence>
```

## Verification

- Self-check: did I pick `answer_directly` for a real_time question with a tool available? If yes, switch.
- For `ask_user`, the question must be answerable in one sentence and reference the missing arg or authorization.
- For `call_tool`, args are either present or marked `unknown` with the field that caused it.
