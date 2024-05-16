import numpy as np
from scipy.optimize import minimize
from backtesting import Backtester

class StrategyOptimizer:
    """
    Optimizes trading strategies by adjusting parameters to maximize performance.
    """

    def __init__(self, strategy, historical_data):
        """
        Initializes the optimizer with a trading strategy and historical data.
        Args:
        strategy (object): An instance of the trading strategy to be optimized.
        historical_data (DataFrame): Pandas DataFrame containing historical market data.
        """
        self.strategy = strategy
        self.historical_data = historical_data
        self.backtester = Backtester(strategy, historical_data)

    def objective_function(self, params):
        """
        Objective function to be minimized. In this case, we are maximizing the negative Sharpe ratio.
        Args:
        params (list): List of parameters for the strategy.
        Returns:
        float: Negative Sharpe ratio.
        """
        self.strategy.set_parameters(params)
        backtest_results = self.backtester.run_backtest()
        return -backtest_results['sharpe_ratio']  # Negative for minimization

    def optimize(self, param_bounds):
        """
        Runs the optimization process.
        Args:
        param_bounds (dict): Dictionary of parameter bounds. Example: {'param1': (0, 1), 'param2': (0, 100)}
        Returns:
        OptimizeResult: The result of the optimization process.
        """
        initial_guess = [np.mean(bounds) for bounds in param_bounds.values()]
        result = minimize(self.objective_function, initial_guess, bounds=list(param_bounds.values()), method='L-BFGS-B')
        return result

# Example usage:
if __name__ == "__main__":
    from strategies.sample_strategy import SampleStrategy
    import pandas as pd

    data = pd.read_csv('path/to/historical/data.csv')
    strategy = SampleStrategy()
    optimizer = StrategyOptimizer(strategy, data)
    optimal_params = optimizer.optimize({'param1': (0, 1), 'param2': (10, 100)})
    print("Optimal Parameters:", optimal_params.x)
