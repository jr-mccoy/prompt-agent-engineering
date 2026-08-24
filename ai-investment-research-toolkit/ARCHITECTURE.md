# AI Investment Research Toolkit — Architecture & Design

*For informational and research purposes only. Not financial, investment, or tax advice.*

**Status: BLUEPRINT (now largely built).** This was the original design document. As of
Phase 7, build steps 1–6 in §13 are complete, the loop is executable on paper, **and every
stage prompt / command / the orchestrator now invokes the gate-enforcing scripts directly**
(Phase 7 also added `build_snapshot.py`, `screen_rank.py`, and `brokers.py --report`) —
see [`PIPELINE_OVERVIEW.md`](PIPELINE_OVERVIEW.md) for live build status and
[`DRY_RUN.md`](DRY_RUN.md) for a worked end-to-end paper run proving the gates. Only §13
step 7 (the real-money `LiveBrokerAdapter`) remains deferred behind Gate C. This document
is kept as the authoritative design/manifest; the gate, schema, and seam specs (§5/§6/§10)
are what the code implements.

**Document version:** 1.1 · **Date:** 2026-06-18

---

## 1. Purpose & scope

Build a portable, local-first toolkit that uses AI agents (Claude Code / Codex) to:

- do **deep research** on candidate assets,
- **discover and store patterns** that have historically been associated with success or
  failure,
- **screen** a universe for opportunities (especially cheap / early ones),
- **monitor** holdings and watchlist for catalysts and thesis-break signals ("see the
  train coming"),
- **act on paper first**, with real-money execution deferred behind a track record, and
- **journal every prediction and score it**, feeding results back to improve the patterns.

### Decisions this design is built around (from intake)

| Decision | Choice | Design consequence |
|---|---|---|
| Action autonomy | **Paper-trading first**, then decide | Execution layer is a paper adapter; real adapter exists but ships **disabled**. |
| Asset classes | **Public equities (incl. micro/small-cap), crypto/tokens, options/derivatives** | Per-asset-class research modules; crypto and options are net-new (repo gaps). |
| This deliverable | **Architecture document only** | No prompts/skills built here; this doc is the manifest. |
| Data / broker access | **None yet** | Everything external is a stubbable **adapter seam**; §10 lists what to acquire. |

### Non-goals

- Not financial advice; not a guarantee of returns; not a substitute for a professional.
- Not a high-frequency / latency-sensitive trading system. Cadence is daily/periodic.
- Not a real-money autotrader in any shipped phase until §5 Gate C is satisfied.

---

## 2. What already exists vs. the gap

The repo's [`referenced-prompts/domain-finance/`](referenced-prompts/domain-finance/) already provides **135 analytical
prompts** — the "how to think about an asset" layer. This toolkit does **not** rebuild
them; it orchestrates them.

**Reused as-is (referenced by path, not copied):**

- Research: `referenced-prompts/domain-finance/investing-research/finance_investment_thesis_builder.md`,
  `finance_catalyst_map_builder.md`, `finance_competitive_moat_analyzer.md`,
  `finance_position_sizing_framework.md`, `finance_short_thesis_constructor.md`
- Valuation: `referenced-prompts/domain-finance/valuation/finance_reverse_dcf_expectations.md`,
  `finance_dcf_model_builder.md`
- Quant discipline: `referenced-prompts/domain-finance/quant-fintech-data/finance_backtest_design_critique.md`,
  `finance_alt_data_thesis_evaluator.md`, `finance_trading_strategy_premortem.md`
- Macro: `referenced-prompts/domain-finance/markets-macro/finance_sector_rotation_framework.md`
- Forecasting / calibration (all under `referenced-prompts/domain-reasoning-craft/forecasting/`):
  `forecasting_base_rate_establishment.md`, `forecasting_brier_tracker_design.md`,
  `forecasting_calibration_self_audit.md`, `forecasting_what_would_change_my_mind.md`,
  `forecasting_signal_vs_noise_filter.md`

**The gap this toolkit fills:** the AI-native *orchestration loop* — a pattern knowledge
base, a screener that applies it, a monitor with tripwires, a paper-action stage, and a
calibration feedback loop that closes back onto the knowledge base.

**Packaging precedent:** [`financial-records-toolkit/`](../financial-records-toolkit/) —
a local-first, privacy-first bundle (skills + agents + slash command + config + git-ignored
`data/` + `.gitignore` + a hard verification gate). This toolkit mirrors that structure.

---

## 3. Design principles (load-bearing guardrails)

These are not advice; they are enforced as **hard gates** (§5) and prompt constraints.

1. **Paper-first.** Real money is gated behind a recorded track record (Gate C). Every
   stage runs end-to-end against a simulated account before any live order is possible.
2. **No fabricated data.** Every figure traces to a real adapter/source or user-provided
   input. Unknowns are *queued for retrieval*, never guessed — the same discipline as the
   financial-records toolkit's "no invented merchants" rule. (Techniques: QA-05, DS-02.)
3. **Anti-overfitting is structural.** The pattern KB cannot promote a pattern to
   "validated" without out-of-sample evidence and a minimum sample size (Gate A). Survivorship,
   look-ahead, and multiple-comparisons checks are mandatory steps, not suggestions.
4. **Calibrated uncertainty, never false precision.** Every prediction carries a probability
   and a confidence band; outputs are scenario ranges, not point forecasts. (QA-04, NE-10.)
5. **Calibration before capital.** Real execution is unlocked only after ≥100 resolved
   predictions and a Brier score ≤ 0.18 — and a manual switch you flip (Gate C).
6. **Risk limits + kill switch.** Position and portfolio limits are checked before any order
   (Gate B); a global kill switch halts all action stages.
7. **Local-first / privacy.** Secrets and the `data/` working tree stay out of version
   control (`.gitignore`). API keys live in environment/secret files, never in prompts.
8. **Adversarial by default.** Each thesis gets a pre-mortem and a "what would change my
   mind" tripwire set before it can drive an order. (QA-02.)

---

## 4. The system loop (8 stages)

Each stage lists: **purpose → inputs → process → output → reused/seams.**

### Stage 0 — Mandate & Config
- **Purpose:** Encode the rules of engagement so every later stage is bounded.
- **Inputs:** User objective, capital (simulated), risk tolerance, asset-class scope, cadence.
- **Process:** Fill `config/mandate.yaml`, `risk_limits.yaml`, `asset_classes.yaml`,
  `data_sources.yaml`. Define the kill switch.
- **Output:** Validated config set; refuses to run later stages if required fields missing.
- **Seams:** none (local config).

### Stage 1 — Universe & Data Sourcing
- **Purpose:** Define the hunting ground and pull the raw material.
- **Inputs:** Mandate; asset-class filters (e.g. microcaps under $X mcap, tokens by mcap/age,
  optionable underlyings).
- **Process:** Resolve the candidate universe; call **data adapters** for prices, fundamentals,
  filings, on-chain metrics, options chains. **Snapshot everything with a timestamp** to a
  dated folder so later backtests can't peek at future data (look-ahead prevention).
- **Output:** `data/snapshots/<date>/universe.csv` + per-candidate raw data.
- **Seams:** `MarketDataAdapter`, `FundamentalsAdapter`, `FilingsAdapter`, `OnChainAdapter`,
  `OptionsChainAdapter` — all stubbed; see §10.

### Stage 2 — Deep Research (per candidate)
- **Purpose:** Produce a structured dossier per candidate.
- **Inputs:** Snapshot data for a candidate.
- **Process:** Orchestrate existing `domain-finance` prompts (thesis builder, moat analyzer,
  catalyst map, reverse-DCF expectations). For **crypto**, add tokenomics / on-chain / contract
  risk (net-new prompts, §8). For **options**, add IV/Greeks/structure (net-new, §8).
- **Output:** `data/output/dossiers/<ticker>.md` — thesis, valuation range, catalysts, risks,
  disconfirming test, per-asset-class specifics.
- **Reused:** see §2 research/valuation prompts.

### Stage 3 — Pattern Discovery & Knowledge Base *(the heart, and the danger zone)*
- **Purpose:** Find and store features historically associated with success/failure — without
  fooling yourself.
- **Inputs:** Dossiers + historical snapshots + resolved outcomes from the journal (Stage 7).
- **Process (discipline is mandatory):**
  1. **Register the hypothesis first** (what, why, expected effect, sample frame) — before
     looking at outcomes. Prevents post-hoc storytelling.
  2. **Split train/holdout**; test on data the pattern was not derived from.
  3. **Anchor to base rates**; a pattern must beat the base rate out-of-sample, not in-sample.
  4. **Account for multiple comparisons** (you tested many features → adjust expectations).
  5. **Estimate decay & capacity** (does the edge fade? does it survive realistic size/costs?).
  6. Assign a **status**: `hypothesis` → `validated` → `retired`.
- **Output:** Versioned pattern records (schema in §6) under `knowledge-base/patterns/`.
- **Reused:** `finance_backtest_design_critique.md`, `finance_alt_data_thesis_evaluator.md`,
  `forecasting_base_rate_establishment.md`, `forecasting_signal_vs_noise_filter.md`.

### Stage 4 — Screening / Opportunity Finder
- **Purpose:** Turn the universe + validated patterns into a ranked shortlist.
- **Inputs:** Universe, dossiers, `validated` patterns only.
- **Process:** Score each candidate by which validated patterns fire and with what confidence;
  rank; attach the evidence trail.
- **Output:** `data/output/watchlist.csv` — ranked, with scores, firing patterns, confidence.
- **Note:** `hypothesis`-status patterns may be shown as "watch / paper-only signal" but cannot
  drive a sizing recommendation.

### Stage 5 — Monitoring & Tripwires
- **Purpose:** The "see the train coming" early-warning layer.
- **Inputs:** Watchlist + open (paper) positions; fresh snapshots on cadence.
- **Process:** Track dated catalysts, thesis-break signals, and price/volatility tripwires
  defined per position. Raise alerts when a tripwire or "change-my-mind" condition trips.
- **Output:** `data/output/alerts/<date>.md`.
- **Reused:** `finance_catalyst_map_builder.md`, `forecasting_what_would_change_my_mind.md`.

### Stage 6 — Decision & Action (paper-first)
- **Purpose:** Convert a high-conviction candidate into an order — on paper.
- **Inputs:** Watchlist entry / alert; mandate; risk limits.
- **Process:** Draft a trade memo (ticker, direction, size, entry, exit, stop, thesis, risks);
  run **position sizing** and a **pre-mortem**; check **risk limits** (Gate B). Route the order
  to the **paper adapter**. The real-execution adapter is present but **disabled** (Gate C).
- **Output:** `data/output/orders/<date>.md` + paper fills + decision-log entry.
- **Reused:** `finance_position_sizing_framework.md`, `finance_trading_strategy_premortem.md`.
- **Seams:** `PaperBrokerAdapter` (active), `LiveBrokerAdapter` (disabled).

### Stage 7 — Journaling & Calibration *(closes the loop)*
- **Purpose:** Make the system honest over time and feed Stage 3.
- **Inputs:** Every prediction/order with its stated probability and thesis.
- **Process:** Log the prediction; when it resolves, score it (**Brier**), update calibration,
  and write the outcome back so Stage 3 can validate or **retire** patterns.
- **Output:** `knowledge-base/journal/` records + a running calibration report.
- **Reused:** `forecasting_brier_tracker_design.md`, `forecasting_calibration_self_audit.md`.

---

## 5. Hard gates & kill switch

The orchestrator refuses to proceed unless each gate passes.

| Gate | Guards | Condition to pass |
|---|---|---|
| **A — Pattern validation** | Stage 3 → Stage 4 | A pattern reaches `validated` only with an out-of-sample test **and** ≥ minimum sample size (set in config). In-sample-only patterns stay `hypothesis`. |
| **B — Order safety** | Stage 6 | No order (even paper) without position-sizing output, a pre-mortem, and a passing risk-limit check. **Defaults:** ≤ 2% per position, ≤ 20% per asset class, ≤ 60% of capital deployed. |
| **C — Real-money unlock** | Stage 6 live adapter | `LiveBrokerAdapter` stays disabled until **all of**: (1) ≥ **100** resolved journaled predictions, (2) Brier ≤ **0.18**, (3) an **integrity-clean journal** (`journal_integrity.py` → `gate_c.integrity_clean`: no tampered `probability`, every resolution backed by `realized_return` + `resolved_on` at/after horizon), and (4) the user manually sets `live_enabled: true`. |
| **Kill switch** | All action stages | A single flag (`mandate.yaml: halt: true`) immediately stops Stages 4–6. Research/journaling may continue read-only. |

---

## 6. Data models

### Pattern record (`knowledge-base/patterns/PATTERN-<id>.md`)

```yaml
---
id: PATTERN-0007
title: "Insider cluster-buying in sub-$300M caps preceding 3-month outperformance"
status: hypothesis        # hypothesis | validated | retired
asset_classes: [equity-microcap]
hypothesis: "≥3 distinct insiders buying within 10 trading days predicts ..."
registered_on: "2026-06-18"      # BEFORE outcome inspection
feature_definition: "precise, reproducible computation of the signal"
sample_frame: "universe + date range the sample is drawn from"
base_rate: "outcome frequency in the sample frame absent the signal"
in_sample_result: { n: 0, lift_vs_base_rate: null }
out_of_sample_result: { n: 0, lift_vs_base_rate: null }   # required for 'validated'
multiple_comparisons_note: "how many features were screened to find this"
decay_estimate: "expected edge half-life / regime sensitivity"
capacity_note: "does edge survive realistic size, liquidity, costs?"
confidence: low            # low | medium | high
last_reviewed: "2026-06-18"
linked_predictions: []     # journal ids that tested this pattern
---
```

### Prediction journal entry (`knowledge-base/journal/PRED-<id>.md`)

```yaml
---
id: PRED-0042
date_opened: "2026-06-18"
asset: "TICKER"
direction: long
probability: 0.62          # stated up front, used for Brier
thesis_ref: "data/output/dossiers/TICKER.md"
patterns_fired: [PATTERN-0007]
horizon: "90 days"
tripwires: ["thesis-break X", "stop at -15%"]
resolution: null           # filled at horizon: outcome + realized return
brier_component: null      # computed at resolution
notes: ""
---
```

---

## 7. File manifest

```
ai-investment-research-toolkit/
├── README.md                         # [BUILT] status + overview + disclaimer
├── ARCHITECTURE.md                   # [BUILT] this document
├── SECURITY.md                       # [BUILT] prompt-injection / untrusted-content threat model + checklist
├── FAILURE_MODES.md                  # [BUILT] prioritized agent failure-mode catalog (detection + recovery)
├── OBSERVABILITY_AND_EVAL.md         # [BUILT] run-log schema + agent-decision eval harness
├── AGENTS.md                         # [SPEC] Codex entry point: agents + how to run the loop
├── PIPELINE_OVERVIEW.md              # [SPEC] visual flow, stage I/O, gates, cadence
├── orchestrator_investment_research.md   # [SPEC] master loop: classify state → run stages → enforce gates
├── prompts/                          # [SPEC] one prompt per stage
│   ├── stage-0-mandate-config.md
│   ├── stage-1-universe-data-sourcing.md
│   ├── stage-2-deep-research.md
│   ├── stage-3-pattern-knowledge-base.md
│   ├── stage-4-screening.md
│   ├── stage-5-monitoring-tripwires.md
│   ├── stage-6-decision-paper-action.md
│   └── stage-7-journaling-calibration.md
├── referenced-prompts/               # [BUILT] vendored copies of the 21 prompts the loop orchestrates (self-contained)
│   ├── domain-finance/               #   16 analytical prompts (research, valuation, crypto, options, quant, macro)
│   └── domain-reasoning-craft/       #   5 forecasting/calibration prompts
├── skills/                           # [BUILT] reusable capabilities (SKILL.md + scripts/ + references/) — 5 skills
│   ├── data-source-adapter/          # normalize provider data behind a stable interface (the seam)
│   ├── pattern-knowledge-base/       # create/validate/retire pattern records; enforce Gate A (+ `--reconcile` INDEX/record check, advisory leakage warnings)
│   │   └── references/leakage_and_skepticism_audit.md  # [BUILT] leakage + result-skepticism audit (hardens Gate A)
│   ├── prediction-journal/           # log predictions, score Brier, calibration report; `journal_integrity.py` tamper-evidence (Gate C `integrity_clean`)
│   ├── paper-trade-executor/         # simulate fills, track positions; Live adapter stub (disabled)
│   └── output-guard/                 # `egress_check.py --scan` — secret-leak / exfiltration scan before writes
├── agents/                           # [SPEC]
│   ├── research-orchestrator.md      # drives the full loop, enforces gates + kill switch
│   ├── pattern-miner.md              # Stage 3 specialist (discipline-enforcing)
│   └── monitor-agent.md              # Stage 5 specialist (tripwire watcher)
├── commands/                         # [SPEC] slash commands
│   ├── investment-run.md             # /investment-run — full cadence pass
│   ├── screen.md                     # /screen — Stages 1,2,4 only
│   ├── monitor.md                    # /monitor — Stage 5 only
│   └── decide.md                     # /decide <ticker> — Stage 6 (paper)
├── config/                           # [SPEC] tunable, non-secret
│   ├── mandate.yaml                  # objective, capital (sim), cadence, halt/kill switch, live_enabled, run_limits (stage-reentry / unavailable-retry / dossier-per-run caps, nonzero_exit_is_hard_stop)
│   ├── risk_limits.yaml              # per-position %, portfolio exposure, per-asset-class caps
│   ├── asset_classes.yaml            # which classes active + their universe filters
│   └── data_sources.yaml            # which adapter implementation backs each seam
├── knowledge-base/                   # [SPEC] the durable memory (may be git-tracked, no secrets)
│   ├── patterns/                     # PATTERN-*.md records
│   ├── INDEX.md                      # pattern index with status + confidence
│   └── journal/                      # PRED-*.md prediction records + calibration report
├── data/                             # [SPEC] working tree — GIT-IGNORED
│   ├── input/                        # user-pasted filings/figures when no API
│   ├── snapshots/<date>/             # timestamped raw pulls (look-ahead prevention)
│   └── output/                       # dossiers, watchlist, alerts, orders
├── .gitignore                        # [SPEC] excludes data/, secrets, local env
└── requirements.txt                  # [SPEC] optional python deps (stdlib-first)
```

---

## 8. Net-new prompts to author (gap-fill, future build)

Authored into `referenced-prompts/domain-finance/` subdirs and referenced by the toolkit by path:

| Prompt | Subdir | Why net-new |
|---|---|---|
| `finance_token_valuation_framework.md` | `referenced-prompts/domain-finance/quant-fintech-data/` (or new `crypto/`) | Repo has no token/tokenomics valuation. |
| `finance_onchain_metrics_analysis.md` | same | On-chain metrics interpretation — gap. |
| `finance_smart_contract_risk_review.md` | same | Contract/protocol risk — gap. |
| `finance_options_structure_selector.md` | `referenced-prompts/domain-finance/` (new `options/`) | Options structure selection — gap. |
| `finance_implied_vol_greeks_analysis.md` | same | IV / Greeks analysis — gap. |
| `finance_pattern_hypothesis_registration.md` | `referenced-prompts/domain-finance/quant-fintech-data/` | Pre-registration discipline for Stage 3 (Gate A). |
| `finance_out_of_sample_validation_protocol.md` | same | Formal holdout/OOS protocol for Gate A. |
| `finance_signal_decay_monitor.md` | same | Detect edge decay → trigger pattern retirement. |

Each follows Tier-1 convention: Objective / When to Use / Inputs / Constraints (Must–Must Not)
/ Instructions / Output Format / Verification / False-Positive Prevention, the finance
disclaimer line, and techniques QA-04, QA-05, CM-02, DS-02, NE-10, NE-11, QA-02.

---

## 9. Asset-class notes

- **Public equities (incl. micro/small-cap):** best supported today. Microcaps add liquidity,
  manipulation, and data-sparsity risk — Stage 3 capacity checks and Stage 6 risk limits matter
  most here.
- **Crypto / tokens:** needs tokenomics, on-chain metrics, and smart-contract/protocol risk
  (net-new prompts). 24/7 markets change the monitoring cadence; custody/exchange risk is a
  distinct risk-limit dimension.
- **Options / derivatives:** adds IV, Greeks, expiry, and assignment risk; position sizing and
  pre-mortem must account for non-linear payoff and time decay. Higher risk → keep behind the
  same gates with tighter per-class caps.

---

## 10. Data & broker dependencies (what you'd acquire)

Everything external is an **adapter seam** with a stub implementation, so the loop runs (on
sample/manual data) before you buy anything.

| Seam | Backs | Minimum to make it real |
|---|---|---|
| `MarketDataAdapter` | prices/volume (Stages 1,5) | A market-data API (equities + crypto). |
| `FundamentalsAdapter` | financials/ratios (Stage 2) | A fundamentals data source or manual `data/input/`. |
| `FilingsAdapter` | 10-K/10-Q/news (Stages 2,5) | A filings/news feed or manual paste. |
| `OnChainAdapter` | token metrics (Stage 2,5) | An on-chain data provider (crypto only). |
| `OptionsChainAdapter` | chains/IV/Greeks (Stage 2,6) | An options-data source (options only). |
| `PaperBrokerAdapter` | simulated fills (Stage 6) | A broker paper-trading API **or** the built-in simulator. |
| `LiveBrokerAdapter` | real orders (Stage 6) | A broker live API — **kept disabled** until Gate C. |

**Manual-only mode:** with no APIs, the loop still runs from `data/input/` (you paste filings,
prices, figures) and the built-in paper simulator. Slower, but fully functional for learning the
system and building an early calibration record.

---

## 11. Runtime modes

- **Claude Code:** run `/investment-run` (orchestrator) for a full cadence pass, or individual
  commands (`/screen`, `/monitor`, `/decide`). Agents coordinate stages.
- **Codex:** `AGENTS.md` is the entry point; the same stage prompts run as a manual sequence.
- **Manual:** walk `PIPELINE_OVERVIEW.md` and run stage prompts yourself.

In all modes, gates and the kill switch are enforced by the orchestrator/stage prompts, not by
trust.

---

## 12. Dry-run walkthrough (one candidate, paper)

Tracing a hypothetical microcap `EXMP` through the loop, showing where gates fire:

1. **Stage 0:** Mandate set — sim capital $50k, max 5%/position, equities+crypto on, options off,
   `live_enabled: false`, `halt: false`.
2. **Stage 1:** Universe = US equities < $300M mcap. `MarketDataAdapter` (stub → sample data)
   pulls prices; snapshot written to `data/snapshots/2026-06-18/`. `EXMP` is in the universe.
3. **Stage 2:** Dossier built via `finance_investment_thesis_builder.md` +
   `finance_competitive_moat_analyzer.md` + `finance_reverse_dcf_expectations.md`. Thesis: priced
   for decline, but insider cluster-buying + improving gross margin.
4. **Stage 3:** Pattern `PATTERN-0007` (insider cluster-buying) is **`hypothesis`** status — it
   has in-sample lift but no out-of-sample test yet. **Gate A blocks** it from driving sizing; it
   may appear on the watchlist as "paper-only signal."
5. **Stage 4:** `EXMP` ranks #3; the screener notes only `validated` patterns counted toward the
   score; `PATTERN-0007` shown as unscored signal.
6. **Stage 5:** Tripwires set: earnings date catalyst, stop at −15%, thesis-break = "insiders
   sell." Monitor watches the snapshot cadence.
7. **Stage 6:** You run `/decide EXMP`. Trade memo drafted; `finance_position_sizing_framework.md`
   sizes to 3%; `finance_trading_strategy_premortem.md` runs. **Gate B** checks risk limits → pass.
   Order routes to `PaperBrokerAdapter`. **Gate C** keeps `LiveBrokerAdapter` disabled — paper fill
   only. Decision logged.
8. **Stage 7:** `PRED-0042` logged with probability 0.62, horizon 90 days, linked to
   `PATTERN-0007`. At resolution, Brier scored, calibration updated, and the outcome written back
   so Stage 3 can move `PATTERN-0007` toward `validated` or `retired`.

Net: a full research-to-action-to-feedback cycle, on paper, with every high-risk surface gated.

---

## 13. Suggested build order (when/if approved)

1. **Foundation:** directory skeleton, config files, `.gitignore`, `PIPELINE_OVERVIEW.md`.
2. **Memory + honesty first:** `pattern-knowledge-base` + `prediction-journal` skills and the
   Stage 3/7 prompts. (Builds the discipline layer before anything can trade.)
3. **Research + screen:** Stage 1/2/4 prompts + `data-source-adapter` (stubs) + net-new
   crypto/options/discipline prompts (§8).
4. **Monitor + paper action:** Stage 5/6 prompts + `paper-trade-executor` (live adapter disabled).
5. **Orchestrator + commands + agents:** tie it together; wire gates and kill switch.
6. **Index integration:** register new prompts in `PROMPT_INDEX.json`/`.md` and add a CLAUDE.md
   routing row. **[DONE]** Phase 6 additionally made the four skill scripts executable
   (Gate A/B/C + kill switch enforced in code; `--self-check` per script; `tests/test_gates.py`;
   `DRY_RUN.md` + `samples/` fixtures). YAML loads via PyYAML if present, else an embedded
   subset parser, so manual-only mode stays dependency-free. **Phase 7 [DONE]** wired the stage
   prompts / commands / orchestrator to those scripts with exact CLIs and added the missing
   executable glue — `build_snapshot.py` (immutable, look-ahead-safe Stage 1 universe writer),
   `screen_rank.py` (Gate A enforced at Stage 4 ranking time), and `brokers.py --report`
   (read-only exposure). A subsequent hardening pass added the `output-guard` skill
   (`egress_check.py`), `journal_integrity.py`, `validate_pattern.py --reconcile`, advisory leakage
   warnings, and `mandate.yaml run_limits`; the suite now runs **35 tests** across
   `tests/test_gates.py` + `tests/test_injection.py` + `tests/test_hardening.py` proving the wired
   flow, injection inertness, and the integrity/reconcile guards.
7. **Real execution (only after Gate C is met):** implement and enable `LiveBrokerAdapter` with
   per-trade human approval — a separate, explicit decision. **[DEFERRED — not built.]**

---

## 14. Resolved defaults & remaining deferrals

**Resolved (these are the build defaults; all are config-tunable later):**

| Decision | Default | Where it lives |
|---|---|---|
| **Gate C — real-money unlock** | ≥ 100 resolved predictions **and** Brier ≤ 0.18 **and** manual `live_enabled: true` | `mandate.yaml`, enforced in §5 Gate C |
| **Gate B — risk limits** | ≤ 2% per position · ≤ 20% per asset class · ≤ 60% deployed | `risk_limits.yaml`, enforced in §5 Gate B |
| **Cadence** | **Dual:** daily monitor/tripwire (Stage 5) + weekly deep research & screen (Stages 1–4) | `mandate.yaml`; crypto's 24/7 nature handled by the daily pass |
| **Knowledge-base storage** | **Private & portable:** `knowledge-base/` git-tracked in the user's *private* repo (no secrets); `data/` stays git-ignored | `.gitignore` + §7 manifest |

**Still deferred (decide when you have accounts):**

- **Provider choices:** which market-data and broker *paper* APIs back each adapter seam (§10).
  Until chosen, all seams ship as stubs and the loop runs on `data/input/` + the built-in
  paper simulator. Selecting providers is what turns the stubs into live adapters.
