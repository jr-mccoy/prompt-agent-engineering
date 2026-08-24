---
title: "Build Input Validation Into a Prompt"
category: prompt-engineering/prompt-creation
description: "Add an input-validation preamble that rejects malformed input with a structured error before any task work happens."
techniques:
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - validation
  - guard
  - input-contract
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/structured-output/structured_json_repair_pattern.md
  - domain-prompt-engineering/prompt-creation/creation_clarification_loop_prompt.md
---

## Objective

Add a guard pass to a prompt so it inspects input against a contract first, returns a structured rejection on failure, and only proceeds to the task when the contract holds.

## When to Use

- The prompt is reached programmatically, so junk input is possible
- Garbage outputs from garbage inputs are causing downstream errors
- You want clean error telemetry instead of silent malformed answers

## Inputs

1. Input contract: required fields, types, allowed values, length bounds
2. The task prompt to guard
3. Whether the caller wants the rejection in JSON or text

## Constraints

**Must:**
- Run validation before any task reasoning
- Emit a structured rejection with field-level errors
- Distinguish missing vs malformed vs out-of-range
- Define exactly one shape for the rejection (callers parse it)

**Must Not:**
- Try to repair input silently — only log repairs the caller can see
- Run partial task work when validation fails
- Hide the validation step from the response (it must be inspectable)

## Instructions

1. Define the contract as a checklist with check methods.
2. Insert the validation block at the top of the prompt.
3. Define the rejection shape (JSON or text) and its fields.
4. Define the proceed condition: all required pass.
5. Optionally allow `repair: true` mode that fixes specific known malformations and notes them.

## Output Format (the guarded prompt structure)

```
INPUT CONTRACT
  required_fields: [...]
  types: ...
  ranges: ...

VALIDATION (run first)
  for each field:
    - present? type-correct? in-range?
  produce errors[]

IF errors NOT EMPTY:
  return:
    {
      "status": "rejected",
      "errors": [
        {"field": "...", "code": "missing|malformed|out_of_range", "detail": "..."}
      ]
    }

ELSE:
  proceed with task prompt

REPAIR MODE (optional)
  if repair: true
    fix known malformations
    record:
      "repairs": [{"field": "...", "from": "...", "to": "..."}]
  then re-validate
```

## Verification

- Rejection shape is byte-stable across runs
- Validation runs before any task reasoning (verifiable from output ordering)
- Each error code is one of the named codes
- Repair mode reports every change; no silent repairs
