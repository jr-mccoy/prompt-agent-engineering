---
name: monitor
description: Run the daily monitor sweep (Stage 5) over the watchlist and open paper positions, evaluating tripwires against the latest point-in-time snapshot. Use this command for the daily/24-7 early-warning pass; it raises alerts, never orders.
version: "1.0.0"
category: orchestration
tags: [investing, orchestration, monitoring, tripwires, kill-switch]
agents_used: [monitor-agent]
---

# /monitor — Daily Tripwire Sweep (Stage 5)

*For informational and research purposes only. Not financial, investment, or tax advice.
Nothing here places real-money trades.*

## Context

`/monitor` runs the daily monitor/tripwire sweep — the early-warning layer that also covers crypto's
24/7 market. It hands control to `orchestrator_investment_research.md` with entry point =
**daily-monitor**, which runs **Stage 5 only**, coordinated by the `monitor-agent`. It reads the
watchlist and open paper positions and evaluates each name's tripwires against the latest snapshot.
Alerts are signals; this command never sizes or places a trade.

## Requirements

Optional focus: **$ARGUMENTS** (a ticker or `as_of` date) narrows the sweep; default is the full
`data/output/watchlist.csv` plus open positions in `data/output/portfolio.json` at today's `as_of`.
The orchestrator reads `config/mandate.yaml` first; if `halt: true`, the sweep runs **read-only**
(alerts may still be written, but no downstream action is taken).

## Stages routed & gates enforced

1. **Stage 5 (Monitor & Tripwires):** for each watchlist name and open paper position, build a dated
   catalyst map and explicit thesis-break tripwires, evaluate them against the latest **point-in-time**
   snapshot, and classify each tripwire `FIRED` / `ARMED` / `UNAVAILABLE`. Queue every `UNAVAILABLE`
   — never read missing data as "nothing tripped," and never loosen a tripwire to avoid a firing.
   Output `data/output/alerts/<as_of>.md`.

No order path is reached. **Gate B / Gate C / Stage 6 are out of scope here** — a fired tripwire is a
candidate for `/decide`, not an order. The **kill switch** holds: read-only when `halt: true`.

Scripts this sweep runs (point-in-time reads + read-only exposure; no order path):

```bash
python skills/data-source-adapter/scripts/adapters.py --seam MarketDataAdapter --key <ticker> --as-of <as_of> --manual data/input
python skills/paper-trade-executor/scripts/brokers.py --report --config config --portfolio data/output/portfolio.json
```

## Hand-off

Invoke `orchestrator_investment_research.md` with entry point = **daily-monitor**, coordinated by the
`monitor-agent`. The orchestrator critiques the Stage 5 output against the Stage 5 verification
checklist.

## Output Format

The run header, the Stage 5 alert report (FIRED tripwires + upcoming dated catalysts + queued
`UNAVAILABLE` items), and the checklist critique. A FIRED tripwire is surfaced as a candidate to hand
to `/decide <ticker>` — not as an order.

## Kill-switch & safety note

Stage 5 never sizes or places a trade. Alerts are signals, not predictions or orders. If `halt:
true`, the sweep is read-only.
