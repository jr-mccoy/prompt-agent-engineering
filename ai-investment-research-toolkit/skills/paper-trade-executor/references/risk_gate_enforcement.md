# Order-Time Enforcement — kill switch, Gate B, and the Gate C lock

*For informational and research purposes only. Not financial, investment, or tax advice.*

Two checks run at order time, in this order, before any paper fill. A third (Gate C) is the lock
that keeps real execution off entirely. Every threshold is **read from the parsed config**
(`config/risk_limits.yaml`, `config/mandate.yaml`) — never hardcoded — so tuning a cap is a config
edit, not a code change.

## 0. Kill switch (first, unconditional)

`check_halt(mandate)` reads `mandate.yaml: halt`. If `true`, the order is `HALTED` immediately —
no sizing logic, no fill. The kill switch stops all action stages (4–6); research and journaling
may continue read-only. This is the single global off switch.

## 1. Gate B — order safety (every order, before any paper fill)

`check_risk_limits(order, portfolio, limits)` returns `(passed, reasons)`. An order passes only if
it clears **every** check. Reasons name each breach for the audit trail.

### Discipline checks (read from `risk_limits.yaml`)

| Limit key | Rule |
|---|---|
| `require_stop_loss: true` | reject if `order.stop` is missing — every order declares a stop / exit |
| `reject_if_unsized: true` | reject if `order.sizing_ref` is empty — no order without position-sizing output |
| `reject_if_no_premortem: true` | reject if `order.premortem_ref` is empty — no order without a pre-mortem |

### Percentage caps (all denominated against `portfolio.capital_base`, evaluated POST-order)

| Cap key | Rule |
|---|---|
| `max_position_pct` (0.02) + `per_asset_class.<class>.max_position_pct` | per-position cap = **the LOWER of** the portfolio cap and the per-class override. Defaults: equity 0.02, crypto 0.01, options 0.005. `(existing position notional + order notional) / capital_base ≤ cap` |
| `max_asset_class_pct` (0.20) | `(existing class notional + order notional) / capital_base ≤ 0.20` |
| `max_deployed_pct` (0.60) | `(deployed notional + order notional) / capital_base ≤ 0.60` |

Plus a paper-account sanity check: a buy cannot deploy more than free `cash`. A `sell` reduces
exposure and skips the caps, but cannot exceed the held quantity (no naked shorts in the paper
sim v1).

### Worked example (capital_base = $50,000)

- Buy 100 × $5 = **$500** equity → 1.0% of capital → **passes** (≤ 2% position, ≤ 20% class, ≤ 60% deployed).
- Buy 500 × $5 = **$2,500** equity → 5.0% → **REJECTED**: `per-position cap ... > limit 0.0200`.
- Buy 750 × $1 = **$750** crypto → 1.5% → **REJECTED**: crypto per-class cap is 0.01 (lower wins).
- Any of the above with no `stop` / `sizing_ref` / `premortem_ref` → **REJECTED** on the discipline check(s).

## 2. Gate C — real-money unlock (the lock, not a runtime check)

`LiveBrokerAdapter` is **disabled by design** and its `place_order` raises `NotImplementedError`.
`gate_c_status(resolved_predictions, brier)` reports whether **all three** conditions hold — it
does **not** enable anything:

| Gate C condition (from `mandate.yaml: gate_c`) | Default |
|---|---|
| `min_resolved_predictions` | ≥ 100 resolved, journaled predictions |
| `max_brier_score` | running Brier ≤ 0.18 |
| `require_manual_enable` / `live_enabled` | a human sets `live_enabled: true` AND `data_sources.yaml: LiveBrokerAdapter.enabled: true` by hand |

Even with all three met, enabling real execution requires implementing a real-broker branch behind
per-trade human approval — a separate, explicit decision (ARCHITECTURE §13 step 7). Until then,
every order routes to `PaperBrokerAdapter`.

## Order of operations (authoritative)

```
place_order(order, portfolio):
    if check_halt(mandate):            -> Fill(HALTED)    # kill switch, no fill
    passed, reasons = check_risk_limits(order, portfolio, limits)
    if not passed:                     -> Fill(REJECTED, reasons)   # Gate B, no fill
    apply deterministic fill at order.price; update portfolio
                                       -> Fill(FILLED)
```

No path reaches a real venue. No blocked order ever mutates the portfolio.
