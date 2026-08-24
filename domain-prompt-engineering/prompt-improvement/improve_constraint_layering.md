---
title: "Restack a Flat Rule List Into Layered Constraint Architecture"
category: prompt-engineering/prompt-improvement
description: "Take a flat list of `Must` / `Must Not` rules and reorganize into layered architecture (safety, scope, content, format, style) with explicit precedence."
techniques:
  - CM-02
  - ST-02
difficulty: advanced
tags:
  - constraint-architecture
  - layering
  - hierarchy
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/skill-development/promptcraft_constraint_architecture_design.md
---

## Objective

Convert a flat constraint list into a layered architecture so precedence is explicit, conflicts surface, and reviewers can reason about each layer independently.

## When to Use

- A prompt's constraint list has grown past 10 items and feels like soup
- A new contributor cannot tell which rule wins when two collide
- You want to review safety rules separately from style rules

## Layers (top to bottom precedence)

1. **Safety** — refusal triggers, never-do rules
2. **Legal / Compliance** — required disclosures, jurisdiction
3. **Scope** — what counts as in-task vs out-of-task
4. **Content** — required claims, banned topics
5. **Format** — schema, length, ordering
6. **Style** — voice, register, vocabulary

## Inputs

1. The flat constraint list
2. The intended task

## Constraints

**Must:**
- Place each rule in exactly one layer
- For rules that span layers, split into one rule per layer
- Mark rules that look like a layer but actually belong to a different one (common: "style" rules that are really safety)
- Add an explicit precedence note at the top of the constraints block

**Must Not:**
- Drop rules during restacking
- Invent new rules to fill empty layers
- Move safety rules below other layers

## Instructions

1. Tag each input rule with its true layer.
2. Split cross-layer rules.
3. Sort within each layer by severity.
4. Add precedence note: "Layer N overrides Layer N+1 in conflict."
5. Compare line count before/after; should be similar (splits cancel merges).

## Output Format

```
LAYERED CONSTRAINTS

[1. SAFETY]
  Must: ...
  Must Not: ...

[2. LEGAL/COMPLIANCE]
  ...

[3. SCOPE]
  ...

[4. CONTENT]
  ...

[5. FORMAT]
  ...

[6. STYLE]
  ...

PRECEDENCE: lower-numbered layer wins on conflict.

LAYER MIGRATIONS
  - "<rule>": flat → layer <n> (was tagged as <other>)

SPLITS
  - "<original>" → layer A: "<part1>" + layer B: "<part2>"

DROPPED (with reasons)
  - <rule>: <reason>
```

## Verification

- Every input rule is placed (or has a documented drop reason)
- Each layer's rules are checkable independently
- Precedence note appears at top
- A re-read of safety layer alone is sufficient to find safety rules
