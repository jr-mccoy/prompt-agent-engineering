---
name: paper-trade-executor
description: Simulate order fills and track a paper portfolio behind a stable broker seam, enforcing the kill switch and Gate B risk limits at order time. Use this skill for "place a paper order", "size/check a trade against risk limits", "track paper positions / PnL", or "Stage 6 decision & action". Exposes two broker seams — PaperBrokerAdapter (an ACTIVE built-in simulator) and LiveBrokerAdapter (present but shipped DISABLED behind Gate C). Never executes real money and never fabricates a fill: an order that fails the kill switch or Gate B is HALTED/REJECTED with reasons, never silently filled.
license: MIT
compatibility: Standard library only. The PaperBrokerAdapter (builtin_simulator) is fully implemented (deterministic fills, position/portfolio tracking, kill-switch + Gate B checks). load_config now parses config/risk_limits.yaml + config/mandate.yaml using PyYAML if installed, else an embedded YAML-subset parser (so it runs with no dependencies). `--self-check` proves FILLED / 3x REJECTED / HALTED / Live-disabled. LiveBrokerAdapter remains a DISABLED stub that raises NotImplementedError until Gate C is met (>=100 resolved predictions, Brier <=0.18, manual live_enabled). The five DATA seams belong to the data-source-adapter skill, not here.
metadata:
  tags: [investing, trading, paper, simulation, broker, seam, gate-b, kill-switch, risk-limits, stub]
  updated: "2026-06-18"
---

# Paper Trade Executor

Provides the **execution seam** between Stage 6 and any venue: one stable interface for placing an
order, with a built-in paper simulator behind it so the whole decision/action stage runs — and
builds a track record — without a broker account or a cent of real money. This is the boundary
that keeps "where orders go" out of the stage prompt: Stage 6 drafts an order, hands it to an
adapter, and gets a normalized `Fill` back, whether that came from the paper simulator or (only
ever behind Gate C) a real broker.

## Purpose

Order placement is where optimism does the most damage, so it is wrapped in two order-time checks
and one hard lock:

| Seam | Backs | Status |
|---|---|---|
| `PaperBrokerAdapter` | simulated fills + paper portfolio tracking | **ACTIVE** (`builtin_simulator`) |
| `LiveBrokerAdapter` | real orders at a broker | **DISABLED** (Gate C) |

`config/data_sources.yaml` selects the implementation per seam. The paper simulator enforces the
kill switch (`mandate.yaml: halt`) and **Gate B** (position sizing + pre-mortem + risk limits from
`risk_limits.yaml`) on every order, then fills deterministically and updates the ledger. The live
adapter ships off and stays off until **Gate C** is met — and even then, enabling it is a separate,
explicit, human decision.

## When to Use This Skill

Use this skill when you need to:
- Place a **paper** order for a Stage 6 decision and get a `Fill` back
- Check a drafted order against the risk limits (Gate B) before committing to it
- Track paper positions, cash, and deployed exposure across runs (`data/output/portfolio.json`)
- Understand the order/fill/portfolio shapes Stage 6 produces and how they hand off to Stage 7

## When NOT to Use This Skill

Do NOT use this skill when:
- You want to place a **real** order → that is `LiveBrokerAdapter`, which is disabled by design (Gate C); there is no supported real-money path in this phase
- You need market / fundamentals / options data → that is the `data-source-adapter` skill
- You are deciding whether a signal is real → that is `pattern-knowledge-base` (Stage 3, Gate A)
- You are logging or Brier-scoring a prediction → that is `prediction-journal` (Stage 7)

## Prerequisites

- `config/mandate.yaml` (kill switch `halt`, `capital.simulated_usd`, the Gate C block)
- `config/risk_limits.yaml` (the three caps, per-class overrides, and the discipline flags)
- A drafted `Order` (Stage 6) carrying a `stop`, a `sizing_ref`, and a `premortem_ref` — Gate B
  rejects an order missing any of these
- For persistence: a writable `data/output/` (the ledger lives at `data/output/portfolio.json`)

## Quick Start

### Step 1: Size and risk-check a drafted order (Gate B, no fill)

**Purpose:** Know whether an order is admissible before you commit it.

1. Draft the `Order` (symbol, asset_class, side, quantity, price, `stop`, `sizing_ref`, `premortem_ref`).
2. Call `check_risk_limits(order, portfolio, limits)`; read `(passed, reasons)`.

**Validation:**
- [ ] `passed` is `True` only if the stop, sizing, and pre-mortem are present AND all three caps hold
- [ ] On failure, `reasons` names every breached cap/flag (nothing is hidden)

### Step 2: Place the paper order

**Purpose:** Route the order through the kill switch + Gate B, then a deterministic paper fill.

```bash
# Compliant equity buy: 100 x $5 = $500 = 1% of a $50k paper account -> FILLED.
python scripts/brokers.py --symbol EXMP --asset-class equity --side buy \
  --quantity 100 --price 5 --stop 4.25 \
  --sizing-ref data/output/orders/2026-06-18.md#sizing \
  --premortem-ref data/output/orders/2026-06-18.md#premortem
```

**Validation:**
- [ ] A blocked order returns `HALTED` (kill switch) or `REJECTED` (Gate B) and does **not** change the portfolio
- [ ] Only a `FILLED` order mutates cash/positions and (without `--no-save`) persists the ledger

### Step 3: Read the paper portfolio

**Purpose:** Track positions, cash, and deployed exposure across runs.

1. Load `data/output/portfolio.json` (or `Portfolio.load(path)`).
2. Use `deployed_notional()`, `class_notional(cls)`, `position_notional(sym)` to see exposure
   against `capital_base`, or print the read-only report:

```bash
# Read-only: deployed / per-class / per-position exposure vs the Gate B caps. Writes nothing.
python scripts/brokers.py --report --config ../../config --portfolio ../../data/output/portfolio.json
```

**Validation:**
- [ ] Deployed / capital_base ≤ 0.60; each class ≤ 0.20; each position ≤ its (lower) per-class cap
- [ ] `capital_base` is unchanged by trading (deploying cash moves value into positions)

## Common Issues

### Issue: My order was REJECTED with a cap reason
Gate B is working. The `reasons` list names the breached cap (per-position / per-class / deployed)
and shows the computed fraction vs. the limit. Reduce size or free exposure — do **not** loosen the
cap to force the order through.

### Issue: My order was REJECTED for "no stop / sizing / pre-mortem"
The discipline flags in `risk_limits.yaml` (`require_stop_loss`, `reject_if_unsized`,
`reject_if_no_premortem`) are set. Attach the `stop`, `sizing_ref`, and `premortem_ref` from the
Stage 6 trade memo. These are not optional — they are the point of Gate B.

### Issue: I want to place a real order
You cannot in this phase. `LiveBrokerAdapter.place_order` raises `NotImplementedError` by design.
Real money is unlocked only by Gate C (≥100 resolved predictions, Brier ≤ 0.18, manual enable) and
then only behind a separately-implemented, human-approved real-broker branch.

## Safety & Constraints

**NEVER:**
- Place or simulate a real-money order — `LiveBrokerAdapter` stays disabled (Gate C)
- Fabricate a fill — an order that fails the kill switch or Gate B is HALTED/REJECTED, never filled
- Bypass, loosen, or hardcode a risk limit to make an order pass — thresholds come from config
- Mutate the portfolio for a HALTED or REJECTED order

**ALWAYS:**
- Check the kill switch (`halt`) first, then Gate B, before any fill
- Read every threshold from the parsed `risk_limits.yaml` / `mandate.yaml`
- Carry provenance: `sizing_ref`, `premortem_ref`, and the `reasons` for any block
- Emit the `PRED-*` handoff so Stage 7 can journal and Brier-score the decision

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/broker_interface.md` | The seam contract: `place_order` flow, PaperBrokerAdapter (active) vs LiveBrokerAdapter (disabled), manual order intake, what is a stub |
| `references/order_schema.md` | Normalized `Order` / `Fill` / `Position` / `Portfolio` shapes, the order lifecycle states, and the `PRED-*` handoff mapping |
| `references/risk_gate_enforcement.md` | Order-time enforcement: kill switch, the exact Gate B algorithm (caps + discipline flags), and the Gate C lock |
| `scripts/brokers.py` | The simulator: PaperBrokerAdapter (implemented) + LiveBrokerAdapter (disabled stub) + `check_halt` / `check_risk_limits` + `exposure_report` + `load_config` + a CLI (`--config`, `--report`, `--halt`, `--self-check`) |

## Related Skills

- `data-source-adapter` — supplies the point-in-time data the decision was built on (Stages 1, 2, 5)
- `pattern-knowledge-base` — only `validated` patterns (Gate A) reach a Stage 6 decision (Stage 3)
- `prediction-journal` — scores the `PRED-*` this skill emits; its Brier feeds Gate C (Stage 7)

## Reused repo prompts (referenced by path)

- Stage 6 driver: `ai-investment-research-toolkit/prompts/stage-6-decision-paper-action.md`
- Position sizing: `referenced-prompts/domain-finance/investing-research/finance_position_sizing_framework.md`
- Pre-mortem: `referenced-prompts/domain-finance/quant-fintech-data/finance_trading_strategy_premortem.md`
