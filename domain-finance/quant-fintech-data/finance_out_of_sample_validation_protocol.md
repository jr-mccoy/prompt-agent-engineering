---
title: "Out-of-Sample Validation Protocol — Holdout Testing, Base-Rate Lift, and the Promotion Gate"
category: finance/quant-fintech-data
description: "Run a pre-registered pattern through a disciplined out-of-sample test: split train/holdout by time with no leakage, measure lift over the base rate in-sample and then on untouched data, adjust the evidence bar for multiple comparisons, require a minimum sample size, and emit a promote / hold / reject verdict. This is the formal Gate A protocol behind the toolkit's pattern knowledge base."
techniques:
  - QA-02
  - QA-05
  - DS-02
  - NE-11
  - NE-10
difficulty: advanced
tags:
  - out-of-sample
  - holdout
  - validation
  - base-rate-lift
  - multiple-comparisons
  - gate-a
updated: "2026-06-18"
related_prompts:
  - domain-finance/quant-fintech-data/finance_pattern_hypothesis_registration.md
  - domain-finance/quant-fintech-data/finance_backtest_design_critique.md
  - domain-finance/quant-fintech-data/finance_signal_decay_monitor.md
  - domain-reasoning-craft/forecasting/forecasting_signal_vs_noise_filter.md
  - ai-investment-research-toolkit/prompts/stage-3-pattern-knowledge-base.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. A pattern that passes out-of-sample can still fail live; validation reduces, but does not remove, the risk of overfitting. All outputs require independent verification before any capital is committed.**

## Objective

Decide whether a pre-registered pattern has a real edge or is an artifact of overfitting. The
protocol takes a registered hypothesis, splits the data so a portion is genuinely untouched,
measures the pattern's lift over its base rate first in-sample and then on the holdout, raises the
evidence bar for how many features were screened, enforces a minimum sample size, and returns a
**promote / hold / reject** verdict with the evidence. This is the formal expression of Gate A:
a pattern may only become `validated` (and thus drive screening or sizing) by clearing this bar.

## When to Use

- Testing a pattern that has been pre-registered (via `finance_pattern_hypothesis_registration.md`)
- Promoting a pattern from `hypothesis` to `validated` in the toolkit's knowledge base (Stage 3)
- Re-validating a pattern on fresh data before continuing to rely on it
- Auditing whether a claimed edge survives outside the data it was discovered in

## Inputs / Context Required

**The registered pattern**
- The registration record: feature definition, sample frame, base rate, expected effect, and the
  count of features screened

**Data (point-in-time)**
- Historical data partitioned (or partitionable) into a derivation/train sample and a disjoint
  holdout, split by time with no leakage across the boundary
- Resolved outcomes for both samples
- The configured minimum out-of-sample sample size (Gate A threshold)
- Any input unavailable → mark `UNAVAILABLE` and queue (DS-02)

## Constraints

### Must
- Split train/holdout strictly by time; the holdout must be data the pattern was NOT derived from,
  with no leakage across the boundary (QA-05).
- Measure lift over the base rate in-sample, then on the holdout; the holdout result is the one
  that counts (NE-11).
- Require the holdout sample size to meet the configured minimum before any promotion (DS-02).
- Raise the required out-of-sample lift in proportion to the number of features screened
  (multiple-comparisons adjustment) (QA-02).
- Judge whether the holdout result is signal or noise (reuse
  `forecasting_signal_vs_noise_filter.md`) and present an uncertainty band (NE-10).
- Emit an explicit promote / hold / reject verdict tied to the evidence (DS-02).

### Must Not
- Promote on in-sample evidence alone, or below the minimum sample size.
- Re-use the holdout repeatedly until it passes (that turns it into training data) — note if the
  holdout has been consumed and require a fresh one.
- Let leakage (look-ahead, overlapping windows, target contamination) into the split.
- Ignore the features-screened count when setting the bar.
- Invent lift, sample sizes, or p-equivalents — queue unknowns (DS-02).

## Instructions

1. **Confirm the registration (QA-02).** Verify the pattern was pre-registered before outcome
   inspection and that the feature definition is reproducible. If not, treat all data as
   contaminated and require a fresh, untouched holdout.

2. **Split by time, check leakage (QA-05).** Define the train/holdout boundary by date. Check for
   look-ahead, overlapping outcome windows, and target leakage. Reuse
   `finance_backtest_design_critique.md` to stress the split for survivorship and snooping.

3. **Measure in-sample lift (NE-11).** On the train sample, compute the outcome rate WITH the
   signal vs. the base rate WITHOUT it: `lift = rate_with_signal − base_rate` (and/or the ratio).
   Record `n`.

4. **Measure out-of-sample lift (NE-11).** Apply the frozen feature definition to the untouched
   holdout; compute the same lift and `n`. This is the decisive number.

5. **Multiple-comparisons adjustment (QA-02).** Given the features-screened count, raise the
   required out-of-sample lift / sample size (more searching → higher bar). State the adjusted
   threshold used.

6. **Signal vs. noise + band (NE-10).** Apply `forecasting_signal_vs_noise_filter.md`; present the
   holdout lift with an uncertainty band, not a single number.

7. **Verdict (DS-02).** Promote to `validated` only if holdout `n` ≥ minimum AND adjusted
   out-of-sample lift > 0 with the band not straddling zero into noise. Otherwise hold
   (`hypothesis`) or reject. State the reason citing `n`, lift, and the threshold.

## Output Format

```
## OOS VALIDATION: [pattern] | as_of [date] | Verdict: [PROMOTE / HOLD / REJECT]
```

### Split integrity
| Check | Finding |
|---|---|
| Pre-registered before outcomes | yes/no |
| Train/holdout boundary (by time) | … |
| Leakage (look-ahead/overlap/target) | … |
| Holdout previously consumed? | … |

### Lift vs. base rate
| Measure | In-sample | Out-of-sample |
|---|---|---|
| n | … | … |
| Base rate | … | … |
| Lift vs. base rate | … | … (band: …) |

### Multiple-comparisons adjustment
- Features screened: … → required OOS lift / min n raised to: …

### Verdict
**[PROMOTE / HOLD / REJECT]** — reason citing holdout n, adjusted lift vs. base rate, and the
minimum sample size. Resulting status: `[validated / hypothesis / rejected]`.

### Open items (queued, not guessed)
- `UNAVAILABLE` inputs

## Verification

- [ ] Pattern was pre-registered before outcome inspection (or a fresh holdout was used).
- [ ] Train/holdout split is by time with no leakage; integrity checks shown.
- [ ] Lift over base rate measured in-sample AND out-of-sample, with n for each.
- [ ] Holdout n meets the configured minimum before any promotion.
- [ ] Required lift raised for the number of features screened.
- [ ] Holdout result judged signal vs. noise with an uncertainty band.
- [ ] Explicit promote/hold/reject verdict tied to the numbers; unknowns queued.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| In-sample brilliance sold as an edge | Decisive number is the out-of-sample holdout lift (NE-11) |
| Holdout re-used until it passes | Track holdout consumption; require a fresh one if consumed (QA-05) |
| Best-of-many features looks significant | Raise the bar by features-screened count (QA-02) |
| Tiny holdout produces a lucky result | Enforce minimum sample size before promotion (DS-02) |
| Leakage inflates the OOS result | Mandatory leakage check + backtest critique on the split |
| Point estimate hides noise | Present lift with an uncertainty band; signal/noise filter (NE-10) |
| Missing data guessed to fill the table | `UNAVAILABLE` + queue (DS-02) |
