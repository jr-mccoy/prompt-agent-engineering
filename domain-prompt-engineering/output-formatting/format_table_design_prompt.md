---
title: "Table Design Prompt"
category: prompt-engineering/output-formatting
description: "Choose columns, sort order, and alignment for a table; decide when a table beats a list."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - QA-01
  - DC-01
difficulty: beginner
tags:
  - table
  - formatting
  - structure
  - output_format
  - decision
updated: "2026-05-11"
related_prompts:
  - domain-prompt-engineering/output-formatting/format_markdown_contract.md
  - domain-prompt-engineering/output-formatting/format_length_budget_designer.md
  - domain-prompt-engineering/structured-output/structured_output_markdown_contract.md
---

## Objective

Design a table for a specific dataset or comparison task: choose columns, sort key, alignment, and cell content rules. Also produces a list-vs-table decision for the given content.

## When to Use

- You need to present comparative or relational data and are unsure whether a table or list is the right format.
- A model is generating tables with wrong columns, poor sort order, or overstuffed cells.
- You want a reusable table schema for a recurring output type (feature comparison, change log, rubric).
- **Not for:** chart or visualization design (different modality). Not for prose comparison without structured data.

## List vs. Table Decision Rule

Use a table when ALL of the following are true:
1. ≥ 2 entities are being compared.
2. ≥ 2 attributes are being compared per entity.
3. Readers will scan across rows (entity-to-entity) as well as down columns (attribute-to-attribute).
4. Each cell can be expressed in ≤ 20 words.

Use a list when ANY of the following is true:
- Single attribute per item.
- Cells require >20 words (use prose instead).
- Order matters more than comparison (use numbered list).
- Rendering environment does not support tables.

## Column Design Rules

| Rule | Rationale |
|------|-----------|
| First column = primary identifier | Enables row-level scanning |
| Columns = attributes, not entities | Entities are rows; mixing causes transposition confusion |
| Max 6 columns in prose context | 7+ columns require horizontal scroll in most renderers |
| Each column has exactly one data type | Don't mix free-text and Yes/No in one column |
| Column header ≤ 3 words | Long headers force cell width inconsistency |
| Empty cells require explicit value | Use "—", "N/A", or "unknown"; never leave blank |

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Data description | Yes | What entities and attributes are being compared |
| Rendering environment | Yes | Markdown / plain text / HTML / Notion / spreadsheet |
| Sort requirement | Optional | Primary sort key and direction |
| Row count estimate | Optional | Determines whether a table or paginated list is better |

## Constraints

**Must:**
- Apply the list-vs-table decision rule before designing the table.
- Produce a column schema (name, data type, alignment, max cell length).
- Specify exactly one primary sort key with direction (ascending/descending).
- If the rendering environment does not support tables, output the equivalent list schema instead.

**Must Not:**
- Create a table with >6 columns without flagging it as a wide-table exception requiring explicit approval.
- Leave any column with mixed data types.
- Use merged cells or nested tables.
- Include a row counter column (1, 2, 3…) unless row identity matters.

## Instructions

1. **Run list-vs-table decision.** Check all four conditions. If any "use a list" condition applies, switch to list schema design.

2. **Define column schema:**
   ```
   Column N: [Name]
   Data type: [text | number | boolean | enum:[A,B,C] | date]
   Alignment: [left | center | right]
   Max cell length: [N words]
   Sort eligible: [yes | no]
   ```

3. **Select sort key.** Primary: the column most readers will use first. Secondary: tiebreaker. Direction: ascending unless recency matters (use descending for dates, ranks).

4. **Write markdown skeleton** with header row and one example data row.

5. **Write cell content rules.** What to include and exclude per column.

## Output Format

```
## Table vs. List Decision
Condition check: [4 conditions with ✓/✗]
Decision: [TABLE | LIST — reason]

## Column Schema
| Column # | Name | Type | Alignment | Max cell | Sort eligible |
|----------|------|------|-----------|----------|--------------|
| 1 | ... | ... | left | N words | yes |
...

Primary sort: Column [N], [ascending/descending]
Secondary sort: Column [N], [ascending/descending] (optional)

## Markdown Skeleton
| [Col1] | [Col2] | [Col3] |
|--------|--------|--------|
| example value | example | example |

## Cell Content Rules
- [Col1]: [What to include; what to exclude; fallback for missing data]
- [Col2]: [...]
...
```

## Verification

- [ ] List-vs-table decision shows all four conditions checked, not just the conclusion.
- [ ] Column count ≤ 6, or a wide-table exception note is present.
- [ ] Every column has an explicit alignment and max cell length.
- [ ] Exactly one primary sort key is named with a direction.
- [ ] Markdown skeleton contains the correct number of separator pipes (must equal header column count).
