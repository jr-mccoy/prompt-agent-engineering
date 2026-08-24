# Order Schema — normalized shapes, lifecycle, and the Stage 7 handoff

*For informational and research purposes only. Not financial, investment, or tax advice.*

Stage 6 and the broker simulator pass four normalized shapes. They are the Python `@dataclass`es
in `scripts/brokers.py`; this document is their authoritative description. Units are explicit in
field names where ambiguous (`_usd`, `_pct`); a value that cannot be sourced goes in `unavailable`
and is **queued, never guessed**.

## `Order` — what Stage 6 drafts (before any gate runs)

```yaml
order_id: "ORD-20260618120000"
timestamp: "2026-06-18T12:00:00+00:00"   # ISO-8601 UTC, when drafted
symbol: "EXMP"
asset_class: "equity"                    # equity | crypto | options
side: "buy"                              # buy | sell
quantity: 100
price: 5.00                              # reference/limit price the paper fill uses
order_type: "limit"                      # limit | market (sim fills deterministically)
stop: 4.25                               # stop / exit trigger — REQUIRED by Gate B
sizing_ref: "data/output/orders/2026-06-18.md#sizing"      # proves sizing ran (Gate B)
premortem_ref: "data/output/orders/2026-06-18.md#premortem" # proves pre-mortem ran (Gate B)
status: "DRAFT"                          # DRAFT | CHECKED | FILLED | REJECTED | HALTED
source: "stage-6"
notes: ""
unavailable: []                          # required fields with no real value (queued)
```

`notional = quantity * price` is the order's exposure at its reference price — the quantity every
Gate B cap is measured against.

## `Fill` — what the broker returns for EVERY routed order

```yaml
order_id: "ORD-20260618120000"
symbol: "EXMP"
status: "FILLED"                         # FILLED | REJECTED | HALTED
filled_quantity: 100                     # 0 on REJECTED/HALTED
fill_price: 5.00                         # null on REJECTED/HALTED
venue: "PaperBrokerAdapter"
timestamp: "2026-06-18T12:00:01+00:00"
reasons: []                              # why REJECTED/HALTED (empty when FILLED)
notes: "Simulated fill at reference price (no slippage model in v1)."
```

A `REJECTED` or `HALTED` Fill is the audit trail of a *blocked* order; it never changes the
portfolio. The `reasons` list names every breached check (e.g. each cap, each missing discipline
artifact, or the kill switch).

## `Position` and `Portfolio` — the running paper ledger

```yaml
# Portfolio (persisted to data/output/portfolio.json)
capital_base: 50000        # = mandate capital.simulated_usd; FIXED denominator for all caps
cash: 49500
currency: "USD"
positions:
  EXMP:                    # Position
    symbol: "EXMP"
    asset_class: "equity"
    quantity: 100
    avg_price: 5.00        # cost basis; the sim takes no live marks (deterministic)
```

`capital_base` does not change as positions open — deploying cash moves value from `cash` into
`positions`. Exposure for the gate is computed at cost basis: `deployed_notional`,
`class_notional`, `position_notional`.

## Order lifecycle

```
DRAFT ──(Stage 6 drafts memo + sizing + pre-mortem)──▶ CHECKED ──(passes kill switch + Gate B)──▶ FILLED
   │                                                       │
   └──(kill switch: halt:true)──▶ HALTED                   └──(Gate B fails)──▶ REJECTED
```

`HALTED` and `REJECTED` are terminal for that order; the portfolio is untouched. `FILLED` is the
only state that mutates `cash`/`positions` and triggers persistence + the `data/output/orders/<date>.md`
write.

## The Stage 6 → Stage 7 handoff (`PRED-*`)

Every order that reaches a decision (filled OR consciously not-taken) emits a prediction block so
Stage 7 can journal and later Brier-score it. The mapping to the §6 `PRED-*` schema
(`knowledge-base/journal/PRED-TEMPLATE.md`) is fixed:

| `PRED-*` field | Source in Stage 6 |
|---|---|
| `asset` | `order.symbol` |
| `direction` | `long` if `side: buy`, `short` if `side: sell`, else `neutral` |
| `probability` | the stated 0–1 probability the thesis resolves in the predicted direction (set UP FRONT) |
| `thesis_ref` | the dossier driving the trade, e.g. `data/output/dossiers/<ticker>.md` |
| `patterns_fired` | the `validated` `PATTERN-*` ids that scored this candidate in Stage 4 |
| `horizon` | the holding/resolution horizon from the trade memo |
| `tripwires` | the Stage 5 thesis-break + stop conditions (e.g. `["thesis-break: insiders sell", "stop at -15%"]`) |
| `resolution` / `brier_component` | left `null` — filled by Stage 7 at the horizon |

Stage 6 writes this block into `data/output/orders/<date>.md`; Stage 7 copies
`PRED-TEMPLATE.md` to `PRED-<id>.md` with these values and never edits `probability` afterward.
