# AGENTS.md — AI Investment Research Toolkit (Codex / agent entry point)

*For informational and research purposes only. Not financial, investment, or tax advice.
Nothing here places real-money trades.*

You are running a **paper-first** investment research loop. Work in **stages** and
**enforce the gates**. You produce calibrated research and a recorded track record —
you do **not** place real orders, and you never let optimism override a gate.

> **Build status (Phase 1 + 2 + 3 + 4 + 5 + 6 + 7):** All **8** stage prompts are built — Stage **0**
> (Mandate & Config), **1** (Universe & Data), **2** (Deep Research), **3** (Pattern Knowledge Base),
> **4** (Screening), **5** (Monitor & Tripwires), **6** (Decision & Action), and **7** (Journaling &
> Calibration) — along with the `data-source-adapter`, `pattern-knowledge-base`, `prediction-journal`,
> and `paper-trade-executor` skills. **Phase 6 made the loop executable:** the four skill scripts are
> now working, stdlib-first Python (`validate_pattern.py` enforces Gate A; `score_brier.py` computes
> Brier + calibration + Gate C progress; `brokers.py` runs the paper simulator + Gate B + kill switch
> + `load_config`; `adapters.py` does manual-only point-in-time reads + `load_data_sources`). Each
> ships a `--self-check`; `tests/test_gates.py` (14 tests) and [`DRY_RUN.md`](DRY_RUN.md) prove every
> gate fires on the fixtures in [`samples/`](samples/). YAML is parsed with PyYAML if installed, else
> an embedded subset parser, so manual-only mode stays dependency-free. The `PaperBrokerAdapter` runs
> as a built-in simulator; the `LiveBrokerAdapter` ships **disabled** behind Gate C. The orchestrator
> (`orchestrator_investment_research.md`), the slash commands (`/investment-run`, `/screen`,
> `/monitor`, `/decide`), and the agents (`research-orchestrator`, `pattern-miner`, `monitor-agent`)
> wire the gates + kill switch (§13 step 5). Every toolkit prompt plus the 8 net-new `domain-finance`
> prompts is registered in `PROMPT_INDEX.json` / `PROMPT_INDEX.md` and routed from the root
> `CLAUDE.md` (§13 step 6). **Phase 7** wired every stage prompt, command, and the orchestrator to those
> scripts with the exact CLIs (the gate steps now invoke the scripts, not "do it by hand") and added the
> executable glue the stages lacked: `build_snapshot.py` (immutable, look-ahead-safe Stage 1 universe
> writer), `screen_rank.py` (Gate A enforced at Stage 4 ranking time), and `brokers.py --report`
> (read-only exposure). `tests/test_gates.py` now runs 20 cases. Only the live-broker implementation
> remains pending — if asked to run it, say it is deferred behind Gate C (`ARCHITECTURE.md` §13 step 7).
> Everything runs paper-first on snapshots and manual data in `data/input/`; there is no real-money path.

## Ground rules

1. **Paper-first.** Real money is gated behind a recorded track record (Gate C in
   `config/mandate.yaml`). Never treat `live_enabled: false` as something to work around.
2. **No fabricated data.** Every figure traces to a real adapter/source or user-provided
   input in `data/input/`. Unknowns are *queued for retrieval*, never guessed.
3. **Anti-overfitting is structural (Gate A).** A pattern reaches `validated` ONLY with an
   out-of-sample test AND ≥ the configured minimum sample size. In-sample-only stays
   `hypothesis` and cannot drive sizing. Register the hypothesis BEFORE inspecting outcomes.
4. **Calibrated uncertainty.** Every prediction carries a probability and is scored (Brier).
   Outputs are scenario ranges, not point forecasts.
5. **Kill switch.** If `mandate.yaml: halt: true`, do not run action stages (4–6). Research
   and journaling may continue read-only.
6. **Run limits (`mandate.yaml: run_limits`).** Honor `max_stage_reentries`,
   `max_unavailable_retries`, `max_dossiers_per_run`, and `nonzero_exit_is_hard_stop` — a
   nonzero exit from a guard script is a hard stop, not a warning to work around.
7. **Egress guard.** Before the loop writes a file, run `output-guard`'s
   `egress_check.py --scan <path>` to flag secret-shaped strings (cloud keys, provider
   tokens, PEM blocks, `key=value` secret assignments); `redact()` masks them.

### Guard commands (call these in the gate steps)

```bash
# Tamper-evidence + resolution honesty (Stage 7 / Gate C):
python skills/prediction-journal/scripts/journal_integrity.py --stamp knowledge-base/journal/PRED-<id>.md
python skills/prediction-journal/scripts/journal_integrity.py --verify knowledge-base/journal/
# INDEX↔record drift reconcile (Stage 3, F18):
python skills/pattern-knowledge-base/scripts/validate_pattern.py --reconcile knowledge-base/patterns --index knowledge-base/INDEX.md
# Secret-shaped egress scan before any file write:
python skills/output-guard/scripts/egress_check.py --scan <path>
```

Gate C now *also* requires an **integrity-clean journal**: `score_brier.py --calibration-report`
sets `unlock_ready: False` unless `journal_integrity.py --verify` reports no tamper and no
dishonest resolution.

## Layout

- Durable memory (TRACKED): `knowledge-base/patterns/`, `knowledge-base/journal/`, `knowledge-base/INDEX.md`
- Working data (GIT-IGNORED): `data/input/` (manual paste), `data/snapshots/`, `data/output/`
- Tunable config: `config/mandate.yaml`, `risk_limits.yaml`, `asset_classes.yaml`, `data_sources.yaml`
- Skills (5): `data-source-adapter`, `pattern-knowledge-base`, `prediction-journal`,
  `paper-trade-executor`, and `output-guard` (egress secret-scan before any file write) —
  each `skills/<skill>/SKILL.md` (+ `references/`, `scripts/`)
- Stage prompts: `prompts/stage-*.md`

## Setup

```bash
pip install -r requirements.txt   # optional; manual-only mode needs only the stdlib

# Prove the gates fire before trusting the loop (all stdlib; no data/API needed):
python -m unittest discover -s tests -v     # 20 gate tests on samples/ fixtures
python skills/pattern-knowledge-base/scripts/validate_pattern.py --self-check
python skills/prediction-journal/scripts/score_brier.py --self-check
python skills/paper-trade-executor/scripts/brokers.py --self-check
python skills/data-source-adapter/scripts/adapters.py --self-check
python skills/data-source-adapter/scripts/build_snapshot.py --self-check   # Stage 1 snapshot writer
python skills/pattern-knowledge-base/scripts/screen_rank.py --self-check    # Stage 4 Gate A scorer
```

See [`DRY_RUN.md`](DRY_RUN.md) for the full one-candidate paper walkthrough showing each gate firing.

## Stage 0 — Mandate & Config (preflight; run this FIRST)

Read `prompts/stage-0-mandate-config.md`. Before any other stage, validate the four config files
(`config/mandate.yaml`, `risk_limits.yaml`, `asset_classes.yaml`, `data_sources.yaml`).

1. **Validate required fields.** If any required field is missing or malformed, this is a **NO-GO** —
   name the file + field and stop; never default-in or guess a value to proceed.
2. **Surface the switches first.** Report `halt` (kill switch) and the Gate C block (`live_enabled`
   + thresholds). `live_enabled` is paper-only regardless — the `LiveBrokerAdapter` is disabled in
   this build; flag any `live_enabled: true` as out of scope, do not honor it.
3. **Check consistency + seam modes.** ≥1 active class with filters; each `per_asset_class` cap ≤ the
   portfolio cap; active crypto/options classes have their seams; report each seam as live vs. manual
   (stub). Confirm `LiveBrokerAdapter: enabled: false`.
4. **Emit GO / NO-GO.** On GO, hand the validated config summary to Stage 1; on NO-GO, list every
   blocker and do not advance.

## Stage 1 — Universe & Data Sourcing (timestamped snapshots)

Read `prompts/stage-1-universe-data-sourcing.md` and use the `data-source-adapter` skill.

1. **Resolve scope.** Read the active classes + filters from `config/asset_classes.yaml`; honor
   the kill switch in `config/mandate.yaml`.
2. **Pull point-in-time data.** Each seam in `config/data_sources.yaml` set to `stub` runs
   manual-only: drop files under `data/input/<seam>/` (see
   `skills/data-source-adapter/references/manual_only_mode.md`). Every value carries an `as_of`.
3. **Snapshot immutably.** Run `skills/data-source-adapter/scripts/build_snapshot.py --as-of <as_of>
   --manual data/input --out data/snapshots` — it writes `data/snapshots/<as_of>/universe.csv` +
   per-candidate raw data, never includes data dated after `as_of` (look-ahead), skips candidates with
   no point-in-time price, and REFUSES to overwrite a prior snapshot (immutability).
4. **Queue unknowns.** Unavailable fields are marked `UNAVAILABLE` and queued — never guessed.

## Stage 2 — Deep Research (per-candidate dossier)

Read `prompts/stage-2-deep-research.md`. Build `data/output/dossiers/<ticker>.md` from the Stage 1
snapshot only, orchestrating the reused `domain-finance` prompts and branching by asset class
(equity / crypto / options). Each dossier needs a variant view, a bear/base/bull valuation range,
dated catalysts, ranked risks, and a pre-committed disconfirming test (which becomes the Stage 7
tripwire). No new mid-dossier data pulls; unknowns stay queued.

## Stage 4 — Screening / Opportunity Finder (Gate A)

Read `prompts/stage-4-screening.md`. Score each candidate only on **`validated`** patterns
(Gate A) weighted by confidence; rank; attach the evidence trail; write `data/output/watchlist.csv`.
`hypothesis`-status patterns appear only as unscored "paper-only signal" and never affect the rank.
`UNAVAILABLE` data → "cannot score," never a silent pass. Honor the kill switch. Run
`skills/pattern-knowledge-base/scripts/screen_rank.py --firings firings.json --patterns-dir
knowledge-base/patterns --out data/output/watchlist.csv` — Gate A is enforced at ranking time in code
(only `validated` patterns that PASS contribute to the score).

## Stage 5 — Monitor & Tripwires (see the train coming)

Read `prompts/stage-5-monitoring-tripwires.md`. On the daily monitor cadence, watch the watchlist
(`data/output/watchlist.csv`) and open paper positions (`data/output/portfolio.json`). For each
name, build a dated catalyst map (reuse `referenced-prompts/domain-finance/investing-research/finance_catalyst_map_builder.md`)
and explicit thesis-break tripwires (reuse
`referenced-prompts/domain-reasoning-craft/forecasting/forecasting_what_would_change_my_mind.md`), evaluate them against
the latest point-in-time snapshot, and write `data/output/alerts/<as_of>.md`. Classify each tripwire
`FIRED` / `ARMED` / `UNAVAILABLE`; queue every `UNAVAILABLE` — never read missing data as "nothing
tripped," and never loosen a tripwire to avoid a firing. Alerts are signals, not orders. Honor the
kill switch (read-only when `halt: true`).

## Stage 6 — Decision & Action (paper-first; Gate B + Gate C)

Read `prompts/stage-6-decision-paper-action.md` and use the `paper-trade-executor` skill. Convert a
watchlist entry / Stage 5 alert into a trade memo, size it (reuse
`referenced-prompts/domain-finance/investing-research/finance_position_sizing_framework.md`), and pre-mortem it (reuse
`referenced-prompts/domain-finance/quant-fintech-data/finance_trading_strategy_premortem.md`).

1. **Enforce Gate B at order time.** Hand the order (with `stop`, `sizing_ref`, `premortem_ref`) to
   the skill's `check_risk_limits` / `place_order`. No order passes without sizing + pre-mortem + a
   passing cap check (≤2%/position with per-class override, ≤20%/class, ≤60% deployed). A REJECTED
   order is not placed — never loosen a cap to force a fill.
2. **Route to paper only (Gate C).** On a pass, route to the `PaperBrokerAdapter` for a deterministic
   fill and update `data/output/portfolio.json`. The `LiveBrokerAdapter` is disabled and never
   reached; treat `live_enabled: false` as immovable.
3. **Write the record.** Save the memo, sizing, pre-mortem, Gate B result, fill, and decision log to
   `data/output/orders/<as_of>.md`. Honor the kill switch (`halt: true` → no order, log no-action).
4. **Emit the prediction.** Write a `PRED-*` block (asset, direction, `probability` UP FRONT,
   `thesis_ref`, `patterns_fired` = validated patterns only, horizon, tripwires) and hand it to Stage 7.

See `skills/paper-trade-executor/references/risk_gate_enforcement.md`. (`scripts/brokers.py` is
implemented — `--config <dir>` loads the YAML, `--self-check` proves the gates. The `LiveBrokerAdapter`
stays a DISABLED stub that raises — never reach it.)

## Stage 3 — Pattern Knowledge Base (discover / validate / retire)

Read `prompts/stage-3-pattern-knowledge-base.md` and use the `pattern-knowledge-base`
skill. For any candidate pattern:

1. **Register first.** Copy `knowledge-base/patterns/PATTERN-TEMPLATE.md` to
   `PATTERN-<id>.md`, fill `hypothesis`, `feature_definition`, `sample_frame`, `base_rate`,
   and `registered_on` — BEFORE looking at outcomes. Set `status: hypothesis`.
2. **Test out-of-sample.** Split train/holdout; a pattern must beat its base rate on data it
   was not derived from. Record `in_sample_result` and `out_of_sample_result`.
3. **Apply Gate A.** Promote to `validated` only if `out_of_sample_result.n` ≥ the configured
   minimum AND lift is positive. Otherwise it stays `hypothesis`. Note multiple-comparisons,
   decay, and capacity. Retire patterns whose edge has decayed.
4. **Update `knowledge-base/INDEX.md`** to reflect status/confidence.

See `skills/pattern-knowledge-base/references/validation_discipline.md`.
`scripts/validate_pattern.py PATTERN-<id>.md` enforces Gate A in code (PASS/FAIL + unmet
conditions); `--self-check` proves the cases. It reports, never mutates — promotion stays your call.
Run `--reconcile knowledge-base/patterns --index knowledge-base/INDEX.md` to catch INDEX↔record
drift (F18); heed the non-blocking `! advisory:` warnings (high multiple-comparisons count,
`sample_frame` missing point-in-time/survivorship language) — they flag, but never change PASS/FAIL.

## Stage 7 — Journaling & Calibration (close the loop)

Read `prompts/stage-7-journaling-calibration.md` and use the `prediction-journal` skill.

1. **Log up front.** When you open a prediction, copy `knowledge-base/journal/PRED-TEMPLATE.md`
   to `PRED-<id>.md` and record `probability` (0–1) BEFORE the outcome is known. Link
   `patterns_fired` and set `tripwires` + `horizon`. Never edit `probability` afterward.
2. **Resolve at horizon.** Fill `resolution` and compute `brier_component = (probability − outcome)^2`.
3. **Update calibration.** Maintain the running Brier score and calibration report; compare
   stated probabilities to realized frequencies.
4. **Write back.** Push the resolved outcome to each linked `PATTERN-*` so Stage 3 can move it
   toward `validated` or `retired`.

See `skills/prediction-journal/references/brier_method.md`. `scripts/score_brier.py --prob P
--outcome 0|1` scores one prediction; `--calibration-report <journal_dir>` gives the running
Brier + calibration table + Gate C progress (now with `integrity` / `gate_c.integrity_clean`;
`unlock_ready` is False unless the journal is integrity-clean); `--self-check` reproduces the
worked example. Stamp each prediction at open with `journal_integrity.py --stamp PRED-<id>.md`
(writes the `lock_hash`), and audit with `--verify <journal_dir>` for tamper + resolution honesty.

## Final report to the user

- Patterns registered / promoted / retired this run, and why (cite the Gate A evidence).
- Alerts raised this sweep (FIRED tripwires + upcoming dated catalysts), and what was queued.
- Paper orders this run: FILLED / REJECTED / HALTED with Gate B reasons; current paper exposure
  (deployed % of capital, per-class). No real orders — `LiveBrokerAdapter` stays disabled (Gate C).
- Predictions opened and resolved; running Brier score and what it implies about Gate C
  progress (`<N>/100` resolved, current Brier vs. 0.18 target).
- Anything left honestly UNKNOWN or queued for data retrieval — never guessed.
