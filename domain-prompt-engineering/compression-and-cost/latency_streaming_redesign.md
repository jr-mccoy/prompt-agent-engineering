---
title: "Redesign a Prompt for Streaming Latency"
category: prompt-engineering/compression-and-cost
description: "Reorder the output schema so the most useful content streams first, reducing time-to-useful-token without reducing quality."
techniques:
  - ST-03
  - CM-01
difficulty: intermediate
tags:
  - latency
  - streaming
  - first-token
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/structured-output/structured_field_ordering_for_speed.md
---

## Objective

Reorganize a prompt's output schema so the highest-value content arrives first in the stream, allowing UIs and downstream callers to act before the full response completes.

## When to Use

- User-facing surfaces with streaming
- Long responses where the first sentence is what users actually need
- Pipelines where downstream steps can begin once a key field arrives

## Inputs

1. Current output schema
2. Which fields are most useful first (per consumer)
3. Whether ordering change is acceptable to consumers (some require fixed order)

## Constraints

**Must:**
- Place the highest-utility field first
- Place fields that require global computation (totals, summaries) where their inputs have already streamed
- Preserve required schema if consumer needs fixed order — instead optimize internally

**Must Not:**
- Reorder if it breaks a parser
- Move dependent fields before their dependencies
- Put preamble or rationale ahead of the answer when streaming to a user

## Instructions

1. Identify highest-utility field per consumer.
2. Check ordering constraints from parsers.
3. Reorder where allowed; if not, optimize length of pre-answer content.
4. Add anti-preamble rule ("no 'Sure' or 'Here is' before the answer").
5. Measure time-to-first-useful-token before and after.

## Output Format

```
CONSUMER MAP
  consumer | highest-utility field | order-flexible? 

REORDERED SCHEMA
  field 1 (was field <m>): <new position>
  ...

PROMPT ADDITION
  Output the fields below in the order shown. Do not prefix with greetings or summaries. The first token must be the first field's content.

PARSER COMPATIBILITY
  - <consumer>: compatible | needs adapter

LATENCY METRICS
  time-to-first-useful-token before: <ms>
  time-to-first-useful-token after: <ms>
  total response time: ~unchanged
```

## Verification

- Highest-utility field is first for each flexible consumer
- Anti-preamble rule present
- Parser compatibility checked
- Latency improvement measured, not assumed
