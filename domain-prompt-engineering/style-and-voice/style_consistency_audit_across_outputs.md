---
title: "Consistency Audit Across Outputs"
category: prompt-engineering/style-and-voice
description: "Detect voice and style drift across N outputs generated from the same prompt by comparing measurable signals."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-01
  - QA-01
  - QA-08
difficulty: intermediate
tags:
  - consistency
  - audit
  - drift
  - style
  - multi_output
updated: "2026-05-11"
related_prompts:
  - domain-prompt-engineering/style-and-voice/style_voice_extraction_from_corpus.md
  - domain-prompt-engineering/style-and-voice/style_length_and_density_control.md
  - domain-prompt-engineering/style-and-voice/style_signature_phrase_kill_list.md
---

## Objective

Given N outputs from the same prompt, measure style consistency across a fixed signal set and produce a drift report that identifies which signals vary, by how much, and across which output pairs.

## When to Use

- You have run the same prompt 3–10 times and suspect outputs vary more than acceptable.
- You are building an eval harness and need a consistency baseline.
- After changing a system prompt, you want to confirm style was stabilized, not just content.
- **Not for:** comparing outputs from different prompts (that is A/B testing, not consistency audit).

## Signal Set

| Signal | Measure | Metric |
|--------|---------|--------|
| S1 — Word count | Total words per output | Mean ± SD |
| S2 — Sentence length | Mean words per sentence | Mean ± SD across outputs |
| S3 — Opener type | First 3 words category (imperative / question / noun / "I" / connector) | Mode + distribution |
| S4 — Qualifier density | Count of hedging words ÷ total words | Mean ± SD |
| S5 — Paragraph count | Total paragraphs | Mode + range |
| S6 — List use | Presence of bullet or numbered list | Frequency (N/total outputs) |
| S7 — Structural pattern | Identical or divergent heading/section structure | Jaccard similarity across outputs |
| S8 — Signature phrases | Recurring multi-word phrases (≥3 words, ≥2 outputs) | Frequency table |

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Outputs to audit | Yes | 3–10 outputs; paste delimited by `===OUTPUT N===` |
| Prompt used | Recommended | To assess whether drift is prompt-addressable |
| Tolerance thresholds | Optional | Acceptable SD per signal; defaults shown below |

**Default tolerances:**
- Word count SD ≤ 15% of mean
- WPS SD ≤ 2 words
- Qualifier density SD ≤ 0.01
- S7 Jaccard ≥ 0.7 (70% structural overlap)

## Constraints

**Must:**
- Compute every signal in the signal set for every output.
- Flag any signal where the observed variance exceeds the tolerance threshold.
- For flagged signals, identify the specific outputs that are outliers (not just "there is variance").
- Produce a ranked drift report: worst-drifting signal first.
- If prompt is provided, produce one concrete prompt-edit recommendation per flagged signal.

**Must Not:**
- Report "outputs are generally consistent" without quantitative backing.
- Average across flagged outliers without noting which outputs skew the mean.
- Exceed the signal set — do not introduce subjective signals like "tone" or "clarity."

## Instructions

1. **Parse outputs.** Label O1, O2, … On. Compute each signal for each output and record in a matrix.

2. **Compute statistics.** For each signal: mean, SD (or mode + range for categorical signals), and observed vs. tolerance comparison.

3. **Flag violations.** For each signal exceeding tolerance: list it as a flagged drift, identify outlier outputs, and describe the direction of drift (e.g., "O4 has 2× the mean qualifier density").

4. **Rank flagged signals** by severity: SD-to-tolerance ratio (highest first).

5. **Diagnose root cause** (if prompt provided):
   - Is the signal underspecified in the prompt? → Add a constraint.
   - Is the signal in conflict with another prompt rule? → Resolve conflict.
   - Is the signal random/temperature-driven? → Use a temperature note.

6. **Build repair recommendations** — one concrete change per flagged signal.

## Output Format

```
## Consistency Audit — [N] Outputs

### Signal Matrix
| Signal | O1 | O2 | O3 | ... | Mean | SD | Tolerance | Status |
|--------|----|----|----|----|------|----|-----------|----|
| S1 Word count | | | | | | | ≤15% | ✓/✗ |
...

### Drift Report (ranked)
1. [Signal]: SD=[X], tolerance=[Y], outliers=[O2, O4]
   Direction: [description]
   Root cause: [if prompt provided]
   Repair: [concrete edit]
2. ...

### Clean Signals
[List signals within tolerance]

### Recommended Prompt Additions
[Copy-paste blocks per repair recommendation]
```

## Verification

- [ ] Signal matrix has N columns (one per output) and 8 rows (one per signal) — no blanks.
- [ ] Every flagged signal names specific outlier outputs.
- [ ] Drift report is sorted by SD-to-tolerance ratio, not arbitrary order.
- [ ] Repair recommendations are concrete prompt edits, not advice like "be more consistent."
- [ ] Clean signals list is mutually exclusive with the Drift Report list.
