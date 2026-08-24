---
title: "Design a Role Charter for a System Prompt"
category: prompt-engineering/system-prompts
description: "Author the role-defining block of a system prompt: identity, scope, expertise boundary, authority, and what this role explicitly is not."
techniques:
  - PR-01
  - CM-02
difficulty: intermediate
tags:
  - system-prompt
  - role
  - charter
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/prompt-creation/creation_role_first_prompt_builder.md
---

## Objective

Produce a role-charter block (4–8 sentences) that anchors a system prompt: who the assistant is, what it knows, what it can do, what it does not do, and how it speaks.

## When to Use

- Designing a new system prompt
- Refactoring a system prompt whose role has drifted
- Aligning multiple deployments around a single role definition

## Inputs

1. The intended role and its production purpose
2. The audience and surface (chat, API, embedded)
3. Real expertise edge: where does this role's knowledge stop?
4. What the role refuses
5. What the role refers out, and to where

## Constraints

**Must:**
- Open with `You are <role>` (concrete, not adjectival)
- State scope in one sentence
- State expertise edge in one sentence
- State authority in one sentence
- Include a "Refuses" line and a "Refers Out" line
- Keep total length ≤ 8 sentences

**Must Not:**
- Use marketing adjectives ("expert", "world-class")
- Define identity by emotion ("you are caring")
- List capabilities without scoping them

## Instructions

1. Write `You are <role>`.
2. Add scope: what tasks fit; what does not.
3. Add expertise edge: what topics the role does not opine on.
4. Add authority: what the role can decide unilaterally.
5. Add "Refuses" and "Refers Out".
6. Add voice direction (1 line: register and required vocabulary).

## Output Format

```
ROLE CHARTER

You are <role>.

Scope: <what tasks belong here>.

Expertise: <topics where you have grounded competence>; you do not address <topics outside>.

Authority: you can <decide / produce / publish>; you do not <reach beyond>.

Refuses: <list>.

Refers Out: <topic> → <named target>.

Voice: <register>; uses <required vocabulary>; avoids <banned register>.
```

## Verification

- Total ≤ 8 sentences
- No marketing adjectives
- Refuses and Refers Out are concrete, not generic
- A reader can predict the role's behavior on a hard case from the charter alone
