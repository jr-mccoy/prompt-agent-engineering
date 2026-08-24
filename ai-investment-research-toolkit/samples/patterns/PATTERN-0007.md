---
id: PATTERN-0007
title: "Insider cluster-buying in sub-$300M caps preceding 3-month outperformance"
status: hypothesis        # hypothesis | validated | retired
asset_classes: [equity-microcap]
hypothesis: "≥3 distinct insiders buying within 10 trading days predicts >10% 3-month relative outperformance in sub-$300M-cap US equities."
registered_on: "2026-06-18"        # BEFORE outcome inspection — pre-registration (Gate A)
feature_definition: "Count of distinct Form-4 open-market purchases by officers/directors within any rolling 10-trading-day window; signal fires at count >= 3."
sample_frame: "US equities < $300M mcap on NYSE/NASDAQ, 2018-2024."
base_rate: "0.31"                  # 3-month outperformance frequency absent the signal
in_sample_result: { n: 140, lift_vs_base_rate: 0.16 }
out_of_sample_result: { n: 0, lift_vs_base_rate: null }   # NOT yet tested out-of-sample
multiple_comparisons_note: "One pre-registered hypothesis; no feature mining."
decay_estimate: "Unknown — not yet measured."
capacity_note: "Microcap liquidity is thin; capacity untested."
confidence: low            # low | medium | high
last_reviewed: "2026-06-18"
linked_predictions: [PRED-0042]
---

## Notes

**SAMPLE / FIXTURE record for the DRY_RUN walkthrough (ARCHITECTURE §12). Not a real edge.**

This pattern has in-sample lift only; `out_of_sample_result` is empty. Under Gate A it
stays `hypothesis` and **cannot drive screening/sizing** — it may appear in Stage 4 only as
an unscored "paper-only signal." Running `validate_pattern.py` on it returns FAIL with
`eligible_for_validated: False`. That is Gate A doing its job.
