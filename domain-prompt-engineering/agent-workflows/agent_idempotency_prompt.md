---
title: "Idempotency Rules for Agents With Side Effects"
category: prompt-engineering/agent-workflows
description: "Prevent duplicate side effects on retry by giving the agent rules for checking, recording, and gating actions with idempotency keys."
techniques:
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - idempotency
  - retry
  - side-effects
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/agent-workflows/agent_self_correction_loop.md
---

## Objective

When an agent performs side-effectful actions (sending email, creating tickets, calling APIs), add prompt rules that prevent duplicates on retry by using idempotency keys, pre-action checks, and post-action recording.

## When to Use

- Retries are likely (network, transient errors, tool retries)
- Side effects are visible to humans or systems
- Duplicate work is expensive or embarrassing

## Inputs

1. List of side-effectful actions the agent can perform
2. Available pre-action check tools (search, query, list)
3. Available post-action record store (file, KV, database)
4. Idempotency-key generation rule (deterministic from inputs)

## Constraints

**Must:**
- Generate an idempotency key deterministically from the action's inputs
- Pre-check whether the action was already performed before performing
- Record after successful performance
- On retry, the pre-check must find the prior record and skip
- Surface "already done" as a non-error outcome

**Must Not:**
- Use random or time-based idempotency keys
- Skip the post-action record (it breaks future pre-checks)
- Treat "already done" as success without acknowledging the prior performance

## Instructions

1. Define idempotency key per action type.
2. Define pre-check method per action.
3. Define post-record method per action.
4. Add prompt rules: pre-check → act → record, in that order.
5. Define the "already done" response shape.

## Output Format

```
ACTIONS WITH IDEMPOTENCY

action: send_email
  key: hash(to + subject + body_first_200_chars)
  pre_check: search outbox for key
  record: write key + sent_at to outbox

action: create_ticket
  key: hash(project + title + reporter)
  pre_check: search tickets where idempotency_key = key
  record: store key on ticket

PROMPT ADDITION
  Before any side-effectful action:
    1. Compute idempotency key from inputs
    2. Run pre-check
    3. If found:
        - emit { "status": "already_done", "prior_record_id": <id>, "key": <key> }
        - do not re-perform
    4. If not found:
        - perform action
        - record {key, result, ts}
        - emit { "status": "performed", "key": <key>, "result": ... }

ON FAILURE BETWEEN ACT AND RECORD
  - log inconsistency event
  - retry record only (do not retry act)
  - if record cannot be written, escalate

ALREADY-DONE RESPONSE
  Always treated as successful idempotent return; never silent.
```

## Verification

- Keys are deterministic from inputs (no time, no randomness)
- Every action has pre-check and record
- "Already done" is surfaced, not hidden
- Failure between act and record has a defined recovery path
