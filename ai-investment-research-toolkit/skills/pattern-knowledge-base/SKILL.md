---
name: pattern-knowledge-base
description: Create, validate, promote, and retire pattern records that capture features historically associated with investment success or failure — while enforcing the anti-overfitting discipline (Gate A). Use this skill for "register a trading/investing pattern", "is this signal real or overfit", "promote a pattern to validated", "out-of-sample test a pattern", or maintaining the durable pattern knowledge base. Enforces pre-registration, out-of-sample validation, base-rate anchoring, and minimum sample size before any pattern can drive a decision.
license: MIT
compatibility: Standard library only (records are markdown + YAML frontmatter you edit directly). scripts/validate_pattern.py is implemented and enforces Gate A in code; it uses PyYAML if installed, else an embedded YAML-subset parser, so it runs with no dependencies. `--self-check` proves the Gate A cases.
metadata:
  tags: [investing, pattern, knowledge-base, overfitting, out-of-sample, base-rate, calibration, gate-a]
  updated: "2026-06-18"
---

# Pattern Knowledge Base

Creates and curates the toolkit's durable memory of patterns — features that have
historically preceded success or failure — and enforces the discipline that keeps the
knowledge base honest. This is the heart of the system **and its danger zone**:
"find the details that predict winners" is exactly where overfitting, survivorship
bias, look-ahead bias, and data-snooping live.

## Purpose

A pattern is only useful if its edge is real out-of-sample. This skill makes the
discipline structural: a pattern cannot be promoted to `validated` (and thus cannot
influence screening or sizing) until it has passed an out-of-sample test on a minimum
sample size, beating its base rate. Everything else stays a `hypothesis` — visible,
but unable to drive a decision (Gate A).

## When to Use This Skill

Use this skill when you need to:
- Register a new candidate pattern as a falsifiable hypothesis (before inspecting outcomes)
- Decide whether a signal is a real edge or an artifact of overfitting / multiple comparisons
- Promote a pattern from `hypothesis` to `validated`, or retire a decayed one
- Maintain `knowledge-base/INDEX.md` and the `PATTERN-*.md` records

## When NOT to Use This Skill

Do NOT use this skill when:
- You are logging or scoring a specific prediction → use `prediction-journal`
- You are building a per-asset research dossier → that is Stage 2
- You want a quick opinion on a stock with no record-keeping discipline (this skill exists *because* that is how people fool themselves)

## Prerequisites

- Read/write access to `knowledge-base/patterns/` and `knowledge-base/INDEX.md`
- The minimum out-of-sample sample size for Gate A (set in your mandate/config)
- Historical data partitioned so a holdout exists that the pattern was NOT derived from

## Quick Start

### Step 1: Register the hypothesis FIRST (before looking at outcomes)

**Purpose:** Pre-commit the claim so you cannot tell a post-hoc story.

1. Copy `knowledge-base/patterns/PATTERN-TEMPLATE.md` to `PATTERN-<id>.md`.
2. Fill `hypothesis`, `feature_definition` (precise, reproducible), `sample_frame`,
   `base_rate`, and `registered_on`. Set `status: hypothesis`, `confidence: low`.

**Validation:**
- [ ] `registered_on` is set *before* any outcome inspection
- [ ] `feature_definition` is unambiguous enough to recompute identically
- [ ] `base_rate` is the outcome frequency in the sample frame **without** the signal

### Step 2: Test in-sample, then OUT-of-sample

**Purpose:** Separate "fits the past" from "predicts the future."

1. Measure lift vs. base rate on the training sample → record `in_sample_result`.
2. Test on the holdout the pattern was NOT derived from → record `out_of_sample_result`.
3. Note `multiple_comparisons_note` (how many features you screened to find this).

**Validation:**
- [ ] Holdout is genuinely disjoint from the derivation sample (no leakage)
- [ ] `out_of_sample_result.n` and `lift_vs_base_rate` are both recorded

### Step 3: Apply Gate A — promote, hold, or retire

**Purpose:** Only real, durable edges earn the right to drive decisions.

- Promote to `status: validated` ONLY if `out_of_sample_result.n` ≥ the configured
  minimum AND out-of-sample lift is positive. Otherwise keep `status: hypothesis`.
- Add `decay_estimate` and `capacity_note` (does it survive size, liquidity, costs?).
- Move to `status: retired` (with a dated reason) if a re-test fails or the edge decays
  below the base rate.
- Update `knowledge-base/INDEX.md`.

```bash
# Implemented: returns PASS/FAIL and lists every unmet Gate A condition (never mutates).
python scripts/validate_pattern.py ../../knowledge-base/patterns/PATTERN-0001.md
python scripts/validate_pattern.py --self-check     # prove the Gate A cases

# Stage 4: rank a universe with Gate A enforced — only validated patterns score; hypotheses
# are emitted as unscored "paper-only signal" and can never move the rank.
python scripts/screen_rank.py --firings firings.json \
  --patterns-dir ../../knowledge-base/patterns --out ../../data/output/watchlist.csv
python scripts/screen_rank.py --self-check

# Reconcile INDEX.md against the PATTERN-*.md records (catches memory drift, F18).
python scripts/validate_pattern.py --reconcile ../../knowledge-base/patterns \
  --index ../../knowledge-base/INDEX.md
```

`validate_pattern.py` also emits non-blocking advisory warnings (`! advisory:`) — a high
multiple-comparisons count, and a `sample_frame` missing point-in-time / survivorship
language. These DO NOT change PASS/FAIL: a PASS still means "eligible," not "audited clean."

**Validation:**
- [ ] No pattern is `validated` on in-sample evidence alone
- [ ] `--reconcile` shows no drift between `INDEX.md` and the records
- [ ] `INDEX.md` status matches the record
- [ ] In `screen_rank`, a `hypothesis`/`retired` firing contributes 0 to the score (paper-only signal)

## Common Issues

### Issue: The signal looks amazing in-sample but you screened 200 features
That is multiple comparisons. The more features tested, the more "significant" ones
appear by chance. Record the count in `multiple_comparisons_note` and raise the bar:
demand stronger out-of-sample lift before promoting.

### Issue: The pattern used data that wasn't available at decision time
Look-ahead bias. Re-derive using only point-in-time data (Stage 1 snapshots are
timestamped for exactly this reason) and re-test.

### Issue: Edge is real but vanishes after costs / can't take size
Capacity failure. Keep it `hypothesis` (or retire it) and note it in `capacity_note`;
an edge you can't realistically harvest is not a `validated` pattern.

## Safety & Constraints

**NEVER:**
- Promote a pattern to `validated` without an out-of-sample test at or above the minimum sample size
- Inspect outcomes before `registered_on` is set (that is how hypotheses become post-hoc stories)
- Let a `hypothesis` pattern contribute to position sizing (it may appear as a paper-only signal only)
- Invent results, sample sizes, or base rates — leave fields blank and queue the work instead

**ALWAYS:**
- Anchor lift to an explicit base rate, never to a gut feel
- Record how many features were screened (multiple comparisons)
- Re-review `validated` patterns on a cadence for decay; retire honestly

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/pattern_schema.md` | Field-by-field schema + `hypothesis → validated → retired` lifecycle |
| `references/validation_discipline.md` | Gate A method: pre-registration, holdout, base rates, multiple comparisons, decay, capacity |
| `scripts/validate_pattern.py` | Automated Gate A checker — returns PASS/FAIL + unmet conditions; `--reconcile <dir> --index INDEX.md` catches INDEX↔record drift (F18); emits non-blocking `! advisory:` warnings (multiple-comparisons count, missing point-in-time/survivorship language); `--self-check` proves the cases |
| `scripts/screen_rank.py` | Stage 4 screener: enforces Gate A at ranking time — runs each fired pattern through `validate_pattern`, counts only `validated` ones (confidence-weighted) toward the score, and emits `hypothesis`/`retired` firings as unscored "paper-only signal"; writes `watchlist.csv`; `--self-check` |

## Related Skills

- `prediction-journal` — log predictions and Brier-score them; resolved outcomes feed pattern validation/retirement here.

## Reused repo prompts (referenced by path)

- `referenced-prompts/domain-finance/quant-fintech-data/finance_backtest_design_critique.md`
- `referenced-prompts/domain-finance/quant-fintech-data/finance_alt_data_thesis_evaluator.md`
- `referenced-prompts/domain-reasoning-craft/forecasting/forecasting_base_rate_establishment.md`
- `referenced-prompts/domain-reasoning-craft/forecasting/forecasting_signal_vs_noise_filter.md`
