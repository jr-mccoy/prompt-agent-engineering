---
title: "Position Sizing Framework — Conviction, Edge, Odds, and Kelly-Aware Limits"
category: finance/investing-research
description: "Size a position from edge, odds, and conviction using a Kelly-aware framework with fractional-Kelly discipline, explicit risk limits (per-name, drawdown, liquidity), and an estimation-error stress test."
techniques:
  - NE-11
  - NE-10
  - DS-02
  - QA-04
  - CM-02
difficulty: advanced
tags:
  - position-sizing
  - kelly-criterion
  - risk-limits
  - conviction
  - expected-value
  - bet-sizing
updated: "2026-06-08"
related_prompts:
  - domain-finance/investing-research/finance_investment_thesis_builder.md
  - domain-finance/investing-research/finance_portfolio_construction_review.md
  - domain-finance/risk-management/finance_position_risk_sizing.md
  - domain-finance/field_guide.md
---

*For informational purposes only. Not financial, investment, or tax advice. Bet-sizing formulas amplify estimation error; outputs are upper-bound references, not targets.*

## Objective

Translate a thesis's edge, odds, and conviction into a position size that is mathematically grounded yet survivable. The framework computes the full-Kelly optimal fraction, applies fractional-Kelly discipline (because edge and odds are estimated, not known), and binds the result with hard risk limits — per-name cap, portfolio drawdown tolerance, and liquidity/exit constraints. The output is a recommended size with the reasoning trace and an estimation-error stress test, never a single confident number.

## When to Use

- Sizing a new position after the thesis and payoff scenarios are built
- Resizing after a material change in conviction, odds, or price
- Reconciling "how much do I believe this" with "how much can I lose"
- Imposing discipline on a high-conviction idea that tempts over-sizing
- Setting initial size vs. a planned scale-in/scale-out path

## Inputs / Context Required

**Payoff inputs**
- Probability-weighted scenarios from the thesis: P(win), P(loss), and the up/down outcomes (e.g., +40% / −20%)
- Current price and the bear-case loss (downside) used for risk budgeting
- Expected value and upside/downside skew, if already computed

**Conviction & edge**
- Conviction level (High/Med/Low) and what it is grounded in
- Whether the edge is differentiated (variant view) or shared (consensus)
- Estimation confidence: how reliable are the probability and payoff inputs

**Risk limits (constraints)**
- Per-name maximum (% of portfolio) and the house Kelly fraction (e.g., 1/4 to 1/2 Kelly)
- Maximum tolerable drawdown contribution from this position
- Liquidity: average daily volume, position as days-to-exit, gap-risk considerations
- Correlation to existing book (if known)

## Constraints

### Must
- Compute full-Kelly explicitly and apply a fractional-Kelly haircut, stating the fraction and why (NE-11).
- Treat probabilities and payoffs as estimates with error; require an estimation-error stress test (QA-04).
- Bind the Kelly output by hard risk limits (per-name, drawdown, liquidity); the recommended size is the MINIMUM of the Kelly-implied size and the limits (CM-02).
- Express size as a range with conditions, not a single point (NE-10).
- Specify each input precisely (definition, source) (DS-02).

### Must Not
- Recommend full Kelly; it is mathematically optimal only with perfectly known odds and is far too volatile in practice.
- Size purely on conviction without odds and edge.
- Ignore liquidity/exit constraints (a great size you cannot exit is a bad size).
- Invent probabilities or payoffs. Mark `[ASSUMED]` and stress-test sensitivity to them.
- Let a high-conviction narrative override the per-name and drawdown caps.

## Instructions

1. **Restate the bet precisely (DS-02).** Define P(win), P(loss), the win payoff (b = gain/loss ratio), and the loss size, each tied to the thesis scenarios. Note the conviction level and whether the edge is differentiated.

2. **Compute expected value and edge (NE-11).**
```
b = (upside gain) / (downside loss)        e.g., +40% / 20% → b = 2.0
p = P(win),  q = 1 − p
Expected value (per $1) = p × upside − q × |downside|
Edge exists only if EV > 0; if EV ≤ 0, do not size — revisit the thesis.
```

3. **Compute the Kelly fraction (NE-11).**
```
Full Kelly fraction  f* = (b·p − q) / b = p − q/b
   where b = win/loss payoff ratio, p = win prob, q = loss prob
```
   If f* ≤ 0, the bet has no positive edge at these odds — size = 0.

4. **Apply fractional Kelly (QA-04).** Because p and b are estimates, scale down:
```
Sized fraction = k × f*      (k = 1/4 to 1/2 typical; state the house k)
Rationale: estimation error in p and b makes full Kelly over-bet; fractional Kelly
   sacrifices little expected growth for large reductions in volatility and ruin risk.
```

5. **Bind by risk limits (CM-02).**
```
Recommended size = MIN( k·f* , per-name cap , drawdown-budget size , liquidity-cap size )
   drawdown-budget size = (max tolerable drawdown contribution) / (bear-case loss %)
   liquidity-cap size    = bounded so days-to-exit ≤ threshold at participation limit
```

6. **Estimation-error stress test (QA-04).** Recompute the Kelly size under pessimistic inputs (lower p, lower b). Show how sensitive the size is to a 5–10pp shift in p. If the size collapses under modest input changes, recommend the lower bound.

7. **Define the scale path.** State the initial size, the conditions to add (catalyst confirmed, price improves edge) and to trim (thesis weakens, size limit hit on appreciation).

## Output Format

```
## POSITION SIZING: [Company] ([Ticker]) | Conviction: [H/M/L] | Edge: [differentiated / shared]
```

### Bet Definition
| Input | Value | Source / `[ASSUMED]` |
|---|---|---|
| P(win) = p | [%] | |
| P(loss) = q | [%] | |
| Upside gain | [%] | |
| Downside loss | [%] | |
| Payoff ratio b | [x] | |

### Edge & Kelly
```
EV = p×upside − q×|downside| = [ ]        → edge exists: [yes/no]
Full Kelly f* = p − q/b = [ ]
Fractional Kelly = k × f* (k = [1/4–1/2]) = [ ]% of capital
```

### Risk Limits Binding
| Constraint | Implied max size | Binding? |
|---|---|---|
| Fractional Kelly | [%] | |
| Per-name cap | [%] | |
| Drawdown budget = maxDD / bear-loss | [%] | |
| Liquidity (days-to-exit) | [%] | |
- **Recommended size = MIN(...) = [%]**

### Estimation-Error Stress
| Input shift | New f* | New sized fraction |
|---|---|---|
| p −5pp | | |
| b −0.5 | | |
| Both pessimistic | | |
- **Robustness verdict:** [size stable / collapses → use lower bound]

### Scale Path
- **Initial:** [%] | **Add if:** … | **Trim if:** …

## Verification

- [ ] EV is computed and positive before any sizing; non-positive EV → size 0.
- [ ] Full Kelly f* is shown with inputs, then haircut to fractional Kelly with the fraction stated.
- [ ] Full Kelly is never the recommendation; fractional discipline is applied and justified.
- [ ] The recommended size is the MINIMUM of Kelly and all hard risk limits.
- [ ] Drawdown-budget and liquidity caps are each computed.
- [ ] An estimation-error stress test shows sensitivity to lower p and b.
- [ ] Probabilities/payoffs are sourced or `[ASSUMED]`; sensitivity tested if assumed.
- [ ] A scale path (add/trim conditions) is specified.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Recommending full Kelly | Full Kelly shown for reference only; fractional Kelly (1/4–1/2) is the rule, with rationale |
| Sizing on conviction alone | Requires p, q, b, and positive EV before any size is computed |
| Treating estimated odds as known | Estimation-error stress test mandatory; collapsing size → lower bound |
| Ignoring liquidity/exit | Liquidity cap (days-to-exit) is a binding constraint in the MIN |
| Letting a narrative override caps | Per-name and drawdown caps bind the Kelly output unconditionally |
| Precision illusion in a single % | Output is a range with binding-constraint trace, not a point |
| Inventing win probabilities | `[ASSUMED]` flags required; sensitivity shown for assumed inputs |
| Over-betting after a winning streak | Scale path and per-name cap prevent conviction-creep into oversizing |
