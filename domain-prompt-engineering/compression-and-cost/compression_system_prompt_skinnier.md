---
title: "Make the System Prompt Skinnier"
category: prompt-engineering/compression-and-cost
description: "Move rules from the system prompt into just-in-time instructions, examples, or developer prompts when they are not universally needed."
techniques:
  - CM-01
  - ST-02
difficulty: advanced
tags:
  - system-prompt
  - jit
  - skinny
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/system-prompts/system_minimal_viable_system_prompt.md
  - domain-prompt-engineering/prompt-creation/creation_progressive_disclosure_prompt.md
---

## Objective

Identify rules in the system prompt that only apply to a subset of inputs and move them to JIT instructions or developer prompts that load conditionally, leaving the system prompt with only universal rules.

## When to Use

- System prompt is paying tokens on every call for rules that fire rarely
- Some rules are deployment-specific (developer prompt territory)
- Caching benefits from a smaller stable system prefix

## Inputs

1. System prompt
2. List of rules with frequency-of-firing estimate
3. Available JIT delivery (conditional appender, retrieval, dev prompt)

## Constraints

**Must:**
- Keep universal rules (safety, refusal, identity) in system prompt
- For rules firing in <50% of calls, propose JIT delivery
- For rules deployment-specific, propose move to developer prompt
- Document the trigger for each JIT-loaded rule

**Must Not:**
- Move safety rules to JIT (unreliable; safety is universal)
- Trigger rules vaguely; triggers must be checks on input
- Lose any rule in the move

## Instructions

1. Tag each rule: universal / conditional / per-deployment.
2. Move conditional rules to JIT with explicit trigger.
3. Move per-deployment rules to developer prompt.
4. Document the trigger logic.
5. Re-run regression set.

## Output Format

```
RULE TAGGING
  - <rule>: universal | conditional (trigger: <pattern>) | per-deployment

NEW SYSTEM PROMPT (skinny)
<universal rules only>

JIT INSTRUCTION SETS
  set <name>:
    trigger: <input check>
    block:
      <rules>

DEVELOPER PROMPT
<per-deployment rules>

TRIGGER LOGIC
  - if <pattern>: append set <name>
  - if <pattern>: append set <name>
  - else: no append

TOKEN ANALYSIS
  system before: <n>
  system after: <n>
  per-call cost (avg): <n> (universal + occasional JIT)

REGRESSION RESULTS
  - happy cases: pass
  - cases requiring JIT: pass (trigger fired)
  - cases not requiring JIT: pass (no extra rules)
```

## Verification

- Safety rules remain universal
- Triggers are falsifiable
- Per-call average cost decreased
- Regression passes across cases that need and don't need JIT
