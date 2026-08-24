---
title: "GPT-Specific Prompting Patterns"
category: prompt-engineering/model-optimization
description: "Apply OpenAI / GPT-family conventions (system messages, JSON mode, structured outputs, function calling) to a prompt with measurable behavior changes."
techniques:
  - PR-01
  - ST-03
difficulty: intermediate
tags:
  - gpt
  - openai
  - model-specific
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/model-optimization/modelopt_claude_specific_patterns.md
  - domain-prompt-engineering/structured-output/structured_json_schema_prompt_builder.md
---

## Objective

Apply GPT-family conventions to a prompt: terse system message, JSON mode or structured outputs, function calling rather than text-encoded tools, response_format declarations.

## When to Use

- Authoring or migrating a prompt for GPT models
- Cross-model prompt under-performs on GPT
- Production usage on GPT needs schema reliability or function-calling wins

## GPT-Specific Patterns

| Pattern | Use case | Effect |
|---|---|---|
| Concise system message | Identity + a few rules | GPT respects short system messages well |
| JSON mode (`response_format: json_object`) | Need parseable JSON every time | Eliminates parser failures |
| Structured outputs (JSON Schema) | Strict typed JSON | Schema-conformant output |
| Function calling | Tool use | Native arguments without text parsing |
| Few-shot in chat format (user/assistant pairs) | Shape demonstration | Closer match to chat prior |
| `temperature: 0` for deterministic tasks | Reproducibility | Same input → same output |
| `seed:` parameter (where supported) | Reproducibility | Stable runs |
| Stop sequences | Truncate at marker | Predictable end |

## Constraints

**Must:**
- Use the strongest available structured-output mechanism (Schema > JSON mode > prompt-only JSON)
- Use function calling instead of text-encoded tool definitions
- Tag prompt with `model: gpt-*` in frontmatter
- Use `seed` and `temperature` settings deliberately

**Must Not:**
- Use Claude XML tags as primary structure (works but suboptimal)
- Encode tool calls in plain text when function calling is available
- Use long polite system messages (waste of tokens; GPT does not reward verbosity)

## Instructions

1. Inspect the prompt; map sections to GPT patterns.
2. Decide schema delivery: Structured Outputs > JSON mode > free text.
3. Migrate inline tool definitions to function calling.
4. Set temperature, seed, stop, response_format.
5. Test for schema compliance and reproducibility.

## Output Format

```
GPT PROMPT BUNDLE

system: |
  You are <role>. <scope>. <rules>.

response_format:
  type: json_schema
  json_schema:
    name: <name>
    schema:
      <JSON Schema>

functions:
  - name: <tool>
    description: ...
    parameters:
      <JSON Schema>

temperature: <value>
seed: <int>
stop: ["..."]

USER MESSAGE
  ...

PATTERNS APPLIED
  - structured outputs: yes
  - function calling: yes (replaced text-encoded tool definitions)
  - terse system message: yes
  - temperature: <value>; seed: <int>

FRONTMATTER ADDITION
  model: gpt-* (or family)
  techniques: + JS-01 (JSON Schema enforcement), FC-01 (function calling)
```

## Verification

- Schema delivery uses strongest available mechanism
- Function calling replaces inline tool definitions
- System message is concise
- Reproducibility settings (temperature, seed) recorded
