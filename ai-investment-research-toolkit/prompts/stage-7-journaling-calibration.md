---
title: "Stage 7 — Journaling & Calibration (Brier scoring, track record, Gate C)"
category: investment-research/journaling-calibration
description: "Close the loop and keep the system honest: log every prediction with a probability stated before the outcome, score it with the Brier score at its horizon, maintain a running calibration report, and write resolved outcomes back to the pattern knowledge base. Builds the track record that gates real-money unlock (Gate C)."
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
  - journaling
  - calibration
  - brier-score
  - track-record
  - prediction
  - gate-c
updated: "2026-06-18"
related_prompts:
  - ai-investment-research-toolkit/skills/prediction-journal/references/brier_method.md
  - ai-investment-research-toolkit/prompts/stage-3-pattern-knowledge-base.md
  - referenced-prompts/domain-reasoning-craft/forecasting/forecasting_brier_tracker_design.md
  - referenced-prompts/domain-reasoning-craft/forecasting/forecasting_calibration_self_audit.md
  - referenced-prompts/domain-reasoning-craft/forecasting/forecasting_what_would_change_my_mind.md
---

*For informational and research purposes only. Not financial, investment, or tax advice.
Nothing here places real-money trades. All outputs require independent verification.*

## Objective

Make the system honest over time. Every prediction is logged with a probability stated
**before** the outcome is known; at its horizon it is scored with the Brier score; a running
calibration report compares stated probabilities to realized frequencies; and resolved
outcomes are written back to the patterns that drove them, so Stage 3 can validate or retire
them. This recorded track record is what gates real-money unlock (Gate C): ≥100 resolved
predictions and a running Brier ≤ 0.18.

## When to Use

- Logging a new prediction at the moment it is opened (with probability, horizon, tripwires)
- Resolving a prediction at its horizon and computing its Brier component
- Updating the running Brier score and calibration table
- Reporting Gate C progress and feeding resolved outcomes back to Stage 3

## Inputs / Context Required

**The prediction (at open)**
- Asset, direction, and a stated `probability` (0–1) you commit to before the outcome
- `thesis_ref` (the dossier/reasoning), `patterns_fired` (linked `PATTERN-*` ids)
- `horizon` and `tripwires` (thesis-break and stop conditions)

**At resolution**
- The realized outcome (hit/miss) and realized return at the horizon

**Config**
- Gate C thresholds from `config/mandate.yaml` (default: 100 resolved, Brier ≤ 0.18)

## Constraints

### Must
- Record `probability` before the outcome is known and treat it as immutable thereafter (QA-02, CM-02).
- **Tamper-stamp at open (F12/F13):** the instant a prediction is OPENED, stamp its `lock_hash`:
  `python skills/prediction-journal/scripts/journal_integrity.py --stamp knowledge-base/journal/PRED-<id>.md`.
  Never edit a locked field (`id`/`date_opened`/`asset`/`direction`/`probability`/`horizon`) after stamping.
- **Resolve honestly:** fill `resolution` with `outcome`, `realized_return`, and a `resolved_on` date
  at/after the horizon end — no early or provenance-free resolutions.
- **Verify before any Gate C claim (F12/F13):** run
  `python skills/prediction-journal/scripts/journal_integrity.py --verify knowledge-base/journal/`.
  `score_brier.py --calibration-report` reports `integrity` + `gate_c.integrity_clean`; `unlock_ready`
  is False unless integrity-clean. A tampered/unverifiable journal **blocks Gate C**.
- **Egress scan before persisting a PRED file (SECURITY §4d):** run
  `python skills/output-guard/scripts/egress_check.py --scan knowledge-base/journal/PRED-<id>.md`;
  redact any finding before the record is written/committed.
- Compute `brier_component = (probability − outcome)^2`, outcome 1 for hit, 0 for miss (QA-04).
- Recompute the running Brier over **all** resolved predictions, never a favorable subset (QA-05).
- Maintain a calibration table (stated probability vs. realized hit rate by bucket) (NE-11).
- Write each resolved outcome back to every linked `PATTERN-*` so Stage 3 can act on it (CM-02).
- Express the track record with uncertainty: small N means a noisy Brier (NE-10).

### Must Not
- Edit a `probability` after the outcome is known (destroys calibration).
- Edit any locked field (`id`/`date_opened`/`asset`/`direction`/`probability`/`horizon`) after the
  `lock_hash` stamp, or report Gate C progress without a clean `--verify` (a tampered journal blocks Gate C).
- Mark a prediction resolved without recording the real outcome, or invent a resolution (DS-02).
- Set `resolved_on` before the horizon end, or resolve without provenance.
- Treat a small-sample Brier score as a green light for Gate C.
- Hedge every prediction near 0.5 to keep Brier low (the calibration table exposes it).

## Instructions

1. **Log the prediction up front and tamper-stamp it (QA-02, F12/F13).** Copy
   `knowledge-base/journal/PRED-TEMPLATE.md` to `PRED-<id>.md`. Fill `asset`, `direction`,
   `probability`, `thesis_ref`, `patterns_fired`, `horizon`, `tripwires`, `date_opened`. Leave
   `resolution` and `brier_component` null. Define the "what would change my mind" tripwires explicitly
   (reuse `forecasting_what_would_change_my_mind.md`). Then stamp the `lock_hash` — locked fields
   (`id`/`date_opened`/`asset`/`direction`/`probability`/`horizon`) must never be edited after:

   ```bash
   python skills/prediction-journal/scripts/journal_integrity.py --stamp knowledge-base/journal/PRED-<id>.md
   ```

2. **Monitor against tripwires.** Until the horizon, watch the tripwires. If your view genuinely
   changes, do not edit the probability — close this prediction and open a new one with a new id.

3. **Resolve at the horizon (QA-04).** Record `resolution: {outcome, realized_return, resolved_on}`
   with `resolved_on` at/after the horizon end (no early or provenance-free resolutions) and compute
   `brier_component = (probability − outcome)^2` — in code, not by hand:

   ```bash
   python skills/prediction-journal/scripts/score_brier.py --prob 0.62 --outcome 1   # -> 0.1444
   ```

4. **Update the running Brier and calibration table (QA-05, NE-11).** Recompute the mean Brier over all
   resolved predictions; bucket predictions by stated probability and compare to realized hit rate.
   The scorer reads the journal dir, ignores unresolved records, and reports Gate C progress:

   ```bash
   # Verify tamper-evidence first (F12/F13): integrity-clean is a precondition for Gate C unlock.
   python skills/prediction-journal/scripts/journal_integrity.py --verify knowledge-base/journal/
   # Running Brier + calibration buckets + N/100 + Brier-vs-0.18 (open predictions excluded).
   # Now also reports `integrity` + `gate_c.integrity_clean`; `unlock_ready` is False unless clean.
   python skills/prediction-journal/scripts/score_brier.py --calibration-report knowledge-base/journal/
   ```

   Reuse `forecasting_brier_tracker_design.md` and `forecasting_calibration_self_audit.md`.

5. **Write back to Stage 3 (CM-02).** Push the resolved outcome to each linked `PATTERN-*` so it can be
   moved toward `validated` or `retired`; confirm the pattern's `linked_predictions` lists this id.

6. **Report Gate C progress (NE-10).** State `N/100` resolved and the current running Brier vs. the 0.18
   target, with an explicit note that small N makes the score noisy. A tampered or unverifiable journal
   (`gate_c.integrity_clean: false`) blocks Gate C — report LOCKED. Never imply readiness before both
   thresholds are met, the journal is integrity-clean, and the manual `live_enabled` switch is flipped.

## Output Format

```
## JOURNAL UPDATE: [open PRED-<id> / resolve PRED-<id>] | As of [date]
```

### Prediction record
| Field | Value |
|---|---|
| id / asset / direction | … |
| probability (stated up front) | … |
| patterns_fired | … |
| horizon / tripwires | … |
| resolution (if resolved) | outcome=… realized_return=… |
| brier_component | … |

### Running track record
| Metric | Value |
|---|---|
| Resolved predictions (N) | … / 100 |
| Running Brier score | … (target ≤ 0.18) |
| Calibration: overconfident / calibrated / hedging | … |

### Calibration table
| Bucket (stated p) | # | mean stated p | realized hit rate | gap |
|---|---|---|---|---|
| 0.0–0.2 | | | | |
| 0.2–0.4 | | | | |
| 0.4–0.6 | | | | |
| 0.6–0.8 | | | | |
| 0.8–1.0 | | | | |

### Write-back & Gate C
- Patterns updated: [PATTERN-* ids that received this outcome]
- Gate C status: **[LOCKED / progress N/100, Brier X vs 0.18]** — [note on sample-size noise]

## Verification

- [ ] `lock_hash` stamped at open; no locked field (id/date_opened/asset/direction/probability/horizon) edited after.
- [ ] `--verify` clean and `gate_c.integrity_clean: true` before any Gate C progress claim; a tampered journal reports LOCKED.
- [ ] `resolved_on` is at/after the horizon end; no early or provenance-free resolutions.
- [ ] Egress scan run on the PRED file; any finding redacted before persisting (SECURITY §4d).
- [ ] `probability` was recorded before the outcome and never edited after.
- [ ] `brier_component == (probability − outcome)^2` with the correct outcome encoding.
- [ ] Running Brier recomputed over all resolved predictions, not a subset.
- [ ] Calibration table present; hedging-near-0.5 would be visible in it.
- [ ] Each linked `PATTERN-*` received the resolved outcome and lists this `id`.
- [ ] Gate C progress states both N/100 and Brier-vs-0.18, with a sample-size-noise caveat.
- [ ] No invented resolutions; unresolved predictions stay null.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Editing the probability after seeing how it's going | `probability` is immutable post-open; changed view → new prediction id |
| Cherry-picking a favorable subset for the Brier score | Running Brier computed over ALL resolved predictions |
| Small-sample Brier read as a green light | Gate C requires ≥100 resolved AND Brier ≤ 0.18 AND manual enable |
| Hedging every call near 0.5 to look "accurate" | Calibration table exposes poor resolution even when rarely very wrong |
| Marking a prediction resolved on a hunch | Resolution requires the real outcome; otherwise stays null |
| Implying live-trading readiness prematurely | Report is explicit: LOCKED until all three Gate C conditions are met |
| Treating a price move as thesis confirmation | Outcome is scored against the pre-stated probability, not after-the-fact narrative |
