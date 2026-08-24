---
name: screen
description: Run the weekly research-and-screen slice (Stages 1, 2, 4) to turn the universe plus validated patterns into a ranked watchlist, enforcing Gate A. Use this command to refresh dossiers and the opportunity shortlist without touching the order path.
version: "1.0.0"
category: orchestration
tags: [investing, orchestration, screening, research, gate-a]
agents_used: [research-orchestrator]
---

# /screen — Research & Screen (Stages 1, 2, 4)

*For informational and research purposes only. Not financial, investment, or tax advice.
Nothing here places real-money trades.*

## Context

`/screen` runs the weekly research-and-screen slice of the loop and stops short of any action. It
hands control to `orchestrator_investment_research.md` with entry point = **weekly-research**, which
walks **Stage 1 (Universe & Data) → Stage 2 (Deep Research) → Stage 4 (Screening)**. Stage 3's
pattern status is **read** (to know which patterns are `validated`), but no new orders, sizing, or
monitoring happen here.

## Requirements

Optional focus: **$ARGUMENTS** (an asset class or `as_of` date) narrows the universe; default is
`config/asset_classes.yaml` and today's `as_of`. The orchestrator reads `config/mandate.yaml` first;
because this slice contains the action stage **4**, a `halt: true` kill switch drops Stage 4 and the
slice runs read-only (Stages 1–2 only).

## Stages routed & gates enforced

1. **Stage 1 (Universe & Data):** derive the universe from `config/asset_classes.yaml` filters;
   snapshot point-in-time data to `data/snapshots/<as_of>/`. Nothing dated after `as_of`;
   `UNAVAILABLE` fields are queued, never guessed.
2. **Stage 2 (Deep Research):** build `data/output/dossiers/<ticker>.md` from the snapshot only —
   thesis, bear/base/bull valuation range, dated catalysts, ranked risks, disconfirming test.
3. **Stage 4 (Screening):** **Gate A enforced** — score and rank candidates on **only `validated`
   patterns** weighted by confidence; `hypothesis`/`retired` patterns appear as unscored "paper-only
   signal" and never affect the rank. `UNAVAILABLE` data → "cannot score," never a silent pass.
   Output `data/output/watchlist.csv`.

Scripts this slice runs (gates enforced in code):

```bash
python skills/data-source-adapter/scripts/build_snapshot.py --as-of <as_of> --manual data/input --out data/snapshots
python skills/pattern-knowledge-base/scripts/screen_rank.py --firings firings.json --patterns-dir knowledge-base/patterns --out data/output/watchlist.csv
```

## Hand-off

Invoke `orchestrator_investment_research.md` with entry point = **weekly-research**, coordinated by
the `research-orchestrator` agent. The orchestrator critiques each stage's output against that
stage's verification checklist and emits the **Gate A statement**.

## Output Format

The run header, the Stage 1/2/4 route + checklist critique, the Gate A statement (validated count
used / hypothesis count excluded), and the ranked watchlist with its evidence trail.

## Kill-switch & safety note

This command never reaches Stage 6 — no sizing, no orders, no broker adapter. If `halt: true`, Stage
4 is dropped and only Stages 1–2 run read-only.
