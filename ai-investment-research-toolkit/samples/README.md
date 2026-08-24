# samples/ — fixtures for the paper dry-run

*For informational and research purposes only. Not financial, investment, or tax advice.*

These are **fixtures**, not real data and not a real edge. They exist so the
[`DRY_RUN.md`](../DRY_RUN.md) walkthrough and `tests/test_gates.py` can prove the gates
deterministically without any API or hand-pasted data. They are tracked on purpose (unlike
`data/`, which is git-ignored) so the dry-run is reproducible from a clean clone.

| Path | Purpose | Gate it exercises |
|---|---|---|
| `patterns/PATTERN-0007.md` | hypothesis pattern, in-sample lift only (no OOS test) | Gate A **blocks** it |
| `patterns/PATTERN-0001.md` | validated pattern, OOS `n = 42 ≥ 30`, lift `+0.11` | Gate A **passes** it |
| `journal/PRED-0042..0044.md` | three resolved predictions (running Brier 0.2915) | Stage 7 calibration |
| `journal/PRED-0045.md` | one **open** prediction (`resolution: null`) | scorer must ignore it |
| `input/prices/EXMP_2026-06-18.json` | point-in-time price; `pe_ratio: null` | adapter queues `UNAVAILABLE`; `build_snapshot.py` writes the universe |
| `firings/EXMP_2026-06-18.json` | `EXMP` fires PATTERN-0001 (validated) + PATTERN-0007 (hypothesis) | `screen_rank.py` scores the validated one only (Gate A at rank time) |

Do not copy these into `knowledge-base/` — that directory is for your real, durable records.
