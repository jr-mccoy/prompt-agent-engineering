---
title: "Multi-Persona Router in a Single System Prompt"
category: prompt-engineering/system-prompts
description: "Design a system prompt that hosts multiple sub-personas behind a deterministic router so the right persona handles the right input."
techniques:
  - DC-01
  - PR-01
difficulty: advanced
tags:
  - multi-persona
  - router
  - system-prompt
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/system-prompts/system_role_charter_designer.md
---

## Objective

Combine 2–5 sub-personas under one system prompt with a router that picks one persona per input, deterministic on input features, with explicit hand-off rules between personas.

## When to Use

- A single assistant must serve distinguishable modes (support, sales, internal)
- Splitting into separate deployments adds operational cost
- Routing decisions are deterministic enough to encode

## Inputs

1. The set of personas with their charters
2. Routing features (intent, channel, user role)
3. Default persona when routing is uncertain
4. Hand-off rules between personas

## Constraints

**Must:**
- Define exactly one router that runs first
- Router emits a chosen persona id and a one-line reason
- Each persona has its own charter, scope, and refusal policy
- Define hand-off events: when persona A passes to persona B mid-session

**Must Not:**
- Let two personas reply in the same turn
- Let a persona override the router unilaterally
- Allow ambiguous routing without a default

## Instructions

1. Define the router rules.
2. Define each persona's charter, scope, refusals.
3. Define hand-off events and the announcement text.
4. Define default persona for ambiguous inputs.
5. Document router determinism (same input → same persona).

## Output Format

```
SYSTEM PROMPT (multi-persona)

ROUTER
  Inputs: <feature set>
  Rules:
    - if <feature pattern>: persona = <id>
    - elif <feature pattern>: persona = <id>
    - else: persona = <default id>
  Emit:
    {"persona": "<id>", "reason": "<one line>"}

PERSONAS

[persona id="support"]
  charter: ...
  scope: ...
  refuses: ...

[persona id="sales"]
  charter: ...
  ...

[persona id="internal"]
  charter: ...
  ...

HAND-OFF EVENTS
  - if user explicitly asks for sales while support is active → switch
  - announcement: "Switching to <persona> for <reason>."
  - never silently switch

DEFAULT
  - persona id = support

DETERMINISM RULE
  - Given identical input, the router must select the same persona on repeated calls.
```

## Verification

- Router is deterministic
- Each persona has a charter and refusal set
- Hand-off events have announcement text
- Default persona named for ambiguous inputs
