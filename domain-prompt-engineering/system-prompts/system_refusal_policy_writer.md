---
title: "Author a Refusal Policy"
category: prompt-engineering/system-prompts
description: "Specify the categories the assistant refuses, the tone of refusal, and the alternative paths offered, as concrete prompt rules."
techniques:
  - CM-02
difficulty: intermediate
tags:
  - refusal
  - policy
  - system-prompt
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/system-prompts/system_user_input_contract.md
---

## Objective

Define what the assistant refuses, in what tone, with what alternative path, and how it responds to repeated attempts. Avoid both excessive refusal and silent compliance with disallowed requests.

## When to Use

- The deployment has policy categories that must be honored
- Refusal style is part of brand or trust posture
- Users repeatedly probe edges and the assistant is inconsistent

## Inputs

1. Refusal categories (from policy, legal, scope)
2. Per-category: must-refuse triggers, allowed adjacent help, exit text
3. Tone target: firm, neutral, brief, no lecturing
4. Repeated-attempt handling

## Constraints

**Must:**
- Define exact phrasing for each category's refusal
- Offer adjacent help when possible (not just "I can't")
- Avoid moralizing; stay short
- Define what to do on repeated attempts (do not escalate language; do not engage)

**Must Not:**
- Use refusal language as a default for any uncertain request (over-refusal)
- Wax philosophical or apologetic
- Promise help that isn't actually delivered after refusing

## Instructions

1. List categories.
2. Per category, write the trigger condition, refusal phrasing, and adjacent help (if any).
3. Define tone rules for all refusals.
4. Define repeated-attempt protocol.

## Output Format

```
REFUSAL POLICY (system-prompt block)

CATEGORY: <name>
  trigger: <input pattern>
  refusal:
    "I can't help with <X>."
  adjacent help (if any):
    "I can help with <Y> if useful."
  no engagement: do not explain rationale beyond <one sentence>.

CATEGORY: <name>
  ...

TONE RULES
  - max 2 sentences
  - no apologies past one "sorry" if at all
  - no moralizing
  - no second-person accusations

REPEATED ATTEMPTS
  - do not change refusal phrasing
  - do not escalate language
  - after <n> consecutive attempts on same category, stop offering adjacent help
```

## Verification

- Every category has a trigger, refusal, and (where applicable) adjacent help
- Tone rules cap length and warmth
- Repeated-attempts protocol prevents the model lecturing
- Adjacent-help offers are real, not aspirational
