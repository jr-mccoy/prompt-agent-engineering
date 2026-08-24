---
name: backtesting-frameworks
description: Build robust backtesting systems for trading strategies with proper handling of look-ahead bias, survivorship bias, and transaction costs. Use when developing trading algorithms, validating strategies, or building backtesting infrastructure.
metadata:
  tags:
    - backtesting
    - frameworks
  updated: "2026-04-11"
---
# Backtesting Frameworks

Build robust, production-grade backtesting systems that avoid common pitfalls and produce reliable strategy performance estimates.

## When to Use This Skill

- Developing trading strategy backtests
- Building backtesting infrastructure
- Validating strategy performance
- Avoiding common backtesting biases
- Implementing walk-forward analysis
- Comparing strategy alternatives

## Core Concepts

### 1. Backtesting Biases

| Bias | Description | Mitigation |
|------|-------------|------------|
| **Look-ahead** | Using future information | Point-in-time data |
| **Survivorship** | Only testing on survivors | Use delisted securities |
| **Overfitting** | Curve-fitting to history | Out-of-sample testing |
| **Selection** | Cherry-picking strategies | Pre-registration |
| **Transaction** | Ignoring trading costs | Realistic cost models |

### 2. Proper Backtest Structure

```
Historical Data
      │
      ▼
┌─────────────────────────────────────────┐
│              Training Set               │
│  (Strategy Development & Optimization)  │
└─────────────────────────────────────────┘
      │
      ▼
┌─────────────────────────────────────────┐
│             Validation Set              │
│  (Parameter Selection, No Peeking)      │
└─────────────────────────────────────────┘
      │
      ▼
┌─────────────────────────────────────────┐
│               Test Set                  │
│  (Final Performance Evaluation)         │
└─────────────────────────────────────────┘
```

### 3. Walk-Forward Analysis

```
Window 1: [Train──────][Test]
Window 2:     [Train──────][Test]
Window 3:         [Train──────][Test]
Window 4:             [Train──────][Test]
                                     ─────▶ Time
```

## Implementation Patterns

### Pattern 1: Event-Driven Backtester

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Dict, List, Optional
import pandas as pd
import numpy as np

class OrderSide(Enum):
    BUY = "buy"
    SELL = "sell"

class OrderType(Enum):
    MARKET = "market"
    LIMIT = "limit"
    STOP = "stop"

@dataclass
class Order:
    symbol: str
    side: OrderSide
    quantity: Decimal
    order_type: OrderType
    limit_price: Optional[Decimal] = None
    stop_price: Optional[Decimal] = None
    timestamp: Optional[datetime] = None

@dataclass
class Fill:
    order: Order
    fill_price: Decimal
    fill_quantity: Decimal
    commission: Decimal
    slippage: Decimal
    timestamp: datetime

@dataclass
class Position:
    symbol: str
    quantity: Decimal = Decimal("0")
    avg_cost: Decimal = Decimal("0")
    realized_pnl: Decimal = Decimal("0")

    def update(self, fill: Fill) -> None:
        if fill.order.side == OrderSide.BUY:
            new_quantity = self.quantity + fill.fill_quantity
            if new_quantity != 0:
                self.avg_cost = (
                    (self.quantity * self.avg_cost + fill.fill_quantity * fill.fill_price)
                    / new_quantity
                )
            self.quantity = new_quantity
        else:
            self.realized_pnl += fill.fill_quantity * (fill.fill_price - self.avg_cost)
            self.quantity -= fill.fill_quantity

@dataclass
class Portfolio:
    cash: Decimal
    positions: Dict[str, Position] = field(default_factory=dict)

    def get_position(self, symbol: str) -> Position:
        if symbol not in self.positions:
            self.positions[symbol] = Position(symbol=symbol)
        return self.positions[symbol]

    def process_fill(self, fill: Fill) -> None:
        position = self.get_position(fill.order.symbol)
        position.update(fill)

        if fill.order.side == OrderSide.BUY:
            self.cash -= fill.fill_price * fill.fill_quantity + fill.commission
        else:
            self.cash += fill.fill_price * fill.fill_quantity - fill.commission

    def get_equity(self, prices: Dict[str, Decimal]) -> Decimal:
        equity = self.cash
        for symbol, position in self.positions.items():
            if position.quantity != 0 and symbol in prices:
                equity += position.quantity * prices[symbol]
        return equity

class Strategy(ABC):
    @abstractmethod
    def on_bar(self, timestamp: datetime, data: pd.DataFrame) -> List[Order]:
        pass

    @abstractmethod
    def on_fill(self, fill: Fill) -> None:
        pass

class ExecutionModel(ABC):
    @abstractmethod
    def execute(self, order: Order, bar: pd.Series) -> Optional[Fill]:
        pass

class SimpleExecutionModel(ExecutionModel):
    def __init__(self, slippage_bps: float = 10, commission_per_share: float = 0.01):
        self.slippage_bps = slippage_bps
        self.commission_per_share = commission_per_share

    def execute(self, order: Order, bar: pd.Series) -> Optional[Fill]:
        if order.order_type == OrderType.MARKET:
            base_price = Decimal(str(bar["open"]))

            # Apply slippage
            slippage_mult = 1 + (self.slippage_bps / 10000)
            if order.side == OrderSide.BUY:
                fill_price = base_price * Decimal(str(slippage_mult))
            else:
                fill_price = base_price / Decimal(str(slippage_mult))

            commission = order.quantity * Decimal(str(self.commission_per_share))
            slippage = abs(fill_price - base_price) * order.quantity

            return Fill(
                order=order,
                fill_price=fill_price,
                fill_quantity=order.quantity,
                commission=commission,
                slippage=slippage,
                timestamp=bar.name
            )
        return None

class Backtester:
    def __init__(
        self,
        strategy: Strategy,
        execution_model: ExecutionModel,
        initial_capital: Decimal = Decimal("100000")
    ):
        self.strategy = strategy
        self.execution_model = execution_model
        self.portfolio = Portfolio(cash=initial_capital)
        self.equity_curve: List[tuple] = []
        self.trades: List[Fill] = []

    def run(self, data: pd.DataFrame) -> pd.DataFrame:
        """Run backtest on OHLCV data with DatetimeIndex."""
        pending_orders: List[Order] = []

        for timestamp, bar in data.iterrows():
            # Execute pending orders at today's prices
            for order in pending_orders:
                fill = self.execution_model.execute(order, bar)
                if fill:
                    self.portfolio.process_fill(fill)
                    self.strategy.on_fill(fill)
                    self.trades.append(fill)

            pending_orders.clear()

            # Get current prices for equity calculation
            prices = {data.index.name or "default": Decimal(str(bar["close"]))}
            equity = self.portfolio.get_equity(prices)
            self.equity_curve.append((timestamp, float(equity)))

            # Generate new orders for next bar
            new_orders = self.strategy.on_bar(timestamp, data.loc[:timestamp])
            pending_orders.extend(new_orders)

        return self._create_results()

    def _create_results(self) -> pd.DataFrame:
        equity_df = pd.DataFrame(self.equity_curve, columns=["timestamp", "equity"])
        equity_df.set_index("timestamp", inplace=True)
        equity_df["returns"] = equity_df["equity"].pct_change()
        return equity_df
```

### Pattern 2: Vectorized Backtester (Fast)

```python
import pandas as pd
import numpy as np
from typing import Callable, Dict, Any

class VectorizedBacktester:
    """Fast vectorized backtester for simple strategies."""

    def __init__(
        self,
        initial_capital: float = 100000,
        commission: float = 0.001,  # 0.1%
        slippage: float = 0.0005   # 0.05%
    ):
        self.initial_capital = initial_capital
        self.commission = commission
        self.slippage = slippage

    def run(
        self,
        prices: pd.DataFrame,
        signal_func: Callable[[pd.DataFrame], pd.Series]
    ) -> Dict[str, Any]:
        """
        Run backtest with signal function.

        Args:
            prices: DataFrame with 'close' column
            signal_func: Function that returns position signals (-1, 0, 1)

        Returns:
            Dictionary with results
        """
        # Generate signals (shifted to avoid look-ahead)
        signals = signal_func(prices).shift(1).fillna(0)

        # Calculate returns
        returns = prices["close"].pct_change()

        # Calculate strategy returns with costs
        position_changes = signals.diff().abs()
        trading_costs = position_changes * (self.commission + self.slippage)

        strategy_returns = signals * returns - trading_costs

        # Build equity curve
        equity = (1 + strategy_returns).cumprod() * self.initial_capital

        # Calculate metrics
        results = {
            "equity": equity,
            "returns": strategy_returns,
            "signals": signals,
            "metrics": self._calculate_metrics(strategy_returns, equity)
        }

        return results

    def _calculate_metrics(
        self,
        returns: pd.Series,
        equity: pd.Series
    ) -> Dict[str, float]:
        """Calculate performance metrics."""
        total_return = (equity.iloc[-1] / self.initial_capital) - 1
        annual_return = (1 + total_return) ** (252 / len(returns)) - 1
        annual_vol = returns.std() * np.sqrt(252)
        sharpe = annual_return / annual_vol if annual_vol > 0 else 0

        # Drawdown
        rolling_max = equity.cummax()
        drawdown = (equity - rolling_max) / rolling_max
        max_drawdown = drawdown.min()

        # Win rate
        winning_days = (returns > 0).sum()
        total_days = (returns != 0).sum()
        win_rate = winning_days / total_days if total_days > 0 else 0

        return {
            "total_return": total_return,
            "annual_return": annual_return,
            "annual_volatility": annual_vol,
            "sharpe_ratio": sharpe,
            "max_drawdown": max_drawdown,
            "win_rate": win_rate,
            "num_trades": int((returns != 0).sum())
        }

# Example usage
def momentum_signal(prices: pd.DataFrame, lookback: int = 20) -> pd.Series:
    """Simple momentum strategy: long when price > SMA, else flat."""
    sma = prices["close"].rolling(lookback).mean()
    return (prices["close"] > sma).astype(int)

# Run backtest
# backtester = VectorizedBacktester()
# results = backtester.run(price_data, lambda p: momentum_signal(p, 50))
```

## Walk-Forward Optimization, Monte Carlo Analysis & Performance Metrics

Walk-forward optimizer (WalkForwardOptimizer with anchored/rolling window generate_splits; grid-search optimization over param_grid selecting best metric per training window; combine_equity_curves stitching test-period results), Monte Carlo analyzer (MonteCarloAnalyzer with bootstrap_returns resampling; analyze_drawdowns returning expected/median/worst-pct/worst-case; probability_of_loss over configurable holding periods; confidence_interval for future return distribution), and comprehensive performance metrics function (calculate_metrics returning total/annual return, Sharpe, Sortino, Calmar, max drawdown, win rate, profit factor).

See [references/walk-forward-monte-carlo-and-metrics.md](references/walk-forward-monte-carlo-and-metrics.md)

## Best Practices

### Do's
- **Use point-in-time data** - Avoid look-ahead bias
- **Include transaction costs** - Realistic estimates
- **Test out-of-sample** - Always reserve data
- **Use walk-forward** - Not just train/test
- **Monte Carlo analysis** - Understand uncertainty

### Don'ts
- **Don't overfit** - Limit parameters
- **Don't ignore survivorship** - Include delisted
- **Don't use adjusted data carelessly** - Understand adjustments
- **Don't optimize on full history** - Reserve test set
- **Don't ignore capacity** - Market impact matters

## Resources

- [Advances in Financial Machine Learning (Marcos López de Prado)](https://www.amazon.com/Advances-Financial-Machine-Learning-Marcos/dp/1119482089)
- [Quantitative Trading (Ernest Chan)](https://www.amazon.com/Quantitative-Trading-Build-Algorithmic-Business/dp/1119800064)
- [Backtrader Documentation](https://www.backtrader.com/docu/)

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/walk-forward-monte-carlo-and-metrics.md` | Walk-forward optimizer, Monte Carlo analyzer, performance metrics |
