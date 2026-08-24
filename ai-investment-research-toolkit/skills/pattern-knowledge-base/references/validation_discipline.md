# Validation Discipline — Gate A

*For informational and research purposes only. Not financial, investment, or tax advice.*

This is the method that keeps the pattern knowledge base from fooling you. Gate A is a
hard gate: a pattern reaches `validated` only after every step here is satisfied. The
six steps are mandatory, not suggestions.

## 1. Pre-register the hypothesis (before outcomes)

Write `hypothesis`, `feature_definition`, `sample_frame`, and `base_rate`, and set
`registered_on`, **before** inspecting any outcomes. This prevents post-hoc storytelling —
the failure mode where you find a pattern in the noise and then invent a reason it "should"
work. If you have already seen the outcomes, say so; the hypothesis is then exploratory and
needs a *fresh* holdout it has never touched.

Reuse: `referenced-prompts/domain-reasoning-craft/forecasting/forecasting_base_rate_establishment.md` to set
the base rate rigorously.

## 2. Split train / holdout

Derive and tune the signal on the training sample only. Reserve a holdout that the pattern
was **not** derived from. Time-series data must be split by time (and ideally embargoed
around the boundary) so that information cannot leak backward — never shuffle rows across
the train/holdout line.

## 3. Anchor to the base rate (out-of-sample, not in-sample)

The pattern must beat the base rate **on the holdout**. In-sample lift proves only that the
rule memorized the training data. Record both `in_sample_result` and `out_of_sample_result`
as `{ n, lift_vs_base_rate }`. If out-of-sample lift collapses toward zero, the in-sample
result was overfitting.

Reuse: `referenced-prompts/domain-reasoning-craft/forecasting/forecasting_signal_vs_noise_filter.md` to judge
whether the holdout result is signal or noise.

## 4. Account for multiple comparisons

If you screened many features to find this one, "significant" results appear by chance. Record
the number screened in `multiple_comparisons_note` and raise the evidence bar accordingly
(roughly: the more you tested, the larger the out-of-sample lift and sample size you should
demand). A single pre-registered hypothesis that survives is worth far more than the best of
hundreds of mined features.

Reuse: `referenced-prompts/domain-finance/quant-fintech-data/finance_backtest_design_critique.md` to stress-test
the design for snooping, survivorship, and look-ahead.

## 5. Estimate decay and capacity

- **Decay:** does the edge fade over time or only exist in certain regimes? Record a
  `decay_estimate` (half-life / regime sensitivity) and a `last_reviewed` cadence.
- **Capacity:** does the edge survive realistic position size, liquidity, and transaction
  costs? An edge that vanishes after costs or cannot absorb size is **not** validated.
  This matters most for microcaps and thin tokens.

Reuse: `referenced-prompts/domain-finance/quant-fintech-data/finance_alt_data_thesis_evaluator.md` for
data-quality / capacity scrutiny.

## 6. Assign status

- `out_of_sample_result.n` ≥ configured minimum AND `lift_vs_base_rate > 0` → `validated`.
- Otherwise → stays `hypothesis` (paper-only signal; cannot drive sizing).
- Re-test fails, or edge decays below base rate, or capacity kills it → `retired` (dated reason).

## Gate A checklist (every promotion must pass all)

- [ ] `registered_on` predates outcome inspection (or a fresh untouched holdout is used)
- [ ] Train/holdout split is genuinely disjoint (time-split, no leakage)
- [ ] Base rate is explicit and the pattern beats it **out-of-sample**
- [ ] `out_of_sample_result.n` ≥ configured minimum sample size
- [ ] Multiple-comparisons count recorded and the bar raised to match
- [ ] Decay and capacity estimated; edge survives realistic costs/size
- [ ] `status` and `knowledge-base/INDEX.md` updated consistently

## The four failure modes this prevents

| Failure | What it looks like | The guard above |
|---|---|---|
| Overfitting | Great in-sample, dead out-of-sample | Steps 2–3 (holdout, OOS base rate) |
| Survivorship bias | Sample silently excludes failures/delistings | Step 1 sample_frame + Step 4 critique |
| Look-ahead bias | Uses data not knowable at decision time | Step 2 time-split + point-in-time snapshots |
| Data-snooping | Best of hundreds of mined features | Step 1 pre-registration + Step 4 multiple comparisons |
