---
title: "Case Inventory from Production Logs"
category: prompt-engineering/evaluation/eval-datasets
description: "Mine production logs into a structured eval test set with extraction filters, deduplication, labeling, and anonymization steps."
techniques:
  - ST-02
  - ST-03
  - CM-02
  - RT-05
  - DT-01
difficulty: intermediate
tags:
  - dataset_curation
  - production_logs
  - deduplication
  - eval_datasets
  - test_set_mining
updated: "2026-05-11"
related_prompts:
  - domain-prompt-engineering/evaluation/eval-datasets/dataset_synthetic_case_generator.md
  - domain-prompt-engineering/evaluation/eval-datasets/dataset_holdout_split_designer.md
  - domain-prompt-engineering/evaluation/correctness_eval_design_prompt.md
---

## Objective

Convert production logs (raw request/response pairs) into a structured, labeled, deduplicated eval test set. Output includes extraction criteria, a deduplication protocol, a labeling schema, anonymization decisions, and a case inventory ready for use in an eval harness.

## When to Use

- Bootstrapping a test set from real production traffic
- After a regression or quality incident: mine logs to find cases similar to the failure
- When synthetic data is insufficient and real distribution coverage is needed
- When building a monitoring dashboard and need representative cases

## Inputs

| Field | Required | Description |
|-------|----------|-------------|
| `log_schema` | Yes | Fields available in logs (e.g., `request_id`, `input`, `output`, `timestamp`, `latency_ms`, `user_id`) |
| `task_description` | Yes | What the prompt does |
| `target_set_size` | Yes | Number of cases in the final set |
| `date_range` | Yes | Time window for log extraction |
| `known_failure_cases` | Optional | Request IDs of known failures to include |
| `pii_fields` | Optional | Fields containing PII that must be anonymized |

## Constraints

**Must:**
- Apply ≥3 extraction filters to reduce noise before deduplication
- Deduplicate using a defined similarity criterion — not just exact-match
- Assign a behavior label to every case using a taxonomy derived from the task
- Document anonymization decisions per PII field
- Produce a coverage report: which behavior labels are over- and under-represented

**Must Not:**
- Include cases where the output field is empty or truncated (log artifact, not real failure)
- Include cases from the last 48 hours (recent traffic may not represent stable behavior)
- Use only high-confidence cases — deliberately include ≥10% borderline/uncertain cases

## Instructions

**Step 1 — Extraction filters**

Define ≥3 filters to apply before deduplication:

| Filter | Field | Condition | Rationale |
|--------|-------|-----------|-----------|
| Completeness | `output` | Not null, not truncated | Avoid log artifacts |
| Recency exclusion | `timestamp` | Older than 48 hours | Avoid recent noise |
| Length filter | `input` | > N characters | Exclude trivially short inputs |
| Error exclusion | `status_code` | Not 4xx/5xx | Avoid API errors |
| [Custom] | | | Specific to task |

**Step 2 — Deduplication**

Choose similarity criterion appropriate to the task:

| Option | Method | Use when |
|--------|--------|----------|
| Exact match | Hash(`input`) | Input is structured/templated |
| Near-duplicate | MinHash / SimHash with threshold ≥0.85 | Free-text inputs |
| Semantic | Embedding cosine similarity ≥0.92 | Inputs have paraphrase variation |
| Manual clusters | Group by intent label | After labeling step |

After deduplication, the set should have <10% near-duplicate pairs (cosine ≥0.90).

**Step 3 — Behavior labeling**

Derive a labeling taxonomy from the task description:

```
Taxonomy (example for a summarization task):
  L1: nominal — standard input, expected summary behavior
  L2: long_input — input exceeds typical length
  L3: ambiguous_request — underspecified or contradictory input
  L4: refusal_trigger — input the model should decline
  L5: format_edge — output format stress case
```

Label each case with its primary and optional secondary label. Flag cases where labeling confidence is < 0.7 as `uncertain`.

**Step 4 — Case schema**

```json
{
  "id": "LOG-001",
  "source_request_id": "<original log ID>",
  "timestamp": "<date only, not time — to prevent re-identification>",
  "input": "<extracted or anonymized input>",
  "output": "<extracted or anonymized output>",
  "behavior_label_primary": "L1",
  "behavior_label_secondary": "L3",
  "labeling_confidence": 0.9,
  "is_uncertain": false,
  "anomaly_flags": ["<empty or list: truncated, duplicate_candidate, pii_residual>"]
}
```

**Step 5 — Anonymization**

For each field in `pii_fields`:

| PII type | Anonymization method |
|----------|---------------------|
| Name | Replace with `[NAME_N]` where N is a counter |
| Email | Replace with `[EMAIL_N]` |
| Date of birth | Replace with `[AGE_RANGE]` (e.g., 30–40) |
| Free text with embedded PII | Regex + entity recognition; flag residuals for manual review |

After anonymization, run a residual PII check: search for patterns matching email, phone, SSN, and name regex patterns.

**Step 6 — Coverage report**

Produce:
| Label | Count | % of set | Target % | Status |
|-------|-------|----------|----------|--------|
| L1 | N | X% | 40% | ✓ |
| L2 | N | X% | 20% | ✓ |
| L4 | N | X% | 15% | ✗ under |

Under-represented labels: supplement with synthetic cases (see `dataset_synthetic_case_generator.md`).

## Output Format

1. **Extraction pipeline** — filters applied, records before/after each step
2. **Deduplication report** — method used, pairs removed, threshold
3. **Case array** — JSON following schema
4. **Coverage report** — label × count × target × status
5. **Anonymization audit** — fields processed, residual PII check result

## Verification

- [ ] ≥3 extraction filters applied with record counts before/after
- [ ] Deduplication uses a defined similarity criterion (not just exact match)
- [ ] Every case has a behavior label and `labeling_confidence`
- [ ] ≥10% of cases are `is_uncertain: true`
- [ ] Residual PII check run and documented
- [ ] Coverage report shows no label with 0 cases
