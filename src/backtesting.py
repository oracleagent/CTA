import pandas as pd
from datetime import datetime

class Backtester:
    """
    Simulates the trading strategy against historical data to evaluate its performance.
    """

    def __init__(self, strategy, data_path):
        """
        Initializes the Backtester with a trading strategy and a path to historical data.
        Args:
        strategy (object): An instance of the trading strategy to be tested.
        data_path (str): The file path to historical market data (CSV).
        """
        self.strategy = strategy
        self.data = pd.read_csv(data_path)

    def run_backtest(self):
        """
        Executes the backtesting of the strategy using the historical data.
        Returns:
        dict: A dictionary containing backtesting results such as net profit and Sharpe ratio.
        """
        print("Starting backtest...")
        initial_balance = 10000  # Starting balance in USD
        balance = initial_balance
        profit = 0
        trades = []

        for index, row in self.data.iterrows():
            signal = self.strategy.generate_signal(row)
            if signal == 'buy':
                # Simplified: buying one unit of asset
                balance -= row['Close']
                trades.append({'entry_price': row['Close'], 'exit_price': None})
            elif signal == 'sell' and trades:
                # Simplified: selling one unit of asset
                last_trade = trades[-1]
                if last_trade['exit_price'] is None:
                    last_trade['exit_price'] = row['Close']
                    profit += last_trade['exit_price'] - last_trade['entry_price']
                    balance += row['Close']

        final_balance = balance + profit
        net_profit = final_balance - initial_balance
        sharpe_ratio = self.calculate_sharpe_ratio([t['exit_price'] - t['entry_price'] for t in trades if t['exit_price']])

        print("Backtesting complete.")
        return {
            'initial_balance': initial_balance,
            'final_balance': final_balance,
            'net_profit': net_profit,
            'sharpe_ratio': sharpe_ratio
        }

    @staticmethod
    def calculate_sharpe_ratio(returns):
        """
        Calculates the Sharpe ratio for the returns during the backtest.
        Args:
        returns (list of float): The list of returns from each trade.
        """
        import numpy as np
        mean_return = np.mean(returns)
        std_deviation = np.std(returns)
        return mean_return / std_deviation if std_deviation else 0

# Example usage:
if __name__ == "__main__":
    from strategies.sample_strategy import SampleStrategy  # Ensure to import your specific strategy
    backtester = Backtester(SampleStrategy(), 'path/to/historical/data.csv')
    results = backtester.run_backtest()
    print(results)
