# Brier Scoring & Calibration Method

*For informational and research purposes only. Not financial, investment, or tax advice.*

This reference defines exactly how predictions are scored, so the running track record is
reproducible both by hand and by `scripts/score_brier.py` (implemented; `--self-check` proves it). It backs
Gate C: real-money unlock requires ≥100 resolved predictions AND a running Brier ≤ 0.18.

Reuse: `referenced-prompts/domain-reasoning-craft/forecasting/forecasting_brier_tracker_design.md` and
`referenced-prompts/domain-reasoning-craft/forecasting/forecasting_calibration_self_audit.md`.

## Brier component (single prediction)

For a binary prediction with stated probability `p` (0–1) and outcome `o` (1 = hit, 0 = miss):

```
brier_component = (p − o)^2
```

- A confident-correct call (`p = 0.9`, `o = 1`) scores `0.01` — low (good).
- A confident-wrong call (`p = 0.9`, `o = 0`) scores `0.81` — high (bad).
- A pure hedge (`p = 0.5`) always scores `0.25`, win or lose — never sharp.

Lower is better. Range is 0 (perfect) to 1 (maximally wrong).

## Running Brier score (track record)

The mean Brier component over **all** resolved predictions:

```
Brier = (1 / N) * Σ (p_i − o_i)^2     for i in resolved predictions
```

Always compute over every resolved prediction, never a favorable subset. `N` is also the
Gate C resolved-prediction count.

## Worked example

| id | p | outcome | (p − o)^2 |
|---|---|---|---|
| PRED-0042 | 0.62 | hit (1) | 0.1444 |
| PRED-0043 | 0.30 | miss (0) | 0.0900 |
| PRED-0044 | 0.80 | miss (0) | 0.6400 |

Running Brier = (0.1444 + 0.0900 + 0.6400) / 3 = **0.2915**. With N = 3 this is far short of
Gate C on both count (need ≥100) and score (need ≤0.18).

## Calibration report

Calibration asks: *when you say 70%, does it happen ~70% of the time?* Bucket resolved
predictions by stated probability and compare the bucket's mean `p` to its realized hit rate.

| Bucket (stated p) | # resolved | mean stated p | realized hit rate | gap |
|---|---|---|---|---|
| 0.0–0.2 | … | … | … | … |
| 0.2–0.4 | … | … | … | … |
| 0.4–0.6 | … | … | … | … |
| 0.6–0.8 | … | … | … | … |
| 0.8–1.0 | … | … | … | … |

- **Well calibrated:** realized hit rate ≈ mean stated p in each bucket (small gap).
- **Overconfident:** stated p consistently higher than realized hit rate.
- **Underconfident / hedging:** predictions cluster near 0.5 with little spread (poor resolution even if rarely very wrong).

Report both the running Brier (sharpness + calibration combined) and the bucket table
(calibration alone), plus Gate C progress: `N/100` resolved and current Brier vs. 0.18.

## Why scores can't be gamed away

Predicting 0.5 forever keeps any single component at 0.25 but never beats a base rate and
fails the calibration table's resolution check — so it cannot reach Brier ≤ 0.18 across a
real, varied set of predictions. Honest, sharp, calibrated forecasting is the only path
through Gate C.
