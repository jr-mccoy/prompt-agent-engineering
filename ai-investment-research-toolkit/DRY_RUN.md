# Paper Dry-Run — proving the gates end-to-end

*For informational and research purposes only. Not financial, investment, or tax advice.
Nothing here places real-money trades.*

**Status (Phase 6).** The four skill scripts are now executable (stdlib-first; PyYAML used
only if already installed). This document traces one candidate — microcap `EXMP` — through the
loop on **sample fixtures**, mirroring [`ARCHITECTURE.md` §12](ARCHITECTURE.md), and shows each
gate firing in code. Every command below was run as-is; the output is copied verbatim.

The fixtures live in [`samples/`](samples/) (tracked, clearly marked as fixtures — not a real
edge): two pattern records, four prediction records (three resolved + one open), and one
point-in-time price file. Nothing here touches a broker; the only execution path is the
in-process paper simulator.

## Run everything at once

```bash
# From the toolkit root:
python -m unittest discover -s tests -v          # 20 gate tests (Phase 6 + Phase 7)
python skills/pattern-knowledge-base/scripts/validate_pattern.py --self-check
python skills/prediction-journal/scripts/score_brier.py --self-check
python skills/paper-trade-executor/scripts/brokers.py --self-check
python skills/data-source-adapter/scripts/adapters.py --self-check
python skills/data-source-adapter/scripts/build_snapshot.py --self-check   # Phase 7
python skills/pattern-knowledge-base/scripts/screen_rank.py --self-check    # Phase 7
```

All report PASS / OK. The per-stage walkthrough below shows what each proves; the
[Phase 7 section](#phase-7--the-same-gates-now-wired-end-to-end) shows the loop wired end-to-end.

---

## Stage 1 — point-in-time data (manual-only, no API)

The price for `EXMP` is read from `samples/input/prices/EXMP_2026-06-18.json`. The `pe_ratio`
field is `null` in the file, so it comes back **queued as `UNAVAILABLE`** — never guessed.

```bash
python skills/data-source-adapter/scripts/adapters.py \
  --seam MarketDataAdapter --key EXMP --as-of 2026-06-18 --manual samples/input
```
```
close_usd: 5.0 | unavailable: ['pe_ratio'] | source: manual_input:EXMP_2026-06-18.json
```

(The adapter also rejects any row/record dated after the `as_of` — look-ahead prevention,
covered by `--self-check` and `tests/`.)

## Stage 3 — Gate A (pattern validation)

`PATTERN-0007` (insider cluster-buying) has **in-sample lift only** — no out-of-sample test.
Gate A **blocks** it: it stays `hypothesis` and cannot drive screening or sizing.

```bash
python skills/pattern-knowledge-base/scripts/validate_pattern.py samples/patterns/PATTERN-0007.md
```
```
RESULT: FAIL
  record_status: hypothesis
  eligible_for_validated: False
  - status is 'hypothesis', not 'validated' (only 'validated' patterns may drive screening / sizing — Gate A)
  - out_of_sample_result.n (0) < min_sample_size (30)
  - out_of_sample_result.lift_vs_base_rate (None) not > 0
```

`PATTERN-0001` passed an out-of-sample test on a disjoint holdout (`n = 42 ≥ 30`, lift `+0.11`),
so it may hold `status: validated` and feed Stage 4 scores:

```bash
python skills/pattern-knowledge-base/scripts/validate_pattern.py samples/patterns/PATTERN-0001.md
```
```
RESULT: PASS
  record_status: validated
  eligible_for_validated: True
```

## Stage 6 — Gate B (order safety), kill switch, Gate C

All orders carry the tracked config via `--config config`. A compliant equity buy
(100 × $5 = $500 = 1% of the $50k paper account) **fills** and updates the ledger:

```bash
python skills/paper-trade-executor/scripts/brokers.py \
  --symbol EXMP --asset-class equity --quantity 100 --price 5 --stop 4.25 \
  --sizing-ref data/output/orders/2026-06-18.md#sizing \
  --premortem-ref data/output/orders/2026-06-18.md#premortem \
  --config config --portfolio /tmp/dryrun_portfolio.json
```
```
fill: FILLED | cash: 49500.0 | EXMP qty: 100.0
```

An order that would push the **cumulative** position past the 2% per-position cap is **REJECTED**
(the prior 100 shares + a new 500 = 600 × $5 = $3,000 = 6% of capital):

```bash
python skills/paper-trade-executor/scripts/brokers.py \
  --symbol EXMP --asset-class equity --quantity 500 --price 5 --stop 4.25 \
  --sizing-ref ...#sizing --premortem-ref ...#premortem \
  --config config --portfolio /tmp/dryrun_portfolio.json --no-save
```
```
fill: REJECTED
  reason: per-position cap: 0.0600 of capital > limit 0.0200 for EXMP (equity)
```

An order missing the Gate B discipline artifacts (no stop, no sizing, no pre-mortem) is
**REJECTED** with every breach named — none silently filled:

```
fill: REJECTED
  reason: require_stop_loss: order has no stop / exit trigger
  reason: reject_if_unsized: no position-sizing output attached (sizing_ref empty)
  reason: reject_if_no_premortem: no pre-mortem attached (premortem_ref empty)
```

The **kill switch** (`--halt`, i.e. `mandate.yaml: halt: true`) stops the order before any
sizing logic — `HALTED`, portfolio untouched:

```
fill: HALTED | reasons: ['kill switch engaged (mandate.yaml halt: true) — action stages stopped']
```

**Gate C** keeps real money unreachable. `LiveBrokerAdapter.place_order` raises, and the status
helper reports all three unlock conditions unmet:

```
place_order -> NotImplementedError (real money OFF by design)
gate_c_status ready: False
  unmet: resolved predictions 3 < 100
  unmet: Brier 0.2915 not at/below 0.18
  unmet: live_enabled is false (manual switch not flipped)
```

## Stage 7 — calibration (closing the loop)

The scorer summarizes the journal. The open prediction (`PRED-0045`, `resolution: null`) is
**excluded** — three resolved records score to a running Brier of **0.2915** (matching
`brier_method.md`), nowhere near the Gate C target:

```bash
python skills/prediction-journal/scripts/score_brier.py --calibration-report samples/journal/
```
```
Resolved predictions: 3
Running Brier: 0.2915

Calibration (stated p vs realized hit rate):
  bucket        n   mean_p   hit_rate   gap
  0.0-0.2     0      -        -        -
  0.2-0.4     1   0.300    0.000    -0.300
  0.4-0.6     0      -        -        -
  0.6-0.8     1   0.620    1.000    +0.380
  0.8-1.0     1   0.800    0.000    -0.800

Gate C progress: 3/100 resolved (count not met); Brier 0.2915 vs <= 0.18 (not met). Unlock-ready: False (still requires manual live_enabled — Gate C).
```

---

## Phase 7 — the same gates, now wired end-to-end

Phase 7 wired the stage prompts/commands/orchestrator to the scripts and added the executable
glue the stages lacked. The one-candidate flow below runs the `/investment-run` path on the same
fixtures, with each gate firing in the wired script — not by hand.

**Stage 1 — `build_snapshot.py` writes the immutable, look-ahead-safe universe.** It reads `EXMP`
point-in-time, applies the active equity filters, and queues `pe_ratio` (null in the fixture):

```bash
python skills/data-source-adapter/scripts/build_snapshot.py \
  --as-of 2026-06-18 --manual samples/input --out /tmp/snap
```
```
included: 1 | candidates_priced: 1 | queued_unavailable: 1 | skipped: []
universe.csv:
symbol,asset_class,as_of,close_usd,high_usd,low_usd,market_cap_usd,open_usd,volume,unavailable,source,filter_notes
EXMP,equity,2026-06-18,5.0,5.08,4.88,280000000,4.92,612000,pe_ratio,manual_input:EXMP_2026-06-18.json,
```

A second build on the same `as_of` is **REFUSED** (exit 2) — snapshots are immutable; a candidate
with only a future-dated record is **skipped**, never back-filled (look-ahead-safe).

**Stage 4 — `screen_rank.py` enforces Gate A at ranking time.** `EXMP` fires the `validated`
`PATTERN-0001` (medium confidence → weight 2) and the `hypothesis` `PATTERN-0007`. Only the
validated one scores; the hypothesis is an **unscored "paper-only signal"** and cannot move the rank:

```bash
python skills/pattern-knowledge-base/scripts/screen_rank.py \
  --firings samples/firings/EXMP_2026-06-18.json --patterns-dir samples/patterns
```
```
rank 1 EXMP score 2
  scored: [('PATTERN-0001', 'medium', 2)]
  paper-only (unscored): [('PATTERN-0007', 'hypothesis')]
```

**Stage 6 — `brokers.py` (Gate B + kill switch) then the read-only exposure report.** The compliant
buy FILLs (as in Stage 6 above); `--report` shows exposure against the caps without touching the ledger:

```bash
python skills/paper-trade-executor/scripts/brokers.py --report \
  --config config --portfolio data/output/portfolio.json
```
```
deployed: 0.01 within True | EXMP pos: 0.01 within True
```

The wired path changes nothing about the gates' behavior — Gate A still blocks `PATTERN-0007`, Gate B
still REJECTS/HALTS, Gate C still keeps the live adapter unreachable. `tests/test_gates.py` now runs
**20** cases (the six Phase-6 invariants plus snapshot immutability/look-ahead, Gate-A-at-rank, and the
exposure-report math). Run them with `python -m unittest discover -s tests`.

## What this proves

| Gate / invariant | Where it fired | Result |
|---|---|---|
| **Gate A** — pattern validation | `validate_pattern.py` on `PATTERN-0007` vs `PATTERN-0001` | hypothesis BLOCKED; validated PASSES |
| **Gate B** — order safety | `brokers.py` over-cap / unsized / no-stop / no-premortem | REJECTED with reasons; compliant FILLED |
| **Kill switch** | `brokers.py --halt` | HALTED, no fill, portfolio untouched |
| **Gate C** — real-money lock | `LiveBrokerAdapter.place_order` | `NotImplementedError` — unreachable |
| **No fabrication** | adapter `UNAVAILABLE`; scorer ignores unresolved | missing data queued, not guessed |

Gates and the kill switch are enforced **as code, not by trust**. The live broker adapter stays
a disabled stub (ARCHITECTURE §13 step 7 — deferred behind Gate C); there is no real-money path
in this build.
