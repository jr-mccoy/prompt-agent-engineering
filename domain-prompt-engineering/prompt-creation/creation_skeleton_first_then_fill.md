---
title: "Skeleton-First Prompt Authoring"
category: prompt-engineering/prompt-creation
description: "Lock the section structure of a prompt before writing content, then fill each slot with content derived from inputs."
techniques:
  - ST-02
difficulty: beginner
tags:
  - skeleton
  - structure-first
  - authoring
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/prompt-creation/creation_task_prompt_from_blank.md
---

## Objective

Author a prompt by first committing to a section structure, then filling each section. Prevents the common failure mode of long unstructured prose that omits load-bearing elements.

## When to Use

- An author is new to prompt writing
- A team needs prompts to share structure for searchability and review
- You want to make missing-section gaps visible before content drift sets in

## Inputs

1. The skeleton (or a default skeleton)
2. The task to be prompted
3. Available inputs and constraints

## Constraints

**Must:**
- Commit to the skeleton before writing any section's content
- Mark missing inputs as `[GAP: needed for <section>]` rather than inventing
- Fill sections in order; do not skip
- Re-read inputs before each section to avoid hallucinating from earlier sections

**Must Not:**
- Cut sections because content is unknown — leave a `[GAP:]` and continue
- Combine unrelated content into one section
- Add sections not in the skeleton (propose them as an amendment instead)

## Instructions

1. Print the skeleton.
2. For each section, identify the inputs that feed it.
3. Fill from inputs only; mark gaps explicitly.
4. After all sections are drafted, return to gaps and either fill from new info or propose questions.

## Default Skeleton

```
1. Role
2. Objective
3. When to Use
4. Inputs / Context
5. Constraints (Must / Must Not)
6. Instructions
7. Output Format
8. Verification
9. Examples (optional)
```

## Output Format

```
DRAFT
1. Role: <text or [GAP: needed inputs]>
2. Objective: ...
...

GAPS
  - section <n>: <what is missing> | <suggested question>

PROPOSED SKELETON AMENDMENTS (if any)
  - add section <name> because ...
```

## Verification

- Every skeleton section appears in the draft (filled or gap)
- No section was deleted
- Every gap names what is missing in operational terms
- The order matches the skeleton; no reordering without explicit amendment
