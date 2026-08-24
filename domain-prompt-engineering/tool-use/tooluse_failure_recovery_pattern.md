---
title: "Tool Failure Recovery Pattern"
category: prompt-engineering/tool-use
description: "Classify a tool error and choose retry, fallback, or escalate using a typed decision table — no infinite retries."
techniques:
  - ST-02
  - DD-06
  - QA-13
  - CM-02
difficulty: intermediate
tags:
  - tool_use
  - retry
  - fallback
  - escalation
  - error_handling
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/tool-use/tooluse_multi_tool_orchestration.md
  - domain-prompt-engineering/tool-use/tooluse_tool_result_interpretation.md
  - domain-prompt-engineering/tool-use/tooluse_dry_run_pattern.md
---

## Objective

Given a tool call and its error, classify the error and emit `{action, params}` from {`retry`, `retry_with_modified_args`, `fallback_tool`, `ask_user`, `escalate_human`, `give_up`}. Bound retries.

## When to Use

- Tool calls fail intermittently or with structured error codes.
- An orchestrator needs deterministic recovery, not "the model figures it out".
- You want to cap retry budget per call and per session.

## Inputs

```
TOOL_NAME: <name>
TOOL_ARGS: <args sent>
ERROR: <code, message, http_status (if applicable), retry_after (if any)>
ATTEMPT: <integer, current attempt number>
MAX_RETRIES: <integer>
FALLBACK_REGISTRY: <tool_name → fallback_tool with capability_match>
DESTRUCTIVE: <yes|no>
```

## Constraints

### Must
- Classify ERROR into one of: `transient` (timeout, 5xx, rate_limit), `auth` (401/403), `validation` (400, 422), `not_found` (404), `conflict` (409), `quota_exhausted`, `permanent` (501, semantic refusal), `unknown`.
- Apply the decision table:

  | class | DESTRUCTIVE | ATTEMPT < MAX | action |
  |---|---|---|---|
  | transient | * | yes | retry (respect retry_after; else expo backoff 2^ATTEMPT s, cap 30s) |
  | transient | * | no | fallback_tool if exists; else escalate_human |
  | rate_limit | * | yes | retry with delay = max(retry_after, 2^ATTEMPT) |
  | auth | * | * | escalate_human (do not retry) |
  | validation | no | * | retry_with_modified_args (one shot only) |
  | validation | yes | * | ask_user (show what was wrong) |
  | not_found | * | * | ask_user with the missing-target detail |
  | conflict | yes | * | ask_user (state the conflict; do not auto-resolve) |
  | conflict | no | yes | retry_with_modified_args |
  | quota_exhausted | * | * | give_up + report |
  | permanent | * | * | give_up |
  | unknown | * | yes | retry_once; otherwise escalate_human |

- Respect `retry_after` whenever provided.
- Never retry an `auth` or `permanent` class.
- For `retry_with_modified_args`, name which field is being changed and why.

### Must Not
- Loop indefinitely; ATTEMPT ≥ MAX_RETRIES forbids `retry`.
- Silently switch to a fallback whose `capability_match` is partial without telling the user a capability dropped.
- Auto-resolve a `conflict` on a destructive tool.

## Instructions

1. Parse ERROR. Extract `code`, `http_status`, `retry_after`.
2. Classify per the rules above.
3. Pick action from the table.
4. Emit `params` for the action: delay seconds for retry; modified arg for `retry_with_modified_args`; fallback tool name + capability_diff; user question for `ask_user`; ticket fields for `escalate_human`.
5. Append a one-line `audit` note describing why this action was chosen.

## Output Format

```json
{
  "classification": "<class>",
  "action": "<one of the six>",
  "params": {"delay_s": 4, "modified_arg": null, "fallback_tool": null, "ask_user_question": null, "escalation_reason": null},
  "remaining_retries": <int>,
  "audit": "<one line>"
}
```

## Verification

- `action=retry*` ⇒ `ATTEMPT < MAX_RETRIES`.
- `classification=auth | permanent` ⇒ `action ∈ {escalate_human, give_up}`.
- `DESTRUCTIVE=yes` ⇒ `action ≠ retry_with_modified_args`.
- `retry_after` present ⇒ `params.delay_s ≥ retry_after`.
