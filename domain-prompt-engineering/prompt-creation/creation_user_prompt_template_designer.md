---
title: "Design a Reusable User-Prompt Template"
category: prompt-engineering/prompt-creation
description: "Convert one-off prompts into a parameterized template with named variables, a sample fill, and a fill-validator."
techniques:
  - ST-02
  - ST-03
  - CM-02
difficulty: intermediate
tags:
  - templates
  - parameterization
  - reusability
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/prompt-creation/creation_input_validation_prompt.md
  - domain-prompt-engineering/utilities/json_prompt_translator.md
---

## Objective

Take a working one-off prompt and abstract it into a reusable template with explicit `${variable}` slots, declared types, defaults, and a validator that rejects malformed fills.

## When to Use

- A prompt has been used three or more times with minor variation
- A prompt will be embedded in code or a UI and parameterized
- You want to lock the structure so contributors only fill values

## Inputs

1. Two or more concrete instances of the prompt with different content
2. Which parts the user considers "the structure" vs "the inputs"
3. Where the template will be used (UI form, code, chat snippet)
4. Whether the template targets a specific model

## Constraints

**Must:**
- Replace every variable point with `${variable_name}` using snake_case
- Declare each variable's type, allowed values, and default (or "required: true")
- Include one fully filled sample
- Include a validator that rejects fills missing required variables or violating types
- Keep static text byte-identical to the input examples in shared regions (so prompt caching can hit on the prefix)

**Must Not:**
- Introduce variables for things that never varied across the input examples
- Use ambiguous names like `${input}` or `${data}` when a domain term exists
- Silently lowercase or reformat preserved text

## Instructions

1. Diff the input examples; everything that varies is a candidate variable.
2. Name each variable from the user's domain language, not generic English.
3. Place the most stable text earliest to maximize cache prefix length.
4. Write the validator as a checklist, not prose.
5. Provide one sample fill that demonstrates a non-trivial case.

## Output Format

```
TEMPLATE:
<verbatim prompt with ${variable} slots>

VARIABLES:
  - name: <snake_case>
    type: <string | int | enum[a,b,c] | list<string> | multiline>
    required: <true | false>
    default: <value or "n/a">
    description: <one line>

SAMPLE FILL:
  <variable>: <value>
  ...

VALIDATOR:
  - reject if any required variable missing
  - reject if <variable> not in <enum>
  - reject if <variable> length > <n>
  - ...

CACHE NOTE:
  Stable prefix length: <n chars>
  First variable position: <line/section>
```

## Verification

- Every `${name}` in TEMPLATE has a row in VARIABLES
- Every VARIABLE row appears at least once in TEMPLATE
- SAMPLE FILL passes every VALIDATOR rule
- Removing the SAMPLE FILL still leaves a runnable template
