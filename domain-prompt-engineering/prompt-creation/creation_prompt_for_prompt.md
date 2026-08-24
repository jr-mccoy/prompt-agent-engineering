---
title: "Build a Meta-Prompt That Emits Prompts"
category: prompt-engineering/prompt-creation
description: "Author a meta-prompt whose output is itself a prompt, with strict structural constraints and a self-check pass."
techniques:
  - ST-02
  - ST-03
  - QA-01
difficulty: advanced
tags:
  - meta-prompt
  - prompt-generator
  - templating
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/prompt-creation/creation_task_prompt_from_blank.md
  - domain-prompt-engineering/prompt-creation/creation_user_prompt_template_designer.md
---

## Objective

Produce a meta-prompt that takes a brief description of a target task and emits a structured task prompt the user can run as-is. The emitted prompt must conform to a stated schema, not free-form prose.

## When to Use

- An organization wants consistent prompt structure across many authors
- A UI lets users describe a task and the system generates the prompt under the hood
- You need to mass-produce variants of a prompt class

## Inputs (the meta-prompt accepts)

1. Target task description (1–3 sentences)
2. Consumer (human / system / model)
3. Hard constraints (length, format, banned content)
4. Examples of accepted output (optional but recommended)

## Constraints

**Must:**
- Emit the prompt in a fixed schema (the same one every time)
- Refuse if any required input is missing — list what is missing
- Mark inferred elements with `[INFERRED:]` and a one-line reason
- Include a self-check block in the emitted prompt

**Must Not:**
- Hallucinate domain expertise not provided in inputs
- Add safety boilerplate not justified by inputs
- Vary the schema between calls

## Instructions

The meta-prompt should:

1. Validate inputs; refuse with a list if required fields are missing.
2. Derive role from consumer + accepted-output samples.
3. Derive constraints from the user's hard constraints + observed rejection patterns.
4. Emit the prompt in the canonical schema.
5. Append metadata: techniques used, difficulty, suggested model.

## Output Format (the meta-prompt emits)

```
---
title: ...
category: ...
techniques: [...]
difficulty: ...
---

## Objective
...

## Inputs
...

## Constraints
Must: ...
Must Not: ...

## Instructions
...

## Output Format
...

## Verification
...

---
META
  inferred: [...]
  open_questions: [...]
  suggested_model: ...
```

## Verification (of the meta-prompt itself)

- Given identical inputs, output is deterministic in schema and near-deterministic in content
- Missing-input case triggers refusal, not invention
- Emitted prompt passes its own Verification block on a sample run
- Every `[INFERRED:]` tag has a one-line reason
