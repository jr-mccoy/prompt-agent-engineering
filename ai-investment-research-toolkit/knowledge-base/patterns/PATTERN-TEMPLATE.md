---
id: PATTERN-0000
title: "One-line, specific, falsifiable pattern name (asset class + signal + outcome window)"
status: hypothesis        # hypothesis | validated | retired
asset_classes: [equity-microcap]   # equity-microcap | equity | crypto | options
hypothesis: "Precise claim: <signal> predicts <outcome> over <horizon> in <population>."
registered_on: "YYYY-MM-DD"        # BEFORE outcome inspection — pre-registration (Gate A)
feature_definition: "Precise, reproducible computation of the signal (no ambiguity)."
sample_frame: "Universe + date range the sample is drawn from."
base_rate: "Outcome frequency in the sample frame ABSENT the signal."
in_sample_result: { n: 0, lift_vs_base_rate: null }
out_of_sample_result: { n: 0, lift_vs_base_rate: null }   # REQUIRED to reach 'validated'
multiple_comparisons_note: "How many features were screened to find this one."
decay_estimate: "Expected edge half-life / regime sensitivity."
capacity_note: "Does the edge survive realistic size, liquidity, and costs?"
confidence: low            # low | medium | high
last_reviewed: "YYYY-MM-DD"
linked_predictions: []     # PRED-* journal ids that tested this pattern
---

## Notes

Copy this file to `PATTERN-<id>.md` and fill every field. A pattern may NOT be set
to `status: validated` until `out_of_sample_result.n` meets the configured minimum
sample size AND shows positive `lift_vs_base_rate` on data the pattern was not
derived from (Gate A, enforced by the `pattern-knowledge-base` skill and the
Stage 3 prompt). In-sample-only patterns stay `hypothesis`. Patterns whose edge
has decayed below the base rate are moved to `retired`, with a dated reason here.
