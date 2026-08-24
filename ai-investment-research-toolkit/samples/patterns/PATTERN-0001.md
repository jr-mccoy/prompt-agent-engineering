---
id: PATTERN-0001
title: "Sustained gross-margin expansion preceding 6-month re-rating in small-cap software"
status: validated         # hypothesis | validated | retired
asset_classes: [equity]
hypothesis: "Four+ consecutive quarters of gross-margin expansion predicts >15% 6-month relative outperformance in small-cap software."
registered_on: "2025-09-01"        # BEFORE outcome inspection — pre-registration (Gate A)
feature_definition: "Gross margin (gross profit / revenue) rising QoQ for >=4 consecutive reported quarters, point-in-time as of each filing date."
sample_frame: "US small-cap software ($300M-$2B mcap), point-in-time index membership including delisted/acquired names; 2015-2021 train / 2022-2024 disjoint holdout."
base_rate: "0.34"                  # 6-month outperformance frequency absent the signal
in_sample_result: { n: 210, lift_vs_base_rate: 0.19 }
out_of_sample_result: { n: 42, lift_vs_base_rate: 0.11 }   # disjoint 2022-2024 holdout
multiple_comparisons_note: "Three features screened; this one pre-registered before holdout."
decay_estimate: "Edge halved over ~24 months; re-review quarterly."
capacity_note: "Survives realistic costs at small-cap liquidity; caps at ~2% position."
confidence: medium         # low | medium | high
last_reviewed: "2026-06-18"
linked_predictions: []
---

## Notes

**SAMPLE / FIXTURE record for the DRY_RUN walkthrough (ARCHITECTURE §12). Not a real edge.**

This pattern has passed an out-of-sample test on a disjoint 2022-2024 holdout: `n = 42`
(≥ the configured minimum of 30) with positive `lift_vs_base_rate = 0.11`. Under Gate A it
may hold `status: validated` and contribute to Stage 4 screener scores. Running
`validate_pattern.py` on it returns PASS.
