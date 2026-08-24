---
title: "Orchestrator — Investment Research Loop (classify state → run stages → enforce gates)"
category: investment-research/orchestration
description: "The master loop for the paper-first investment research toolkit. Reads config FIRST (kill switch, live lock, cadence), classifies the entry point (daily monitor / weekly research / full run / decide-one), routes through Stages 0→7 in the right order, and enforces the hard gates between stages — Gate A before Stage 4 scoring, Gate B before any Stage 6 order, Gate C keeps the live adapter disabled — plus the kill switch that halts Stages 4–6. Critiques each stage's output against that stage's own verification checklist before advancing. Never places real money; never fabricates data."
techniques:
  - CM-02
  - DS-02
  - QA-04
  - QA-05
  - NE-10
  - RT-06
difficulty: advanced
tags:
  - orchestration
  - master-loop
  - gate-enforcement
  - kill-switch
  - cadence
  - paper-first
updated: "2026-06-18"
related_prompts:
  - ai-investment-research-toolkit/prompts/stage-0-mandate-config.md
  - ai-investment-research-toolkit/prompts/stage-1-universe-data-sourcing.md
  - ai-investment-research-toolkit/prompts/stage-2-deep-research.md
  - ai-investment-research-toolkit/prompts/stage-3-pattern-knowledge-base.md
  - ai-investment-research-toolkit/prompts/stage-4-screening.md
  - ai-investment-research-toolkit/prompts/stage-5-monitoring-tripwires.md
  - ai-investment-research-toolkit/prompts/stage-6-decision-paper-action.md
  - ai-investment-research-toolkit/prompts/stage-7-journaling-calibration.md
  - ai-investment-research-toolkit/skills/data-source-adapter/SKILL.md
  - ai-investment-research-toolkit/skills/pattern-knowledge-base/SKILL.md
  - ai-investment-research-toolkit/skills/prediction-journal/SKILL.md
  - ai-investment-research-toolkit/skills/paper-trade-executor/SKILL.md
---

*For informational and research purposes only. Not financial, investment, or tax advice.
Nothing here places real-money trades. All outputs require independent verification.*

## Objective

Drive the full toolkit as one coordinated loop while keeping every high-risk surface gated.
Given an entry point, the orchestrator (1) reads `config/mandate.yaml` **first** to learn the kill
switch (`halt`), the live lock (`live_enabled`), and the cadence; (2) classifies what kind of run
this is; (3) routes through the correct stages in the correct order; (4) **enforces the gates
between stages, not by trust** — Gate A (only `validated` patterns score in Stage 4), Gate B (no
order without sizing + pre-mortem + a passing risk-limit check), Gate C (`LiveBrokerAdapter` stays
disabled — paper only); (5) **critiques each stage's output against that stage's own verification
checklist** before advancing; and (6) emits one consolidated run report. It coordinates the stage
prompts and skills — it does not re-implement them, and it never relaxes a gate to make progress.

## When to Use

- Running a full cadence pass (Stages 0→7) — the `/investment-run` entry point
- Running the weekly research-and-screen slice (Stages 1, 2, 4) — the `/screen` entry point
- Running the daily monitor sweep (Stage 5) — the `/monitor` entry point
- Acting on one named candidate on paper (Stage 6) — the `/decide <ticker>` entry point
- Any time you need a single front door that classifies state and enforces the gates + kill switch

## Inputs / Context Required

**Config (read FIRST, before any stage)**
- `config/mandate.yaml` — `capital.simulated_usd`, the kill switch `halt`, the cadence, and the
  Gate C block (`live_enabled` + the ≥100-resolved / Brier ≤ 0.18 thresholds)
- `config/risk_limits.yaml` — the three caps (≤2% position, ≤20% class, ≤60% deployed) + per-class
  overrides and the discipline flags (`reject_if_unsized`, `reject_if_no_premortem`, `require_stop_loss`)
- `config/asset_classes.yaml` — active classes + universe filters (Stage 1 scope)
- `config/data_sources.yaml` — which adapter implementation backs each seam (live vs. manual)

**Durable memory & working tree**
- `knowledge-base/patterns/PATTERN-*.md` + `knowledge-base/INDEX.md` — pattern status/confidence (Gate A)
- `knowledge-base/journal/PRED-*.md` — predictions + running Brier (Gate C progress)
- `data/snapshots/<date>/`, `data/output/{dossiers,watchlist.csv,alerts,orders,portfolio.json}`

**The stage prompts and skills** are the implementation; the orchestrator routes to them by path
(see `related_prompts`). The `PaperBrokerAdapter` is active; the `LiveBrokerAdapter` is disabled.

**Gates are enforced by running these scripts, not by trust** (each carries a `--self-check`):

| Gate / stage | Script (run from the toolkit root) |
|---|---|
| Stage 1 snapshot (immutable, look-ahead-safe) | `skills/data-source-adapter/scripts/build_snapshot.py --as-of <d> --manual data/input --out data/snapshots` |
| Stage 3 — **Gate A** per pattern | `skills/pattern-knowledge-base/scripts/validate_pattern.py knowledge-base/patterns/PATTERN-<id>.md` |
| Stage 4 — **Gate A** at rank time | `skills/pattern-knowledge-base/scripts/screen_rank.py --firings firings.json --patterns-dir knowledge-base/patterns --out data/output/watchlist.csv` |
| Stage 6 — **Gate B** + kill switch (paper fill) | `skills/paper-trade-executor/scripts/brokers.py --symbol … --config config --portfolio data/output/portfolio.json` |
| Stage 6 — exposure report (read-only) | `skills/paper-trade-executor/scripts/brokers.py --report --config config --portfolio data/output/portfolio.json` |
| Stage 7 — Brier + **Gate C** progress | `skills/prediction-journal/scripts/score_brier.py --calibration-report knowledge-base/journal/` |

## Constraints

### Must
- Read `config/mandate.yaml` **before any stage** and surface `halt`, `live_enabled`, and the
  cadence in the run header (CM-02).
- Honor the **kill switch**: if `halt: true`, run no action stage (4, 5, 6); Stages 0–3 and 7 may
  proceed read-only. Log the no-action decision.
- Enforce **Gate A** before Stage 4 scoring: only `validated` patterns score and rank; `hypothesis`
  and `retired` patterns appear as unscored signals only (CM-02 — Gate A).
- Enforce **Gate B** before any Stage 6 order: require a sizing output, a pre-mortem, and a passing
  cap check at order time; a `REJECTED` order is not placed (CM-02 — Gate B).
- Keep **Gate C** intact: route orders to the `PaperBrokerAdapter` only; the `LiveBrokerAdapter`
  stays disabled (`live_enabled=false` → paper only) and is never reached.
- **Critique each stage's output against that stage's own Verification checklist** and report
  PASS / fix-needed before advancing to the next stage (QA-04).
- Queue every `UNAVAILABLE` input; never guess a value to keep the loop moving (DS-02, QA-05).

### Must Not
- Reach, enable, or simulate the `LiveBrokerAdapter`, or treat `live_enabled: false` / `halt: true`
  as something to work around (the single most important rule of the loop).
- Loosen, skip, or reorder a gate to advance a stage; a failing gate stops that stage's progress.
- Let any `hypothesis`-status pattern contribute to a Stage 4 score or a Stage 6 decision (Gate A).
- Advance a stage whose verification checklist did not pass — fix or queue, then re-check.
- Invent prices, fills, catalysts, or pattern firings where data is `UNAVAILABLE` (DS-02, QA-04).
- State a point-estimate return; predictions are calibrated probabilities over defined outcomes (NE-10).

## Instructions

1. **Read config + classify the entry point (CM-02).** Load `config/mandate.yaml` first. Read
   `halt`, `live_enabled`, the cadence, and `capital.simulated_usd`. Then classify the run:
   - **full-run** (`/investment-run`) → Stages 0→1→2→3→4→5→6→7 (weekly research + daily monitor folded in)
   - **weekly-research** (`/screen`) → Stages 1, 2, 4 (Stage 3 read for `validated` status; no new orders)
   - **daily-monitor** (`/monitor`) → Stage 5 only
   - **decide-one** (`/decide <ticker>`) → Stage 6 only, for the named ticker
   If `halt: true`, drop every action stage (4, 5, 6) from the route immediately and note it.

2. **Route by cadence (CM-02).** Walk the routed stages in order, invoking each stage prompt with
   its required inputs (above). Stage 3 (pattern KB) and Stage 7 (journaling) fold in whenever new
   dossiers/evidence or resolved predictions exist — they may run read-only even under `halt`.
   Hand specialist stages to their agents where available: Stage 3 → `pattern-miner`, Stage 5 →
   `monitor-agent`, the overall loop → `research-orchestrator`.

3. **Enforce Gate A before Stage 4 scoring (CM-02 — Gate A).** Before screening, confirm pattern
   status with `validate_pattern.py` and score the universe with `screen_rank.py` (above): it counts
   **only `validated` patterns** that PASS toward a candidate's score and rank and emits
   `hypothesis`/`retired` firings as unscored "paper-only signal." Emit the **Gate A statement**
   (validated count used / hypothesis count excluded). `UNAVAILABLE` data → "cannot score," never a
   silent pass.

4. **Enforce Gate B before any Stage 6 order (CM-02 — Gate B).** Require a position-sizing output
   (`finance_position_sizing_framework.md`) and a pre-mortem (`finance_trading_strategy_premortem.md`)
   before order time. Route the order (with `stop`, `sizing_ref`, `premortem_ref`) through
   `brokers.py --config config` (above): the kill switch and Gate B run before any fill and a
   `REJECTED`/`HALTED` Fill is not placed and never mutates the ledger (no stop / no sizing / no
   pre-mortem / any cap breached → REJECTED). Never adjust a cap to force a fill. Emit the
   **Gate B / Gate C statement**.

5. **Hold Gate C + the kill switch (CM-02).** On a Gate B pass, route to the `PaperBrokerAdapter`
   only and update `data/output/portfolio.json`. The `LiveBrokerAdapter` stays disabled
   (`live_enabled=false` → paper only) and is never reached. If `halt: true`, no order is placed and
   the no-action decision is logged. Every Stage 6 decision (taken or declined) emits a `PRED-*`
   block to Stage 7 with `probability` stated up front and only `validated` `patterns_fired`.

6. **Critique each stage's output against its own checklist (QA-04).** After each stage, re-run that
   stage prompt's **Verification** checklist as an acceptance gate. Report PASS or the specific item
   that failed; if an item fails, fix or queue the gap (`UNAVAILABLE`) and re-check — do not advance
   on a failed checklist. This is how the orchestrator keeps the stages honest.

7. **Emit the consolidated run report.** Summarize the run (format below): patterns
   registered/promoted/retired with Gate A evidence; alerts FIRED + items queued; paper orders
   FILLED/REJECTED/HALTED with Gate B reasons and current exposure; predictions opened/resolved with
   the running Brier and `<N>/100` Gate C progress; and anything left honestly UNKNOWN or queued.

## Output Format

```
## INVESTMENT RUN: as_of [date] | entry=[full-run|screen|monitor|decide] | halt=[t/f] | live_enabled=false
```

### Run header (config read first)
| Field | Value |
|---|---|
| Entry point / cadence | [full-run / weekly-research / daily-monitor / decide-one] |
| Kill switch (`halt`) | [false → action stages run / true → Stages 4–6 dropped, read-only] |
| Gate C (`live_enabled`) | false — `LiveBrokerAdapter` disabled (paper only) |
| Capital (simulated) | $… | Stages routed | [e.g. 1,2,4 / 5 / 6 / 0–7] |

### Stage route + checklist critique
| Stage | Ran? | Verification checklist | Verdict |
|---|---|---|---|
| 0 Mandate / 1 Universe / 2 Research / 3 Pattern KB / 4 Screen / 5 Monitor / 6 Decision / 7 Journal | yes/no/skipped(halt) | [PASS / item that failed] | advance / fix / queued |

### Gate A statement (before Stage 4 scoring)
- Patterns used for scoring: [only `validated` — count] · Excluded: [hypothesis/retired count]
- Kill switch (`halt`): [false → watchlist emitted / true → read-only]

### Gate B / Gate C statement (if Stage 6 ran)
- Gate B check: [PASS / REJECTED / N/A] · Reasons: [breached caps/flags, or "none"]
- Caps at order time: position [x.xx% ≤ cap] · class [x.xx% ≤ 20%] · deployed [x.xx% ≤ 60%]
- Gate C: `LiveBrokerAdapter` disabled (live_enabled=false) — paper only
- Kill switch (`halt`): [false → order routed / true → no action logged]

### Consolidated report
- **Patterns:** registered / promoted / retired this run + the Gate A evidence (OOS n, lift vs. base rate).
- **Alerts:** FIRED tripwires + upcoming dated catalysts; everything `UNAVAILABLE` queued.
- **Paper orders:** FILLED / REJECTED / HALTED with Gate B reasons; current exposure (deployed %, per-class).
  No real orders — `LiveBrokerAdapter` stays disabled (Gate C).
- **Predictions:** opened and resolved; running Brier and Gate C progress (`<N>/100` resolved, Brier vs. 0.18).
- **Left UNKNOWN / queued:** anything not resolvable from real data — never guessed.

## Verification

- [ ] `config/mandate.yaml` was read before any stage; `halt`, `live_enabled`, and cadence are in the header.
- [ ] Entry point classified and only the correct stages were routed for that cadence.
- [ ] Kill switch honored: `halt: true` → no Stages 4–6; Stages 0–3/7 read-only; no-action logged.
- [ ] Gate A enforced before Stage 4: only `validated` patterns scored; the Gate A statement was emitted.
- [ ] Gate B enforced before any Stage 6 order: sizing + pre-mortem + cap check; REJECTED orders not placed.
- [ ] Gate C intact: orders routed only to `PaperBrokerAdapter`; `LiveBrokerAdapter` never reached.
- [ ] Each stage's own verification checklist was re-run; no stage advanced on a failed checklist.
- [ ] `UNAVAILABLE` inputs were queued, never guessed; no point-estimate return claims.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| The loop runs an action stage while halted | Read `halt` first; `halt: true` drops Stages 4–6 from the route and logs no-action |
| A hypothesis pattern inflates a Stage 4 rank | Gate A: only `validated` patterns score; hypotheses are unscored signals |
| An order is placed without sizing or a pre-mortem | Gate B at order time rejects on `reject_if_unsized` / `reject_if_no_premortem` |
| A cap is loosened to make a candidate "fit" | Gate B checks position/class/deployed against `risk_limits.yaml`; REJECTED names the breach |
| The live adapter is reached "just to test the path" | Gate C: `LiveBrokerAdapter` disabled (`live_enabled=false`); orders route to paper only |
| A stage advances despite a failed check | Each stage's own Verification checklist is re-run as an acceptance gate before advancing |
| A missing value is filled to keep the loop moving | `UNAVAILABLE` is queued; "cannot score / cannot size," never a silent pass (DS-02, QA-05) |
| The run report sells a forecasted return | Predictions are calibrated probabilities over defined outcomes, not point returns (NE-10) |
