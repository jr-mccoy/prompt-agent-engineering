# Manual-Only Mode — running the loop with no APIs

*For informational and research purposes only. Not financial, investment, or tax advice.*

With every seam set to `implementation: stub` in `config/data_sources.yaml`, the toolkit runs
**fully without any external API**: you paste data into `data/input/`, and the stub adapters
read it and hand normalized records to Stage 1. It is slower than a live feed, but it is enough
to learn the system, build an early calibration record, and run out-of-sample pattern tests on
data you already have. The `data/` tree is git-ignored, so nothing you paste is committed.

## Directory layout

One subdirectory per seam, matching the `manual_input` paths in `config/data_sources.yaml`:

```
data/input/
├── prices/         # MarketDataAdapter   — OHLCV per symbol/token
├── fundamentals/   # FundamentalsAdapter — financials/ratios per ticker
├── filings/        # FilingsAdapter      — 10-K/10-Q/news text or metadata
├── onchain/        # OnChainAdapter      — token metrics (crypto only)
└── options/        # OptionsChainAdapter — chains/IV/Greeks (options only)
```

(Each directory is preserved in git by a `.gitkeep`; the data files themselves are ignored.)

## File naming and the `as_of` contract

Name files so the symbol and the point-in-time date are unambiguous:

```
data/input/prices/EXMP_2026-06-18.csv
data/input/fundamentals/EXMP_2026-06-18.json
data/input/onchain/TOKENX_2026-06-18.json
```

The date in the file is the `as_of` — the date the data was knowable. **Every row/record must be
dated on or before that `as_of`.** The stub rejects any record dated later (look-ahead). When
Stage 1 asks for `EXMP` as of `2026-06-18`, the adapter resolves the matching file, validates the
dates, and returns the normalized `Record`.

## Accepted formats

Phase 1 stubs read the two stdlib-friendly formats below; anything richer is a documented stub
(the function explains what it will parse once implemented):

- **CSV** (e.g. prices): a header row, one row per period, explicit units in the header.
  ```csv
  date,open_usd,high_usd,low_usd,close_usd,volume
  2026-06-18,1.20,1.27,1.18,1.23,450000
  ```
- **JSON** (e.g. fundamentals / on-chain): a flat object of normalized fields.
  ```json
  { "as_of": "2026-06-18", "revenue_usd": 42000000, "gross_margin_pct": 38.5, "pe_ratio": null }
  ```

## How a file becomes a normalized `Record`

1. **Resolve** the file from `data/input/<seam>/<KEY>_<as_of>.<ext>` (implemented helper).
2. **Validate `as_of`**: reject any record dated after the requested `as_of` (implemented helper).
3. **Map** the file's fields into the normalized `fields` map (units explicit); collect any
   requested-but-missing field into `unavailable`.
4. **Stamp provenance**: `source: "manual_input:<filename>"`.

A `null` (JSON) or empty (CSV) cell becomes an `unavailable` entry — it is **queued**, not turned
into `0` or a guess. That is the same no-fabrication rule the whole toolkit runs on.

## Going live later

Manual-only mode and live mode share the identical contract (`references/adapter_interface.md`),
so moving a seam to a provider is a config + adapter change only:

1. Set the seam's `implementation` to the provider id in `config/data_sources.yaml`.
2. Put the API key in an environment variable or a git-ignored `config/*.local.yaml`.
3. Implement the provider branch of `fetch()` in `scripts/adapters.py`.

No stage prompt changes — the stages only ever see normalized `Record`s.
