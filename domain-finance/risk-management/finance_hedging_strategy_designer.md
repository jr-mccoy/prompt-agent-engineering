---
title: "Hedging Strategy Designer — Instrument Selection, Hedge Ratio, Cost, Residual Risk"
category: finance/risk-management
description: "Design a hedging program: define the exposure, select instruments (forwards, futures, swaps, options, collars), compute the hedge ratio, quantify cost and basis risk, and characterize the residual risk that remains after hedging — without inventing prices or correlations."
techniques:
  - RT-03
  - NE-11
  - DS-02
  - QA-04
  - QA-02
difficulty: advanced
tags:
  - hedging
  - hedge-ratio
  - basis-risk
  - derivatives
  - options
  - residual-risk
updated: "2026-06-08"
related_prompts:
  - domain-finance/risk-management/finance_interest_rate_risk_analysis.md
  - domain-finance/risk-management/finance_market_risk_var_stress.md
  - domain-finance/risk-management/finance_counterparty_risk_assessment.md
  - domain-finance/field_guide.md
---

*For informational purposes only. Not financial, investment, hedging, or derivatives advice. Hedge accounting and derivatives use must be reviewed by qualified professionals.*

## Objective

Design a hedging program for a defined exposure by: (1) characterizing the exposure (direction, size, horizon, the variable being hedged), (2) selecting appropriate instruments and explaining the tradeoff each makes, (3) computing the hedge ratio and notional, (4) quantifying the cost (premium, carry, margin) and the basis risk, and (5) explicitly characterizing the **residual risk** that remains because no hedge is perfect. All prices, volatilities, and correlations are user-supplied or marked assumed.

## When to Use

- Hedging FX, rate, commodity, equity, or credit exposure on a position or cash flow
- Choosing between forwards/futures (symmetric) and options/collars (asymmetric) protection
- Sizing a partial vs. full hedge given cost and appetite
- Evaluating an existing hedge for effectiveness and basis risk
- Designing a rolling hedge program for recurring exposures

## Inputs / Context Required

- **Exposure:** Underlying variable, direction (long/short the risk), notional/quantity, and time horizon.
- **Objective:** Lock a rate/price, cap downside while keeping upside, reduce volatility to a target, or meet a covenant.
- **Available instruments:** Forwards, futures, swaps, options, collars, and the liquid hedge underlyings.
- **Market inputs:** Forward/futures prices, option premiums/implied vols, swap rates, and the correlation between the exposure and the hedge instrument (basis). User-supplied.
- **Constraints:** Budget for premium/carry, margin/collateral capacity, accounting (hedge-accounting eligibility), and counterparty preferences.
- **Risk appetite:** How much residual risk is acceptable (target hedge effectiveness or retained-loss tolerance).

## Constraints

### Must
- Define the exposure precisely before selecting any instrument.
- For each candidate instrument, state the tradeoff: cost, payoff shape (symmetric vs. asymmetric), margin/collateral, and basis risk.
- Compute the hedge ratio and resulting notional with the formula shown.
- Quantify cost (premium/carry/margin) and basis risk explicitly.
- Characterize residual risk: basis, correlation breakdown, over/under-hedge, roll, and counterparty risk.
- Present base / adverse / severe outcomes for the hedged vs. unhedged position.

### Must Not
- Invent prices, implied vols, or correlations; mark gaps `[ASSUMED]` and exclude from definitive conclusions.
- Claim a hedge eliminates risk — only transforms/reduces it; residual risk must be named.
- Ignore basis risk when the hedge instrument differs from the exposure.
- Present an option strategy's cost as zero without accounting for premium or foregone upside.
- Recommend a hedge ratio of 1.0 reflexively; the minimum-variance ratio may differ from naïve notional matching.

## Instructions

1. **Characterize the exposure (RT-03).** State what is being hedged, the harmful direction, the notional, and the horizon. Map the exposure's sensitivity (delta/duration/beta) to the hedge underlying.
2. **Select candidate instruments (DS-02).** For each, note the payoff shape and tradeoff:
   - **Forward/Future:** locks price; symmetric (gives up favorable moves); margin/roll for futures; low/no upfront cost.
   - **Swap:** exchanges a variable for fixed exposure; symmetric; counterparty/credit risk.
   - **Option (put/call):** asymmetric — caps downside, retains upside; costs premium.
   - **Collar:** caps downside, caps upside; reduces/zeroes net premium.
3. **Compute the hedge ratio (NE-11).**
   ```
   Minimum-variance hedge ratio:  h* = ρ × (σ_S / σ_F)
     ρ   = correlation between exposure (S) and hedge instrument (F)
     σ_S = volatility of the exposure;  σ_F = volatility of the hedge
   Hedge notional = h* × exposure notional × (price/contract conversion)
   Number of contracts = Hedge notional / (contract size × contract price)
   ```
   For duration hedging: `hedge notional = (D_exposure × V_exposure) / (D_hedge × price_factor)`.
4. **Quantify cost (QA-04).**
   ```
   Option cost = premium × notional  (and/or foregone upside above the cap)
   Forward/future cost ≈ carry (forward−spot basis) + margin funding
   Collar net cost = put premium − call premium received
   ```
5. **Quantify basis risk.** When the hedge underlying ≠ exposure, basis = exposure price − hedge price; show how basis variability leaves residual P&L even at a "full" hedge.
6. **Outcome grid (QA-02).** Compute hedged vs. unhedged P&L under base / adverse / severe moves of the underlying, including basis behavior.
7. **Characterize residual risk.** Enumerate what remains: basis risk, correlation breakdown (ρ falls in stress), over/under-hedge from a wrong ratio, roll risk (term mismatch), and counterparty/collateral risk (link to counterparty prompt).
8. **Disconfirming check.** Name the bias pitfalls — over-hedging from loss aversion, and assuming the hedge correlation holds in stress (it often weakens precisely when needed). Test the hedge under correlation → lower.

## Output Format

### Exposure Definition
| Field | Value |
|---|---|
| Underlying / variable | |
| Harmful direction | |
| Notional / quantity | |
| Horizon | |
| Sensitivity (delta/duration/beta) | |

### Instrument Comparison
| Instrument | Payoff shape | Upfront cost | Margin/collateral | Basis risk | Best when |
|---|---|---|---|---|---|
| Forward/Future | symmetric | low | yes (futures) | | |
| Swap | symmetric | low | counterparty | | |
| Option | asymmetric | premium | none (long) | | |
| Collar | capped both | low/zero net | varies | | |

### Hedge Ratio & Sizing
```
h* = ρ × (σ_S / σ_F) = [ ]
Hedge notional = h* × [exposure notional] = [$ ]
Contracts = [ ]
```

### Cost & Basis
| Item | Value | Basis |
|---|---|---|
| Premium / carry | [$] | |
| Margin funding | [$] | |
| Basis risk (σ of basis) | [ ] | |

### Hedged vs. Unhedged Outcomes (base / adverse / severe)
| Underlying move | Unhedged P&L | Hedge P&L | Net (incl. basis) | Residual loss |
|---|---|---|---|---|
| Base | | | | |
| Adverse | | | | |
| Severe-but-plausible | | | | |

### Residual Risk
[Basis, correlation breakdown, over/under-hedge, roll, counterparty — and the retained loss vs. appetite.]

## Verification

- [ ] The exposure is defined precisely before instrument selection.
- [ ] Each instrument's tradeoff (cost, payoff shape, margin, basis) is stated.
- [ ] The hedge ratio formula is shown with inputs; notional and contracts computed.
- [ ] Cost (premium/carry/margin) is quantified; option cost includes foregone upside.
- [ ] Basis risk is quantified when hedge underlying ≠ exposure.
- [ ] Hedged vs. unhedged outcomes are shown for base/adverse/severe.
- [ ] Residual risk is explicitly enumerated, including correlation breakdown and counterparty risk.
- [ ] No prices, vols, or correlations are invented; gaps `[ASSUMED]` and excluded from conclusions.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Claiming the hedge eliminates risk | Residual risk (basis, correlation, roll, counterparty) always enumerated; hedges transform, not erase |
| Ignoring basis risk | Quantified whenever hedge underlying differs from exposure |
| Option "free" because no margin | Premium and foregone upside counted as cost |
| Reflexive 1.0 hedge ratio | Minimum-variance ratio computed from ρ and vols; may differ from naïve matching |
| Assuming correlation holds in stress | Severe scenario lowers ρ; correlation-breakdown residual shown |
| Over-hedging from loss aversion | Bias named; hedge sized to exposure and appetite, not fear |
| Inventing implied vols to price options | Vols/prices user-supplied or `[ASSUMED]`; barred from definitive cost conclusions |
