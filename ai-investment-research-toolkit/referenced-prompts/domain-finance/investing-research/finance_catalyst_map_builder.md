---
title: "Catalyst Map Builder — Dated Events and Probability-Weighted Impact"
category: finance/investing-research
description: "Map the dated catalysts in a thesis, assign each a probability and a value impact, compute the probability-weighted contribution to the price target, and sequence them on a timeline with confirm/break read-throughs."
techniques:
  - NE-10
  - NE-11
  - DS-02
  - DS-06
  - QA-04
difficulty: intermediate
tags:
  - catalysts
  - event-driven
  - probability-weighting
  - timeline
  - re-rating
  - thesis-tracking
updated: "2026-06-08"
related_prompts:
  - domain-finance/investing-research/finance_investment_thesis_builder.md
  - domain-finance/investing-research/finance_earnings_preview_builder.md
  - domain-finance/investing-research/finance_position_sizing_framework.md
  - domain-finance/field_guide.md
---

*For informational purposes only. Not financial, investment, or tax advice.*

## Objective

Turn a thesis's loose list of "things that could happen" into a structured catalyst map: each catalyst dated or windowed, assigned an independent probability of occurring and a value impact if it does, with a probability-weighted contribution to the overall price target. The map sequences catalysts on a timeline, distinguishes hard catalysts (dated) from soft ones (open-ended), and ties each to a confirm/break read-through so the thesis can be tracked event by event.

## When to Use

- Building or refining the catalyst section of a long or short thesis
- Deciding whether a thesis has a "clock" or is open-ended (re-rating risk)
- Sequencing position sizing or hedging around dated events
- Tracking a multi-catalyst event-driven situation (spin-off, refinancing, regulatory path)
- Prioritizing which catalysts to monitor most closely

## Inputs / Context Required

**Thesis context**
- Company, ticker, current price, and the standing thesis (one line)
- The price target or fair-value range the catalysts are meant to unlock
- Time horizon and base currency

**Catalyst inventory**
- The candidate catalysts: earnings, product launches, regulatory decisions, capital allocation (buyback/dividend/M&A), debt maturities/refinancing, contract wins, legal outcomes, index events
- Known or estimated dates/windows for each (or "open-ended")
- Any base rates or evidence bearing on probability (precedent, management commentary, regulatory timelines)

**Optional**
- Options expiries or implied moves around dated events
- Correlation/dependency between catalysts (e.g., refinancing contingent on an earnings beat)

## Constraints

### Must
- Date or window every catalyst; explicitly label open-ended catalysts as soft (re-rating risk) (DS-02).
- Assign each catalyst an independent probability and a value impact, and compute the probability-weighted contribution (NE-10, NE-11).
- Acknowledge uncertainty in probabilities — these are estimates, not measured frequencies (QA-04).
- Flag dependencies between catalysts so probabilities are not double-counted (DS-06).
- Tie each catalyst to a confirm/break read-through for the thesis.

### Must Not
- Invent dates, regulatory timelines, or base rates. Mark `[ASSUMED]` and state the basis.
- Present probability-weighted impact as a precise forecast; it is a planning estimate with wide error.
- Sum impacts of dependent catalysts as if independent (double-counting).
- Treat a soft, open-ended catalyst as if it had a known date.

## Instructions

1. **Inventory and classify catalysts (DS-02).** List each catalyst, its type, and whether it is **hard** (dated/windowed) or **soft** (open-ended). Soft catalysts carry timing risk and should be flagged.

2. **Assign probability and impact (NE-10).** For each catalyst:
```
P(occur)  = estimated probability the event happens in the window  [state basis; QA-04 uncertainty]
Δvalue    = estimated price/value impact if it occurs (can be + or −)
Contribution = P(occur) × Δvalue
```
   State the basis for each probability (precedent base rate, management guidance, regulatory calendar) and mark `[ASSUMED]` where it is a judgment call.

3. **Handle dependencies (DS-06).** Identify catalysts that are conditional on one another. Use conditional probabilities to avoid double-counting:
```
P(B and A) = P(A) × P(B | A)   — do not add P(A)·Δ + P(B)·Δ when B requires A
```

4. **Aggregate the map.**
```
Probability-weighted re-rating = Σ Contribution_i (independent catalysts)
   + Σ conditional contributions (dependent chains)
Compare to the gap between current price and the price target:
   coverage = weighted re-rating / (target − current price)
```
   A low coverage ratio means the target relies on catalysts not yet identified — flag it.

5. **Sequence on a timeline.** Order catalysts by date. Note clustering (multiple events in one window raise event risk) and any gaps where the thesis has no clock.

6. **Rank by monitoring priority (DS-06).** Prioritize catalysts by |contribution| × proximity. List the leading indicators to watch for each.

7. **Read-throughs.** For each catalyst, state what its occurrence/non-occurrence confirms or breaks in the thesis.

## Output Format

```
## CATALYST MAP: [Company] ([Ticker]) | Price [$] → Target [$] | Horizon [ ]
```

### Catalyst Register
| Catalyst | Type | Hard/Soft | Date / window | P(occur) | Δvalue | Contribution | Basis |
|---|---|---|---|---|---|---|---|
| | | | | [%] | [±%] | [±%] | [source/`[ASSUMED]`] |

### Dependencies
| Dependent catalyst | Conditional on | P(B\|A) | Adjusted contribution |
|---|---|---|---|

### Aggregate
```
Probability-weighted re-rating = Σ contributions = [±%]
Gap to target = (Target − Current)/Current = [%]
Coverage = weighted re-rating / gap = [x]   → [flag if << 1]
```

### Timeline
| Date / window | Catalyst | Clustered? | Has-clock note |
|---|---|---|---|

### Monitoring Priority
| Rank | Catalyst | |Contribution| × proximity | Leading indicator |
|---|---|---|---|

### Read-Throughs
| Catalyst | If occurs | If does not occur |
|---|---|---|

## Verification

- [ ] Every catalyst is dated/windowed or explicitly labeled soft/open-ended.
- [ ] Each catalyst has a probability and impact, with the basis stated.
- [ ] Probability estimates are flagged as uncertain, not measured frequencies.
- [ ] Dependent catalysts use conditional probabilities; no double-counting.
- [ ] The probability-weighted re-rating is computed and compared to the price gap (coverage ratio).
- [ ] Low coverage (target relies on un-mapped catalysts) is flagged.
- [ ] Catalysts are sequenced on a timeline with clustering and clock-gaps noted.
- [ ] No invented dates, regulatory timelines, or base rates; `[ASSUMED]` flags present.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Presenting probability-weighted impact as a precise forecast | Label as a planning estimate with wide error; QA-04 uncertainty stated |
| Inventing regulatory dates or base rates | Mark `[ASSUMED]` with stated basis; never fabricate calendars |
| Double-counting dependent catalysts | Conditional probabilities required for contingent events |
| Treating a soft catalyst as if dated | Hard/soft classification mandatory; soft catalysts flagged for timing risk |
| Over-relying on catalysts to justify the target | Coverage ratio exposes targets that depend on un-mapped catalysts |
| Anchoring on a single big catalyst | Monitoring priority weights by contribution AND proximity, not size alone |
| Optimism on probabilities | Basis required for each estimate; judgment calls explicitly `[ASSUMED]` |
