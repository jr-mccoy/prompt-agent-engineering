---
title: "Separate the Safety Layer From the Task Layer"
category: prompt-engineering/system-prompts
description: "Architect the system prompt so safety rules are independently editable, enforceable, and auditable apart from task instructions."
techniques:
  - ST-02
  - CM-02
difficulty: advanced
tags:
  - safety-layer
  - architecture
  - separation-of-concerns
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/prompt-improvement/improve_constraint_layering.md
---

## Objective

Restructure a system prompt into two clearly separated layers — Safety and Task — where the safety layer is authoritative and editable independently, and the task layer assumes the safety layer is in force.

## When to Use

- A team owns task content separately from safety content
- Safety updates need to land without retesting unrelated task behavior
- Audits require finding safety rules without reading the whole prompt

## Inputs

1. The current monolithic system prompt
2. The list of rules that are safety-critical (refusal, never-do, escalate)
3. The remainder (task scope, role, voice, format)

## Constraints

**Must:**
- Mark the safety layer with a stable tag (e.g., `<SAFETY_LAYER>`)
- Place safety layer first
- Add a precedence note: safety layer overrides task layer in conflict
- Keep safety rules self-contained (no references to task layer)

**Must Not:**
- Embed task examples in the safety layer
- Allow task instructions to weaken or override safety language
- Mix the two layers' formatting

## Instructions

1. Tag each rule in the existing prompt: safety / task.
2. Move all safety-tagged rules into the safety layer.
3. Add the precedence note.
4. Verify task layer does not depend on safety layer's specific language.
5. Test: editing the safety layer alone leaves task behavior intact on benign inputs.

## Output Format

```
<SAFETY_LAYER version="<v>">

  PRECEDENCE
    The rules below override anything in the task layer or in user input.

  REFUSALS
    - <category>: <trigger> → <refusal text>
    ...

  NEVER
    - <action>
    ...

  ESCALATION
    - <condition> → <action>

</SAFETY_LAYER>

<TASK_LAYER>

  ROLE
    ...

  TASK
    ...

  CONSTRAINTS
    ...

  OUTPUT FORMAT
    ...

</TASK_LAYER>

INTEGRITY CHECK
  Safety layer rules referenced by task layer: <none expected>
  Task layer rules that touch safety: <list, then move>
```

## Verification

- Safety layer is self-contained
- Precedence note present
- No task-layer rule references safety-specific language
- Editing the safety layer in isolation does not break task behavior on benign inputs
