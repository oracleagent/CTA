import numpy as np

class PerformanceMetrics:
    """
    Handles the calculation of various performance metrics for a trading portfolio.
    """

    @staticmethod
    def calculate_profit_loss(trades):
        """
        Calculates total profit or loss from a list of trades.
        Args:
        trades (list of dicts): Each trade containing 'entry_price' and 'exit_price'.
        Returns:
        float: Net profit or loss.
        """
        profit_loss = sum(trade['exit_price'] - trade['entry_price'] for trade in trades if 'exit_price' in trade)
        return profit_loss

    @staticmethod
    def calculate_sharpe_ratio(returns, risk_free_rate=0.01):
        """
        Calculates the Sharpe Ratio for the given returns.
        Args:
        returns (list of floats): List of periodic returns.
        risk_free_rate (float): Annual risk-free rate, default is 1%.
        Returns:
        float: The Sharpe Ratio, adjusted for the risk-free rate.
        """
        excess_returns = np.array(returns) - risk_free_rate / len(returns)
        if np.std(excess_returns) == 0:
            return float('nan')
        return np.mean(excess_returns) / np.std(excess_returns)

    @staticmethod
    def calculate_max_drawdown(cumulative_returns):
        """
        Calculates the maximum drawdown in the list of cumulative returns.
        Args:
        cumulative_returns (list of floats): The cumulative returns over a period.
        Returns:
        float: The maximum drawdown expressed as a percentage.
        """
        peak = cumulative_returns[0]
        max_drawdown = 0
        for return_ in cumulative_returns:
            if return_ > peak:
                peak = return_
            drawdown = (peak - return_) / peak
            if drawdown > max_drawdown:
                max_drawdown = drawdown
        return max_drawdown

# Example usage:
if __name__ == "__main__":
    trades = [{'entry_price': 100, 'exit_price': 110}, {'entry_price': 120, 'exit_price': 115}]
    returns = [0.1, 0.05, -0.02, 0.03]
    cumulative_returns = [100, 105, 103, 106]

    metrics = PerformanceMetrics()
    print("Profit/Loss:", metrics.calculate_profit_loss(trades))
    print("Sharpe Ratio:", metrics.calculate_sharpe_ratio(returns))
    print("Max Drawdown:", metrics.calculate_max_drawdown(cumulative_returns))
