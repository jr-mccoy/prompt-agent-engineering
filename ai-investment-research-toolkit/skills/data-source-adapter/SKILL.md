---
name: data-source-adapter
description: Normalize external market data behind a stable, stubbable interface — the seam between the toolkit and any data provider. Use this skill for "pull prices/fundamentals/filings/on-chain/options data", "add a market-data provider", "run the loop with no API (manual-only mode)", or "snapshot point-in-time data for Stage 1". Exposes one interface per data seam (MarketData, Fundamentals, Filings, OnChain, OptionsChain); every seam ships as a documented stub that reads pasted data from data/input/ until a real provider is wired in. Never returns fabricated values — unavailable data is reported as such and queued.
license: MIT
compatibility: Standard library only (manual-only mode reads files you place under data/input/). The manual reader, point-in-time check, and load_data_sources are implemented; load_data_sources uses PyYAML if installed, else an embedded YAML-subset parser (so it runs with no dependencies). `--self-check` proves look-ahead rejection, UNAVAILABLE queueing, and config load. The live provider fetch (_fetch_live) stays a deferred stub until a provider is purchased. The broker seams (PaperBrokerAdapter, LiveBrokerAdapter) are NOT part of this skill — they belong to the paper-trade-executor skill (Stage 6).
metadata:
  tags: [investing, data-sourcing, adapter, seam, point-in-time, look-ahead-prevention, manual-only, stub]
  updated: "2026-06-18"
---

# Data Source Adapter

Provides the **seam** between the toolkit and the outside world: one stable interface per data
need, with a stub implementation behind each so the whole research/screen loop runs on
sample or manually-pasted data before any provider is purchased. This is the boundary that
keeps "where the data comes from" out of the stage prompts — Stage 1 asks an adapter for
point-in-time data and gets a normalized record back, whether that came from a live API or a
file you dropped in `data/input/`.

## Purpose

External data is the toolkit's largest source of both cost and risk (look-ahead bias, silent
gaps, fabricated fill-ins). This skill isolates all of it behind five adapters with identical
contracts:

| Seam | Backs | Stages |
|---|---|---|
| `MarketDataAdapter` | prices / volume | 1, 5 |
| `FundamentalsAdapter` | financials / ratios | 2 |
| `FilingsAdapter` | 10-K / 10-Q / news | 2, 5 |
| `OnChainAdapter` | token metrics (crypto only) | 2, 5 |
| `OptionsChainAdapter` | chains / IV / Greeks (options only) | 2, 6 |

`config/data_sources.yaml` selects the implementation per seam (`stub` or a `<provider-id>`).
With everything on `stub`, the toolkit runs in **manual-only mode**: each adapter reads pasted
data from its `manual_input` path under `data/input/`. The contract is the same either way, so
upgrading a seam to a live provider does not touch any stage prompt.

## When to Use This Skill

Use this skill when you need to:
- Pull point-in-time data for the Stage 1 universe & snapshot
- Run the loop with no API keys at all (manual-only mode from `data/input/`)
- Add or swap a data provider behind a seam without changing the stages
- Understand the normalized record shape a stage will receive

## When NOT to Use This Skill

Do NOT use this skill when:
- You want to place or simulate an order → that is the `paper-trade-executor` skill (Stage 6)
- You are deciding whether a signal is real → that is `pattern-knowledge-base` (Stage 3)
- You are logging/scoring a prediction → that is `prediction-journal` (Stage 7)

## Prerequisites

- `config/data_sources.yaml` (which implementation backs each seam; defaults are all `stub`)
- For manual-only mode: data files placed under the seam's `manual_input` path (see
  `references/manual_only_mode.md`)
- For a live seam: the provider's API key in an environment variable or a git-ignored
  `config/*.local.yaml` — **never** in a tracked file or a prompt

## Quick Start

### Step 1: Decide live vs. manual per seam

**Purpose:** Know where each adapter gets its data before Stage 1 runs.

1. Open `config/data_sources.yaml`. Any seam set to `implementation: stub` runs manual-only.
2. For each `stub` seam, confirm its `manual_input` path exists under `data/input/`.

**Validation:**
- [ ] Every active seam is either a real provider id (with a key in env/local config) or `stub`
- [ ] Each `stub` seam has a `manual_input` directory

### Step 2: Place data for manual-only mode

**Purpose:** Feed the stubs without any API.

1. For each seam, drop files in its `manual_input` path (e.g. `data/input/prices/`,
   `data/input/fundamentals/`). Accepted layout and formats are in
   `references/manual_only_mode.md`.
2. Each record must carry the date it was knowable (its `as_of`) — that is what preserves
   point-in-time integrity for Stage 1 snapshots.

**Validation:**
- [ ] Every record has an `as_of` no later than the snapshot date
- [ ] Missing values are absent (to be queued), not filled with a placeholder number

### Step 3: Call the seam (interface is identical live or manual)

**Purpose:** Get a normalized, point-in-time record back.

```bash
# Implemented: the manual reader resolves the data/input/<seam>/ path + the as_of contract
# and queues missing fields as UNAVAILABLE. Only the live provider fetch stays a deferred
# stub (raises until a provider is wired in). See references/adapter_interface.md.
python scripts/adapters.py --seam MarketDataAdapter --key EXMP --as-of 2026-06-18 --manual data/input
python scripts/adapters.py --self-check
```

**Validation:**
- [ ] Unavailable fields come back marked `UNAVAILABLE` (queued), never guessed
- [ ] Nothing dated after `as_of` is returned

### Step 4: Write the immutable Stage 1 snapshot

**Purpose:** Produce the look-ahead-safe `universe.csv` Stage 2/4 read.

```bash
# Derives the universe, applies active-class filters, writes data/snapshots/<as_of>/universe.csv.
# REFUSES to overwrite a written snapshot (immutability); skips any candidate with no PIT price.
python scripts/build_snapshot.py --as-of 2026-06-18 --manual data/input --out data/snapshots
python scripts/build_snapshot.py --self-check
```

**Validation:**
- [ ] A second build on the same `as_of` is refused (exit 2) — snapshots are immutable
- [ ] Candidates with no point-in-time price are skipped, not back-filled (no look-ahead)

## Common Issues

### Issue: A field is missing for a candidate
Report it as `UNAVAILABLE` and let Stage 1 queue it for retrieval. Do **not** substitute a
sector average, a prior value, or a plausible guess — fabricated data poisons every downstream
stage and Gate A.

### Issue: The only data you have is dated after the snapshot
That is look-ahead. Exclude it from the snapshot; a point-in-time snapshot may only contain
values knowable on or before its `as_of`.

### Issue: You want to go live on one seam
Set that seam's `implementation` to the provider id in `config/data_sources.yaml`, put the key
in an environment variable or a git-ignored `config/*.local.yaml`, and implement the provider
branch in `scripts/adapters.py`. No stage prompt changes.

## Safety & Constraints

**NEVER:**
- Return a fabricated value for missing data — report `UNAVAILABLE` and queue it
- Return data dated after the requested `as_of` (look-ahead leakage)
- Put an API key in a tracked file, a prompt, or `config/data_sources.yaml`
- Add the broker seams here — they live in the `paper-trade-executor` skill

**ALWAYS:**
- Carry an `as_of` on every record and respect the point-in-time contract
- Normalize to the documented record shape so stages are provider-agnostic
- Record provenance (which seam/provider or which `manual_input` file supplied each value)

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/adapter_interface.md` | The seam contract: method signatures, normalized record shape, `as_of` and unknown-handling rules |
| `references/manual_only_mode.md` | How to run with no APIs: `data/input/<seam>/` layout, formats, and how a file becomes a normalized record |
| `scripts/adapters.py` | `DataSourceAdapter` + manual reader + `load_data_sources` + `--self-check`; the live provider fetch raises `NotImplementedError` until a provider is wired in |
| `scripts/build_snapshot.py` | Stage 1 universe writer: derives the manual-only universe, applies the active-class filters, writes an immutable `data/snapshots/<as_of>/universe.csv` (+ `raw/`), refuses to overwrite a written snapshot, skips candidates with no point-in-time price (look-ahead-safe); `--self-check` |

## Related Skills

- `pattern-knowledge-base` — consumes point-in-time snapshots to validate patterns (Stage 3)
- `prediction-journal` — scores predictions made on this data (Stage 7)
- `paper-trade-executor` — owns the broker seams and order simulation (Stage 6)

## Reused repo prompts (referenced by path)

- Stage 1 driver: `ai-investment-research-toolkit/prompts/stage-1-universe-data-sourcing.md`
