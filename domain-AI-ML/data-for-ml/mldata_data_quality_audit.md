---
title: "ML Data Quality Audit"
category: AI-ML/data-for-ml
description: "Audit a dataset across completeness, validity, consistency, uniqueness, timeliness, and outliers — producing severity-ranked, evidence-backed findings with concrete remediation before the data trains a model."
techniques:
  - ST-02
  - RT-05
  - DS-06
  - QA-12
  - QA-01
difficulty: intermediate
tags:
  - data-quality
  - data-validation
  - outliers
  - data-profiling
  - data-cleaning
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/data-for-ml/mldata_dataset_curation_plan.md
  - domain-AI-ML/data-for-ml/mldata_data_leakage_detector.md
  - domain-AI-ML/data-for-ml/mldata_sampling_bias_audit.md
---

# ML Data Quality Audit

**Objective:** Systematically audit a dataset across the core quality dimensions — completeness, validity, consistency, uniqueness, timeliness, and outliers/anomalies — and produce a severity-ranked list of findings, each anchored to specific columns/rows with evidence and a concrete remediation, before the data is used to train or evaluate a model.

**When to Use:**
- Before training on a new or refreshed dataset.
- When model behavior is erratic and you suspect data, not modeling, is the cause.
- When inheriting a dataset whose provenance and cleanliness are unknown.
- As a recurring gate on a production data feed.

**When NOT to Use:**
- To hunt for train/test contamination or target leakage specifically (use `mldata_data_leakage_detector.md`).
- To check whether the sample represents the deployment population (use `mldata_sampling_bias_audit.md`).
- To assess label correctness/agreement (use `mldata_annotation_quality_review.md`).

## Inputs / Context

Provide what you can; the audit degrades gracefully if some are missing:
- **Schema** — columns, types, expected ranges/units, allowed categories, and which fields are required.
- **Dataset profile** — row count, per-column null rates, distinct counts, min/max/quantiles (or the data itself if available).
- **Business rules** — cross-field constraints (e.g., `end_date ≥ start_date`), valid enumerations, referential expectations.
- **Intended use** — the task and the moment of inference, so timeliness can be judged.
- **Known issues** — any quality problems already suspected.

## Constraints

**Must:**
- Anchor every finding to a specific column (and example rows/values) — no generic "data is dirty."
- Assign each finding a severity (Critical / High / Medium / Low) tied to its modeling impact, not just its frequency.
- Cover all six dimensions explicitly, noting where one is N/A and why.

**Must Not:**
- Report a profiling number (null rate, outlier count, distinct count) as fact if it was not supplied or computable from the input — state it as "to be measured."
- Flag rare values as outliers without distinguishing genuine anomalies from legitimate long-tail data.
- Recommend dropping or imputing without stating the assumption it relies on and its risk.

**Instructions:**

1. **Confirm scope and expectations.** Restate the schema, required fields, valid ranges/enums, and business rules so the audit measures against an explicit standard, not intuition.

2. **Audit completeness.** Identify missingness per column, distinguish structural missing (not applicable) from true gaps, and flag fields whose null rate undermines their usability for the task.

3. **Audit validity.** Check types, ranges, units, and enumerations against the schema; flag values that are impossible (negative ages), out of range, or off-enum.

4. **Audit consistency.** Test cross-field and cross-record rules (date ordering, totals matching components, referential links, contradictory duplicates) and conflicting representations of the same entity.

5. **Audit uniqueness.** Identify exact and near-duplicate rows and key collisions; distinguish illegitimate duplicates from legitimate repeated events.

6. **Audit timeliness.** Assess data freshness and staleness relative to the inference moment, and whether time fields are plausible and monotonic where expected.

7. **Audit outliers/anomalies.** Surface extreme values and distributional anomalies; separate data-entry errors from real but rare observations, and note the method/threshold used.

8. **Rank and remediate.** Order findings by (modeling impact × prevalence). For each, give a specific fix (correct, impute with method, drop with rule, add a validation gate) and its risk.

**Output Format:**

A markdown report:
- **Quality Scorecard** — table: Dimension | Status (Pass/Warn/Fail) | Key Finding.
- **Findings (ranked)** — table: Finding | Dimension | Severity | Evidence (column/example) | Modeling Impact | Remediation.
- **Outlier/Anomaly Notes** — method, thresholds, and judgment calls.
- **Clean Aspects Verified** — what passed, so it isn't re-litigated.
- **Recommended Validation Gates** — checks to encode so issues are caught automatically next time.
- **INSUFFICIENT EVIDENCE** — an enumerated verdict per dimension, not a fallback. Use it where the audit ran on a schema, a sample, or a description rather than on a profiled dataset, and say what would resolve it: a profiling pass over a stated window reporting null rate, cardinality, range, and duplicate rate per column. A `Pass` awarded without that pass is an assumption wearing a verdict's clothes.

## Verification

- [ ] All six dimensions are addressed (or marked N/A with a reason).
- [ ] Every finding names a specific column and gives example values/rows.
- [ ] Each finding has a severity justified by modeling impact, not just count.
- [ ] Outlier calls state the detection method and threshold and separate errors from real long-tail values.
- [ ] Every remediation states its assumption and risk; profiling numbers not supplied are marked "to be measured."
- [ ] Dimensions that could not be evidenced are marked INSUFFICIENT EVIDENCE with the profiling output that would resolve them — not defaulted to Pass.

## False-Positive Prevention

❌ **DON'T:**
- Treat all missingness as a defect — some nulls are structurally valid (field not applicable to that row).
- Call long-tail values "outliers to remove" when they may be the rare, important cases the model must learn.
- Flag duplicates without checking whether they are legitimate repeated events (re-orders, repeat visits).
- Impute silently and present a "clean" dataset that hides how much was fabricated.

✅ **DO:**
- Separate structural missing from true gaps before judging completeness.
- State the outlier-detection method and threshold, and decide error-vs-real per case.
- Confirm duplicate semantics against a business key before removing rows.
- Make every imputation explicit, with its method, assumption, and the risk it introduces.

## Example Output

```markdown
## Data Quality Audit: Patient Readmission Dataset v2

### Quality Scorecard
| Dimension | Status | Key Finding |
|---|---|---|
| Completeness | Warn | `lab_a1c` 38% null; missingness correlates with outpatient source |
| Validity | Fail | `age` contains 14 values > 120 and 3 negatives |
| Consistency | Warn | `discharge_date < admit_date` in 211 rows |
| Uniqueness | Pass | No duplicate encounter IDs after key check |
| Timeliness | Warn | 6% of rows older than the 24-month modeling window |
| Outliers | Warn | `length_of_stay` has a cluster at 999 (likely sentinel) |

### Findings (ranked)
| Finding | Dimension | Severity | Evidence | Modeling Impact | Remediation |
|---|---|---|---|---|---|
| Impossible ages | Validity | Critical | age=210, age=-3 | Corrupts age features | Reject rows; add range gate 0–120 |
| 999 LOS sentinel | Outliers | High | length_of_stay=999 (n=420) | Inflates LOS signal | Map 999→null; impute median by service |
| Discharge<admit | Consistency | High | 211 rows | Breaks duration features | Quarantine; re-derive from EHR |
| a1c missingness | Completeness | Medium | 38% null, source-correlated | Risk of missing-not-at-random bias | Add missingness indicator; do not naive-impute |

### Outlier/Anomaly Notes
- Used IQR (1.5×) per service line for LOS; the 999 cluster is a known legacy sentinel, treated as missing rather than removed.

### Clean Aspects Verified
- Encounter IDs unique; referential link to patient table intact.

### Recommended Validation Gates
1. Reject age outside [0,120] at intake.
2. Assert discharge_date ≥ admit_date.
3. Flag any LOS == 999 as sentinel-missing automatically.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** the audit walks the six dimensions in fixed order.
- **RT-05 (Evidence-Based Reasoning):** each finding is anchored to a named column and example values.
- **DS-06 (Prioritization & Severity Guidance):** findings ranked by modeling impact × prevalence.
- **QA-12 (False Positives Identification):** separates real anomalies from legitimate rare/structural data.
- **QA-01 (Self-Verification):** the checklist gates the report before the data is trusted.

**Related Prompts:**
- `mldata_dataset_curation_plan.md` — encode these gates at intake when building the dataset.
- `mldata_data_leakage_detector.md` — a different failure mode: contamination vs dirtiness.
- `mldata_sampling_bias_audit.md` — clean data can still be unrepresentative.
