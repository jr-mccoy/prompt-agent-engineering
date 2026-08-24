---
title: "Options Structure Selector — Map a Thesis to the Right Structure, Payoff, and Risk"
category: finance/options
description: "Translate a directional/volatility thesis (view, conviction, horizon, vol regime) into the options structure that expresses it efficiently — single legs, verticals, calendars, or defined-risk spreads — with explicit payoff, breakeven, max-loss, capital, and assignment/expiry risk. Selects defined-risk structures by default and rejects mismatches between thesis and structure."
techniques:
  - NE-11
  - NE-10
  - QA-02
  - DS-02
  - QA-04
difficulty: advanced
tags:
  - options
  - options-structures
  - payoff-diagram
  - breakeven
  - defined-risk
  - assignment-risk
updated: "2026-06-18"
related_prompts:
  - domain-finance/options/finance_implied_vol_greeks_analysis.md
  - domain-finance/investing-research/finance_position_sizing_framework.md
  - domain-finance/quant-fintech-data/finance_trading_strategy_premortem.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. Options can expire worthless and some structures carry unlimited or undefined loss. All outputs require independent verification before any capital is committed.**

## Objective

Given a precise thesis — direction, conviction, horizon, and a view on implied volatility — select
the options structure that expresses it with the best risk/reward and the least unnecessary risk.
The deliverable names the structure, shows its payoff, breakeven(s), max loss, capital at risk,
and the assignment/expiry hazards, and explicitly checks that the structure *matches* the thesis
(e.g. don't sell premium when you expect vol to rise). Defined-risk structures are the default;
undefined-risk structures are flagged and require explicit justification.

## When to Use

- Choosing how to express a Stage 2 thesis in options rather than the underlying
- Comparing candidate structures (long call vs. call vertical vs. calendar) for one view
- Pre-committing breakeven, max-loss, and exit before entry
- Catching a thesis/structure mismatch (direction or vol view) before risking capital

## Inputs / Context Required

**Thesis parameters**
- Direction (up / down / range-bound), conviction (size of expected move), horizon (to a date)
- Volatility view: do you expect IV to rise, fall, or hold? (pair with
  `finance_implied_vol_greeks_analysis.md`)

**Market & chain data (point-in-time)**
- Underlying price; the relevant option chain (strikes, expiries, IV, Greeks, open interest,
  bid/ask/liquidity)
- Earnings/catalyst dates within the horizon (assignment & IV-crush risk)
- Account constraints: capital, defined-risk requirement, approval level
- Any input unavailable → mark `UNAVAILABLE` and queue (DS-02)

## Constraints

### Must
- Match the structure to **both** the directional and the volatility view; state the match
  explicitly (long premium when expecting vol up; short premium / spreads when expecting vol down)
  (QA-02).
- Show payoff, breakeven(s), max loss, max gain (or "undefined"), and capital at risk with
  embedded formulas (NE-11).
- Default to **defined-risk** structures; if proposing undefined/large-loss structures (naked
  short options), flag the unlimited/large loss prominently and justify (NE-10).
- Account for assignment risk, early exercise (American), expiry, liquidity (bid/ask), and
  IV-crush around catalysts (DS-02).
- Pre-commit an exit / management plan and flag conclusions resting on `UNAVAILABLE` data (QA-04).

### Must Not
- Recommend selling premium into an expected vol expansion (or buying premium into expected
  vol crush) — a thesis/structure mismatch.
- Quote a structure without breakeven and max-loss.
- Propose an undefined-risk structure as the default or without an explicit risk flag.
- Ignore liquidity (wide spreads can dominate edge) or catalyst-timing/IV-crush.
- Invent chain prices, IV, or Greeks — queue unknowns (DS-02).

## Instructions

1. **Restate the thesis precisely (QA-02).** Direction, conviction (expected move size), horizon,
   and IV view. If the IV view is missing, get it from `finance_implied_vol_greeks_analysis.md`
   before selecting — vol view drives long-vs-short premium.

2. **Shortlist matching structures.** From the view, list 2–3 candidate structures and reject any
   that mismatch direction or vol. Examples: bullish + vol-up → long call / call vertical (debit);
   bullish + vol-down → put credit spread; range + vol-down → iron condor (defined-risk);
   event with IV-crush expected → avoid long premium through the print.

3. **Quantify each candidate (NE-11).** For each, compute breakeven(s), max loss, max gain (or
   undefined), capital at risk, and approximate probability-of-profit framing. E.g. for a debit
   vertical: `max_loss = net_debit`, `breakeven = long_strike + net_debit`, `max_gain =
   strike_width − net_debit`.

4. **Risk overlay (DS-02, NE-10).** Note assignment/early-exercise, expiry, liquidity (bid/ask
   width), and catalyst/IV-crush risk per candidate. Default to defined-risk; flag any
   undefined-risk leg prominently.

5. **Select and plan (QA-04).** Recommend the best-matched structure with rationale; pre-commit
   entry conditions, an exit/management plan (profit target, stop, roll/close rules), and list any
   queued unknowns.

## Output Format

```
## OPTIONS STRUCTURE: <UNDERLYING> | as_of [date] | Thesis: [dir/conviction/horizon/vol view]
```

### Candidate structures
| Structure | Matches dir? | Matches vol? | Breakeven(s) | Max loss | Max gain | Capital |
|---|---|---|---|---|---|---|
| … | yes/no | yes/no | … | … | …/undefined | … |

### Recommended structure
- Structure: … · Why it matches the thesis (direction + vol): …
- Payoff summary: breakeven … · max loss … · max gain … · capital at risk …

### Risk overlay
| Risk | Note |
|---|---|
| Assignment / early exercise | … |
| Expiry / time decay | … |
| Liquidity (bid/ask) | … |
| Catalyst / IV-crush | … |

### Management plan & open items
- Entry condition · profit target · stop · roll/close rules
- `UNAVAILABLE` inputs (queued)

## Verification

- [ ] Structure matches BOTH the directional and the volatility view (stated explicitly).
- [ ] Breakeven(s), max loss, max gain (or "undefined"), and capital are computed and shown.
- [ ] Defined-risk default honored; any undefined-risk leg is flagged and justified.
- [ ] Assignment, expiry, liquidity, and catalyst/IV-crush risks are addressed.
- [ ] An exit/management plan is pre-committed.
- [ ] Chain inputs sourced or queued; no invented IV/Greeks/prices.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Selling premium into expected vol expansion | Require explicit vol-view match; reject mismatches (QA-02) |
| Quoting a structure without its loss profile | Mandatory breakeven + max-loss with formulas (NE-11) |
| Undefined-risk structure slipped in as default | Defined-risk default; unlimited-loss legs flagged + justified (NE-10) |
| Edge erased by wide bid/ask | Liquidity overlay required per candidate |
| Long premium held through an IV-crush event | Catalyst/IV-crush check in the risk overlay |
| Missing chain data filled with guesses | `UNAVAILABLE` + queue (DS-02) |
