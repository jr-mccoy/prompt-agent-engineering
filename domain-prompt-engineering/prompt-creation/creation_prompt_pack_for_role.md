---
title: "Build a Prompt Pack for a Role"
category: prompt-engineering/prompt-creation
description: "Produce a coherent set of 5–12 prompts for a single role (e.g. CSM, sales rep, recruiter) that share voice, schema, and naming."
techniques:
  - ST-02
  - PR-01
difficulty: intermediate
tags:
  - prompt-pack
  - role
  - bundle
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/prompt-creation/creation_role_first_prompt_builder.md
---

## Objective

Design a coherent bundle of prompts for a single role, sharing role definition, voice, output schema scaffolding, and naming convention so the user experiences the pack as one tool.

## When to Use

- A role has 5–15 recurring tasks worth prompting
- A team is rolling out AI assistance to a function (CS, sales, finance)
- You want consistent UX across prompts for a single user

## Inputs

1. The target role and 1–2 sentence scope
2. The 5–12 most frequent tasks for that role (with frequency)
3. Tools/data the role has access to
4. Voice/register constraints (brand, formality)

## Constraints

**Must:**
- Share a single ROLE block across all prompts (defined once, referenced by name)
- Share a naming convention (e.g., `csm_<task>.md`)
- Share an output-schema scaffold (e.g., always include `summary`, `next_actions`)
- Document inter-prompt handoffs (output of one is input of another)
- Cover the top tasks by frequency, not by glamour

**Must Not:**
- Redefine the role inconsistently across prompts
- Add prompts for tasks not on the input list
- Use different output schemas per prompt without justification

## Instructions

1. Write the shared ROLE block.
2. List prompts: `<prefix>_<task>.md` for each top task.
3. For each, define inputs, output, and how it links to others.
4. Choose one common output scaffold; allow per-prompt extension.
5. Identify which prompts depend on others (chain or branch).

## Output Format

```
ROLE (shared)
<role block>

NAMING CONVENTION
  prefix: <e.g. csm_>
  pattern: <prefix>_<task_snake_case>.md

SHARED OUTPUT SCAFFOLD
  summary: ...
  next_actions: [...]
  <role-specific extensions allowed>

PROMPT LIST
  1. csm_<task>.md
     inputs: ...
     output: scaffold + <extensions>
     depends_on: [list]
  2. ...

HANDOFFS
  prompt A.output.<field> → prompt B.input.<field>

OUT OF SCOPE
  - <tasks deliberately not included> — reason
```

## Verification

- Role block is byte-identical across all prompts
- Naming convention applies to every prompt
- Every prompt covers a task on the input list
- Handoffs validate (every consumed field is produced by some prompt or external source)
