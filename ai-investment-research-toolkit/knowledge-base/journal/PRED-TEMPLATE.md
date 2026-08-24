---
id: PRED-0000
date_opened: "YYYY-MM-DD"
asset: "TICKER"
direction: long            # long | short | neutral
probability: 0.50          # stated UP FRONT, 0-1, used for Brier scoring
thesis_ref: "data/output/dossiers/TICKER.md"   # the reasoning this tests
patterns_fired: []         # PATTERN-* ids this prediction is testing
horizon: "90 days"         # when this resolves
lock_hash: ""              # set ONCE at open by journal_integrity.py --stamp (tamper-evidence)
tripwires: []              # e.g. ["thesis-break: insiders sell", "stop at -15%"]
resolution: null           # at horizon: { outcome: hit|miss, realized_return: 0.0, resolved_on: "YYYY-MM-DD" }
brier_component: null       # (probability - outcome)^2, computed at resolution
notes: ""
---

## Notes

Copy this file to `PRED-<id>.md` at the moment you open a prediction, then run
`journal_integrity.py --stamp PRED-<id>.md` to write the `lock_hash`. The
`probability` is recorded BEFORE the outcome is known and is never edited after —
that is what makes Brier scoring honest, and the `lock_hash` makes any later edit
to a locked field (id / date_opened / asset / direction / probability / horizon)
tamper-evident (FAILURE_MODES.md F12). At the horizon, fill `resolution` with the
`outcome`, `realized_return`, and a `resolved_on` date at/after the horizon end
(no early or provenance-free resolutions — F13), compute `brier_component`, update
the running calibration report, and write the outcome back to every linked
`PATTERN-*` so Stage 3 can move it toward `validated` or `retired`. `score_brier.py`
runs `journal_integrity.py verify` and will not report Gate C `unlock_ready` on a
tampered or unverifiable journal. (Managed by the `prediction-journal` skill and
the Stage 7 prompt.)
