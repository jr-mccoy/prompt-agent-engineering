# Backtesting Frameworks — Walk-Forward Optimization, Monte Carlo Analysis & Performance Metrics

## Pattern 3: Walk-Forward Optimization

```python
from typing import Callable, Dict, List, Tuple, Any
import pandas as pd
import numpy as np
from itertools import product

class WalkForwardOptimizer:
    """Walk-forward analysis with anchored or rolling windows."""

    def __init__(
        self,
        train_period: int,
        test_period: int,
        anchored: bool = False,
        n_splits: int = None
    ):
        """
        Args:
            train_period: Number of bars in training window
            test_period: Number of bars in test window
            anchored: If True, training always starts from beginning
            n_splits: Number of train/test splits (auto-calculated if None)
        """
        self.train_period = train_period
        self.test_period = test_period
        self.anchored = anchored
        self.n_splits = n_splits

    def generate_splits(
        self,
        data: pd.DataFrame
    ) -> List[Tuple[pd.DataFrame, pd.DataFrame]]:
        """Generate train/test splits."""
        splits = []
        n = len(data)

        if self.n_splits:
            step = (n - self.train_period) // self.n_splits
        else:
            step = self.test_period

        start = 0
        while start + self.train_period + self.test_period <= n:
            if self.anchored:
                train_start = 0
            else:
                train_start = start

            train_end = start + self.train_period
            test_end = min(train_end + self.test_period, n)

            train_data = data.iloc[train_start:train_end]
            test_data = data.iloc[train_end:test_end]

            splits.append((train_data, test_data))
            start += step

        return splits

    def optimize(
        self,
        data: pd.DataFrame,
        strategy_func: Callable,
        param_grid: Dict[str, List],
        metric: str = "sharpe_ratio"
    ) -> Dict[str, Any]:
        """
        Run walk-forward optimization.

        Args:
            data: Full dataset
            strategy_func: Function(data, **params) -> results dict
            param_grid: Parameter combinations to test
            metric: Metric to optimize

        Returns:
            Combined results from all test periods
        """
        splits = self.generate_splits(data)
        all_results = []
        optimal_params_history = []

        for i, (train_data, test_data) in enumerate(splits):
            # Optimize on training data
            best_params, best_metric = self._grid_search(
                train_data, strategy_func, param_grid, metric
            )
            optimal_params_history.append(best_params)

            # Test with optimal params
            test_results = strategy_func(test_data, **best_params)
            test_results["split"] = i
            test_results["params"] = best_params
            all_results.append(test_results)

            print(f"Split {i+1}/{len(splits)}: "
                  f"Best {metric}={best_metric:.4f}, params={best_params}")

        return {
            "split_results": all_results,
            "param_history": optimal_params_history,
            "combined_equity": self._combine_equity_curves(all_results)
        }

    def _grid_search(
        self,
        data: pd.DataFrame,
        strategy_func: Callable,
        param_grid: Dict[str, List],
        metric: str
    ) -> Tuple[Dict, float]:
        """Grid search for best parameters."""
        best_params = None
        best_metric = -np.inf

        # Generate all parameter combinations
        param_names = list(param_grid.keys())
        param_values = list(param_grid.values())

        for values in product(*param_values):
            params = dict(zip(param_names, values))
            results = strategy_func(data, **params)

            if results["metrics"][metric] > best_metric:
                best_metric = results["metrics"][metric]
                best_params = params

        return best_params, best_metric

    def _combine_equity_curves(
        self,
        results: List[Dict]
    ) -> pd.Series:
        """Combine equity curves from all test periods."""
        combined = pd.concat([r["equity"] for r in results])
        return combined
```

---

## Pattern 4: Monte Carlo Analysis

```python
import numpy as np
import pandas as pd
from typing import Dict, List

class MonteCarloAnalyzer:
    """Monte Carlo simulation for strategy robustness."""

    def __init__(self, n_simulations: int = 1000, confidence: float = 0.95):
        self.n_simulations = n_simulations
        self.confidence = confidence

    def bootstrap_returns(
        self,
        returns: pd.Series,
        n_periods: int = None
    ) -> np.ndarray:
        """
        Bootstrap simulation by resampling returns.

        Args:
            returns: Historical returns series
            n_periods: Length of each simulation (default: same as input)

        Returns:
            Array of shape (n_simulations, n_periods)
        """
        if n_periods is None:
            n_periods = len(returns)

        simulations = np.zeros((self.n_simulations, n_periods))

        for i in range(self.n_simulations):
            # Resample with replacement
            simulated_returns = np.random.choice(
                returns.values,
                size=n_periods,
                replace=True
            )
            simulations[i] = simulated_returns

        return simulations

    def analyze_drawdowns(
        self,
        returns: pd.Series
    ) -> Dict[str, float]:
        """Analyze drawdown distribution via simulation."""
        simulations = self.bootstrap_returns(returns)

        max_drawdowns = []
        for sim_returns in simulations:
            equity = (1 + sim_returns).cumprod()
            rolling_max = np.maximum.accumulate(equity)
            drawdowns = (equity - rolling_max) / rolling_max
            max_drawdowns.append(drawdowns.min())

        max_drawdowns = np.array(max_drawdowns)

        return {
            "expected_max_dd": np.mean(max_drawdowns),
            "median_max_dd": np.median(max_drawdowns),
            f"worst_{int(self.confidence*100)}pct": np.percentile(
                max_drawdowns, (1 - self.confidence) * 100
            ),
            "worst_case": max_drawdowns.min()
        }

    def probability_of_loss(
        self,
        returns: pd.Series,
        holding_periods: List[int] = [21, 63, 126, 252]
    ) -> Dict[int, float]:
        """Calculate probability of loss over various holding periods."""
        results = {}

        for period in holding_periods:
            if period > len(returns):
                continue

            simulations = self.bootstrap_returns(returns, period)
            total_returns = (1 + simulations).prod(axis=1) - 1
            prob_loss = (total_returns < 0).mean()
            results[period] = prob_loss

        return results

    def confidence_interval(
        self,
        returns: pd.Series,
        periods: int = 252
    ) -> Dict[str, float]:
        """Calculate confidence interval for future returns."""
        simulations = self.bootstrap_returns(returns, periods)
        total_returns = (1 + simulations).prod(axis=1) - 1

        lower = (1 - self.confidence) / 2
        upper = 1 - lower

        return {
            "expected": total_returns.mean(),
            "lower_bound": np.percentile(total_returns, lower * 100),
            "upper_bound": np.percentile(total_returns, upper * 100),
            "std": total_returns.std()
        }
```

---

## Performance Metrics

```python
def calculate_metrics(returns: pd.Series, rf_rate: float = 0.02) -> Dict[str, float]:
    """Calculate comprehensive performance metrics."""
    # Annualization factor (assuming daily returns)
    ann_factor = 252

    # Basic metrics
    total_return = (1 + returns).prod() - 1
    annual_return = (1 + total_return) ** (ann_factor / len(returns)) - 1
    annual_vol = returns.std() * np.sqrt(ann_factor)

    # Risk-adjusted returns
    sharpe = (annual_return - rf_rate) / annual_vol if annual_vol > 0 else 0

    # Sortino (downside deviation)
    downside_returns = returns[returns < 0]
    downside_vol = downside_returns.std() * np.sqrt(ann_factor)
    sortino = (annual_return - rf_rate) / downside_vol if downside_vol > 0 else 0

    # Calmar ratio
    equity = (1 + returns).cumprod()
    rolling_max = equity.cummax()
    drawdowns = (equity - rolling_max) / rolling_max
    max_drawdown = drawdowns.min()
    calmar = annual_return / abs(max_drawdown) if max_drawdown != 0 else 0

    # Win rate and profit factor
    wins = returns[returns > 0]
    losses = returns[returns < 0]
    win_rate = len(wins) / len(returns[returns != 0]) if len(returns[returns != 0]) > 0 else 0
    profit_factor = wins.sum() / abs(losses.sum()) if losses.sum() != 0 else np.inf

    return {
        "total_return": total_return,
        "annual_return": annual_return,
        "annual_volatility": annual_vol,
        "sharpe_ratio": sharpe,
        "sortino_ratio": sortino,
        "calmar_ratio": calmar,
        "max_drawdown": max_drawdown,
        "win_rate": win_rate,
        "profit_factor": profit_factor,
        "num_trades": int((returns != 0).sum())
    }
```
