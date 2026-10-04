---
name: dataset_profile
description: Quick operational profile of one tabular dataset (CSV, Parquet, JSON Lines, Excel sheet, or a warehouse table) — shape, inferred types, null and empty-string rates, distinct counts, candidate keys, duplicate rows, numeric ranges and percentiles, top categorical values, date coverage, and sentinel values — ending in a short list of data-quality flags and questions for the data owner. Masks likely PII in sample values. Distinct from the ML dataset-validation skill (leakage, labels, drift) and from the data-dictionary writer (documents meaning); this answers "what is actually in this file?" in minutes.
version: "1.0.0"
category: data-analysis
tags: [data-analysis, profiling, data-quality, csv, parquet, eda, nulls, duplicates, schema]
agents_used: []
---

# Dataset Profile

Run a fast, factual profile of a single dataset before anyone builds a metric,
dashboard, model, or join on it. You report what is **measured** in the data,
keep it separate from what you **infer** about meaning, and never invent a
column's business definition.

[Extended thinking: Most bad analyses start with an unprofiled input — a key that
is not unique, "nulls" that are really empty strings or `-1`, a date column that
silently stops three weeks ago, a category with a near-duplicate spelling. A
profile catches these in minutes. The command is deliberately single-agent and
direct-execution: it is a quick pre-flight, not a study. It stops at flags and
questions; interpretation and documentation are routed to the domain prompts.]

## Requirements
$ARGUMENTS

Expected: a path to the dataset (or a table name plus how to query it), and
optionally the intended key column(s), the expected grain ("one row per order"),
and the expected date range. If no dataset is given, ask for it and stop.

## When NOT to use

- ML training/inference data checks (leakage, label quality, train/test drift) →
  `skills/ml-ai/dataset-validation/`
- Writing analyst-facing documentation of what tables and columns *mean* →
  `domain-data-analytics/framing-and-metrics/analytics_data_dictionary_writer.md`
  (this profile is a good input to it)
- Checking one computed business number → `/metric_sanity_check`
  (`commands/data-analysis/metric_sanity_check.md`)
- Designing ongoing data-quality tests for a pipeline →
  `skills/data-engineering/data-quality-frameworks/`

## Instructions

### Phase 1 — Locate and load safely

1. Check file size (or table row count) **before** loading. If the data is too
   large to load comfortably in memory (a rough guide: above ~1 GB for pandas),
   profile with an engine that streams or samples (DuckDB, a warehouse `SELECT`
   with aggregates) or profile a stated random sample and label every figure as
   sample-based.
2. Record how the file was read: delimiter, encoding, header row, sheet name,
   and any parse warnings. Mixed-type warnings are findings, not noise.
3. **PII guard:** identify columns that look like personal data (emails, phone
   numbers, names, addresses, national IDs, free-text notes). Profile them
   (null rate, distinct count, format validity) but **mask sample values** in
   the output (e.g., `j***@example.com`). Never paste raw rows containing PII.

Gate: if the file cannot be parsed consistently, stop and report the parse
problem — a profile of a mis-parsed file is worse than none.

### Phase 2 — Structural profile

For the whole table: row count, column count, fully duplicated rows.
For each column:
- declared/stored type vs inferred type (e.g., numbers stored as text)
- null count and rate; **empty-string** and whitespace-only count separately
- distinct count (non-null) and whether it is unique and non-null (candidate key)
- If key columns were given: duplicate count on that key, and null keys

Grain check: if an expected grain was given, test it (duplicates on the grain
key = grain violated). If not given, state the grain the data *appears* to have,
tagged `[inferred]`.

### Phase 3 — Value profile

- **Numeric:** min, max, mean, p1/p25/p50/p75/p99, count of zeros and negatives
- **Categorical / text:** top 10 values with share, number of rare values,
  near-duplicate spellings (case/whitespace variants), min/max length
- **Dates/timestamps:** min, max, presence of time zone, rows per period
  (day/week/month) to expose gaps and a stale tail
- **Sentinels:** values that commonly stand in for missing data — `-1`, `0`
  where impossible, `9999`, `1900-01-01`, `"N/A"`, `"null"`, `"none"`, `"-"`

### Phase 4 — Flags and questions

Turn the profile into at most ~10 flags, each with severity (HIGH / MEDIUM /
LOW), the evidence (the numbers), and the question it raises for the data owner.
Do not "fix" the data in this command.

## Reference snippets (adapt; verify against your installed versions)

pandas (small/medium files):

```python
import pandas as pd

df = pd.read_csv(PATH, low_memory=False)   # or pd.read_parquet(PATH)
n = len(df)
profile = pd.DataFrame({
    "dtype": df.dtypes.astype(str),
    "nulls": df.isna().sum(),
    "null_rate": df.isna().mean().round(4),
    "distinct": df.nunique(dropna=True),
})
text_cols = df.select_dtypes(include="object").columns
profile.loc[text_cols, "empty_str"] = [
    (df[c].astype(str).str.strip() == "").sum() for c in text_cols
]
profile["candidate_key"] = (profile["distinct"] == n) & (profile["nulls"] == 0)
print(f"rows={n} cols={df.shape[1]} duplicate_rows={df.duplicated().sum()}")
print(profile.to_string())
print(df.describe(include="number", percentiles=[.01, .25, .5, .75, .99]).T.to_string())
```

DuckDB (large files; `SUMMARIZE` availability and output columns vary by
version `[verify]`):

```sql
SUMMARIZE SELECT * FROM 'data.parquet';
SELECT key_col, COUNT(*) AS n FROM 'data.parquet' GROUP BY 1 HAVING COUNT(*) > 1 LIMIT 20;
```

## Output

```markdown
# Dataset Profile: <name>
Source: <path/table> · Read as: <format, delimiter, encoding> · Rows: <n> (<full | sample of n>)
Expected grain: <given | [inferred] ...> · Grain check: PASS / FAIL (<dupes> duplicate keys)

## Columns
| Column | Type (stored → inferred) | Null % | Empty-str | Distinct | Key? | Notes |

## Numeric ranges
| Column | Min | p50 | p99 | Max | Zeros | Negatives |

## Dates
| Column | Min | Max | TZ? | Gaps / stale tail |

## Flags
| Severity | Flag | Evidence | Question for owner |

## Suggested next step
- <e.g., document with analytics_data_dictionary_writer; confirm key with owner>
```

## Success Criteria

- Every number in the output was computed from the data (or labelled as sample-based)
- Grain stated and tested, or explicitly `[inferred]`
- Nulls, empty strings, and sentinels reported separately
- No raw PII in the output
- Flags are evidence-backed and phrased as questions, not conclusions about meaning

## Constraints

- NEVER modify, clean, or overwrite the source data
- NEVER invent what a column means; mark guesses `[inferred]` and ask
- NEVER present sample-based figures as full-table figures
