# Broker Interface — the execution seam contract

*For informational and research purposes only. Not financial, investment, or tax advice.
NOTHING here places real-money trades.*

Stage 6 routes a drafted order through a **broker seam** and gets a `Fill` back, without knowing
or caring whether the venue is the built-in paper simulator or (someday, behind Gate C) a real
broker. This document is the authoritative description of that contract; `scripts/brokers.py` is
its Python expression. Two rules dominate everything else:

1. **No real-money execution.** The only active adapter is the in-process `PaperBrokerAdapter`.
   `LiveBrokerAdapter` ships **disabled** and stays disabled until **Gate C** is met (≥100 resolved
   journaled predictions AND running Brier ≤ 0.18 AND a manual `live_enabled: true`). Even calling
   its `place_order` is a hard stop (`NotImplementedError`).
2. **No fabricated fill.** Every routed order returns a `Fill`, but an order that fails the kill
   switch or Gate B comes back `HALTED` / `REJECTED` with reasons and **does not touch the
   portfolio**. The simulator never invents a successful fill to look good.

## The two seams

| Seam | Backs | Status | Selected by |
|---|---|---|---|
| `PaperBrokerAdapter` | simulated fills + paper portfolio | **ACTIVE** | `config/data_sources.yaml: PaperBrokerAdapter.implementation: builtin_simulator` |
| `LiveBrokerAdapter` | real orders at a broker | **DISABLED** (Gate C) | `config/data_sources.yaml: LiveBrokerAdapter.enabled: false` |

## The contract

```python
class PaperBrokerAdapter:           # ACTIVE
    seam = "PaperBrokerAdapter"
    def __init__(self, mandate: dict, limits: dict): ...
    def place_order(self, order: Order, portfolio: Portfolio) -> Fill:
        """Route ONE order: kill switch -> Gate B -> deterministic paper fill at order.price.
        Returns a Fill (FILLED | REJECTED | HALTED). Only a FILLED order mutates the portfolio."""

class LiveBrokerAdapter:            # DISABLED — present by design, off by design (Gate C)
    seam = "LiveBrokerAdapter"
    def __init__(self, mandate: dict, enabled: bool = False): ...
    def gate_c_status(self, resolved_predictions: int, brier: float | None) -> tuple[bool, list]:
        """Report whether ALL THREE Gate C conditions are met. Does NOT enable anything."""
    def place_order(self, order: Order, portfolio: Portfolio) -> Fill:
        """Real execution — raises NotImplementedError until Gate C + a manual implementation."""
```

Read helpers on `Portfolio` expose exposure for the gate: `deployed_notional()`,
`class_notional(asset_class)`, `position_notional(symbol)` — all denominated against
`capital_base` (the fixed simulated account size; see `order_schema.md`).

## Order flow (what `place_order` does, in order)

1. **Kill switch** (`check_halt(mandate)`): if `halt: true`, return a `HALTED` Fill, no fill.
2. **Gate B** (`check_risk_limits(order, portfolio, limits)`): discipline checks (stop, sizing,
   pre-mortem) + the three percentage caps. On any failure, return a `REJECTED` Fill with the
   list of breached reasons, no fill. (Full algorithm: `risk_gate_enforcement.md`.)
3. **Fill**: deterministic fill at `order.price` (no slippage model in v1), update cash/positions,
   return a `FILLED` Fill. Stage 6 then writes `data/output/orders/<date>.md` and persists the
   ledger to `data/output/portfolio.json`.

## Manual order intake (no live broker needed)

The paper simulator does not read external feeds — Stage 6 hands it an `Order` it drafted. For a
file-driven run you may stage orders as JSON/CSV under `data/input/orders/` and load them into the
`Order` shape before calling `place_order`; the simulator treats them identically. Any field that
cannot be sourced is recorded in the order's `unavailable` list and **queued, never guessed** —
and an order missing a Gate-B-required field (stop / sizing / pre-mortem) is rejected, not filled.

## What is a stub in Phase 3

| Piece | Phase 3 status |
|---|---|
| Kill switch check (`check_halt`) | **implemented** (stdlib) |
| Gate B risk-limit check (`check_risk_limits`) | **implemented** (stdlib) |
| Paper fill + portfolio tracking + persistence (`PaperBrokerAdapter`, `Portfolio`) | **implemented** (stdlib) |
| `LiveBrokerAdapter.place_order` (real orders) | **DISABLED stub** — raises `NotImplementedError` (Gate C) |
| `load_config()` (parse `risk_limits.yaml` / `mandate.yaml`) | **stub** — needs pyyaml; pass parsed dicts for now |

The contract above is stable; only the *backing* of the live seam changes if Gate C is ever met —
and that is a separate, explicit, human-approved decision, not a config toggle.
