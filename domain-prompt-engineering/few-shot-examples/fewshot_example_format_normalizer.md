---
title: "Normalize the Format of Few-Shot Examples"
category: prompt-engineering/few-shot-examples
description: "Make every few-shot example share input shape, output shape, and delimiter conventions so the model imitates structure, not noise."
techniques:
  - ST-03
difficulty: beginner
tags:
  - normalization
  - few-shot
  - delimiters
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/few-shot-examples/fewshot_example_selector.md
---

## Objective

Standardize a set of few-shot examples so each has identical structure, delimiters, and field naming. The model learns the schema, not the inconsistencies.

## When to Use

- A prompt has examples gathered from different sources with different formats
- The model is producing output that mimics surface variations from examples
- A new author is adding examples to an existing pack

## Inputs

1. The current example set
2. The target output schema
3. Delimiter conventions (XML tags, headers, JSON, etc.)

## Constraints

**Must:**
- Pick one delimiter convention and apply to all examples
- Make every input section appear in the same order
- Make every output section appear in the same order
- Preserve content; only restructure

**Must Not:**
- Drop content while normalizing
- Change which fields exist (this is normalize, not redesign)
- Mix delimiter styles within the pack

## Instructions

1. Pick the delimiter convention (XML tags is recommended for Claude; JSON for OpenAI structured outputs).
2. Define canonical section ordering for input and output.
3. For each example, restructure to canonical order with chosen delimiters.
4. Verify content preserved by diff.
5. Lock the convention with a comment.

## Output Format

```
CONVENTION
  delimiter: <xml-tags | json | headers | ...>
  input fields (ordered): [...]
  output fields (ordered): [...]

NORMALIZED EXAMPLES
  <example id="1">
    <input>
      <field_a>...</field_a>
      <field_b>...</field_b>
    </input>
    <output>
      <field_x>...</field_x>
      <field_y>...</field_y>
    </output>
  </example>
  ...

DIFF (per example)
  example 1:
    structure changes: ...
    content preserved: yes / details

LOCK COMMENT
  "Few-shot examples follow the <delimiter> convention defined above. Do not mix styles."
```

## Verification

- All examples use the same convention
- Field ordering identical across examples
- Content unchanged (only structure changed)
- Lock comment present
