---
title: "Build a Prompt Using the Constraint-First Pattern"
category: prompt-engineering/prompt-creation
description: "Author a prompt by enumerating Must / Must Not rules first, then deriving role, task, and output format from the constraint set."
techniques:
  - CM-02
  - ST-02
difficulty: intermediate
tags:
  - constraint-first
  - rules
  - guardrails
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/goal-orientation/goalorientation_constraint_architecture_workshop.md
  - domain-prompt-engineering/instruction-design/instruction_must_should_may_classifier.md
---

## Objective

When the failure modes are clearer than the success criteria, build the prompt around the constraint set first. Constraints drive the rest of the structure.

## When to Use

- The task has been failing in known specific ways
- A reviewer has rejected past outputs with concrete reasons
- Compliance, safety, or formatting requirements dominate

## Inputs

1. List of past failures with one-line cause for each
2. List of non-negotiable requirements (legal, brand, format, length)
3. List of desirable-but-flexible properties

## Constraints

**Must:**
- Convert each past failure into a `Must Not` rule with a falsifiable test
- Convert each non-negotiable into a `Must` rule with a falsifiable test
- Mark each desirable property as `Should` (not Must)
- Sort rules by severity (safety > correctness > format > style)

**Must Not:**
- Write rules that cannot be checked from the output alone
- Mix unrelated concerns into a single rule
- Add rules that no past failure or requirement justifies

## Instructions

1. Enumerate the constraint set first; everything else waits.
2. Apply the must / should / may distinction (RFC-2119 style).
3. Assign a check method to each rule: regex / structural / pairwise / human.
4. Choose the smallest role consistent with the constraint set.
5. Choose the output format that makes constraints easiest to verify.

## Output Format

```
CONSTRAINTS (sorted by severity)
  Must:
    - [check: <regex|structural|pairwise|human>] <rule>
  Must Not:
    - [check: ...] <rule>
  Should:
    - [check: ...] <rule>

ROLE
<smallest role consistent with constraints>

TASK
<imperative>

OUTPUT FORMAT
<format chosen to make constraints checkable>

VERIFICATION
<which rules the model self-checks before returning>
```

## Verification

- Every past failure maps to at least one `Must Not`
- Every non-negotiable maps to at least one `Must`
- Every rule has a check method named
- No `Should` rule was misclassified from a real `Must`
