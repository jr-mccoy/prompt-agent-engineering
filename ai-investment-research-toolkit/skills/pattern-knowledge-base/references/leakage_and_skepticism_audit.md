*For informational and research purposes only. Not financial, investment, or tax advice.*

# Leakage & Result-Skepticism Audit — Stage 3 Pattern Discipline

Companion to `validation_discipline.md`. That doc defines Gate A (the *gate*); this doc is
the **adversarial audit** you run before trusting a pattern's lift — interrogating the
*data* (leakage families) and the *result* (is the lift real or noise) the way you'd
interrogate a too-good-to-be-true ML eval.

**Core stance:** `validate_pattern.py` enforces *arithmetic and presence* (is OOS `n` ≥
min, is OOS lift > 0, are `registered_on` / `base_rate` filled, is the schema valid). It
**cannot** verify *substance*: that the holdout is genuinely disjoint, that no future data
leaked, that the sample isn't survivorship-pruned, or that the lift survives the
multiple-comparisons count. Those are free-text / human-trust fields. **A PASS from the
checker means "eligible," not "clean."** This audit is what makes it clean.

Run this audit before flipping `status: hypothesis → validated`, and re-run it on cadence
for any `validated` pattern whose `linked_predictions` have newly resolved.

---

## How to read each check

For each check: **Inspect** (which `PATTERN-*.md` field / artifact) → **Red flag** → **Remediation**.

---

## A. Temporal leakage (look-ahead) — the snapshot is the defense; verify it held

The toolkit's intended defense is point-in-time `data/snapshots/<date>/` (ARCHITECTURE §2,
§4 Stage 1, §13 `build_snapshot.py`): every signal must be computable from data dated **at
or before** the decision date. Verify it actually held — the snapshot only prevents
look-ahead if the pattern was *derived from it*, not re-pulled live.

| # | Inspect | Red flag | Remediation |
|---|---|---|---|
| A1 | `feature_definition` | Uses any value that is only knowable *after* the decision date (restated fundamentals, period-end aggregates, "next-quarter" figures, as-of-today index membership). | Re-express the feature strictly from data observable at the snapshot date; re-derive and re-test. |
| A2 | `sample_frame` + the snapshot folder it cites | Sample was built from a *live* pull or a single recent snapshot, not dated point-in-time snapshots — so historical rows silently carry today's data. | Rebuild the sample from `data/snapshots/<date>/` per as-of date; never backfill a snapshot. |
| A3 | `out_of_sample_result` split boundary (notes body) | Holdout is split *randomly* over a time-ordered process; no embargo around the train/holdout boundary, so a feature with a multi-day window straddles the line. | Split by time; embargo a gap ≥ the longest feature/label window around the boundary (`validation_discipline.md` §2). |
| A4 | `feature_definition` label horizon vs. `registered_on` | Outcome window (e.g. "60-day forward return") overlaps the period the feature is measured on — the label bleeds into the feature. | Define feature measurement to end strictly before the outcome window opens. |

> Code gap: `validate_pattern.py` never reads the snapshot folder, the split boundary, or
> feature timing. A1–A4 are **un-enforced by code** — they live only in this audit.

---

## B. Target leakage — is the signal a disguised function of the outcome?

| # | Inspect | Red flag | Remediation |
|---|---|---|---|
| B1 | `feature_definition` | The feature is a proxy for, or partially computed from, the outcome itself (e.g. "stock was acquired" used to predict acquisition; trailing return that includes the scoring window). | Drop or recompute the feature using only pre-outcome inputs; re-test. |
| B2 | `base_rate` provenance | Base rate was computed on the *same* rows used to measure lift, or conditioned on the outcome — so "lift over base rate" is circular. | Compute `base_rate` on the sample frame **absent the signal**, independent of the lift measurement (schema rule for `base_rate`). |
| B3 | A single dominant sub-signal | One component of the feature collapses the result if removed — interrogate it as a likely post-outcome proxy. | Ablate the component; if lift collapses to ~base rate, that component was the leak, not an edge. |

---

## C. Train/holdout contamination — is the holdout truly out-of-sample?

This is the financial analogue of the ML "eval ran on training rows" bug. Gate A's whole
promise (`out_of_sample_result`) is void if the holdout overlaps the derivation sample.

| # | Inspect | Red flag | Remediation |
|---|---|---|---|
| C1 | `in_sample_result` vs `out_of_sample_result` | OOS lift ≈ in-sample lift on a noisy financial signal — suspiciously *too* consistent; suggests the "holdout" overlaps train. | Confirm row-level disjointness; expect some OOS shrinkage. No shrinkage at all is itself a red flag. |
| C2 | `sample_frame` + holdout definition | Same issuer/ticker (or same parent entity across share classes, ADRs, tickers post-rename) appears in both train and holdout. | Group-split by issuer, not by row — all of an entity's history sits on one side of the line. |
| C3 | Tuning history (notes body) | Thresholds/parameters were tuned by repeatedly checking the *holdout* — the holdout has become a second training set. | Reserve a *fresh, untouched* holdout (per `validation_discipline.md` §1); the touched one is now in-sample. |
| C4 | Normalization / ranking features | Cross-sectional z-scores, percentile ranks, or universe-relative features computed over the *full* period including holdout dates. | Compute any cross-sectional transform within each as-of snapshot only — never pooled across train+holdout. |

---

## D. Survivorship bias — does the sample silently exclude the failures?

| # | Inspect | Red flag | Remediation |
|---|---|---|---|
| D1 | `sample_frame` | Universe is "currently listed" / "current index members" — delisted, bankrupt, acquired, or merged names are absent, so the worst outcomes were deleted before measurement. | State the universe as point-in-time membership including names that later died; rebuild from dated snapshots. |
| D2 | `base_rate` | Base rate is computed over survivors only, understating the true failure frequency and inflating apparent lift. | Recompute base rate over the full point-in-time population (survivors + casualties). |
| D3 | `capacity_note` + microcap/thin-token scope | Sample excludes names that were untradeable / illiquid at the time but are now liquid (or vice versa) — common in equity-microcap and crypto. | Restrict to names that were actually in-scope and tradeable at each as-of date. |

> Code gap: `validate_pattern.py` does not parse `sample_frame` for survivorship language.
> D1–D3 are **un-enforced by code**.

---

## E. Multiple-comparisons inflation — is "significant" just the best of many?

| # | Inspect | Red flag | Remediation |
|---|---|---|---|
| E1 | `multiple_comparisons_note` | Field says "screened 200 features," "swept many thresholds," "tried several windows" — yet the OOS bar used is the same minimum as a single pre-registered hypothesis. | Raise the required OOS lift / `n` with the count tested; a pattern mined from hundreds needs far stronger OOS evidence than one pre-registered (`validation_discipline.md` §4). |
| E2 | `multiple_comparisons_note` is blank or "1" but the notes reveal exploration | Undercounted comparisons — every threshold, window, and universe slice you tried is a comparison, even the ones you discarded. | Honestly count *all* variants explored; record the real number. |
| E3 | `registered_on` vs. the exploration | Hypothesis was "registered" *after* the sweep surfaced the winner — post-hoc story dressed as pre-registration. | Treat as exploratory; demand a fresh untouched holdout the winner never saw. |

> Code gap: `validate_pattern.py` checks only that `multiple_comparisons_note` *exists* as a
> field; it does **not** parse the count or raise the OOS bar accordingly. The bar-raising is
> entirely a human judgment captured in this audit.

---

## F. Brier / lift skepticism — is the edge signal or noise?

The ML-eval reflex: when a number looks good, audit the *measurement*, not just the data.
For patterns the "headline metric" is OOS `lift_vs_base_rate`; downstream, Stage 7 scores
resolved predictions with Brier / calibration (`linked_predictions`).

| # | Inspect | Red flag | Remediation |
|---|---|---|---|
| F1 | `out_of_sample_result.{n, lift_vs_base_rate}` | Lift is positive but `n` is barely over the minimum — the lift is within sampling noise of zero. | Apply `forecasting_signal_vs_noise_filter.md`: estimate the noise band for this `n`; if the lift sits inside it, it stays `hypothesis`. |
| F2 | `out_of_sample_result` vs `base_rate` | Tiny absolute lift over a base rate measured on a different/larger sample — apples-to-oranges denominators manufacture lift. | Measure base rate and OOS outcome on the *same* sample-frame definition. |
| F3 | `linked_predictions` (Stage 7 Brier) | A `validated` pattern's resolved predictions show Brier no better than the base-rate forecast — calibration says the "edge" doesn't pay out live. | Retire (dated reason) per `validation_discipline.md` §6; live calibration overrides historical OOS lift. |
| F4 | `decay_estimate` vs. age of evidence | OOS test is years old; `decay_estimate` says half-life is short; `last_reviewed` is stale — the edge may already be gone. | Re-test on recent snapshots before trusting; refresh `last_reviewed`. |
| F5 | Direction of `lift_vs_base_rate` | Sign convention ambiguity — a "win" that's actually the label/outcome defined backwards (the financial analogue of a flipped positive class). | Confirm the outcome definition and lift sign produce a *tradeable* direction; re-state if inverted. |

---

## Most important gap (read this if nothing else)

`validate_pattern.py` is a **presence-and-arithmetic** gate. It confirms the *fields exist*
and the *numbers clear the threshold*. It cannot confirm the holdout is genuinely disjoint
and time-split (§A3, §C1–C4), that no future data leaked (§A1–A2, §A4), that the sample
isn't survivorship-pruned (§D), or that the multiple-comparisons count justifies the lift
bar (§E). **A checker PASS therefore means "eligible for `validated`," never "audited
clean."** Promotion to `validated` requires a human to run sections A–F and record the
findings in the record's notes body — the gap between PASS and clean is exactly this audit.

(Now implemented as **non-blocking advisories**: `validate_pattern.py` emits a *warning* — not a
gate failure — when `multiple_comparisons_note` parses to a high count without a correspondingly
raised OOS bar, or when `sample_frame` lacks point-in-time / survivorship language. These warnings
flag the record for this audit; they do **not** auto-promote, auto-fail, or auto-correct. The
substance checks (§A–F) stay human — a warning means "run the audit here," never "audited clean.")

---

## One-line verdict format (append to the record notes body)

```
LEAKAGE+SKEPTICISM AUDIT — PATTERN-<id> | <date>
  Temporal (A): [clean / flag …]   Target (B): [clean / flag …]
  Contamination (C): [clean / flag …]   Survivorship (D): [clean / flag …]
  Multiple-comparisons (E): [count=N, bar raised? y/n]   Brier/lift (F): [signal / noise / decayed]
  Verdict: [AUDITED CLEAN → eligible for validated] | [HOLD as hypothesis: <reason>] | [RETIRE: <reason>]
```
