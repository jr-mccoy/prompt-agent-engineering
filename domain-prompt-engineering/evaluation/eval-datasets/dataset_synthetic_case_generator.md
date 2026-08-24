---
title: "Synthetic Case Generator"
category: prompt-engineering/evaluation/eval-datasets
description: "Generate synthetic eval cases with axis-based coverage guarantees and quality validation, to supplement or replace real log data when coverage gaps exist."
techniques:
  - ST-02
  - ST-03
  - CM-02
  - DT-01
  - QA-01
difficulty: intermediate
tags:
  - synthetic_data
  - dataset_generation
  - coverage_design
  - axis_coverage
  - eval_datasets
updated: "2026-05-11"
related_prompts:
  - domain-prompt-engineering/evaluation/eval-datasets/dataset_case_inventory_from_logs.md
  - domain-prompt-engineering/evaluation/eval-datasets/dataset_difficulty_stratifier.md
  - domain-prompt-engineering/evaluation/correctness_eval_design_prompt.md
---

## Objective

Generate synthetic eval cases for a specified task using an axis-based coverage design, ensuring that the case set spans the input space systematically rather than clustering in the mode. Output includes a coverage grid, generation instructions per axis, quality validation criteria, and the generated cases.

## When to Use

- When production logs are unavailable, insufficient, or privacy-restricted
- When coverage gaps exist in a real log-derived dataset
- When you need cases at specific difficulty levels or input combinations not present in logs
- When building an eval set before the system is deployed

## Inputs

| Field | Required | Description |
|-------|----------|-------------|
| `task_description` | Yes | What the prompt does and what inputs it accepts |
| `input_schema` | Yes | Fields, types, ranges, and constraints |
| `coverage_axes` | Yes | 2–5 dimensions that define the input space (e.g., length, formality, domain, ambiguity) |
| `target_count` | Yes | Total cases to generate |
| `quality_model` | Optional | Model to use for quality validation of generated cases |

## Constraints

**Must:**
- Define ≥2 coverage axes from the task spec
- Generate cases that cover all combinations of axis levels (or a sampled subset for large grids)
- State generation instructions per axis level — not "generate a variety"
- Run a quality validation pass: check each case for realism and task-relevance
- Produce a coverage matrix showing case counts per axis combination

**Must Not:**
- Generate >30% of cases at the same axis level combination (mode collapse)
- Include cases with inputs that violate the `input_schema`
- Skip quality validation — at minimum run a self-consistency check

## Instructions

**Step 1 — Axis definition**

For each coverage axis, define levels and generation instructions:

```
Axis: input_length
Levels:
  short: 1–3 sentences. Generate by: state the core request in minimal words.
  medium: 4–8 sentences. Generate by: add context and one constraint.
  long: >8 sentences. Generate by: include background, constraints, and examples.

Axis: ambiguity
Levels:
  clear: Request has one valid interpretation. Generate by: use specific nouns, named outputs.
  ambiguous: Request has ≥2 valid interpretations. Generate by: omit the object or goal qualifier.

[Repeat for each axis]
```

**Step 2 — Coverage grid**

| Axis 1 | Axis 2 | Axis 3 | Target count | Actual count |
|--------|--------|--------|--------------|--------------|
| short | clear | — | N | |
| short | ambiguous | — | N | |
| medium | clear | — | N | |
| medium | ambiguous | — | N | |
| long | clear | — | N | |
| long | ambiguous | — | N | |
| **Total** | | | N | |

If the grid is too large (>target_count), sample systematically: prioritize combinations that are underrepresented in real logs or have high-stakes behavior.

**Step 3 — Case generation protocol**

For each grid cell:
1. Select axis levels for this cell
2. Apply the generation instruction for each axis simultaneously
3. Verify the generated input against `input_schema` (all required fields present, types correct)
4. Assign a behavior label from the task taxonomy
5. Produce a `generation_seed`: brief natural-language description of what was generated

Case schema:
```json
{
  "id": "SYN-001",
  "axis_profile": {"input_length": "short", "ambiguity": "clear"},
  "input": "<generated input>",
  "generation_seed": "<1-sentence description of generation intent>",
  "behavior_label": "<label from taxonomy>",
  "is_synthetic": true,
  "quality_check": {
    "schema_valid": true,
    "realistic": true,
    "task_relevant": true,
    "quality_issues": []
  }
}
```

**Step 4 — Quality validation**

Run two validation passes:

*Structural pass (automated):*
- [ ] Required fields present
- [ ] Field types match `input_schema`
- [ ] Input length within expected range for axis level
- [ ] No repeated inputs (exact match)

*Realism pass (LLM or human):*
- [ ] Input reads as plausible real user input (not obviously machine-generated)
- [ ] Input is coherent (no contradictory constraints)
- [ ] Input is task-relevant (would a real user send this?)

Reject and regenerate any case failing realism checks.

**Step 5 — Mode collapse check**

After generating the full set, compute:
- Largest axis combination by count / total count → must be < 30%
- Embedding clustering: if ≥40% of cases fall in the same cluster (cosine ≥0.85), flag as mode collapse

**Step 6 — Coverage report**

| Axis combination | Target | Actual | Status |
|-----------------|--------|--------|--------|
| short × clear | N | N | ✓ |
| long × ambiguous | N | N | ✓ |
| … | | | |

Flag any cell with 0 actual cases and explain why (constraint conflict, generation failure).

## Output Format

1. **Axis definitions** — each axis with levels and generation instructions
2. **Coverage grid** — target and actual counts per combination
3. **Case array** — JSON array following schema
4. **Quality validation summary** — pass/fail counts, rejection reasons
5. **Mode collapse check** — largest combination %, embedding cluster result

## Verification

- [ ] ≥2 coverage axes defined with explicit generation instructions per level
- [ ] Coverage grid populated (no empty target cells without explanation)
- [ ] Every case passed both structural and realism validation passes
- [ ] No axis combination exceeds 30% of total cases
- [ ] Mode collapse check completed and documented
