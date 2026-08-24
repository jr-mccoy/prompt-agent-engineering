---
title: "Design Negative Few-Shot Examples"
category: prompt-engineering/few-shot-examples
description: "Create examples that show what the model should not do, formatted so the model does not imitate them by accident."
techniques:
  - PR-03
  - CM-02
difficulty: advanced
tags:
  - negative-examples
  - anti-pattern
  - boundary
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/prompt-creation/creation_negative_prompt_designer.md
---

## Objective

Build examples that demonstrate the failure mode the model should avoid, paired with a corrected version, formatted in a way that prevents the model from interpreting the bad example as desirable.

## When to Use

- Positive examples alone are not eliminating a known failure pattern
- The boundary between accepted and rejected outputs is subtle
- A small number of recurring rejections justifies dedicated anti-examples

## Inputs

1. The failure pattern to discourage
2. 2–3 real rejected outputs (or synthesized ones marked synthetic)
3. The corrected version of each

## Constraints

**Must:**
- Wrap the bad output in tags or markers that make it visually and structurally distinct (`<rejected>`, `BAD:`)
- Pair every bad example with a corrected version (`<corrected>`, `GOOD:`)
- Include a one-line reason explaining why bad is bad
- Ensure surface differences are not the lesson; the rule is the lesson

**Must Not:**
- Place the bad example without a corrected pair
- Make the bad example more vivid or memorable than the corrected one
- Use negative examples for failure modes that already have explicit `Must Not` rules (redundant)

## Instructions

1. Pick 2–3 failure patterns worth dedicated examples.
2. For each, create or curate one bad output and its correction.
3. Tag clearly. Add the one-line reason between bad and corrected.
4. Verify visual hierarchy: corrected version should be more salient.
5. Add a note in the prompt: "Examples below labeled `<rejected>` show what NOT to produce."

## Output Format

```
NEGATIVE EXAMPLE BLOCK

<example id="1">
  Input: ...
  <rejected>
    <bad output>
  </rejected>
  Reason: <one line>
  <corrected>
    <good output>
  </corrected>
</example>

<example id="2">
  ...
</example>

PROMPT INTEGRATION NOTE
  "Treat content inside <rejected> as anti-patterns. Match the style and structure of <corrected> only."
```

## Verification

- Every `<rejected>` has a `<corrected>`
- Reason is one line and operational
- Visual hierarchy makes corrected more prominent
- No negative example duplicates an existing `Must Not` rule
