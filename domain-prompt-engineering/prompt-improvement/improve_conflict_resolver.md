---
title: "Resolve Conflicting Rules in a Prompt"
category: prompt-engineering/prompt-improvement
description: "Find pairs of rules that contradict, classify the conflict type, and propose a resolution that preserves the dominant intent."
techniques:
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - conflict-resolution
  - rules
  - hierarchy
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/instruction-design/instruction_conflict_taxonomy.md
  - domain-prompt-engineering/prompt-improvement/improve_redundancy_eliminator.md
---

## Objective

Identify pairs of rules in a prompt that pull in opposite directions, classify the conflict, and produce a resolution: hierarchy, scoping, or rewrite.

## When to Use

- A prompt produces inconsistent outputs that swing between two patterns
- A reviewer asks "which rule wins here?" and the prompt has no answer
- You inherited a prompt with rules accreted from multiple authors

## Inputs

1. The current prompt
2. Examples where outputs swung between patterns (if available)
3. Authority list: which rule sources have priority (legal > brand > taste, etc.)

## Constraints

**Must:**
- Identify pairs that conflict and label the type:
  - `direct` — A says do X, B says do not do X
  - `scope-overlap` — A applies to all cases, B applies to a subclass and disagrees
  - `priority-tied` — both apply but no precedence given
  - `vacuous` — appears to conflict but rules apply at different times/scopes
- For `direct` and `priority-tied`, propose a resolution: precedence rule, scoping qualifier, or rewrite
- Preserve dominant intent based on the authority list

**Must Not:**
- Resolve by deleting one side without justification
- Introduce new content; rewrites must use existing rule material
- Leave a `direct` conflict unresolved

## Instructions

1. List rule pairs flagged as conflicting. For each, classify the type.
2. For `direct` conflicts, choose the dominant rule by authority and either delete or scope the loser.
3. For `scope-overlap`, add an explicit scoping qualifier ("except when <case>").
4. For `priority-tied`, add a precedence sentence to the prompt.
5. For `vacuous`, add a comment in the prompt clarifying scope so the apparent conflict disappears.

## Output Format

```
CONFLICT PAIRS
  pair 1:
    rule A: "<text>"
    rule B: "<text>"
    type: direct | scope-overlap | priority-tied | vacuous
    authority winner: <A | B | n/a>
    resolution: <precedence | scope | rewrite | clarify>
    new text: "<resolved rule(s)>"

REWRITTEN PROMPT
<full rewrite with resolutions applied>

UNRESOLVED
  - <pair id>: <why resolution requires user input>
```

## Verification

- No `direct` conflict is left unresolved
- Each resolution preserves the higher-authority intent
- The rewritten prompt does not introduce new constraints
- A sample run on the swing-pattern inputs now produces consistent output
