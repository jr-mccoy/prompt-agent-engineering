---
title: "Dry-Run / Propose-Confirm-Execute Pattern"
category: prompt-engineering/tool-use
description: "Three-step protocol for irreversible tool calls: propose with a diff, get explicit confirmation, then execute with idempotency."
techniques:
  - ST-02
  - CM-02
  - DP-04
  - QA-01
difficulty: intermediate
tags:
  - tool_use
  - dry_run
  - confirmation
  - irreversible
  - idempotency
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/tool-use/tooluse_disambiguation_pattern.md
  - domain-prompt-engineering/tool-use/tooluse_failure_recovery_pattern.md
  - domain-prompt-engineering/tool-use/tooluse_multi_tool_orchestration.md
---

## Objective

For irreversible tool calls (delete, send, charge, force-push, deploy), enforce a three-step protocol: (1) propose with a diff or summary, (2) wait for explicit confirmation, (3) execute once with an idempotency key.

## When to Use

- The tool's action cannot be undone within the session, or undo is costly.
- Past sessions have executed actions the user did not actually authorize.
- You want a per-call audit row showing proposal → confirmation → execution.

## Inputs

```
TOOL_NAME: <name>
TOOL_ARGS: <args resolved>
ACTION_DESCRIPTION: <one sentence in present tense>
DIFF_OR_SUMMARY: <before → after, or list of items affected>
CONFIRMATION_TEXT_REQUIRED: <e.g., "yes", "confirm", or the destination ID>
SESSION_ID: <stable session identifier>
PRIOR_CONFIRMATION: <optional: yes if user already confirmed in this turn>
```

## Constraints

### Must
- Step 1 (propose): emit a structured proposal — `tool`, `args`, `action_description`, `diff_or_summary`, `idempotency_key`, `expires_at`. Do not invoke.
- `idempotency_key = sha1(SESSION_ID + tool + canonical_json(args))`. Same key ⇒ same proposal.
- Step 2 (await): require `CONFIRMATION_TEXT_REQUIRED` to be present in the user's next message verbatim (case-insensitive). Synonyms ("ok", "go") do NOT pass unless they are the configured token.
- Step 3 (execute): include `idempotency_key` in the call. If a prior execution with the same key succeeded in the session, return the cached result instead of re-calling.
- A proposal expires after a configured TTL (default 5 minutes). After expiry, restart from step 1.

### Must Not
- Skip step 1 because the args feel obvious.
- Accept implicit confirmation ("looks good", thumbs-up reaction).
- Re-prompt with a slightly different proposal in step 3 — that is a new proposal and goes back to step 1.
- Continue if `PRIOR_CONFIRMATION` is for a different proposal (different idempotency key).

## Instructions

1. Build proposal block with all five fields.
2. Render `diff_or_summary` as either a unified diff (for file/text changes) or a bulleted "will affect" list (for state changes), capped at 10 items + "and N more".
3. State the exact confirmation token: "Reply with `<token>` to proceed."
4. On user reply: hash and compare against the stored idempotency_key. On match + correct token, execute. On mismatch, restart.
5. After execute, emit a receipt: `{idempotency_key, executed_at, result_summary, undo_hint?}`.

## Output Format

```yaml
# Step 1 — proposal:
proposal:
  tool: <name>
  args: {<...>}
  action_description: "<sentence>"
  diff_or_summary: |
    <diff or bullets>
  idempotency_key: <sha1>
  expires_at: <ISO>
  confirmation_token: <token>

# Step 2 — awaiting:
state: awaiting_confirmation

# Step 3 — execution receipt:
receipt:
  idempotency_key: <sha1>
  executed_at: <ISO>
  result_summary: "<sentence>"
  undo_hint: "<command or 'no automatic undo'>"
```

## Verification

- Proposal includes all five fields and a non-empty `diff_or_summary`.
- `idempotency_key` is reproducible from `SESSION_ID + tool + canonical_json(args)`.
- Execution path runs only when (a) confirmation token matches verbatim AND (b) idempotency_key matches the proposal AND (c) `now < expires_at`.
- Receipt's `idempotency_key` equals the proposal's.
