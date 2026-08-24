---
title: "Premise-Check Pattern"
category: prompt-engineering/reasoning-strategies
description: "Add a step that verifies input premises before reasoning, refusing or asking when the premise is false or unverifiable."
techniques:
  - QA-01
difficulty: intermediate
tags:
  - premise-check
  - assumptions
  - refusal
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/reasoning-strategies/reasoning_self_check_pattern.md
  - domain-prompt-engineering/hallucination-control/hallucination_grounding_only_pattern.md
---

## Objective

Insert a premise-check step at the start of a prompt: identify the assumptions the input carries, verify each, and refuse / ask / proceed-with-caveat as appropriate before reasoning.

## When to Use

- Inputs frequently contain false premises that derail outputs
- "Why did Y happen?" questions when Y did not happen
- Tasks where the model must not validate a faulty assumption by answering

## Inputs

1. The base prompt
2. Common false-premise patterns observed
3. Tolerance: refuse, ask, or proceed with caveat

## Constraints

**Must:**
- Surface premises as an explicit list before reasoning
- For each premise, mark `verified | unverified | false`
- If any load-bearing premise is false, refuse to answer the original question and surface the falsehood
- Proceed only when all load-bearing premises check out, or proceed with caveats when configured

**Must Not:**
- Answer a question that requires accepting a false premise (e.g., "Why did the company go bankrupt?" when the company did not go bankrupt)
- Hide premise issues in a footnote at the end
- Auto-correct premises silently

## Instructions

1. Extract premises from input.
2. Verify each against context (or known facts within model's confident range).
3. If false-premise found:
   - mode = refuse: do not answer; explain falsehood
   - mode = ask: state the falsehood and ask for confirmation
   - mode = caveated: answer hypothetically, marked clearly
4. If verified, proceed.

## Output Format

```
PREMISES EXTRACTED
  - <premise>: status (verified | unverified | false)

LOAD-BEARING ASSESSMENT
  - <premise>: load-bearing? yes/no

ACTION
  - mode: refuse | ask | caveated | proceed
  - response: <text>

PROCEED-WITH-CAVEAT (if applicable)
  - hypothetical answer: ...
  - caveat: <named falsehood>

REFUSAL (if applicable)
  - the premise that <X> is false: <evidence>
  - I cannot answer the question as posed.
  - I can answer this related question: <reformulation>
```

## Verification

- Every premise is listed with status
- False premises trigger refuse/ask/caveated, not silent answer
- Load-bearing tag separates ornamental premises from critical ones
- Reformulation offered when refusing
