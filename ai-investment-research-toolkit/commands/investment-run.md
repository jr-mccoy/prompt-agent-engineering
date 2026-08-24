---
name: investment-run
description: Run a full cadence pass of the paper-first investment research loop (Stages 0→7), enforcing Gate A, Gate B, Gate C, and the kill switch. Use this command to run the complete weekly research-and-screen plus the daily monitor and any paper decisions in one coordinated pass.
version: "1.0.0"
category: orchestration
tags: [investing, orchestration, paper-trading, gate-enforcement, kill-switch]
agents_used: [research-orchestrator, pattern-miner, monitor-agent]
---

# /investment-run — Full Cadence Pass

*For informational and research purposes only. Not financial, investment, or tax advice.
Nothing here places real-money trades.*

## Context

`/investment-run` is the front door to the whole loop. It hands control to
`orchestrator_investment_research.md`, which reads `config/mandate.yaml` first (kill switch, live
lock, cadence), classifies this as a **full-run**, and walks Stages 0→7 in order: Mandate → Universe
& Data → Deep Research → Pattern KB → Screening → Monitor & Tripwires → Decision & Action → Journaling
& Calibration. It does not re-implement any stage — it routes to the stage prompts and skills and
enforces the gates between them.

## Requirements

Optional focus: **$ARGUMENTS** (e.g. an asset class or a date) narrows the run; with no arguments the
orchestrator uses `config/asset_classes.yaml` and today's `as_of`. The run always begins by reading
`config/mandate.yaml`; if `halt: true`, all action stages (4, 5, 6) are dropped and only the
research/journaling stages run read-only.

## Stages routed & gates enforced

1. **Stage 0–2 (Mandate → Universe → Research):** validate config, snapshot point-in-time data, build
   per-candidate dossiers. No fabricated values — `UNAVAILABLE` inputs are queued.
2. **Stage 3 (Pattern KB) via `pattern-miner`:** register-before-outcome; promote to `validated` only
   on an out-of-sample test ≥ the configured minimum (**Gate A** preparation).
3. **Stage 4 (Screening):** **Gate A enforced** — only `validated` patterns score and rank;
   `hypothesis`/`retired` patterns appear as unscored signals.
4. **Stage 5 (Monitor) via `monitor-agent`:** evaluate tripwires against the latest snapshot; alerts
   are signals, not orders.
5. **Stage 6 (Decision & Action):** **Gate B enforced** — no order without sizing + pre-mortem + a
   passing cap check; **Gate C** keeps the `LiveBrokerAdapter` disabled (paper only).
6. **Stage 7 (Journaling):** log/resolve predictions, update the running Brier and Gate C progress.

The **kill switch** (`mandate.yaml: halt: true`) stops Stages 4–6 instantly; Stages 0–3 and 7 may
continue read-only.

Each gate is enforced by running its skill script (`build_snapshot.py`, `validate_pattern.py`,
`screen_rank.py`, `brokers.py --config config`, `score_brier.py`) — see the "scripts the orchestrator
invokes" table in `orchestrator_investment_research.md`. A full worked run on the tracked fixtures is
in [`DRY_RUN.md`](../DRY_RUN.md).

## Hand-off

Invoke `orchestrator_investment_research.md` with entry point = **full-run**. Coordinate the
`research-orchestrator` agent for the loop, `pattern-miner` for Stage 3, and `monitor-agent` for
Stage 5. The orchestrator critiques each stage's output against that stage's own verification
checklist before advancing.

## Output Format

The orchestrator's consolidated run report: the run header (config read first), the stage route +
checklist critique, the Gate A and Gate B/Gate C statements, and the consolidated summary (patterns,
alerts, paper orders, predictions + Brier/Gate C progress, anything left UNKNOWN/queued).

## Kill-switch & safety note

`live_enabled` stays `false` and the `LiveBrokerAdapter` is never reached — this command cannot place
real money. If `halt: true`, no action stage runs and the no-action decision is logged.
