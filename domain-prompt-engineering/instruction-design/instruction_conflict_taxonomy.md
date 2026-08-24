---
title: "Instruction Conflict Taxonomy"
category: prompt-engineering/instruction-design
description: "Classify any pair of conflicting instructions in a prompt into one of four named conflict types and emit a resolution path."
techniques:
  - ST-02
  - ST-03
  - CM-02
  - QA-01
  - DC-01
difficulty: intermediate
tags:
  - conflict_classification
  - instruction_design
  - prompt_audit
  - taxonomy
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/instruction-design/instruction_hierarchy_designer.md
  - domain-prompt-engineering/instruction-design/instruction_precedence_test_set.md
  - domain-prompt-engineering/debugging/debug_failure_mode_taxonomy.md
---

## Objective

Take a prompt as input and emit a complete classification of every internal instruction conflict using a fixed four-class taxonomy, plus the minimal edit that resolves each conflict.

## When to Use

- Prompt has grown by accretion and now produces inconsistent outputs.
- A model violates one rule when it follows another (and you cannot tell which is "right").
- Before publishing a system prompt to production.

## Inputs

- `PROMPT_TEXT`: the full prompt (system + developer combined).
- `RULE_IDS_OPTIONAL`: pre-numbered rule IDs if available.

## Conflict Taxonomy (fixed)

| Class | Definition | Example |
|-------|------------|---------|
| `DIRECT` | Two rules require literally opposite outputs. | "Always include a citation" vs "Never include URLs". |
| `SCOPE_OVERLAP` | Rules cover overlapping cases with different actions, no precedence given. | "If user asks medical question, refuse" vs "If user is a clinician, answer". |
| `PRIORITY_TIED` | Both rules apply, both list themselves as "highest priority". | "Brevity above all" + "Cite every claim". |
| `VACUOUS` | Rule cannot be falsified or measured; conflicts with any concrete rule. | "Be helpful" vs "Refuse harmful requests". |

## Constraints

### Must
- Use only the four class labels above; do not invent new ones.
- Every conflict row must cite the two rule IDs (or quote the two rule strings if no IDs).
- Provide a `resolution_edit` that is a single concrete textual change (delete, reword, add precedence) — not advice.
- If zero conflicts found, output `CONFLICTS: 0` and stop.

### Must Not
- Output prose paragraphs.
- Group multiple conflicts under one row.
- Use the word "consider" anywhere.

## Instructions

1. Number every rule in `PROMPT_TEXT` if not already numbered (`R1..Rn`).
2. Build the n×n conflict matrix; for each pair, run the four-class test in order: DIRECT → SCOPE_OVERLAP → PRIORITY_TIED → VACUOUS. First match wins.
3. For each detected conflict, write one row of the output table.
4. For VACUOUS conflicts, the resolution edit must rewrite the vague rule into a falsifiable form OR delete it.
5. Sort output rows by class (DIRECT first, VACUOUS last), then by lowest rule ID.

## Output Format

```
CONFLICTS: <n>

| # | Class           | Rule A | Rule B | Why it conflicts (≤25 words)         | resolution_edit (single change) |
|---|-----------------|--------|--------|--------------------------------------|---------------------------------|
| 1 | DIRECT          | R3     | R7     | ...                                  | Delete R7.                      |
| 2 | SCOPE_OVERLAP   | R5     | R12    | ...                                  | Add precedence: R12 wins when user role = clinician. |
```

After the table, list every rule ID that appears in zero conflicts under `CLEAN_RULES: [R1, R4, ...]`.

## Verification

- Conflict count matches table row count? (yes/no)
- Every row has exactly one class label from the fixed set? (yes/no)
- Every `resolution_edit` is a concrete edit verb (Delete | Replace | Add | Reorder), not a suggestion? (yes/no)
- For one DIRECT conflict, hand-construct the input that triggers it and confirm output ambiguity.

## Examples (output snippet)

```
| 1 | DIRECT        | R3 | R7  | R3 requires URL; R7 forbids URLs. | Replace R7: "Cite by title only, no URLs." |
| 2 | PRIORITY_TIED | R1 | R9  | Both claim highest priority.       | Add precedence: R1 > R9.                    |
| 3 | VACUOUS       | R2 | R5  | R2 unfalsifiable ("be helpful").    | Delete R2.                                  |
```
