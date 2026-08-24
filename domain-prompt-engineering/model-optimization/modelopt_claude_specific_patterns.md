---
title: "Claude-Specific Prompting Patterns"
category: prompt-engineering/model-optimization
description: "Apply Claude-specific patterns (XML tags, prefill, system message conventions, extended thinking) to a prompt for measurable behavior improvements."
techniques:
  - PR-01
  - ST-03
difficulty: intermediate
tags:
  - claude
  - model-specific
  - xml-tags
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/model-optimization/modelopt_gpt_specific_patterns.md
  - domain-prompt-engineering/structured-output/structured_xml_tag_pattern.md
---

## Objective

Apply Claude-family conventions to a prompt and predict the behavior change for each.

## When to Use

- A prompt is being authored or migrated for Claude (Sonnet, Opus, Haiku)
- A model-agnostic prompt under-performs on Claude
- Production usage on Claude needs latency or quality wins

## Claude-Specific Patterns

| Pattern | Use case | Effect |
|---|---|---|
| XML tags around inputs / outputs (`<input>`, `<output>`) | Structured separation | Cleaner extraction; reduced formatting drift |
| `<system>` style instructions in system role | Persistent rules | Survives turn-to-turn |
| Output prefill | Force structured start of response | Eliminates preambles like "Sure," |
| `<thinking>` blocks (extended thinking) | Multi-step reasoning tasks | Higher quality on hard tasks; cost more |
| Long-context document tags (`<document title="...">`) | RAG / long inputs | Better grounding and citation |
| "Stop sequences" planning | When response should end at a marker | Predictable termination |
| Roleplay using direct character description | Persona stability | Less drift mid-session |

## Constraints

**Must:**
- Apply each pattern only when its use case matches
- Tag the prompt with `model: claude-*` in frontmatter
- Document expected behavior change
- Do not remove patterns that work for cross-model portability without a flag

**Must Not:**
- Use OpenAI-isms ("respond in JSON only as a JSON object") instead of native XML tags
- Apply extended thinking to trivial tasks
- Stack three optimization patterns without measuring

## Instructions

1. Read the prompt; tag candidate sections for each pattern.
2. Apply patterns one at a time; measure on a small test set.
3. Keep changes that improve metric or readability.
4. Annotate frontmatter with model targeting.

## Output Format

```
CLAUDE PROMPT (modernized)

<system>
  <role>...</role>
  <rules>...</rules>
</system>

<task>
  <input>
    ...
  </input>
  <constraints>
    ...
  </constraints>
</task>

<output_schema>
  ...
</output_schema>

PATTERNS APPLIED
  - XML tags: yes — sections wrapped
  - Prefill: yes — start with "<answer>"
  - Extended thinking: yes — budget <n>
  - Stop sequence: yes — "</answer>"

EXPECTED BEHAVIOR CHANGES
  - <pattern>: <observed/predicted change>

FRONTMATTER ADDITION
  model: claude-sonnet-4-6 (or family)
  techniques: + XT-01 (XML tagging), PF-01 (prefill)
```

## Verification

- Each applied pattern matches a use case
- Frontmatter targets the model family
- Behavior change predicted or measured
- No conflicting OpenAI-isms left in
