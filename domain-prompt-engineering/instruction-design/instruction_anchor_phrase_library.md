---
title: "Instruction Anchor Phrase Library Builder"
category: prompt-engineering/instruction-design
description: "Build a per-model-family library of empirically reliable anchor phrases (the wordings that change behavior most reliably for that family)."
techniques:
  - ST-02
  - QA-01
  - PR-01
  - PR-03
  - DC-01
difficulty: advanced
tags:
  - anchor_phrases
  - model_family
  - empirical_library
  - reusable_components
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/instruction-design/instruction_imperative_vs_declarative.md
  - domain-prompt-engineering/instruction-design/instruction_must_should_may_classifier.md
  - domain-prompt-engineering/model-optimization/
---

## Objective

Produce a versioned table of anchor phrases for one model family, each entry showing the behavior it controls, the measured effect size, and the failure mode it replaces. Output is a reusable artifact that other prompts cite by ID.

## When to Use

- Standing up a new prompt-engineering practice for one model family.
- Migration between model versions where prior anchor phrases stopped working.
- Onboarding a team that keeps re-discovering the same phrasings.

## Inputs

- `MODEL_FAMILY`: e.g., `claude-opus-4-7`, `gpt-5`, `gemini-3-pro`.
- `EXISTING_PHRASES_OPTIONAL`: candidate phrases gathered from team prompts.
- `EVAL_BUDGET`: total runs available across phrases (default 200).

## Constraints

### Must
- Every entry has fields: `id`, `phrase` (verbatim), `controls` (one behavior), `replaces_failure_mode`, `effect_size`, `n_runs`, `paired_baseline_phrase`, `version`, `tested_on_model`.
- `effect_size` is a single percentage point delta on a defined metric (e.g., `+38pp adherence to JSON schema`).
- Each phrase is paired against a baseline phrase tested in the same prompt slot, same temperature, same N.
- Minimum 10 runs per phrase per model.
- Phrases are dedicated to ONE behavior; multi-purpose phrases get split.

### Must Not
- Include phrases without a paired baseline.
- Include phrases sourced from blog posts without local replication.
- Mix model families in one library file.

## Instructions

1. Define one behavior per phrase in falsifiable terms (e.g., "Output begins with `{` and parses as JSON").
2. For each candidate phrase, write its paired baseline ("Return JSON" vs "Return JSON. Begin your reply with `{`.").
3. Run N=10+ generations for each, measure the behavior, record the delta.
4. Discard any phrase with `effect_size < 10pp` or with overlapping CI; keep tied phrases only if cheaper.
5. Tag each phrase with `version` (the date of measurement) and `tested_on_model` (exact model ID).
6. Store as a single table per family.

## Output Format

```
MODEL_FAMILY: <id>
CALIBRATED_ON: <YYYY-MM-DD>

| id   | phrase                                | controls                       | replaces_failure_mode      | effect_size | n_runs | paired_baseline_phrase            | version    | tested_on_model     |
|------|----------------------------------------|--------------------------------|----------------------------|-------------|--------|------------------------------------|------------|---------------------|
| A001 | "Begin your reply with `{`."           | JSON-first output              | preamble_before_json       | +38pp       | 30     | "Return JSON."                     | 2026-05-10 | claude-opus-4-7     |
| A002 | "Stop after the closing `}`."          | JSON-only output (no trailer)  | trailing_explanation       | +52pp       | 30     | (no instruction)                   | 2026-05-10 | claude-opus-4-7     |
| A003 | "If unsure, output `{\"unknown\":true}`." | calibrated unknowns         | confident_hallucination    | +21pp       | 40     | "Be careful."                      | 2026-05-10 | claude-opus-4-7     |
```

After the table:
```
RETIRED
| id | reason |
|----|--------|
| A009 | effect_size 4pp on opus-4-7; kept as historical only |
```

## Verification

- Every row has a paired baseline and N ≥ 10? (yes/no)
- Effect size measurement metric is defined for the row's `controls` field? (yes/no)
- Library is scoped to a single `MODEL_FAMILY`? (yes/no)
- Recompute one row's effect size on a fresh sample of 10; confirm within ±10pp.

## Examples

Anchor IDs are referenced by other prompts:
> "Apply anchor A001 + A002 to enforce JSON-only output."

This decouples behavior intent from specific wording so library updates propagate.
