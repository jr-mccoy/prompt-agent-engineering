---
title: "Build a Task Prompt From a Blank Page"
category: prompt-engineering/prompt-creation
description: "Structured intake that converts a fuzzy goal into a first-draft, production-shaped task prompt with role, inputs, constraints, output contract, and verification."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - prompt-creation
  - greenfield
  - intake
  - first-draft
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/prompt-creation/creation_clarification_loop_prompt.md
  - domain-prompt-engineering/skill-development/promptcraft_specification_defines_done.md
---

## Objective

Take a fuzzy goal ("I want a prompt that does X") and produce a first-draft task prompt that has every load-bearing element of a production prompt, even if rough. The output is a draft to iterate on, not a final prompt.

## When to Use

- You are starting from a blank page with a vague intent
- You need a prompt that someone else will refine
- You want to avoid skipping mandatory elements (role, inputs, output contract, refusal conditions)

## Inputs (collect before drafting)

1. One-sentence goal in the user's words
2. Who consumes the output (human reader, downstream system, another model)
3. One real example of an input the prompt must handle
4. One example of an output that would be accepted
5. One example of an output that would be rejected and why
6. Hard constraints (length, format, forbidden content, required citations)
7. Failure mode that worries the user most

If any of items 2–6 are missing, ask for them before drafting. Do not invent them.

## Constraints

**Must:**
- Produce six labeled sections: Role, Inputs, Task, Constraints, Output Format, Verification
- Use only information the user supplied; mark inferred items with `[INFERRED:]`
- Make the output contract specific enough to grade pass/fail
- Include at least one `Must Not` rule derived from the rejected-output example

**Must Not:**
- Pad the prompt with generic best-practice rules unrelated to this task
- Use the words "best practices", "high quality", or "world class" without operational definitions
- Add safety boilerplate not requested by the user
- Compress unfamiliar domain language; preserve the user's vocabulary

## Instructions

1. Restate the goal in one sentence and confirm consumer.
2. Derive the role from the consumer + accepted-output example.
3. Translate the rejected-output example into one specific `Must Not`.
4. Translate the accepted-output example into the Output Format section.
5. Convert the user's worried failure mode into a Verification step.
6. Mark every section that is inferred rather than stated with `[INFERRED:]` and a one-line reason.

## Output Format

```
ROLE: <one sentence>
INPUTS: <ordered list of named inputs and their shape>
TASK: <imperative description of what to produce>
CONSTRAINTS:
  Must:
    - ...
  Must Not:
    - ...
OUTPUT FORMAT: <exact structure, fields, length cap>
VERIFICATION: <self-check the model performs before returning>

INFERRED ITEMS:
  - <field>: <why inferred>
OPEN QUESTIONS:
  - <questions that should be answered before next iteration>
```

## Verification

Before returning, confirm:
- Every accepted-output property appears in OUTPUT FORMAT
- The rejected-output property appears in `Must Not`
- VERIFICATION names a concrete check, not "review carefully"
- No section is silently invented; inferred items are flagged
- OPEN QUESTIONS lists at least the highest-risk gap
