---
title: "Stage 5 — Monitoring & Tripwires (see the train coming)"
category: investment-research/monitoring-tripwires
description: "Watch the watchlist and open paper positions for dated catalysts and thesis-break / change-my-mind tripwires, then raise alerts when one trips. The early-warning layer between a screened candidate and a decision. Alerts are signals, not orders — Stage 6 decides. Point-in-time only; unknowns are queued, never guessed."
techniques:
  - DS-02
  - QA-05
  - RT-06
  - NE-10
  - QA-04
difficulty: advanced
tags:
  - monitoring
  - tripwires
  - catalysts
  - early-warning
  - point-in-time
  - kill-switch
updated: "2026-06-18"
related_prompts:
  - ai-investment-research-toolkit/prompts/stage-4-screening.md
  - ai-investment-research-toolkit/prompts/stage-6-decision-paper-action.md
  - ai-investment-research-toolkit/skills/data-source-adapter/SKILL.md
  - ai-investment-research-toolkit/skills/data-source-adapter/references/manual_only_mode.md
  - referenced-prompts/domain-finance/investing-research/finance_catalyst_map_builder.md
  - referenced-prompts/domain-reasoning-craft/forecasting/forecasting_what_would_change_my_mind.md
---

*For informational and research purposes only. Not financial, investment, or tax advice.
Nothing here places real-money trades. All outputs require independent verification.*

## Objective

Watch the Stage 4 watchlist and any open paper positions on the monitoring cadence and **raise an
alert the moment a pre-defined tripwire or catalyst window trips** — the "see the train coming"
layer. For each name, build a dated **catalyst map** (when known, scheduled events could move the
thesis) and a set of **thesis-break / change-my-mind tripwires** (the specific, pre-committed
conditions that would falsify the thesis or force an exit), then evaluate them against the latest
point-in-time snapshot. The load-bearing discipline is the same as Stage 1: every value carries the
date it was knowable, nothing dated after `as_of` is used, and a value that cannot be sourced is
recorded as `UNAVAILABLE` and queued — never guessed into a "nothing tripped" result. Alerts are
**signals, not orders**: this stage decides what deserves attention, Stage 6 decides what (if
anything) to do about it, behind Gate B / Gate C.

## When to Use

- Running the daily `cadence.monitor` sweep over the watchlist + open paper positions
- Refreshing tripwires/catalysts after Stage 4 re-ranks or Stage 6 opens a paper position
- Catching a dated catalyst (earnings, unlock, expiry, ruling) before it lands
- Deciding which names are quiet vs. which warrant a Stage 6 look — without yet sizing anything

## Inputs / Context Required

**What to watch**
- The Stage 4 watchlist (`data/output/watchlist.csv`) with its evidence trail
- Open paper positions (`data/output/portfolio.json`) and their tripwires
- The Stage 2 dossiers (`data/output/dossiers/<ticker>.md`) for each name's thesis + pre-committed
  disconfirming test

**Fresh, point-in-time data**
- The latest snapshot for the sweep date via the `data-source-adapter` skill
  (`MarketDataAdapter` for price/vol, `FilingsAdapter` for news/filings, `OnChainAdapter` for token
  metrics); seams on `stub` run manual-only (see `data-source-adapter/references/manual_only_mode.md`)

**Config**
- `config/mandate.yaml` — `cadence.monitor`; if `halt: true`, the kill switch limits this stage to
  read-only observation (alerts may still be recorded, but no action is emitted)
- `config/asset_classes.yaml` — which classes are in scope (crypto trades 24/7)

## Constraints

### Must
- Build, per name, a **dated catalyst map** (reuse `finance_catalyst_map_builder.md`) and a set of
  **thesis-break tripwires** (reuse `forecasting_what_would_change_my_mind.md`), each with an
  explicit, checkable trigger condition (RT-06).
- Evaluate every tripwire against the latest snapshot **as of the sweep date only**; capture each
  observed value with its `as_of` and source (QA-05).
- Classify each tripwire as `FIRED`, `ARMED` (defined, not yet tripped), or `UNAVAILABLE` (the
  needed value could not be sourced) — and queue every `UNAVAILABLE` for retrieval (DS-02).
- Judge whether a `FIRED` tripwire is signal or noise before escalating it (QA-04).
- Honor the kill switch: if `halt: true`, observe and record alerts read-only; emit no action and
  hand nothing to Stage 6.

### Must Not
- Use any value dated after the sweep `as_of` (look-ahead leakage) to declare a tripwire (un)tripped.
- Invent a catalyst date, a price level, or an observed metric where the data is `UNAVAILABLE` —
  a missing value is queued, never treated as "nothing tripped" (DS-02, QA-05).
- Silently loosen, move, or drop a tripwire to avoid an inconvenient firing (the cardinal sin of
  this stage).
- Size a position, place an order, or recommend a specific trade — that is Stage 6, behind Gate B /
  Gate C (NE-10).
- Forecast a return or assert "this will happen" — alerts flag conditions, they do not predict.

## Instructions

1. **Assemble the watch set.** From `data/output/watchlist.csv` and `data/output/portfolio.json`,
   list every name to monitor this sweep. For each, pull its thesis and pre-committed disconfirming
   test from the dossier.

2. **Build catalyst maps (RT-06).** For each name, reuse `finance_catalyst_map_builder.md` to lay
   out dated, scheduled catalysts (earnings, token unlocks, option expiries, rulings, lockups) with
   their dates and the direction each could move the thesis. Mark any catalyst whose date is
   `UNAVAILABLE` and queue it — do not guess a date.

3. **Define thesis-break tripwires (RT-06).** Reuse `forecasting_what_would_change_my_mind.md` to
   turn each thesis into explicit, checkable tripwires: thesis-break conditions (e.g. "insiders
   sell", "gross margin reverses"), price/volatility stops (e.g. "−15% from entry"), and catalyst
   windows. State the exact trigger condition for each so firing is unambiguous.

4. **Evaluate against the latest snapshot (QA-05).** For each tripwire, fetch the needed value as of
   the sweep date via the data adapter (point-in-time; rejects anything dated after `as_of`) and
   compare to the trigger. Record the observed value, its `as_of`, and its source.

   ```bash
   python skills/data-source-adapter/scripts/adapters.py \
     --seam MarketDataAdapter --key <SYMBOL> --as-of <as_of> --manual data/input
   # Open paper positions + exposure to watch (read-only):
   python skills/paper-trade-executor/scripts/brokers.py --report --config config \
     --portfolio data/output/portfolio.json
   ```

5. **Classify and filter (DS-02 / QA-04).** Mark each tripwire `FIRED`, `ARMED`, or `UNAVAILABLE`.
   For every `FIRED`, apply a signal-vs-noise judgment before escalating; queue every `UNAVAILABLE`.

6. **Write the alerts.** Save `data/output/alerts/<as_of>.md` with the per-name tripwire status, the
   firing evidence, upcoming dated catalysts, and a recommended next stage (monitor / take to Stage
   6). Honor the kill switch in the header.

## Output Format

```
## ALERTS: as_of [date] | Watch set: [N names] | Cadence: monitor | Mode: [live/manual]
```

### Fired tripwires (escalate — signal, not order)
| Symbol | Class | Tripwire | Trigger condition | Observed (as_of) | Signal/noise | Recommended next |
|---|---|---|---|---|---|---|
| … | … | thesis-break: insiders sell | ≥1 Form 4 sale | yes, 2026-06-18 | signal | take to Stage 6 |

### Armed tripwires (defined, not tripped)
| Symbol | Tripwire | Trigger condition | Latest observed (as_of) |
|---|---|---|---|
| … | stop at −15% | price ≤ entry×0.85 | −6% (2026-06-18) |

### Upcoming dated catalysts
| Symbol | Catalyst | Date | Thesis direction | Source |
|---|---|---|---|---|
| … | Q2 earnings | 2026-07-29 | confirms/breaks | filing calendar |

### Unavailable (queued — never guessed)
| Symbol | Tripwire / catalyst | Missing value | Queued for |
|---|---|---|---|
| … | token unlock date | unlock schedule | OnChainAdapter retrieval |

### Monitoring statement
- Kill switch (`halt`): [false → alerts may route to Stage 6 / true → read-only observation]
- Point-in-time integrity: [all observed values dated ≤ as_of] · Unavailable queued: [count]

## Verification

- [ ] Each name has explicit tripwires with checkable trigger conditions and a dated catalyst map.
- [ ] Every observed value carries an `as_of` ≤ the sweep date; nothing dated later was used.
- [ ] `FIRED` / `ARMED` / `UNAVAILABLE` are distinguished; every `UNAVAILABLE` is queued.
- [ ] No tripwire was moved, loosened, or dropped to avoid a firing.
- [ ] `FIRED` tripwires passed a signal-vs-noise judgment before escalation.
- [ ] No position sizing, orders, or return forecasts appear (those are Stage 6).
- [ ] Kill switch honored (read-only when `halt: true`).

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Missing data read as "nothing tripped" | `UNAVAILABLE` → queued and shown, never a silent all-clear (DS-02) |
| A catalyst date is invented to fill a gap | Unknown dates marked `UNAVAILABLE` and queued; no guessed dates |
| A tripwire is quietly loosened to avoid firing | Trigger conditions are pre-committed and stated; firings are recorded as-is |
| A stale snapshot is treated as fresh | Every value carries an `as_of`; sweep date stamped; later-dated values rejected |
| A one-off blip escalated as a real break | Signal-vs-noise judgment required before escalation (QA-04) |
| An alert is read as a buy/sell instruction | Alerts are signals only; sizing/orders are Stage 6 behind Gate B/C (NE-10) |
| "Live" data assumed when running on stubs | Per-seam mode (live/manual) recorded in the header |
