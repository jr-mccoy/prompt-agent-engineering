---
name: prediction-journal
description: Log every investment prediction up front with a stated probability, then score it at its horizon with the Brier score and update a running calibration report. Use this skill for "log a prediction", "score my forecast", "Brier score", "am I calibrated", "track record for going live", or closing the research loop by writing resolved outcomes back to the pattern knowledge base. Makes the system honest over time and gates real-money unlock (Gate C).
license: MIT
compatibility: Standard library only (journal entries are markdown + YAML frontmatter you edit directly). scripts/score_brier.py is implemented — single-prediction Brier, running Brier, calibration buckets, and Gate C progress over a journal dir; it uses PyYAML if installed, else an embedded YAML-subset parser, so it runs with no dependencies. `--self-check` reproduces the worked example.
metadata:
  tags: [investing, prediction, journal, brier, calibration, track-record, gate-c]
  updated: "2026-06-18"
---

# Prediction Journal

Records every prediction the system makes, with a probability stated **before** the
outcome is known, and scores it when it resolves. This is what makes the toolkit honest
over time: calibration is measured, not assumed, and real-money execution stays locked
until the track record earns it (Gate C).

## Purpose

A prediction you can't score teaches you nothing. This skill captures each prediction as
a `PRED-*.md` record with an up-front probability, computes the Brier score at resolution,
maintains a running calibration report (stated probability vs. realized frequency), and
writes resolved outcomes back to the linked patterns so Stage 3 can validate or retire them.

## When to Use This Skill

Use this skill when you need to:
- Log a new prediction with its probability, horizon, and tripwires (at the moment you open it)
- Resolve a prediction at its horizon and compute its Brier component
- Update the running Brier score and calibration report
- Check Gate C progress (≥100 resolved predictions and Brier ≤ 0.18)
- Feed resolved outcomes back to `pattern-knowledge-base`

## When NOT to Use This Skill

Do NOT use this skill when:
- You are creating or validating a *pattern* → use `pattern-knowledge-base`
- You want to change a probability after seeing the outcome (never allowed — that destroys calibration)
- You need a research dossier or a trade memo → those are Stages 2 and 6

## Prerequisites

- Read/write access to `knowledge-base/journal/`
- A probability (0–1) you are willing to commit to before the outcome is known
- The Gate C thresholds from `config/mandate.yaml` (default: 100 resolved, Brier ≤ 0.18)

## Quick Start

### Step 1: Log the prediction UP FRONT

**Purpose:** Capture the probability before the outcome exists — the basis for honest scoring.

1. Copy `knowledge-base/journal/PRED-TEMPLATE.md` to `PRED-<id>.md`.
2. Fill `asset`, `direction`, `probability` (0–1), `thesis_ref`, `patterns_fired`,
   `horizon`, and `tripwires`. Set `date_opened`. Leave `resolution` and `brier_component` null.

**Validation:**
- [ ] `probability` is recorded before any outcome is known
- [ ] `patterns_fired` links the `PATTERN-*` ids this prediction tests
- [ ] `tripwires` and `horizon` are concrete

### Step 2: Resolve at the horizon and score

**Purpose:** Turn a resolved prediction into a Brier component.

1. At `horizon`, fill `resolution: { outcome: hit|miss, realized_return: <r> }`.
2. Compute `brier_component = (probability − outcome)^2`, where outcome is 1 for hit, 0 for miss.

```bash
# Implemented: single-prediction Brier component.
python scripts/score_brier.py --prob 0.62 --outcome 1     # -> 0.1444
python scripts/score_brier.py --self-check                # reproduce the worked example
```

**Validation:**
- [ ] `probability` was NOT edited after the outcome was known
- [ ] `brier_component` equals `(probability − outcome)^2`

### Step 3: Update calibration and write back

**Purpose:** Keep the running track record honest and feed Stage 3.

1. Recompute the running Brier score (mean of all `brier_component`s) and the calibration
   report (bucket predictions by stated probability; compare to realized hit frequency).
2. Write the resolved outcome back to each linked `PATTERN-*` so Stage 3 can move it toward
   `validated` or `retired`.
3. Report Gate C progress: `<N>/100` resolved and current Brier vs. the 0.18 target.

```bash
# Implemented: running Brier + calibration buckets + Gate C progress over a journal dir.
python scripts/score_brier.py --calibration-report ../../knowledge-base/journal/
```

**Validation:**
- [ ] Running Brier score recomputed over ALL resolved predictions
- [ ] Each linked pattern received the resolved outcome

### Step 4: Stamp at open, verify integrity before Gate C

**Purpose:** Make the journal tamper-evident and resolution-honest — a track record you can't quietly rewrite.

1. At OPEN, stamp the record. `journal_integrity.py --stamp PRED-<id>.md` writes a
   `lock_hash` over the immutable open-time fields (`id`, `date_opened`, `asset`,
   `direction`, `probability`, `horizon`). Editing any locked field later is detected as TAMPER.
2. Audit the journal with `--verify <journal_dir>`. It flags (a) tamper — any `lock_hash`
   that no longer matches its locked fields — and (b) resolution honesty: every resolved
   record needs a numeric `realized_return` and a `resolved_on` date at/after the horizon
   end, and every resolved record must carry a `lock_hash`.

```bash
# Implemented: tamper-evidence + resolution-honesty audit.
python scripts/journal_integrity.py --stamp ../../knowledge-base/journal/PRED-0001.md
python scripts/journal_integrity.py --verify ../../knowledge-base/journal/
```

`score_brier.py --calibration-report` folds this in: its output carries `integrity` and
`gate_c.integrity_clean`, and `unlock_ready` is **False unless the journal is integrity-clean**.

**Validation:**
- [ ] Every open prediction was `--stamp`ed (carries a `lock_hash`)
- [ ] `--verify` reports no tamper and no dishonest resolution before relying on Gate C

## Common Issues

### Issue: Tempted to nudge the probability after seeing how it's going
Don't. The whole point is comparing pre-commitment to reality. If your view changes,
*close* the prediction and open a new one with a new id and timestamp; never edit the old probability.

### Issue: Brier looks great but only on a handful of predictions
Small samples are noisy. Gate C requires ≥100 resolved predictions precisely so the Brier
score means something before any capital is at risk.

### Issue: Always predicting ~0.5 to keep Brier low
That is hedging, not calibration. The calibration report (stated vs. realized by bucket)
exposes it: a forecaster who only ever says 50% is never sharp, even if rarely very wrong.

## Safety & Constraints

**NEVER:**
- Edit `probability` after the outcome is known
- Mark a prediction resolved without recording the realized outcome
- Treat a small-sample Brier score as a green light for Gate C
- Invent resolutions — if the outcome isn't in yet, leave it null

**ALWAYS:**
- Record the probability before the outcome exists
- Recompute the running Brier over all resolved predictions, not a favorable subset
- Write resolved outcomes back to the linked patterns

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/journal_schema.md` | Field-by-field prediction-record schema |
| `references/brier_method.md` | Brier scoring + calibration-report method and worked examples |
| `scripts/score_brier.py` | Brier scorer + calibration report + Gate C progress; folds in `integrity` / `gate_c.integrity_clean` (`unlock_ready` is False unless integrity-clean); `--self-check` reproduces the worked example |
| `scripts/journal_integrity.py` | Tamper-evidence + resolution honesty — `--stamp PRED-<id>.md` writes the open-time `lock_hash`; `--verify <journal_dir>` audits tamper + resolution honesty |

## Related Skills

- `pattern-knowledge-base` — resolved predictions here feed pattern validation/retirement (Gate A).

## Reused repo prompts (referenced by path)

- `referenced-prompts/domain-reasoning-craft/forecasting/forecasting_brier_tracker_design.md`
- `referenced-prompts/domain-reasoning-craft/forecasting/forecasting_calibration_self_audit.md`
- `referenced-prompts/domain-reasoning-craft/forecasting/forecasting_what_would_change_my_mind.md`
