---
title: "Decide What Belongs in System vs User Prompt"
category: prompt-engineering/prompt-creation
description: "Classify each rule, fact, and instruction into system, developer, or user role based on stability, sensitivity, and override behavior."
techniques:
  - ST-02
  - CM-02
difficulty: intermediate
tags:
  - system-prompt
  - role-split
  - instruction-hierarchy
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/system-prompts/system_role_charter_designer.md
  - domain-prompt-engineering/instruction-design/instruction_hierarchy_designer.md
---

## Objective

Given a flat list of instructions intended for a model, classify each one into system, developer, or user role and produce three clean blocks plus the rationale for each placement.

## When to Use

- A prompt has grown into a single wall of text and behavior is drifting
- Migrating from chat-style to API-style with role separation
- Designing a multi-tenant system where users supply their own input but the operator owns the rules

## Inputs

1. The current flat prompt (or a list of instructions)
2. Whether end-users can see the system prompt
3. Whether end-users can override any instruction (and which)
4. The expected lifetime of each instruction (per-call vs durable)

## Constraints

**Must:**
- Place identity, immutable rules, and refusal policies in system
- Place task wiring, tool definitions, and per-deployment defaults in developer (or system if no developer role exists)
- Place the request being answered in user
- Justify each placement with one of: stability, sensitivity, override-resistance, scope
- Flag any rule that does not cleanly fit one role

**Must Not:**
- Duplicate the same rule across roles unless required for redundancy and explicitly noted
- Move user-supplied content into system
- Promote ad-hoc per-task instructions into system

## Instructions

1. Mark each instruction with stability (per-call / per-session / durable).
2. Mark each instruction with override-allowed (yes / no / partial).
3. Apply placement rules:
   - durable + no-override → system
   - per-deployment + no-override → developer
   - per-call → user
4. For unfit items, propose either a rewrite that fits or a "split" that separates the durable part from the variable part.
5. Re-emit the three blocks with stable internal ordering.

## Output Format

```
SYSTEM PROMPT:
<block>

DEVELOPER PROMPT:
<block>

USER PROMPT:
<block>

PLACEMENT RATIONALE:
  - "<instruction excerpt>" → <role> (reason: <stability|sensitivity|override|scope>)
  - ...

UNFIT ITEMS:
  - <item>: <proposed rewrite or split>
```

## Verification

- No instruction appears in more than one role without a `RATIONALE` note marking it intentional duplication
- User block contains only inputs, never rules
- Every system rule survives a hostile user message attempting override
- The three blocks together preserve every original instruction (no silent drops)
