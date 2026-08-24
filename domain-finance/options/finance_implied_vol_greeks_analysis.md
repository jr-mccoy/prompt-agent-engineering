---
title: "Implied Volatility & Greeks Analysis — Level, Skew, Term, and Position Sensitivities"
category: finance/options
description: "Interpret an option's or position's implied volatility (level vs. realized, skew, term structure) and Greeks (delta, gamma, theta, vega, and rho where relevant) to understand what is priced in, where the risk sits, and how the position behaves under price, time, and vol shocks — with embedded formulas, scenario sensitivity, and a guard against treating model Greeks as certainties."
techniques:
  - NE-11
  - NE-10
  - DS-02
  - QA-02
  - QA-04
difficulty: advanced
tags:
  - implied-volatility
  - greeks
  - vol-skew
  - term-structure
  - theta-decay
  - options
updated: "2026-06-18"
related_prompts:
  - domain-finance/options/finance_options_structure_selector.md
  - domain-finance/quant-fintech-data/finance_trading_strategy_premortem.md
  - domain-finance/valuation/finance_valuation_sensitivity_scenario.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. Greeks are model outputs that change with conditions and assumptions; they are estimates, not guarantees. All outputs require independent verification before any capital is committed.**

## Objective

Read what the options market is pricing and how a position will behave. The deliverable explains
the implied-volatility picture (level vs. realized, skew, term structure — i.e. what's "expensive"
or "cheap" and why), quantifies the position's Greeks and what each one means for P&L under price,
time, and vol moves, and runs a scenario sensitivity (spot ±, vol ±, days forward). It treats
Greeks as condition-dependent estimates, not certainties, and anchors "high/low IV" to a base rate
rather than a gut call.

## When to Use

- Deciding whether options are rich or cheap before selecting a structure (pairs with
  `finance_options_structure_selector.md`)
- Understanding a position's exposure (directional, decay, vol) before or after entry
- Stress-testing how a position behaves into a catalyst (IV-crush) or a vol shock
- Diagnosing why a position is gaining/losing despite the underlying barely moving

## Inputs / Context Required

**Vol data (point-in-time)**
- Implied volatility by strike and expiry (the surface, or at least ATM IV + a couple of skew
  points); realized/historical volatility for comparison; IV rank/percentile if available
- Term structure (front vs. back month)

**Position & Greeks**
- The contract(s) / position; underlying price; days to expiry; per-leg and net Greeks (delta,
  gamma, theta, vega; rho if rates matter)
- Catalyst/earnings dates within the horizon
- Any input unavailable → mark `UNAVAILABLE` and queue (DS-02)

## Constraints

### Must
- Compare IV to realized vol and to its own history (IV rank/percentile) before calling it
  high/low — anchor to a base rate (NE-11).
- Interpret skew and term structure (what the shape implies about demand/risk pricing), not just
  ATM IV (DS-02).
- Quantify each Greek and translate it into plain P&L terms (e.g. theta = $/day decay; vega =
  $/vol-point) with embedded formulas (NE-11).
- Run a scenario sensitivity across spot, vol, and time, presenting a range of outcomes (NE-10).
- Treat Greeks as model estimates that move with conditions; state assumptions and flag missing
  inputs (QA-02, QA-04).

### Must Not
- Call IV "high" or "low" without a realized/historical reference.
- Report Greeks as fixed truths (they change with spot, vol, and time — note gamma/vanna effects
  qualitatively).
- Ignore term structure or skew when they materially change the read.
- Omit catalyst/IV-crush effects when an event sits inside the horizon.
- Invent IV points, Greeks, or realized-vol figures — queue unknowns (DS-02).

## Instructions

1. **Frame the vol picture (NE-11).** State ATM IV, realized vol over a comparable window, and IV
   rank/percentile. Compute the IV/RV relationship (e.g. `vrp = IV − RV`) to judge rich/cheap;
   anchor "high/low" to this, not intuition.

2. **Read skew and term (DS-02).** Describe the skew (put vs. call IV) and term structure (front
   vs. back); say what the shape implies (e.g. downside demand, event premium in the front month).

3. **Quantify the Greeks (NE-11).** For the position, state net delta (directional exposure),
   gamma (how delta changes), theta ($/day decay), vega ($/vol-point), and rho if relevant.
   Translate each into P&L: e.g. `daily_decay ≈ theta`, `pnl_from_vol ≈ vega × ΔIV`,
   `pnl_from_move ≈ delta × ΔS + 0.5 × gamma × ΔS²`.

4. **Scenario sensitivity (NE-10).** Build a grid over spot (−/0/+), vol (−/0/+), and a few days
   forward; show approximate P&L in each cell so the dominant risk is visible. Highlight the worst
   realistic cell.

5. **Catalyst & caveats (QA-02, QA-04).** If an event is in the horizon, model IV-crush on the
   position. State the assumptions behind the Greeks (they are estimates), and list queued unknowns.

## Output Format

```
## IV & GREEKS: <UNDERLYING / POSITION> | as_of [date]
```

### Volatility picture
| Measure | Value | Reference | Read (rich/cheap/neutral) |
|---|---|---|---|
| ATM IV | … | realized vol … | … |
| IV rank/percentile | … | own history | … |
| Skew (put vs call) | … | — | implies … |
| Term (front vs back) | … | — | implies … |

### Position Greeks → P&L meaning
| Greek | Value | P&L translation |
|---|---|---|
| Delta | … | $ per $1 underlying move |
| Gamma | … | how delta shifts |
| Theta | … | $ decay per day |
| Vega | … | $ per 1 vol point |

### Scenario sensitivity (approx P&L)
| | Vol − | Vol 0 | Vol + |
|---|---|---|---|
| Spot − | … | … | … |
| Spot 0 | … | … | … |
| Spot + | … | … | … |

### Catalyst, assumptions & open items
- IV-crush impact (if event in horizon) · Greek assumptions (estimates) · `UNAVAILABLE` (queued)

## Verification

- [ ] IV is compared to realized vol and its own history before any high/low call.
- [ ] Skew and term structure are interpreted, not just ATM IV.
- [ ] Each Greek is quantified and translated into plain P&L terms with formulas.
- [ ] A spot × vol × time scenario sensitivity is presented; worst realistic cell highlighted.
- [ ] Greeks are framed as condition-dependent estimates; assumptions stated.
- [ ] Catalyst/IV-crush handled; missing inputs queued, not invented.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| "IV is high" with no reference | Anchor to realized vol + IV rank/percentile (NE-11) |
| Greeks treated as fixed certainties | State they move with conditions; note gamma/vanna qualitatively (QA-02) |
| ATM-only read misses the real risk | Require skew + term-structure interpretation (DS-02) |
| Single-point P&L hides the risk shape | Mandatory spot × vol × time scenario grid (NE-10) |
| Long premium through earnings surprises trader | Model IV-crush when an event is in the horizon |
| Missing vol/Greek inputs guessed | `UNAVAILABLE` + queue (DS-02, QA-04) |
