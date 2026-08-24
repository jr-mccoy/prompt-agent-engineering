---
title: "Explain a Prompt Diff"
category: prompt-engineering/prompt-improvement
description: "Take a before/after prompt diff and produce a structured explanation of what changed, why each change matters, and what risks each introduces."
techniques:
  - QA-01
difficulty: intermediate
tags:
  - diff
  - explanation
  - changelog
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/library-maintenance/library_prompt_changelog_writer.md
---

## Objective

Given two prompt versions (before/after), classify each change, explain its likely behavioral impact, and list risks. Output is suitable for a code review or changelog entry.

## When to Use

- A prompt is being reviewed before merge
- Documenting changes for an audit trail
- Communicating prompt evolution to non-author stakeholders

## Inputs

1. Prompt version A (before)
2. Prompt version B (after)
3. Optional: the failing case that motivated the change

## Constraints

**Must:**
- Classify each change as: `clarification`, `tightening`, `loosening`, `refactor`, `feature-add`, `removal`
- Predict at least one behavioral impact per change
- List risks: what new failure modes the change could enable
- Identify any change that is silently behavioral (looks cosmetic but is not)

**Must Not:**
- Treat any non-trivial change as cosmetic without inspection
- Skip changes because they look minor
- Use vague impact terms ("better", "stronger")

## Instructions

1. Compute a line-level diff.
2. For each hunk, classify the change.
3. Predict impact on at least one input class.
4. Surface risks: which input classes might now fail that did not before.
5. Note hidden-behavioral changes (e.g., adding "concise" to a previously verbose-tolerant prompt).

## Output Format

```
DIFF SUMMARY
  total hunks: <n>
  classifications:
    clarification: <n>
    tightening: <n>
    loosening: <n>
    refactor: <n>
    feature-add: <n>
    removal: <n>

PER-HUNK ANALYSIS
  hunk 1:
    diff:
      - "<old>"
      + "<new>"
    classification: ...
    impact: <input class affected> → <expected behavior change>
    risk: <new failure mode possible>

HIDDEN BEHAVIORAL CHANGES
  - <hunk id>: looks like <X> but actually <Y>

CHANGELOG ENTRY (suggested)
  - <one-line summary>
  - <bullet for each material change>

REGRESSION CASES TO ADD
  - <case>: covers <hunk id>'s expected behavior
```

## Verification

- Every diff hunk has a classification and impact
- At least one risk listed per non-cosmetic hunk
- Hidden behavioral changes are flagged, not buried
- Suggested changelog entry is concise and accurate
