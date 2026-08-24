---
title: "Probe a New Model's Capabilities"
category: prompt-engineering/model-optimization
description: "Run a structured capability probe against a new model: instruction following, format adherence, tool use, refusal style, reasoning, and length control."
techniques:
  - QA-01
difficulty: intermediate
tags:
  - probe
  - capability-discovery
  - new-model
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/model-optimization/modelopt_quirks_catalog_builder.md
---

## Objective

Profile a new model along a fixed set of capability axes so a team knows what it does well, where it differs from the predecessor, and what prompts may need adjustment.

## When to Use

- A new model is released and you need to decide whether/how to use it
- A vendor swap is being evaluated
- A team builds a per-model dossier as part of governance

## Capability Axes

1. **Instruction following** — does it obey explicit constraints (length, format, refusal triggers)?
2. **Schema adherence** — does it produce valid JSON / XML reliably?
3. **Tool use / function calling** — does it call the right tool with right args?
4. **Refusal style** — what does it refuse, how, and how often?
5. **Reasoning depth** — does it solve multi-hop problems without explicit CoT scaffolding?
6. **Length control** — does it respect hard caps?
7. **Multilingual** — quality across target languages?
8. **Long-context** — recall and grounding at large input sizes?
9. **Determinism** — variance at temperature 0?
10. **Latency / cost** — wall-clock and token cost on standard prompts?

## Constraints

**Must:**
- Run the probe set per axis
- Use identical probe prompts across models compared
- Record both metrics and qualitative notes
- Highlight axes where the model differs sharply from a chosen baseline

**Must Not:**
- Probe with prompts the model has likely seen during training
- Conflate axes (e.g., calling a length-control failure a "reasoning" failure)
- Skip axes because they "shouldn't matter for our use case" — they may later

## Instructions

1. Use the standard probe set or build one (5–10 prompts per axis).
2. Run on baseline model and new model.
3. Score per axis.
4. Aggregate into capability dossier.
5. Identify prompts in your library most affected.

## Output Format

```
MODEL: <name>
BASELINE: <name>

PER-AXIS RESULTS
  axis | baseline metric | new model metric | delta | notes
  instruction_following | ... | ... | ... | ...
  schema_adherence | ... | ... | ... | ...
  ...

QUALITATIVE NOTES
  - <axis>: observed pattern, surprises, failure mode

DOSSIER ENTRY
  strengths: [...]
  weaknesses: [...]
  refusal style: ...
  recommended for: [task classes]
  not recommended for: [task classes]

PROMPTS LIKELY AFFECTED
  - <prompt path>: axis impacted, predicted behavior change
```

## Verification

- Probe set used for both models
- All 10 axes scored
- Dossier produced with strengths and weaknesses
- Affected prompt list is concrete, not abstract
