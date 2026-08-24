---
title: "Cross-Asset Correlation & Regime Analysis — Diversification, Co-Movement, and Tail Behavior"
category: finance/markets-macro
description: "Build and interpret a cross-asset correlation matrix, distinguish regime-dependent and tail correlations from full-sample averages, assess true diversification and concentration, and stress-test the portfolio against correlation breakdown — with all return data user-supplied."
techniques:
  - RT-06
  - NE-11
  - QA-02
  - NE-10
  - QA-04
difficulty: advanced
tags:
  - correlation
  - cross-asset
  - diversification
  - regime
  - tail-risk
updated: "2026-06-08"
related_prompts:
  - domain-finance/risk-management/finance_market_risk_var_stress.md
  - domain-finance/risk-management/finance_tail_risk_premortem.md
  - domain-finance/investing-research/finance_portfolio_construction_review.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. Correlations are unstable, regime-dependent, and backward-looking; all return data is user-supplied and outputs require professional review.**

## Objective

Construct a cross-asset correlation analysis that (1) builds the correlation matrix from user-supplied returns with method and window stated, (2) distinguishes full-sample correlation from regime-conditional and tail correlation, (3) assesses true diversification and hidden concentration, and (4) stress-tests the portfolio against correlation breakdown ("correlations go to 1 in a crisis") — guarding against treating a single estimate as stable or causal.

## When to Use

- Checking whether a portfolio is as diversified as its asset count suggests
- Diagnosing why "diversifiers" failed together in a drawdown
- Assessing regime-dependence of the stock/bond correlation
- Building the correlation input to a VaR/stress model or portfolio construction review
- Pressure-testing a "this asset is uncorrelated" claim

## Inputs / Context Required

```
<correlation_inputs>
Assets / portfolio: (list assets, indices, or factors) | Base currency | As-of date

USER-SUPPLIED RETURN DATA (do not assume returns or correlations from memory):
  - Return series per asset (frequency: daily/weekly/monthly), with date range and source
    OR a pre-computed correlation matrix (state method, window, source)
  - Portfolio weights per asset (if assessing a specific portfolio)
  - Volatilities per asset (if available, else compute from returns)

REGIME LABELS (optional but recommended):
  - Sub-periods to compute conditional correlations (e.g., risk-on vs. risk-off, pre/post a date,
    high-vol vs. low-vol windows) — user supplies the date splits or vol threshold

CONTEXT:
  - Stated diversification assumptions to test (e.g., "bonds hedge equities")
  - Risk limit / concentration policy (if any)
QUESTION (optional): __________
</correlation_inputs>
```

If return data (or a supplied matrix) is not provided, request it. Do not fabricate returns or correlations.

## Constraints

### Must
- Use only user-supplied returns or a user-supplied matrix; state method (Pearson/Spearman), frequency, window, and source.
- Show correlation/covariance computation as formula → inputs → result (NE-11).
- Compute and compare full-sample vs. regime-conditional vs. tail (crisis-window) correlations (RT-06).
- Assess diversification quantitatively (e.g., effective number of bets / diversification ratio), not just by counting assets.
- Stress-test under correlation breakdown (NE-10/QA-02): re-run portfolio risk assuming correlations rise toward 1.
- Flag the difference between correlation and causation and the instability of estimates (QA-04).
- Note estimation caveats: short windows, non-stationarity, frequency effects, and that low average correlation can mask high tail correlation.

### Must Not
- Assert returns or correlations from memory.
- Present a single full-sample correlation as the stable, forward-looking relationship.
- Treat low average correlation as evidence of crisis-time diversification (tail correlations differ).
- Equate correlation with a causal/hedging relationship.
- Count assets as independent bets without measuring effective diversification.

## Instructions

**Step 1 — Restate data and method.** State assets, frequency, window, source, and correlation method.

**Step 2 — Build the correlation/covariance matrix (NE-11).**

```
Pairwise correlation:
  ρ(x,y) = Cov(x,y) / (σx · σy)
  Cov(x,y) = (1/(n−1)) Σ (x_i − x̄)(y_i − ȳ)
Covariance matrix entry: Σ_ij = ρ_ij · σ_i · σ_j
State n (sample size) and window; flag if n is small relative to asset count.
```

**Step 3 — Regime-conditional correlations (RT-06).** Recompute the matrix within each user-supplied regime/sub-period (or high-vol vs. low-vol windows). Tabulate how key pairs change across regimes (especially equity/bond, equity/credit, equity/gold, equity/USD).

**Step 4 — Tail correlation.** Compute correlation conditional on large adverse moves (e.g., worst-decile days of a reference asset). Compare to full-sample to expose diversification that disappears in stress.

**Step 5 — Diversification assessment.**

```
Portfolio variance:        σ_p^2 = w' Σ w
Diversification ratio:     DR = (Σ w_i σ_i) / σ_p     (higher = more diversification benefit)
Effective number of bets:  ENB ≈ 1 / Σ (p_k^2)   over variance contributions / principal components
Marginal & component risk contributions: identify the asset(s) driving most of σ_p.
```

**Step 6 — Correlation-breakdown stress (NE-10/QA-02).** Re-run σ_p assuming pairwise correlations shift toward a stress level (e.g., 0.8–1.0 across risk assets). Report the increase in portfolio volatility/VaR and which "diversifiers" fail.

**Step 7 — Bias & caveat pass (QA-04).** State estimation instability, correlation≠causation, and the regime-blindness/tail-blindness guardrails; give one monitoring trigger (e.g., rising realized correlation).

## Output Format

### Data & Method
[Step 1 — assets, frequency, window, source, method, sample size]

### Full-Sample Correlation Matrix

| | A | B | C | D |
|---|---|---|---|---|
| A | 1.00 | | | |
| B | | 1.00 | | |
| C | | | 1.00 | |
| D | | | | 1.00 |

### Regime-Conditional Correlations (key pairs)

| Pair | Full-sample | Risk-on / low-vol | Risk-off / high-vol | Change |
|---|---|---|---|---|

### Tail Correlation (conditional on adverse moves)

| Pair | Full-sample ρ | Tail ρ (worst-decile) | Diversification holds? |
|---|---|---|---|

### Diversification Assessment

| Metric | Formula | Inputs | Result |
|---|---|---|---|
| Portfolio vol σ_p | w'Σw | | |
| Diversification ratio | | | |
| Effective number of bets | | | |
| Top risk contributor | | | |

### Correlation-Breakdown Stress

| Assumption | σ_p / VaR | Δ vs. base | Failing diversifiers |
|---|---|---|---|
| Base correlations | | — | |
| Stress (ρ → 0.8–1.0 risk assets) | | | |

### Caveats & Monitoring
[Step 7 — instability, causation, regime/tail-blindness guardrails, monitoring trigger]

## Verification

- [ ] All returns or the supplied matrix are user-provided with method, frequency, window, source.
- [ ] Correlation/covariance shown as formula → inputs → result; sample size stated.
- [ ] Regime-conditional correlations computed and compared to full-sample.
- [ ] Tail correlation computed and compared to full-sample for key pairs.
- [ ] Diversification measured quantitatively (DR / ENB / risk contributions), not by asset count.
- [ ] Correlation-breakdown stress re-runs portfolio risk and names failing diversifiers.
- [ ] Estimation instability and correlation≠causation flagged; monitoring trigger given.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Asserting returns/correlations from memory | All data is user-supplied with method/window/source; stop if missing |
| Treating full-sample correlation as stable/forward-looking | Compute regime-conditional and tail correlations; state instability |
| Low average correlation = crisis diversification | Tail-correlation analysis required; show where diversification disappears |
| Counting assets as independent bets | Measure effective number of bets / diversification ratio |
| Correlation read as causation/hedge | Explicit correlation≠causation flag; "hedge" claims require mechanism |
| Small-sample matrix over-trusted | Flag n vs. asset count; note estimation error and frequency effects |
