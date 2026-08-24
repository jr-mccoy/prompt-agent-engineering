# Adapter Interface — the seam contract

*For informational and research purposes only. Not financial, investment, or tax advice.*

Every data seam implements the **same contract** so the stage prompts never know (or care)
whether a value came from a live API or a file under `data/input/`. This document is the
authoritative description of that contract; `scripts/adapters.py` is its (stubbed) Python
expression. Two rules dominate everything else:

1. **Point-in-time (`as_of`).** A call asks for data *as it was knowable on a given date*. An
   adapter must never return a value dated after `as_of`. This is what prevents look-ahead bias
   in Stage 1 snapshots and Stage 3 out-of-sample tests.
2. **No fabrication.** If a value is unavailable, the adapter returns it marked `UNAVAILABLE`
   (to be queued for retrieval). It never invents, interpolates, or substitutes a proxy silently.

## The base interface

```python
class DataSourceAdapter:
    """Common contract for every data seam (stubbed in Phase 1)."""

    seam_name: str                 # e.g. "MarketDataAdapter"
    implementation: str            # "stub" | "<provider-id>" (from config/data_sources.yaml)
    manual_input: str              # data/input/<seam>/ path used in manual-only mode

    def fetch(self, key: str, as_of: str) -> "Record":
        """Return a normalized Record for `key` as knowable on `as_of` (YYYY-MM-DD).

        - implementation == "stub"  -> read from manual_input (manual-only mode)
        - implementation == provider -> call the provider (NotImplementedError until wired)
        Missing fields are returned as UNAVAILABLE, never guessed.
        """
```

## Per-seam method signatures

Each seam exposes a thin, intention-revealing method on top of `fetch`:

| Seam | Method | `key` | Returns (normalized) |
|---|---|---|---|
| `MarketDataAdapter` | `get_prices(symbol, as_of)` | ticker/token | OHLCV + currency, point-in-time |
| `FundamentalsAdapter` | `get_fundamentals(symbol, as_of)` | ticker | revenue, margins, balance-sheet items, ratios |
| `FilingsAdapter` | `get_filings(symbol, since, as_of)` | ticker | list of filing/news records dated ≤ `as_of` |
| `OnChainAdapter` | `get_onchain_metrics(token, as_of)` | token/contract | active addresses, TVL, flows, holder concentration |
| `OptionsChainAdapter` | `get_options_chain(underlying, as_of)` | underlying | per-contract strike/expiry/IV/Greeks/OI |

All methods take `as_of` and obey the two dominant rules above.

## The normalized `Record`

Stages always receive the same shape, regardless of provider:

```yaml
seam: MarketDataAdapter        # which seam produced this
key: "EXMP"                    # symbol / token / underlying requested
as_of: "2026-06-18"            # the point-in-time date the data is valid for
source: "manual_input"         # "manual_input:<file>" | "<provider-id>"
fields:                        # normalized field map; units explicit
  close_usd: 1.23
  volume: 450000
  market_cap_usd: 180000000
unavailable: [pe_ratio]        # fields that could not be sourced -> queued, NOT guessed
notes: ""                      # provenance / caveats
```

Field conventions:
- **Units are explicit** in the field name where ambiguous (`_usd`, `_pct`, `_days`).
- **`unavailable`** lists every requested field that had no real value. Stage 1 turns these into
  retrieval-queue rows. An empty value is *never* represented as `0` or a placeholder.
- **`source`** records provenance so a snapshot is auditable and reproducible.

## `as_of` validation (implemented helper)

`scripts/adapters.py` implements `validate_as_of(record_date, as_of)` in pure stdlib: it returns
`True` only if `record_date <= as_of`. Any record failing this is rejected (look-ahead). This is
the one piece of integrity logic that must work even in manual-only mode.

## What is a stub in Phase 1

| Piece | Phase 1 status |
|---|---|
| `seam -> data/input/<seam>/` path resolution | **implemented** (stdlib) |
| `validate_as_of()` point-in-time check | **implemented** (stdlib) |
| Manual-only file read → `Record` | **implemented for trivial formats** (CSV/JSON via stdlib); richer parsing is a documented stub |
| Live provider `fetch` | **stub** — raises `NotImplementedError` with the provider wiring steps |
| `config/data_sources.yaml` load | **stub** — raises `NotImplementedError` until pyyaml is added |

The contract above is stable; only the *backing* of each seam changes when you go live.
