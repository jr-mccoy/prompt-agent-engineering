---
title: "Modernize a Legacy Prompt"
category: prompt-engineering/prompt-improvement
description: "Update a prompt written for older models or older conventions to current best practice without changing intent."
techniques:
  - CM-02
  - ST-02
difficulty: intermediate
tags:
  - legacy
  - modernization
  - migration
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/model-optimization/modelopt_within_family_migration.md
---

## Objective

Take a prompt written for an older model generation or earlier convention and produce a modernized version that uses current patterns (XML tags for Claude, JSON mode for OpenAI, structured output declarations, role separation) without altering task intent.

## When to Use

- A prompt was written 12+ months ago for a now-superseded model
- The prompt uses patterns ("Let's think step by step", over-long preambles) that newer models do not need
- A library of legacy prompts is being migrated forward

## Inputs

1. The legacy prompt
2. The legacy model (if known)
3. The current target model
4. Examples of the legacy prompt's outputs that were considered good

## Common Legacy Patterns to Modernize

| Legacy Pattern | Modernization |
|---|---|
| "Let's think step by step" trailer | Use extended-thinking budget or scratchpad block |
| Long polite preamble ("You are a very helpful assistant...") | Concise role sentence |
| Few-shot examples ad-hoc inline | Structured examples with input/output tags |
| Free-form output | Declared schema (JSON / XML tags) |
| Repeated emphasis ("VERY IMPORTANT", "CRITICAL") | One-time precedence rule |
| Token-padding instructions ("be detailed") | Explicit length / item-count cap |
| Prompts addressed to "the AI" | Direct imperative or role-defined voice |
| "Do not hallucinate" | Grounding contract or refusal-on-uncertainty |

## Constraints

**Must:**
- Modernize each legacy pattern found
- Preserve task intent and output schema
- If modernization changes output shape, surface it for review (do not auto-apply)
- Note which model generation each modernization targets

**Must Not:**
- Add features unrelated to the legacy pattern (scope creep)
- Drop instructions that were load-bearing even if they look ornamental
- Substitute hype words ("agentic", "autonomous") for clarity

## Instructions

1. Tag each legacy pattern in the prompt.
2. Apply the corresponding modernization.
3. Run mentally on the legacy good-output examples; flag any deviation.
4. Emit the modernized prompt plus a migration log.

## Output Format

```
LEGACY PATTERNS FOUND
  - pattern: <name> | location: line <n> | modernization: <what>

MODERNIZED PROMPT
<full prompt>

MIGRATION LOG
  - "<old text>" → "<new text>" | reason: ...

OUTPUT-SHAPE CHANGES (if any)
  - <change>: needs reviewer decision

DEFERRED (not modernized, with reason)
  - <pattern>: <why kept>
```

## Verification

- Every flagged legacy pattern was either modernized or deferred with reason
- Output schema unchanged unless flagged
- Legacy good-output examples are still consistent with the new prompt
- No new vague terms introduced
