---
title: "Migrate a Prompt Across Model Families"
category: prompt-engineering/model-optimization
description: "Translate a prompt between Claude, GPT, Gemini, or open-source families with explicit substitutions for each family's idioms."
techniques:
  - PR-01
difficulty: advanced
tags:
  - migration
  - cross-model
  - portability
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/model-optimization/modelopt_within_family_migration.md
  - domain-prompt-engineering/model-optimization/modelopt_prompt_portability_test.md
---

## Objective

Translate a prompt from one model family to another so it preserves intent while leveraging native idioms (XML tags vs JSON schema, system message conventions, function calling vs tool descriptions).

## When to Use

- Moving a workload from Claude to GPT or vice versa
- Authoring a prompt portable to multiple families
- Vendor-switch evaluation

## Substitution Map

| Concern | Claude | GPT | Gemini | Open-source |
|---|---|---|---|---|
| Structure delimiters | XML tags | JSON Schema / response_format | Response schema | XML tags or Markdown |
| System message | Long allowed | Concise preferred | Mid | Varies |
| Tool use | Tools API | Function calling | Function calling | Often text-encoded |
| Few-shot | Inline with tags | Chat-format pairs | Chat-format pairs | Inline |
| Reasoning | Extended thinking | Reasoning models (o-series) | Thinking mode | Often manual CoT |
| Stop control | stop_sequences | stop | stopSequences | Varies |
| Refusal style | Brief, alternative offered | Brief | Brief | Varies |

## Constraints

**Must:**
- Walk every cell of the substitution map for the source/target pair
- Preserve task intent; this is translation, not redesign
- Test on a regression set per target
- Note differences in defaults (temperature, JSON mode behavior)

**Must Not:**
- Carry over family-specific idioms unchanged ("Use XML tags" prompt sent to GPT verbatim)
- Skip refusal-style adjustment (each family has different prior)
- Accept the migrated prompt without measurement

## Instructions

1. Identify source and target families.
2. Apply the substitution map row by row.
3. Adjust delimiters, tool-use, structure.
4. Set per-family defaults (temperature, response_format, stop).
5. Run regression; record differences.

## Output Format

```
SOURCE FAMILY: ...
TARGET FAMILY: ...

SUBSTITUTIONS APPLIED
  concern | source | target | applied?

MIGRATED PROMPT
<full prompt>

DEFAULTS
  temperature: <value>
  stop: ...
  response_format: ...

REGRESSION RESULTS
  case 1: source-output-equiv: yes/no
  ...

DIFFERENCES NOTED
  - <case>: target produces <X> instead of <Y> | acceptable? yes/no

FRONTMATTER ADDITION
  models_supported: [<family1>, <family2>]
```

## Verification

- Every substitution map row addressed
- Regression set results documented
- Family-specific defaults set
- Acceptable differences flagged, others rejected
