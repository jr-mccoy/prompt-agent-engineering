---
title: "Market-Risk Framing — VaR Methods, Limitations, and Complementary Stress Tests"
category: finance/risk-management
description: "Frame market risk with Value-at-Risk across parametric, historical, and Monte Carlo methods — foregrounding VaR's limitations (not a worst case, breaks in the tails) and pairing it with mandatory stress and tail measures, without inventing volatilities or correlations."
techniques:
  - NE-11
  - NE-10
  - QA-04
  - QA-02
  - RT-03
difficulty: advanced
tags:
  - market-risk
  - value-at-risk
  - expected-shortfall
  - stress-testing
  - volatility
  - backtesting
updated: "2026-06-08"
related_prompts:
  - domain-finance/risk-management/finance_stress_test_scenario_design.md
  - domain-finance/risk-management/finance_tail_risk_premortem.md
  - domain-finance/risk-management/finance_hedging_strategy_designer.md
  - domain-finance/field_guide.md
---

*For informational purposes only. Not financial, investment, or risk-management advice. VaR is a statistical estimate, not a guarantee; review all outputs with qualified professionals.*

## Objective

Frame the market risk of a position or portfolio using Value-at-Risk computed by parametric (variance-covariance), historical-simulation, and Monte Carlo methods, with each method's assumptions and limitations made explicit. Present VaR alongside Expected Shortfall (Conditional VaR) and a mandatory complementary stress test, so the analysis never relies on VaR as a maximum-loss figure. All inputs (volatilities, correlations, factor sensitivities) are supplied by the user or marked assumed.

## When to Use

- Sizing or limit-setting for a trading book, treasury portfolio, or investment mandate
- Risk reporting to a CRO, investment committee, or regulator
- Comparing the risk of two portfolios on a common metric
- Diagnosing why a portfolio's realized losses exceeded its modeled risk
- Building the market-risk leg of an enterprise stress program

## Inputs / Context Required

- **Portfolio composition:** Positions/exposures, notional or market value per instrument, currency.
- **Risk factors:** Equity, rate, FX, credit-spread, commodity sensitivities (deltas/durations/betas).
- **Volatility & correlation inputs:** Per-factor volatility and the correlation matrix (or a historical return series the user supplies). State the estimation window.
- **Confidence level & horizon:** e.g., 99% / 1-day, or 95% / 10-day. Specify both.
- **Method preference:** Parametric, historical, Monte Carlo, or all three (recommended).
- **Distributional assumption:** Normal, t-distribution (state degrees of freedom), or empirical.
- **Stress scenarios:** Any prescribed shocks (regulatory or internal); otherwise the model proposes severe-but-plausible ones for confirmation.
- **Backtest data (if available):** Historical P&L vs. prior VaR for exception counting.

## Constraints

### Must
- State every VaR method's assumptions and limitations before reporting a number (NE-11, QA-04).
- Foreground that VaR is **not** a worst case: it estimates the loss threshold not exceeded with a stated confidence; losses beyond it are expected (1−confidence) of the time and can be far larger.
- Report Expected Shortfall (ES / CVaR) alongside VaR to characterize tail severity.
- Pair VaR with at least one stress test that does not rely on the modeled distribution.
- Show the formula and inputs for each computed figure.
- State the estimation window and note that VaR assumes the distribution and correlations observed in that window persist.
- Report scaling assumptions explicitly when converting horizons (e.g., √t scaling and its limits).

### Must Not
- Present VaR as the maximum or worst possible loss.
- Invent volatilities, correlations, or a return series; mark missing inputs `[ASSUMED]` and state the placeholder used.
- Use √t time-scaling for non-linear (optionality-heavy) portfolios without flagging the breakdown.
- Assume normality silently when the portfolio has material tail/optionality exposure.
- Add VaRs across desks/assets as if they were additive (they are not; diversification and correlation matter).
- Omit the limitations and stress complement, even if the user asks only for "the VaR number."

## Instructions

1. **Map exposures to risk factors (NE-10).** Translate each position into factor sensitivities (delta, duration, beta, vega). Flag non-linear instruments (options, convertibles) where delta-only treatment understates risk.
2. **State confidence and horizon.** Confirm the z-score / quantile used:
   ```
   95% → z ≈ 1.645      99% → z ≈ 2.326   (one-tailed, normal)
   ```
3. **Parametric (variance-covariance) VaR.**
   ```
   Parametric VaR = z × σ_p × √t × V
     σ_p = √(wᵀ Σ w)            (portfolio volatility from weights w, covariance Σ)
     V   = portfolio market value
     t   = horizon in the σ's time unit
   ```
   State limitation: assumes normal, linear exposures; understates tail risk and option risk.
4. **Historical-simulation VaR.** Apply the supplied historical factor changes to today's positions; take the (1−confidence) quantile of the simulated P&L distribution. State limitation: bounded by the window; misses unobserved shocks; equally weights stale and recent data unless decayed.
5. **Monte Carlo VaR.** Simulate factor paths from the assumed distribution/correlation; revalue (full revaluation for non-linear books); take the quantile. State limitation: only as good as the assumed distribution and correlation matrix; model risk concentrated here.
6. **Expected Shortfall.**
   ```
   ES_α = E[ Loss | Loss > VaR_α ]
   ```
   Report ES at the same confidence; it captures average severity in the tail VaR ignores.
7. **Complementary stress (RT-03).** Apply at least one severe-but-plausible scenario (e.g., correlations → 1, a historical crisis replay, or a prescribed shock set) and report the P&L. This does not depend on the modeled quantile.
8. **Backtest (if data provided, QA-02).** Count exceptions vs. expected (e.g., ~2–3 per year at 99%/1-day over 250 days). Excess exceptions indicate model underestimation; cluster the exceptions in time.
9. **Bias & disconfirming check.** Name the relevant pitfalls — precision-illusion (a single VaR figure feigning certainty), recency (calm-window volatility), survivorship (excluding blown-up instruments). State how each is mitigated.

## Output Format

### Method Comparison
| Method | VaR ([conf] / [horizon]) | Key Assumption | Primary Limitation |
|---|---|---|---|
| Parametric | [$] | normal, linear | understates tails & optionality |
| Historical | [$] | window repeats | bounded by observed history |
| Monte Carlo | [$] | assumed dist/corr | model risk in assumptions |
| **Expected Shortfall** | **[$]** | tail average | depends on tail modeling |

### Computation Trace (one per method)
```
Parametric VaR = z × σ_p × √t × V
  z = [ ]  σ_p = [ ]  √t = [ ]  V = [$ ]  → VaR = [$ ]
```

### VaR vs. Stress (base / adverse / severe)
| Measure | Base (modeled) | Adverse stress | Severe-but-plausible stress |
|---|---|---|---|
| Portfolio P&L | [$] | [$] | [$] |
| Loss vs. capital/limit | [%] | [%] | [%] |
| Scenario description | normal window | [shock set] | [crisis replay / corr→1] |

### Backtest Summary (if data provided)
| Confidence | Expected exceptions | Observed exceptions | Clustered? | Verdict |
|---|---|---|---|---|

### Limitations Statement
[Explicit paragraph: VaR is a threshold not a ceiling; tail losses exceed it (1−conf) of the time; assumptions, window, and scaling caveats restated.]

## Verification

- [ ] Each VaR method's assumptions and limitations are stated before its number.
- [ ] VaR is explicitly described as a threshold, not a maximum loss; tail-exceedance is quantified.
- [ ] Expected Shortfall is reported at the same confidence as VaR.
- [ ] At least one stress test independent of the modeled distribution is included.
- [ ] Confidence level, horizon, z-score/quantile, and estimation window are all stated.
- [ ] No volatilities or correlations are invented; gaps marked `[ASSUMED]` with the placeholder shown.
- [ ] Non-linear instruments are flagged; √t scaling caveats noted where applicable.
- [ ] Backtest exception count (if data given) is compared to the expected rate and clustering checked.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Treating VaR as the worst-case loss | Mandatory limitations statement: VaR is a confidence threshold; losses beyond it are expected and unbounded |
| Single precise VaR figure implying certainty | Report three methods + ES + stress; precision-illusion named and divergence shown |
| Normality hiding fat tails | Require t-distribution or historical/empirical option; flag normality when optionality is present |
| √t scaling on optionality-heavy books | Flag breakdown; require full revaluation for non-linear portfolios |
| Adding desk VaRs as additive | Use the covariance/correlation aggregation; show diversification benefit explicitly |
| Calm-window volatility understating risk | Name recency bias; require a stress that does not depend on the window |
| Backtest passing by chance | Report observed vs. expected exceptions and time-clustering, not a pass/fail alone |
