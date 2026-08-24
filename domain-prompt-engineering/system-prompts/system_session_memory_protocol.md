---
title: "Session Memory Protocol"
category: prompt-engineering/system-prompts
description: "Specify what the assistant remembers across turns, what it forgets, and how it surfaces remembered facts so users can correct them."
techniques:
  - CM-02
  - ST-03
difficulty: intermediate
tags:
  - memory
  - session
  - persistence
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/system-prompts/system_persistent_rule_set_builder.md
---

## Objective

Add a session-memory protocol to the system prompt: which facts persist across turns, which expire, how the assistant surfaces remembered items, and how the user corrects them.

## When to Use

- Multi-turn assistants where prior turns matter
- Assistants that have a memory feature and need rules around it
- Cases where stale or incorrect memory degrades behavior

## Inputs

1. Memory categories (preferences, named entities, facts about the user, in-flight task state)
2. Lifetime per category (turn / session / cross-session)
3. Surfacing rules (when to mention what is remembered)
4. Correction protocol

## Constraints

**Must:**
- Define lifetime per category
- Surface remembered facts when they affect output ("Using the preference you set earlier: <X>")
- Allow user to correct any remembered item with a clear command
- Forget on user request without arguing

**Must Not:**
- Persist anything beyond its declared lifetime
- Surface remembered items in every turn (noise)
- Resist a forget command

## Instructions

1. Enumerate categories and lifetimes.
2. Define when to surface memory (load-bearing surfacing only).
3. Define correction commands ("Forget that.", "That was wrong: <correction>").
4. Define what is never remembered.

## Output Format

```
SESSION MEMORY PROTOCOL

CATEGORIES
  - preferences: lifetime = session
  - named_entities: lifetime = session
  - user_facts: lifetime = cross-session (only with consent)
  - task_state: lifetime = until task complete

NEVER REMEMBERED
  - sensitive personal information unless user explicitly asks to remember
  - one-off jokes, asides, transient context

SURFACING RULES
  - mention remembered fact when it changes the output of this turn
  - never mention more than 2 remembered facts per turn
  - prefix with "Using <fact you mentioned earlier>:"

CORRECTION COMMANDS
  - "Forget <X>" → drop X immediately, acknowledge
  - "That was wrong: <new>" → replace value, acknowledge
  - "What do you remember about me?" → enumerate up to <n>

CONFLICTS
  - if remembered fact contradicts new statement, ask once; default to new statement
```

## Verification

- Lifetimes named per category
- Surfacing is load-bearing only
- Correction commands have exact phrasings
- Forget request is honored without negotiation
