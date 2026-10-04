---
title: "Live Currency Sink/Faucet Audit — Ledger Reconciliation, Supply Growth, Distribution, and Targeted Fixes"
category: game-development/economy
description: "Audit a live game currency from telemetry: reconcile faucets and sinks against observed money supply to expose logging gaps or exploits, measure net injection, sink ratio and weekly supply growth against a target, check who holds the money and who pays the sinks, attribute growth to specific sources, and propose fixes with projected effect, provenance tags on every number, and a re-measure date instead of a single big nerf."
techniques:
  - NE-11
  - RT-06
  - RT-23
  - QA-02
difficulty: advanced
tags:
  - game-economy
  - currency-sinks
  - faucets
  - inflation
  - live-ops
  - economy-telemetry
  - gold-is-worthless
  - prices-keep-rising
  - players-hoarding-currency
updated: "2026-10-03"
related_prompts:
  - domain-game-development/economy/economy_system_design.md
  - domain-game-development/economy/economy_liveops_monetization_ethics.md
  - domain-data-analytics/analysis-and-sql/analytics_metric_movement_investigation.md
---

# Live Currency Sink/Faucet Audit

**Objective:** Tell a live team whether its currency is inflating, why, who it is
hurting, and which changes will bring it back inside target — every figure traced to
telemetry, an estimate or a guess, and every fix paired with the metric that will
show whether it worked.

**When to Use:**
- Prices between players keep rising, or veteran players hold so much currency that
  rewards no longer matter.
- A season or patch changed rewards or costs and nobody has checked the net effect.
- The money supply moved more than the logged faucets and sinks explain.
- **Not this prompt if** you are designing the currencies, sources, sinks and drop
  tables from scratch — use `domain-game-development/economy/economy_system_design.md`;
  this prompt audits a running economy from data. For the season calendar and the
  ethics of paid offers, use
  `domain-game-development/economy/economy_liveops_monetization_ethics.md`. For a
  general "why did this metric move" investigation outside game economies, use
  `domain-data-analytics/analysis-and-sql/analytics_metric_movement_investigation.md`.

## Inputs / Context

1. **Ledger telemetry**: every currency grant and removal event with source/sink
   type, amount, player id, level, timestamp — over at least 2–4 weeks.
2. **Supply snapshots**: total currency held at start and end, all accounts and
   active accounts (define "active", e.g. played in last 14 days).
3. **Market data** if players trade: median prices for a fixed basket of goods.
4. **Holdings distribution**: percentiles of balances by level bracket.
5. **Targets**: acceptable weekly supply growth, sink ratio, price drift.
6. **Recent changes**: patches, events, new items, known exploits or bot waves.

## Method

1. **Reconcile the ledger (NE-11).**
   `expected end supply = start supply + Σ faucets − Σ sinks`. The unexplained
   difference is a logging gap, an unlogged source, a duplication exploit or account
   deletions; size it per day and as a share of faucets.
2. **Compute the core rates.** Per day: total faucets, total sinks, net injection,
   sink ratio (sinks ÷ faucets); weekly supply growth
   `(end ÷ start)^(7 ÷ days) − 1`; per-active-player net.
3. **Tag provenance (RT-23).** Mark every number `[data]` (from telemetry),
   `[estimate]` (computed from data with a stated assumption) or `[guess]` (needed to
   proceed, to be replaced). Round projections to the quality of their weakest input.
4. **Look at distribution.** Median and p90/p99 holdings, share held by the top 1%,
   by level bracket. Inflation hurts new players most when prices are set by rich ones.
5. **Correlate with prices (RT-06).** Basket price index against supply growth over
   the same window; check whether the price rise is broad (inflation) or confined to
   a few goods (supply shock).
6. **Attribute the growth.** Break faucets down by source and by share of accounts.
   A source concentrated in a small share of accounts suggests a farming loop or bots.
7. **Check sink incidence.** For each sink, cost as a share of each bracket's
   income. Sinks that bite new players harder than veterans are regressive.
8. **Hunt exploits (QA-02).** Buy-low/sell-high vendor loops, duplicated rewards on
   reconnect, refund paths, items crafted for less than they sell for.
9. **Propose fixes with projections.** Prefer desirable sinks and targeted faucet
   fixes over broad reward cuts. For each: projected change per day with
   provenance, the metric to watch, the re-measure date, and the rollback rule.

## Output Format

```
# Currency audit — [currency]   Window: [dates]   Active definition: [..]

## Ledger reconciliation  — start | +faucets | −sinks | expected | observed | unexplained/day
## Flows                  — source/sink | per day | share | provenance
## Core rates             — net/day | sink ratio | weekly growth vs target
## Distribution           — bracket | median | p90 | p99 | top-1% share
## Prices                 — basket index change vs supply change
## Attribution            — source | accounts producing | concentration | suspicion
## Sink incidence         — sink | % of income by bracket | regressive?
## Exploit candidates     — loop | checked how | verdict
## Fixes                  — change | projected effect/day | provenance | watch metric | re-measure | rollback
## Projected position     — net/day and weekly growth after fixes vs target
```

## Verification

- [ ] Faucets and sinks each sum to their stated totals.
- [ ] The reconciliation shows the unexplained amount, even if zero.
- [ ] Weekly growth is computed from the stated start, end and window.
- [ ] Every number carries `[data]`, `[estimate]` or `[guess]`.
- [ ] Every fix has a watch metric, a re-measure date and a rollback rule.
- [ ] The projected position is recomputed from the fixes, not asserted.

## False-Positive Prevention

1. **Supply growth is not automatically inflation.** A growing player base or a new
   sink about to launch may absorb it; check prices and per-player figures.
2. **Rich veterans are not a defect.** Late-game wealth can be intended; the problem
   is when their wealth sets prices new players must pay.
3. **Concentrated faucets are not proof of bots.** A popular farming spot looks the
   same; label it a suspicion until account behaviour confirms it.
4. **Do not count inactive hoards as live supply.** Balances of churned players do
   not chase goods; report active supply separately.
5. **Projections are not outcomes.** Players adapt; re-measure before stacking more fixes.
6. **Cutting rewards is the costliest lever.** Players feel takeaways sharply;
   prefer sinks players want.

## Example Output

**Input:** Online RPG, gold. 28-day window (27 daily steps). Active = played in last
14 days. Target: total supply growth ≤ 2% per week; active supply is used for the
distribution view.

```
# Currency audit — gold   Window: 28 days   Active: played in last 14 days

## Ledger reconciliation (all accounts)
Start 2.800B + faucets 27 × 98.0M − sinks 27 × 66.0M = 3.664B expected
Observed 3.750B → unexplained 86M = 3.2M/day (3.3% of faucets) [data] → investigate

## Flows (per day, [data])
Faucets: quests 41.0M · mob drops 28.5M · vendor sales 22.0M · login 6.5M = 98.0M
Sinks: vendor purchases 21.4M · repairs 18.2M · crafting 12.3M · AH fees+tax 9.6M · travel 4.5M = 66.0M

## Core rates
Net +32.0M/day · sink ratio 66.0 ÷ 98.0 = 67.3%
Growth (3.750 ÷ 2.800)^(7/27) − 1 = 7.9%/week vs target ≤ 2%  → over

## Distribution (active)
Median 14k · p99 2.4M · top 1% hold 38% of active supply

## Prices
Basket (ore, potions, mid-tier gear) +21% over the window — broad, tracks supply.

## Attribution
Vendor sales: 60% (13.2M/day) from one item, Gilded Shell, sold by 3% of accounts → farming loop [suspicion]

## Sink incidence
Repairs: 12% of income for levels < 20, 2% at endgame → regressive

## Exploit candidates
| Craft-and-vendor loops | margin per recipe | cleared — all recipes lose ≥ 15% |
| Reward on reconnect | duplicate quest-complete events | cleared — 0 duplicates in window |
| Unlogged source | 86M unexplained | open — compare server grants to ledger |

## Fixes
| Gilded Shell vendor price −70% | −9.24M/day [estimate: farm volume unchanged] | shell sales/day | day 14 | revert if quest completion drops > 5% |
| Gold housing décor, endgame-targeted | +6.0M sinks/day [guess] | décor gold spent/day | day 14 | — |
| AH tax 5% → 6% | +1.6M/day [estimate: 8.0M tax at 5%, volume unchanged] | AH volume | day 14 | revert if volume −15% |
| Repairs −50% under level 20 | −1.0M sinks/day [estimate] | new-player gold at level 20 | day 14 | — |

## Projected position
Net 32.0 − 9.24 − 6.0 − 1.6 + 1.0 = 16.16M/day ≈ 16.2M/day
Weekly growth ≈ 16.16 × 7 ÷ 3,750 = 3.0% — still above 2%. Do not stack more cuts
now; re-measure at day 14 (décor sink is a guess), then use a pre-agreed second lever.
```

## Techniques Used

- **NE-11 Embedded Calculation Formulas** — ledger reconciliation, sink ratio, compounded weekly growth.
- **RT-06 Correlation and Cross-Analysis** — supply growth against the price basket and faucet concentration.
- **RT-23 Input Provenance Tagging** — data, estimate and guess labels on every flow and projection.
- **QA-02 Adversarial Stress-Test** — exploit loops and unlogged sources hunted before fixes are proposed.

## Related Prompts

- `domain-game-development/economy/economy_system_design.md` — designing the currency model being audited.
- `domain-game-development/economy/economy_liveops_monetization_ethics.md` — season calendar and paid-offer ethics.
- `domain-data-analytics/analysis-and-sql/analytics_metric_movement_investigation.md` — general metric-movement investigation.
