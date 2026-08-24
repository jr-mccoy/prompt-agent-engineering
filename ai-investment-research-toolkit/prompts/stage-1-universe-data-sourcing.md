---
title: "Stage 1 — Universe & Data Sourcing (timestamped snapshots, look-ahead prevention)"
category: investment-research/universe-data-sourcing
description: "Define the hunting ground from the mandate's asset-class filters, pull the raw material through the data-source-adapter seams (or data/input/ in manual-only mode), and snapshot everything with a timestamp to a dated folder so later backtests cannot peek at future data. Unknowns are queued for retrieval, never guessed."
techniques:
  - DS-02
  - QA-05
  - CM-02
  - QA-04
difficulty: advanced
tags:
  - universe-construction
  - data-sourcing
  - point-in-time
  - look-ahead-prevention
  - snapshots
  - adapters
updated: "2026-06-18"
related_prompts:
  - ai-investment-research-toolkit/skills/data-source-adapter/SKILL.md
  - ai-investment-research-toolkit/skills/data-source-adapter/references/manual_only_mode.md
  - ai-investment-research-toolkit/prompts/stage-2-deep-research.md
  - ai-investment-research-toolkit/prompts/stage-4-screening.md
---

*For informational and research purposes only. Not financial, investment, or tax advice.
Nothing here places real-money trades. All outputs require independent verification.*

## Objective

Turn the mandate into a concrete candidate universe and pull the raw data each later stage
needs — **as a timestamped, point-in-time snapshot**. The defining discipline of this stage is
look-ahead prevention: every figure is captured with the date it was knowable, written to a
dated snapshot folder, and never silently refreshed with future data. Where a value is
unavailable, it is recorded as a queued retrieval item, not invented. The output is a
reproducible `universe.csv` plus per-candidate raw data that Stage 2 (research) and Stage 4
(screening) consume without ever seeing data from after the snapshot date.

## When to Use

- Starting a research/screen cadence pass (the weekly Stages 1–4 sweep per the mandate)
- Building a fresh point-in-time snapshot for a new candidate date
- Running in manual-only mode (no APIs) from pasted data in `data/input/`
- Re-sourcing a universe after changing `config/asset_classes.yaml` filters
- Reconstructing a historical snapshot for an out-of-sample pattern test (Stage 3)

## Inputs / Context Required

**Mandate & scope**
- `config/mandate.yaml` — objective, cadence, and the kill switch (`halt`)
- `config/asset_classes.yaml` — which classes are `active: true` and their `universe_filters`
  (e.g. equity market-cap band + liquidity floor + exchanges; crypto mcap/age/on-chain; options
  underlyings/open-interest/expiry)

**Data access**
- `config/data_sources.yaml` — which implementation backs each adapter seam (`stub` →
  manual-only mode reads from the `manual_input` path under `data/input/<seam>/`)
- The `data-source-adapter` skill for the seam interface and the manual-only layout

**Snapshot target**
- The candidate date (`as_of`) for this snapshot — defaults to today; set explicitly when
  reconstructing history. All pulled data must be knowable on or before this date.

## Constraints

### Must
- Read the active classes and filters from config; the universe is defined by config, not by
  hand-picked names (CM-02).
- Capture every pulled value into `data/snapshots/<as_of>/` with the `as_of` timestamp before
  any downstream use; the snapshot is the single source of truth for this pass (QA-05).
- Enforce point-in-time integrity: only include data knowable on or before `as_of`; never
  backfill a past snapshot with later-revised figures (QA-05).
- Define every universe field precisely (units, currency, source seam) in the snapshot so it is
  reproducible and auditable (DS-02).
- Record data provenance per field: which seam/source supplied it, or `manual_input` plus the
  file it came from.
- Respect the kill switch: if `mandate.yaml: halt: true`, sourcing for action stages stops;
  read-only reconstruction for Stage 3 may continue.

### Must Not
- Invent prices, market caps, fundamentals, on-chain metrics, or option chains. An unavailable
  value is queued for retrieval (status `UNAVAILABLE`), never guessed (DS-02, QA-05).
- Pull or include any value dated after `as_of` into that snapshot (look-ahead leakage).
- Mix asset classes' filters or silently widen a band beyond what config specifies.
- Drop delisted/failed names from a historical universe (that is survivorship bias — keep them
  with their point-in-time status).
- Overwrite an existing dated snapshot; each `as_of` is immutable once written.

## Instructions

1. **Load scope (CM-02).** Read `config/asset_classes.yaml`; list each `active: true` class and
   its `universe_filters`. Read `config/mandate.yaml`; if `halt: true`, restrict to read-only
   reconstruction and say so. Resolve `as_of` (default today).

2. **Resolve adapters (DS-02).** For each data need, read `config/data_sources.yaml` to find the
   backing implementation. For any seam set to `stub`, use **manual-only mode**: read pasted data
   from the seam's `manual_input` path (see `data-source-adapter/references/manual_only_mode.md`).
   Note per seam whether it is live or manual.

3. **Construct the universe.** Apply each class's filters to produce the candidate list:
   - **Equity:** market-cap band, liquidity floor (avg daily $ volume), exchanges.
   - **Crypto:** market-cap floor, minimum token age, on-chain-data availability.
   - **Options:** restrict to the active equity underlyings, then open-interest / days-to-expiry.
   Record, per candidate, the field values that caused inclusion and their provenance.

4. **Pull point-in-time raw data (QA-05).** For each candidate, retrieve the raw material later
   stages need (prices/volume, fundamentals, filings/news; on-chain for tokens; chains/IV for
   options). Tag each value with `as_of` and its source. If a value is unavailable, write the
   field as `UNAVAILABLE` and add a row to the retrieval queue — do not guess.

5. **Snapshot immutably (QA-05).** Write `data/snapshots/<as_of>/universe.csv` and the
   per-candidate raw data under the same folder. Do not modify a prior snapshot. This folder is
   what Stage 2 and Stage 4 read — they must never reach past it to live data.
   **Use the writer — immutability and look-ahead-safety are enforced in code:**

   ```bash
   # Reads each candidate point-in-time via the adapter, applies the active-class filters,
   # writes data/snapshots/<as_of>/universe.csv (+ raw/). REFUSES to overwrite a written
   # snapshot (exit 2); skips any candidate with no point-in-time price (no look-ahead leak).
   python skills/data-source-adapter/scripts/adapters.py \
     --seam MarketDataAdapter --key <SYMBOL> --as-of <as_of> --manual data/input   # spot-check one record
   python skills/data-source-adapter/scripts/build_snapshot.py \
     --as-of <as_of> --manual data/input --out data/snapshots
   ```

6. **Acknowledge coverage gaps (QA-04).** Summarize what fraction of fields were sourced vs.
   queued, per class, and flag any candidate too sparsely covered to research responsibly.

## Output Format

```
## UNIVERSE SNAPSHOT: as_of [date] | Classes: [equity/crypto/options] | Mode: [live/manual/mixed]
```

### Scope applied
| Class | Active | Filters applied | # candidates |
|---|---|---|---|
| equity | yes/no | mcap band · liquidity floor · exchanges | … |
| crypto | yes/no | mcap floor · min age · on-chain required | … |
| options | yes/no | underlyings · OI · DTE | … |

### Candidate universe (excerpt; full set → `data/snapshots/<as_of>/universe.csv`)
| Symbol | Class | Inclusion field(s) | Value | Source seam | as_of |
|---|---|---|---|---|---|
| … | … | market_cap_usd | … | MarketDataAdapter / manual_input | … |

### Data coverage & retrieval queue
| Seam | Mode | Fields sourced | Fields UNAVAILABLE (queued) |
|---|---|---|---|
| MarketDataAdapter | … | … | … |
| FundamentalsAdapter | … | … | … |
| FilingsAdapter | … | … | … |
| OnChainAdapter | … | … | … |
| OptionsChainAdapter | … | … | … |

### Point-in-time / integrity statement
- Snapshot folder written: `data/snapshots/<as_of>/`
- All included values knowable on/before `as_of`: [yes — or list exceptions, which must be removed]
- Delisted/failed names retained with point-in-time status (survivorship): [yes/no]
- Queued (not guessed) items: [count] — see retrieval queue above

## Verification

- [ ] Universe is derived from `config/asset_classes.yaml` filters, not hand-picked.
- [ ] Every value carries an `as_of` and a source/provenance; nothing dated after `as_of`.
- [ ] Unavailable values are marked `UNAVAILABLE` and queued, never filled with a guess.
- [ ] The snapshot is written to `data/snapshots/<as_of>/` and no prior snapshot was overwritten.
- [ ] Delisted/failed names are retained (no survivorship trimming of historical universes).
- [ ] Field definitions (units, currency, seam) are explicit enough to reproduce the pull.
- [ ] Kill switch honored if `halt: true`.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| A blank field gets filled with a plausible-looking number | Mark `UNAVAILABLE` + queue it; coverage stats expose gaps |
| Snapshot quietly refreshed with later-revised data | Snapshots are immutable per `as_of`; never overwrite |
| Pattern later "predicts" using data from after the decision date | Point-in-time tag on every value; reject anything dated > `as_of` |
| Universe silently excludes failures/delistings | Retain delisted names with point-in-time status; survivorship note required |
| Filters widened ad hoc to include a favored name | Universe comes from config filters only; changes go through `asset_classes.yaml` |
| "Live" data assumed when running on stubs | Per-seam mode (live/manual) recorded in the coverage table |
