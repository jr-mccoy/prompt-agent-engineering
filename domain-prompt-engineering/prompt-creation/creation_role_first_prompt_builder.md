---
title: "Build a Prompt Using the Role-First Pattern"
category: prompt-engineering/prompt-creation
description: "Author a prompt that opens with a tightly bounded role, then derives task, constraints, and format consistent with that role."
techniques:
  - ST-01
  - ST-02
  - PR-01
difficulty: beginner
tags:
  - role-first
  - persona
  - structure
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/style-and-voice/style_persona_designer_for_writing.md
---

## Objective

Produce a prompt where the role definition is the first and most load-bearing element, and every subsequent section is consistent with what that role would actually do.

## When to Use

- The task is judgment-heavy and a clear professional perspective improves output
- You need to constrain vocabulary, scope, and refusal behavior simultaneously
- You want the prompt readable by a non-technical reviewer

## Inputs

1. The target task in one sentence
2. The professional or functional perspective the model should take
3. What that role would refuse to do
4. What that role would defer to a different role
5. Sample inputs the role will see

## Constraints

**Must:**
- Open with `You are <role>` followed by 2–4 sentences defining scope, expertise boundary, and authority
- Make every later constraint traceable to the role definition
- Include a `Refer Out` clause naming what gets escalated
- Specify the role's voice (vocabulary register, formality)

**Must Not:**
- Use marketing language ("expert", "world-class", "10x") — replace with concrete capabilities
- Give the role authority it would not have in real life
- Bury the role behind preamble or context

## Instructions

1. Write the role in 2–4 sentences: identity, expertise, scope edge.
2. Write what the role refuses (1–3 items).
3. Write what the role refers out (1–3 items, with where to refer).
4. Derive constraints: keep only those a real person in this role would impose.
5. Derive output format: match what this role would actually deliver.

## Output Format

```
ROLE
You are <role>. <scope sentence>. <expertise boundary>. <authority>.

REFUSES
  - <item>

REFERS OUT
  - <item> → <where>

VOICE
  - register: <formal | neutral | casual>
  - vocabulary: <domain terms required, jargon banned>

TASK
<imperative>

CONSTRAINTS
  Must: ...
  Must Not: ...

OUTPUT FORMAT
<exact structure>
```

## Verification

- A reader who only sees the ROLE block can predict 80% of CONSTRAINTS
- REFUSES and REFERS OUT contain at least one item each
- VOICE is operational (banned and required terms named, not adjectives)
- No constraint conflicts with the role's stated authority
