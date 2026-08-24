---
name: risk-metrics-calculation
description: Calculate portfolio risk metrics including VaR, CVaR, Sharpe, Sortino, and drawdown analysis. Use when measuring portfolio risk, implementing risk limits, or building risk monitoring systems.
metadata:
  tags:
    - calculation
    - metrics
    - monitoring
    - risk
  updated: "2026-04-11"
---
# Risk Metrics Calculation

Comprehensive risk measurement toolkit for portfolio management, including Value at Risk, Expected Shortfall, and drawdown analysis.

## When to Use This Skill

- Measuring portfolio risk
- Implementing risk limits
- Building risk dashboards
- Calculating risk-adjusted returns
- Setting position sizes
- Regulatory reporting

## Core Concepts

### 1. Risk Metric Categories

| Category | Metrics | Use Case |
|----------|---------|----------|
| **Volatility** | Std Dev, Beta | General risk |
| **Tail Risk** | VaR, CVaR | Extreme losses |
| **Drawdown** | Max DD, Calmar | Capital preservation |
| **Risk-Adjusted** | Sharpe, Sortino | Performance |

### 2. Time Horizons

```
Intraday:   Minute/hourly VaR for day traders
Daily:      Standard risk reporting
Weekly:     Rebalancing decisions
Monthly:    Performance attribution
Annual:     Strategic allocation
```

## Implementation

### Pattern 1: Core Risk Metrics

```python
import numpy as np
import pandas as pd
from scipy import stats
from typing import Dict, Optional, Tuple

class RiskMetrics:
    """Core risk metric calculations."""

    def __init__(self, returns: pd.Series, rf_rate: float = 0.02):
        """
        Args:
            returns: Series of periodic returns
            rf_rate: Annual risk-free rate
        """
        self.returns = returns
        self.rf_rate = rf_rate
        self.ann_factor = 252  # Trading days per year

    # Volatility Metrics
    def volatility(self, annualized: bool = True) -> float:
        """Standard deviation of returns."""
        vol = self.returns.std()
        if annualized:
            vol *= np.sqrt(self.ann_factor)
        return vol

    def downside_deviation(self, threshold: float = 0, annualized: bool = True) -> float:
        """Standard deviation of returns below threshold."""
        downside = self.returns[self.returns < threshold]
        if len(downside) == 0:
            return 0.0
        dd = downside.std()
        if annualized:
            dd *= np.sqrt(self.ann_factor)
        return dd

    def beta(self, market_returns: pd.Series) -> float:
        """Beta relative to market."""
        aligned = pd.concat([self.returns, market_returns], axis=1).dropna()
        if len(aligned) < 2:
            return np.nan
        cov = np.cov(aligned.iloc[:, 0], aligned.iloc[:, 1])
        return cov[0, 1] / cov[1, 1] if cov[1, 1] != 0 else 0

    # Value at Risk
    def var_historical(self, confidence: float = 0.95) -> float:
        """Historical VaR at confidence level."""
        return -np.percentile(self.returns, (1 - confidence) * 100)

    def var_parametric(self, confidence: float = 0.95) -> float:
        """Parametric VaR assuming normal distribution."""
        z_score = stats.norm.ppf(confidence)
        return self.returns.mean() - z_score * self.returns.std()

    def var_cornish_fisher(self, confidence: float = 0.95) -> float:
        """VaR with Cornish-Fisher expansion for non-normality."""
        z = stats.norm.ppf(confidence)
        s = stats.skew(self.returns)  # Skewness
        k = stats.kurtosis(self.returns)  # Excess kurtosis

        # Cornish-Fisher expansion
        z_cf = (z + (z**2 - 1) * s / 6 +
                (z**3 - 3*z) * k / 24 -
                (2*z**3 - 5*z) * s**2 / 36)

        return -(self.returns.mean() + z_cf * self.returns.std())

    # Conditional VaR (Expected Shortfall)
    def cvar(self, confidence: float = 0.95) -> float:
        """Expected Shortfall / CVaR / Average VaR."""
        var = self.var_historical(confidence)
        return -self.returns[self.returns <= -var].mean()

    # Drawdown Analysis
    def drawdowns(self) -> pd.Series:
        """Calculate drawdown series."""
        cumulative = (1 + self.returns).cumprod()
        running_max = cumulative.cummax()
        return (cumulative - running_max) / running_max

    def max_drawdown(self) -> float:
        """Maximum drawdown."""
        return self.drawdowns().min()

    def avg_drawdown(self) -> float:
        """Average drawdown."""
        dd = self.drawdowns()
        return dd[dd < 0].mean() if (dd < 0).any() else 0

    def drawdown_duration(self) -> Dict[str, int]:
        """Drawdown duration statistics."""
        dd = self.drawdowns()
        in_drawdown = dd < 0

        # Find drawdown periods
        drawdown_starts = in_drawdown & ~in_drawdown.shift(1).fillna(False)
        drawdown_ends = ~in_drawdown & in_drawdown.shift(1).fillna(False)

        durations = []
        current_duration = 0

        for i in range(len(dd)):
            if in_drawdown.iloc[i]:
                current_duration += 1
            elif current_duration > 0:
                durations.append(current_duration)
                current_duration = 0

        if current_duration > 0:
            durations.append(current_duration)

        return {
            "max_duration": max(durations) if durations else 0,
            "avg_duration": np.mean(durations) if durations else 0,
            "current_duration": current_duration
        }

    # Risk-Adjusted Returns
    def sharpe_ratio(self) -> float:
        """Annualized Sharpe ratio."""
        excess_return = self.returns.mean() * self.ann_factor - self.rf_rate
        vol = self.volatility(annualized=True)
        return excess_return / vol if vol > 0 else 0

    def sortino_ratio(self) -> float:
        """Sortino ratio using downside deviation."""
        excess_return = self.returns.mean() * self.ann_factor - self.rf_rate
        dd = self.downside_deviation(threshold=0, annualized=True)
        return excess_return / dd if dd > 0 else 0

    def calmar_ratio(self) -> float:
        """Calmar ratio (return / max drawdown)."""
        annual_return = (1 + self.returns).prod() ** (self.ann_factor / len(self.returns)) - 1
        max_dd = abs(self.max_drawdown())
        return annual_return / max_dd if max_dd > 0 else 0

    def omega_ratio(self, threshold: float = 0) -> float:
        """Omega ratio."""
        returns_above = self.returns[self.returns > threshold] - threshold
        returns_below = threshold - self.returns[self.returns <= threshold]

        if returns_below.sum() == 0:
            return np.inf

        return returns_above.sum() / returns_below.sum()

    # Information Ratio
    def information_ratio(self, benchmark_returns: pd.Series) -> float:
        """Information ratio vs benchmark."""
        active_returns = self.returns - benchmark_returns
        tracking_error = active_returns.std() * np.sqrt(self.ann_factor)
        active_return = active_returns.mean() * self.ann_factor
        return active_return / tracking_error if tracking_error > 0 else 0

    # Summary
    def summary(self) -> Dict[str, float]:
        """Generate comprehensive risk summary."""
        dd_stats = self.drawdown_duration()

        return {
            # Returns
            "total_return": (1 + self.returns).prod() - 1,
            "annual_return": (1 + self.returns).prod() ** (self.ann_factor / len(self.returns)) - 1,

            # Volatility
            "annual_volatility": self.volatility(),
            "downside_deviation": self.downside_deviation(),

            # VaR & CVaR
            "var_95_historical": self.var_historical(0.95),
            "var_99_historical": self.var_historical(0.99),
            "cvar_95": self.cvar(0.95),

            # Drawdowns
            "max_drawdown": self.max_drawdown(),
            "avg_drawdown": self.avg_drawdown(),
            "max_drawdown_duration": dd_stats["max_duration"],

            # Risk-Adjusted
            "sharpe_ratio": self.sharpe_ratio(),
            "sortino_ratio": self.sortino_ratio(),
            "calmar_ratio": self.calmar_ratio(),
            "omega_ratio": self.omega_ratio(),

            # Distribution
            "skewness": stats.skew(self.returns),
            "kurtosis": stats.kurtosis(self.returns),
        }
```

## Advanced Patterns

Portfolio-level risk calculations (`PortfolioRisk` with weighted return/volatility, marginal and component risk, risk parity weights via SciPy optimize, correlation matrix, diversification ratio, tracking error, and conditional correlation during stress periods); rolling window analysis (`RollingRiskMetrics` with rolling volatility, Sharpe, VaR, max drawdown, beta, and volatility regime classification); and stress testing (`StressTester` with 5 historical crisis scenarios from 2000–2022, hypothetical shock testing, and Monte Carlo stress with elevated volatility) are all in the reference file.

See [references/portfolio-rolling-and-stress-testing.md](references/portfolio-rolling-and-stress-testing.md)

## Quick Reference

```python
# Daily usage
metrics = RiskMetrics(returns)
print(f"Sharpe: {metrics.sharpe_ratio():.2f}")
print(f"Max DD: {metrics.max_drawdown():.2%}")
print(f"VaR 95%: {metrics.var_historical(0.95):.2%}")

# Full summary
summary = metrics.summary()
for metric, value in summary.items():
    print(f"{metric}: {value:.4f}")
```

## Best Practices

### Do's
- **Use multiple metrics** - No single metric captures all risk
- **Consider tail risk** - VaR isn't enough, use CVaR
- **Rolling analysis** - Risk changes over time
- **Stress test** - Historical and hypothetical
- **Document assumptions** - Distribution, lookback, etc.

### Don'ts
- **Don't rely on VaR alone** - Underestimates tail risk
- **Don't assume normality** - Returns are fat-tailed
- **Don't ignore correlation** - Increases in stress
- **Don't use short lookbacks** - Miss regime changes
- **Don't forget transaction costs** - Affects realized risk

## Resources

- [Risk Management and Financial Institutions (John Hull)](https://www.amazon.com/Risk-Management-Financial-Institutions-5th/dp/1119448115)
- [Quantitative Risk Management (McNeil, Frey, Embrechts)](https://www.amazon.com/Quantitative-Risk-Management-Techniques-Princeton/dp/0691166277)
- [pyfolio Documentation](https://quantopian.github.io/pyfolio/)

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/portfolio-rolling-and-stress-testing.md` | Pattern 2 (PortfolioRisk: weights, marginal/component risk, risk parity, diversification ratio, conditional correlation), Pattern 3 (RollingRiskMetrics: volatility, Sharpe, VaR, max drawdown, beta, regime), Pattern 4 (StressTester: 5 historical scenarios, hypothetical shocks, Monte Carlo) |
