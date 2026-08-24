---
name: decide
description: Convert one named candidate into a paper order (Stage 6) behind Gate B and Gate C — never real money. Use this command as /decide <ticker> to draft a trade memo, size it, pre-mortem it, run the order-time risk-limit check, route a paper fill, and emit a PRED-* prediction for the journal.
version: "1.0.0"
category: orchestration
tags: [investing, orchestration, paper-trading, gate-b, gate-c]
agents_used: [research-orchestrator]
---

# /decide &lt;ticker&gt; — Paper Decision & Action (Stage 6)

*For informational and research purposes only. Not financial, investment, or tax advice.
Nothing here places real-money trades.*

## Context

`/decide <ticker>` is the only command that can reach an order path — and it is **paper only**. It
hands control to `orchestrator_investment_research.md` with entry point = **decide-one**, which runs
**Stage 6** for the named ticker via the `paper-trade-executor` skill. Because this is the order
path, it carries the strongest gate enforcement in the toolkit.

## Requirements

Ticker: **$ARGUMENTS** — the symbol to act on (e.g. `/decide EXMP`). The candidate must already have
a dossier (`data/output/dossiers/<ticker>.md`) and the `validated` `PATTERN-*` ids that scored it in
Stage 4 (Gate A). The orchestrator reads `config/mandate.yaml` first: if `halt: true`, **no order is
placed** and the no-action decision is logged.

## Stages routed & gates enforced

**Stage 6 (Decision & Action):**

1. **Draft the trade memo** — ticker, asset_class, direction, entry, stop/exit, 1–2 line thesis,
   ranked key risks. `UNAVAILABLE` facts are queued, never filled with a favorable guess.
2. **Size it** (reuse `referenced-prompts/domain-finance/investing-research/finance_position_sizing_framework.md`) and
   **pre-mortem it** (reuse `referenced-prompts/domain-finance/quant-fintech-data/finance_trading_strategy_premortem.md`)
   — both are **Gate B** prerequisites.
3. **Enforce Gate B at order time** — hand the order (with `stop`, `sizing_ref`, `premortem_ref`) to
   the `paper-trade-executor` skill's `check_risk_limits` / `place_order`. Reject if no stop, no
   sizing, no pre-mortem, or any cap is breached (≤2% position with per-class override, ≤20% class,
   ≤60% deployed). **A REJECTED order is not placed — never loosen or hardcode a cap to force a fill.**
4. **Route to paper only (Gate C)** — on a pass, route to the `PaperBrokerAdapter` for a deterministic
   fill and update `data/output/portfolio.json`. The `LiveBrokerAdapter` is **disabled**
   (`live_enabled=false`) and is never reached or worked around.
5. **Emit the prediction** — write a `PRED-*` block (asset, direction, `probability` stated UP FRONT,
   `thesis_ref`, `patterns_fired` = validated only, horizon, tripwires) for Stage 7. Save the memo,
   sizing, pre-mortem, Gate B result, fill, and decision log to `data/output/orders/<as_of>.md`.

Scripts this command runs (Gate B + kill switch in code; live money unreachable):

```bash
python skills/paper-trade-executor/scripts/brokers.py --symbol <ticker> --asset-class <equity|crypto|options> \
  --side buy --quantity <Q> --price <P> --stop <STOP> \
  --sizing-ref data/output/orders/<as_of>.md#sizing --premortem-ref data/output/orders/<as_of>.md#premortem \
  --config config --portfolio data/output/portfolio.json
python skills/paper-trade-executor/scripts/brokers.py --report --config config --portfolio data/output/portfolio.json
```

## Hand-off

Invoke `orchestrator_investment_research.md` with entry point = **decide-one** and the ticker,
coordinated by the `research-orchestrator` agent. The orchestrator critiques the Stage 6 output
against the Stage 6 verification checklist and emits the **Gate B / Gate C statement**.

## Output Format

The run header, the trade memo, the sizing & pre-mortem summary, the **Gate B / Gate C statement**
(PASS/REJECTED + caps + `LiveBrokerAdapter` disabled + kill-switch status), the paper fill / decision
log, and the `PRED-*` handoff block.

## Kill-switch & safety note

Gate C is immovable here: the `LiveBrokerAdapter` stays disabled and `live_enabled: false` is never
treated as something to work around. If `halt: true`, no order is placed and the no-action decision
is logged. Only `validated` patterns (Gate A) may justify the decision; the prediction is a
calibrated probability over a defined outcome, not a point-estimate return.
