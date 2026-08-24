---
title: "Streamable Table Row Emitter"
category: prompt-engineering/structured-output
description: "Generate one validated row at a time so consumers can stream, paginate, and reject rows without buffering the whole table."
techniques:
  - ST-02
  - ST-03
  - OC-03
  - QA-01
difficulty: intermediate
tags:
  - table
  - streaming
  - row_validation
  - structured_output
  - pagination
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/structured-output/structured_field_ordering_for_speed.md
  - domain-prompt-engineering/structured-output/structured_json_repair_pattern.md
---

## Objective

Produce a per-row emission protocol so a model streams a long table as independently parseable, independently validatable rows — enabling early consumer cancellation and per-row retry.

## When to Use

- Output table can exceed 200 rows or 8K tokens.
- Consumer wants to render or persist rows as they arrive.
- One bad row should not invalidate the whole batch.

## Inputs

```
COLUMNS: <ordered list with name and type>
ROW_DELIMITER: <newline | NDJSON | <row>...</row>>
MAX_ROWS: <number>
SORT_KEY: <column name or "stable_input_order">
DUP_POLICY: <skip | error | first_wins>
```

## Constraints

### Must
- Emit one row per delimiter unit. No row spans delimiter boundaries.
- Emit a header line first, then rows, then a terminator: `__END__ rows=<count>`.
- Each row carries a monotonic `row_index` starting at 1.
- Each row is self-validating: types match COLUMNS, no embedded delimiters in values (escape per format), no trailing commas.
- On a row that cannot be produced, emit `{"row_index": <n>, "__row_error": "<reason>"}` instead of skipping silently.

### Must Not
- Buffer multiple rows then emit them as a JSON array (defeats streaming).
- Reorder rows after emission.
- Exceed MAX_ROWS; if more rows are needed, emit `__TRUNCATED__ remaining=<estimate>` before `__END__`.

## Instructions

1. Pick format:
   - NDJSON when columns are typed and consumer is JSON-aware.
   - CSV with explicit quote rules when consumer is a database/spreadsheet.
   - `<row>...</row>` XML when columns include long prose.
2. Emit header per format:
   - NDJSON: `{"__header": {"columns": [...], "version": 1}}`
   - CSV: `col1,col2,...`
   - XML: `<table version="1"><columns>col1,col2</columns>`
3. Emit rows. For each, run a 4-check before emit: types ok, delimiter-safe, dup against SORT_KEY (per DUP_POLICY), within MAX_ROWS.
4. On error in step 3, emit `__row_error` and continue.
5. Emit terminator with row count.

## Output Format

```
header_line: <verbatim>
row_template: <verbatim with {column placeholders}>
error_template: <__row_error envelope>
terminator: __END__ rows=<count>
truncation_signal: __TRUNCATED__ remaining=<n>

consumer_pseudocode:
- read header → validate columns
- read until terminator or truncation
- per row: validate types, check row_index monotonic
- on __row_error: log and continue
```

## Verification

- Header includes all and only COLUMNS, in order.
- Row format chosen escapes the delimiter (e.g., CSV uses `"` quoting with `""` escape).
- DUP_POLICY behavior is exemplified in pseudocode.
- Terminator is exact bytes — not a prose sentence.
