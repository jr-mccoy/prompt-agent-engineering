# Pipeline Overview — AI Investment Research Toolkit

*For informational and research purposes only. Not financial, investment, or tax advice.
Nothing here places real-money trades.*

**Build status:** Phases 1–7 are built. Phase 1 (Foundation + memory/honesty layer), Phase 2
(Research + Screen), Phase 3 (Monitor + paper action), Phase 4 (Orchestrator + commands + agents —
§13 step 5), Phase 5 (Stage 0 + index integration — §13 step 6), and **Phase 6 (the loop is now
executable + the gates are proven)**. All **8** stage prompts (**0** Mandate & Config, plus **1–7**)
and their **five** skills (`data-source-adapter`, `pattern-knowledge-base`, `prediction-journal`,
`paper-trade-executor`, `output-guard`) exist; the core skill scripts are now **working stdlib-first Python** —
`validate_pattern.py` enforces Gate A, `score_brier.py` computes Brier + calibration + Gate C
progress, `brokers.py` runs the paper simulator + Gate B + kill switch + `load_config`, and
`adapters.py` does manual-only point-in-time reads + `load_data_sources`. Each ships a
`--self-check`; the test suite (now **35 tests** across `tests/test_gates.py`, `tests/test_injection.py`,
and `tests/test_hardening.py`) and [`DRY_RUN.md`](DRY_RUN.md) prove every gate fires on the
[`samples/`](samples/) fixtures (YAML parsed with PyYAML if present, else an embedded
subset parser, so manual-only mode stays dependency-free). A later hardening pass added the
`output-guard` skill (`egress_check.py --scan`), `journal_integrity.py` (journal tamper-evidence,
folded into `score_brier.py` so Gate C also requires an **integrity-clean journal**),
`validate_pattern.py --reconcile` (INDEX/record drift), non-blocking advisory leakage warnings, and
a `run_limits` block in `mandate.yaml` (stage-reentry / unavailable-retry / dossier-per-run caps —
orchestrator-enforced, not a runtime harness). The `PaperBrokerAdapter` runs as a
built-in simulator while the `LiveBrokerAdapter` ships **disabled** behind Gate C. The orchestrator
(`orchestrator_investment_research.md`), the slash commands (`/investment-run`, `/screen`, `/monitor`,
`/decide`), and the agents (`research-orchestrator`, `pattern-miner`, `monitor-agent`) wire the gates
+ kill switch. Every toolkit prompt (8 stages + orchestrator + 4 commands + 3 agents) plus the 8
net-new `domain-finance` prompts is registered in the repo's `PROMPT_INDEX.json` / `PROMPT_INDEX.md`
and routed from the root `CLAUDE.md`. **Phase 7** wired every stage prompt, command, and the
orchestrator to those scripts with exact CLIs (no more by-hand/stub gate prose) and added the
executable glue the stages lacked: `build_snapshot.py` (immutable, look-ahead-safe Stage 1 universe
writer), `screen_rank.py` (Gate A enforced at Stage 4 ranking time), and `brokers.py --report`
(read-only exposure). The suite now runs **35** cases (`tests/test_gates.py` + `tests/test_injection.py`
+ `tests/test_hardening.py`) and [`DRY_RUN.md`](DRY_RUN.md) shows the loop wired end-to-end on the
fixtures. Only the live-broker implementation remains **pending** (see
`ARCHITECTURE.md` §13 step 7 — deliberately deferred behind Gate C).

## The loop

```
        ┌───────────────────────────────────────────────────────────────┐
        │                                                               │
        ▼                                                               │
┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌───────────────────────┐
│ 0 MANDATE &  │──▶│ 1 UNIVERSE & │──▶│ 2 DEEP       │──▶│ 3 PATTERN KB          │
│   CONFIG     │   │   DATA       │   │   RESEARCH   │   │   (discover/validate) │  ◀── [BUILT]
│  [BUILT]     │   │   [BUILT]    │   │   [BUILT]    │   │   ── Gate A ──        │
└──────────────┘   └──────────────┘   └──────────────┘   └───────────┬───────────┘
                                                                      │ validated only
                                                                      ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌───────────────────────┐
│ 7 JOURNAL &  │◀──│ 6 DECISION & │◀──│ 5 MONITOR &  │◀──│ 4 SCREEN /            │
│   CALIBRATE  │   │   ACTION     │   │   TRIPWIRES  │   │   OPPORTUNITY FINDER  │
│  [BUILT]     │   │  paper-first │   │  [BUILT]     │   │  [BUILT]              │
│  Brier ───┐  │   │  [BUILT]     │   └──────────────┘   └───────────────────────┘
└───────────┼──┘   │  ── Gate B ──│
            │      │  ── Gate C ──│
            │      └──────────────┘
            └────── feedback: resolved outcomes update patterns (Stage 3) ──────▶
```

Verdict labels on the arrows: Stage 3 emits only `validated` patterns into Stage 4
(Gate A); Stage 6 passes only orders that clear Gate B (risk limits) and is held to
paper by Gate C (real-money lock). The kill switch (`mandate.yaml: halt: true`) stops
Stages 4–6 instantly; Stages 3 and 7 may continue read-only.

## Stage I/O

| # | Stage | Required inputs | Primary outputs | Gate |
|---|---|---|---|---|
| 0 | Mandate & Config | objective, sim capital, scope, cadence | validated `config/*.yaml` | refuses run if required fields missing |
| 1 | Universe & Data | mandate, asset-class filters | `data/snapshots/<date>/universe.csv` + raw data | — (timestamped: look-ahead prevention) |
| 2 | Deep Research | snapshot data per candidate | `data/output/dossiers/<ticker>.md` | — |
| 3 | **Pattern KB** | dossiers, historical snapshots, resolved journal outcomes | versioned `knowledge-base/patterns/PATTERN-*.md` | **Gate A** (OOS + min sample → `validated`) |
| 4 | Screening | universe, dossiers, `validated` patterns only | `data/output/watchlist.csv` (ranked) | hypothesis patterns shown as unscored signal |
| 5 | Monitor & Tripwires | watchlist, open paper positions, fresh snapshots | `data/output/alerts/<date>.md` | kill switch halts |
| 6 | Decision & Action | watchlist/alert, mandate, risk limits | `data/output/orders/<date>.md` + paper fills + decision log | **Gate B** (sizing+premortem+limits) · **Gate C** (live locked) |
| 7 | **Journaling & Calibration** | every prediction with stated probability + thesis | `knowledge-base/journal/PRED-*.md` + calibration report | feeds Stage 3 |

## Gates & kill switch (ARCHITECTURE §5)

| Gate | Guards | Pass condition |
|---|---|---|
| **A — Pattern validation** | 3 → 4 | `validated` only with an out-of-sample test AND ≥ configured minimum sample size; in-sample-only stays `hypothesis`. |
| **B — Order safety** | Stage 6 | No order (even paper) without position sizing, a pre-mortem, and a passing risk-limit check (≤2%/position, ≤20%/class, ≤60% deployed). |
| **C — Real-money unlock** | Stage 6 live adapter | `LiveBrokerAdapter` disabled until ≥100 resolved predictions AND Brier ≤0.18 AND an **integrity-clean journal** (`journal_integrity.py` → `gate_c.integrity_clean`) AND manual `live_enabled: true`. |
| **Kill switch** | Stages 4–6 | `mandate.yaml: halt: true` stops all action stages immediately; research/journaling continue read-only. |

## Cadence (§14 default)

- **Daily** — Stage 5 monitor/tripwire sweep (also covers crypto's 24/7 market).
- **Weekly** — Stages 1–4 deep research + screen.
- Stages 3 and 7 run whenever new evidence or resolved predictions arrive.

## Where outputs land

```
ai-investment-research-toolkit/
├── knowledge-base/            # TRACKED durable memory (no secrets)
│   ├── INDEX.md               # pattern index
│   ├── patterns/PATTERN-*.md  # Stage 3 records
│   └── journal/PRED-*.md      # Stage 7 predictions + calibration report
└── data/                      # GIT-IGNORED working tree
    ├── input/                 # manual-only mode: pasted prices/filings/figures
    ├── snapshots/<date>/      # Stage 1 timestamped raw pulls
    └── output/                # dossiers, watchlist, alerts, orders (Stages 2,4,5,6)
        └── portfolio.json     # Stage 6 running paper ledger (cash + positions; paper-trade-executor)
```

## Runtime modes

- **Claude Code:** `/investment-run` orchestrator (full cadence), or `/screen`, `/monitor`, `/decide <ticker>` — backed by the `research-orchestrator`, `pattern-miner`, and `monitor-agent` agents.
- **Codex / any agent:** `AGENTS.md` is the entry point; run stage prompts as a sequence.
- **Manual:** walk this file and run the stage prompts in `prompts/` yourself.

In every mode the gates and kill switch are enforced by the stage prompts / orchestrator,
not by trust.
