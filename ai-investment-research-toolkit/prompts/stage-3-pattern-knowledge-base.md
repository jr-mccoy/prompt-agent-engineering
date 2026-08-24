---
title: "Stage 3 — Pattern Discovery & Knowledge Base (Gate A: anti-overfitting discipline)"
category: investment-research/pattern-knowledge-base
description: "Discover and store features historically associated with investment success or failure without fooling yourself: register hypotheses before inspecting outcomes, test out-of-sample against base rates, account for multiple comparisons, estimate decay and capacity, and assign hypothesis/validated/retired status under Gate A."
techniques:
  - QA-02
  - QA-04
  - QA-05
  - CM-02
  - DS-02
  - NE-10
  - NE-11
difficulty: advanced
tags:
  - pattern-discovery
  - overfitting
  - out-of-sample
  - base-rate
  - knowledge-base
  - gate-a
updated: "2026-06-18"
related_prompts:
  - ai-investment-research-toolkit/skills/pattern-knowledge-base/references/validation_discipline.md
  - ai-investment-research-toolkit/prompts/stage-7-journaling-calibration.md
  - referenced-prompts/domain-finance/quant-fintech-data/finance_backtest_design_critique.md
  - referenced-prompts/domain-finance/quant-fintech-data/finance_alt_data_thesis_evaluator.md
  - referenced-prompts/domain-reasoning-craft/forecasting/forecasting_base_rate_establishment.md
  - referenced-prompts/domain-reasoning-craft/forecasting/forecasting_signal_vs_noise_filter.md
---

*For informational and research purposes only. Not financial, investment, or tax advice.
Nothing here places real-money trades. All outputs require independent verification.*

## Objective

Find and store features that have historically preceded investment success or failure, and
do it without self-deception. The output is a set of versioned pattern records, each assigned
a status (`hypothesis` / `validated` / `retired`) under Gate A: a pattern may only become
`validated` — and thus influence screening or sizing — after an out-of-sample test on a
minimum sample size that beats its base rate. This stage is the heart of the system and its
single biggest risk surface; the discipline below is mandatory, not optional.

## When to Use

- Registering a new candidate pattern as a falsifiable hypothesis before inspecting outcomes
- Deciding whether an observed edge is real or an artifact of overfitting / data-snooping
- Promoting a pattern from `hypothesis` to `validated`, or retiring a decayed one
- Re-reviewing the knowledge base on a cadence as resolved predictions arrive from Stage 7

## Inputs / Context Required

**The candidate signal**
- A precise, reproducible `feature_definition` (how the signal is computed, no ambiguity)
- The `sample_frame`: universe + date range the sample is drawn from
- Asset class(es) in scope (equity-microcap / equity / crypto / options)

**Evidence base**
- Point-in-time historical data partitioned into a derivation (train) sample and a disjoint holdout
- The base rate: outcome frequency in the sample frame **absent** the signal
- How many features were screened to surface this one (for multiple-comparisons accounting)
- Resolved outcomes from the prediction journal (Stage 7), where available

**Config**
- The Gate A minimum out-of-sample sample size (from your mandate/config)

## Constraints

### Must
- Register the hypothesis (what, why, expected effect, sample frame, base rate) and set
  `registered_on` **before** inspecting outcomes (QA-02, CM-02).
- Anchor every lift claim to an explicit base rate, and require the pattern to beat it
  **out-of-sample**, not in-sample (QA-04, NE-11).
- Test on a holdout the pattern was not derived from; time-series splits must be by time with
  no leakage across the boundary (QA-05).
- Record how many features were screened and raise the evidence bar for multiple comparisons (QA-05).
- Estimate decay (edge half-life / regime sensitivity) and capacity (survives realistic size,
  liquidity, costs) before promotion (NE-10).
- Assign `status` strictly per Gate A and keep `knowledge-base/INDEX.md` consistent (CM-02).
- **Read the checker's `! advisory:` lines and work the human leakage audit before any promotion**
  (audit §A/§E): `validate_pattern.py` prints non-blocking advisories (high multiple-comparisons count;
  `sample_frame` missing point-in-time/survivorship language). They do not block, but you must run
  `skills/pattern-knowledge-base/references/leakage_and_skepticism_audit.md` (sections A–F) before
  flipping any pattern `hypothesis`→`validated`. Keep `registered_on` honest (no backfilling).

### Must Not
- Promote a pattern to `validated` on in-sample evidence alone, or below the minimum sample size.
- Inspect outcomes before the hypothesis is registered (post-hoc storytelling).
- Let a `hypothesis`-status pattern drive position sizing (it may appear only as an unscored signal).
- Invent base rates, sample sizes, or lift figures — leave fields blank and queue the work (DS-02).
- Present a pattern as an edge without acknowledging decay and capacity limits.

## Instructions

1. **Register the hypothesis first (QA-02, CM-02).** Copy `knowledge-base/patterns/PATTERN-TEMPLATE.md`
   to `PATTERN-<id>.md`. Fill `hypothesis`, `feature_definition`, `sample_frame`, `base_rate`, and
   `registered_on`; set `status: hypothesis`, `confidence: low`. If outcomes were already seen, say so
   and reserve a fresh, untouched holdout.

2. **Establish the base rate (NE-11).** Compute the outcome frequency in the sample frame without the
   signal. This is the bar the pattern must clear. (Reuse `forecasting_base_rate_establishment.md`.)

3. **Measure in-sample lift, then split and test out-of-sample (QA-05).** Record `in_sample_result`
   `{n, lift_vs_base_rate}`. Then test on the disjoint holdout and record `out_of_sample_result`.
   Judge whether the holdout result is signal or noise (reuse `forecasting_signal_vs_noise_filter.md`).

4. **Account for multiple comparisons (QA-05).** Record in `multiple_comparisons_note` how many
   features were screened; the more tested, the larger the out-of-sample lift and sample size required.
   (Reuse `finance_backtest_design_critique.md` to stress-test for snooping, survivorship, look-ahead.)

5. **Estimate decay and capacity (NE-10).** Record `decay_estimate` and `capacity_note`; confirm the
   edge survives realistic size, liquidity, and costs (critical for microcaps and thin tokens). Reuse
   `finance_alt_data_thesis_evaluator.md` for data-quality / capacity scrutiny.

6. **Apply Gate A and assign status (CM-02).** `validated` only if `out_of_sample_result.n` ≥ the
   configured minimum AND out-of-sample `lift_vs_base_rate > 0`; otherwise stays `hypothesis`. Retire
   (with a dated reason) any pattern whose edge has decayed below the base rate or failed re-test.
   **Run the checker — Gate A is enforced in code, not by eye:**

   ```bash
   # PASS/FAIL + every unmet condition; it reports, never mutates — promotion stays your call.
   python skills/pattern-knowledge-base/scripts/validate_pattern.py knowledge-base/patterns/PATTERN-<id>.md
   # exit 0 = PASS (eligible to hold status: validated), 1 = FAIL. Prove the cases: --self-check
   ```

   Do not set `status: validated` on a record the checker FAILs. Read any `! advisory:` lines the
   checker prints (non-blocking) and, before flipping `hypothesis`→`validated`, work the human audit
   `skills/pattern-knowledge-base/references/leakage_and_skepticism_audit.md` (sections A–F).

7. **Update and reconcile the index.** Sync the row in `knowledge-base/INDEX.md` (status, confidence,
   last_reviewed), then reconcile record-vs-index in code so Stage 4 is never blocked:

   ```bash
   python skills/pattern-knowledge-base/scripts/validate_pattern.py \
     --reconcile knowledge-base/patterns --index knowledge-base/INDEX.md
   ```

## Output Format

```
## PATTERN REVIEW: PATTERN-<id> — [title] | As of [date] | Gate A: [PASS / HOLD / RETIRE]
```

### Registration (pre-commitment)
| Field | Value |
|---|---|
| Hypothesis | … |
| Feature definition | … |
| Sample frame | … |
| Registered on | [date — before outcome inspection?] [yes/no] |

### Base rate & lift
| Measure | In-sample | Out-of-sample |
|---|---|---|
| n | … | … |
| Base rate | … | … |
| Lift vs. base rate | … | … |

### Discipline checks
| Check | Finding |
|---|---|
| Multiple comparisons (features screened) | … |
| Look-ahead / leakage | … |
| Survivorship | … |
| Decay estimate | … |
| Capacity (size/liquidity/cost) | … |

### Gate A verdict
**[VALIDATED / STAYS HYPOTHESIS / RETIRED]** — [reason citing the out-of-sample n, lift vs. base
rate, and the minimum sample size]. New `status`: `[…]`. `confidence`: `[low/medium/high]`.

### Knowledge-base updates
- Record written/updated: `knowledge-base/patterns/PATTERN-<id>.md`
- INDEX.md row updated: [yes/no]
- Queued for retrieval (not guessed): [list any blank fields awaiting data]

## Verification

- [ ] `registered_on` predates outcome inspection (or a fresh untouched holdout was used).
- [ ] An explicit base rate is stated and the pattern beats it **out-of-sample**.
- [ ] The holdout is genuinely disjoint from the derivation sample (time-split, no leakage).
- [ ] `out_of_sample_result.n` ≥ the configured minimum before any `validated` status.
- [ ] Number of features screened is recorded and the bar raised accordingly.
- [ ] Decay and capacity are estimated; the edge survives realistic costs/size.
- [ ] `status` and `knowledge-base/INDEX.md` agree; `--reconcile` PASSes.
- [ ] Checker advisories read; §A–F leakage audit worked before any hypothesis→validated flip.
- [ ] No invented figures; blanks are queued, not guessed.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Great in-sample result presented as an edge | Require out-of-sample lift over base rate at ≥ minimum sample size before `validated` |
| Post-hoc story dressed up as a hypothesis | `registered_on` must predate outcome inspection; otherwise use a fresh holdout |
| Best of hundreds of mined features looks "significant" | Record features-screened count; raise the OOS bar for multiple comparisons |
| Pattern uses data not knowable at decision time | Time-split + point-in-time snapshots; check Layer for look-ahead leakage |
| Sample silently excludes failures/delistings | State `sample_frame` explicitly; run survivorship critique |
| Edge that vanishes after costs or can't take size | Mandatory capacity note; an unharvestable edge is not `validated` |
| Hypothesis pattern sneaks into position sizing | Only `validated` patterns score in Stage 4; hypotheses are unscored signals |
