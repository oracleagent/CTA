import time
from .strategy import AdvancedStrategy
from ..api.binance.client import BinanceClient

class Trader:
    def __init__(self, client, strategy):
        self.client = client
        self.strategy = strategy

    def fetch_market_data(self):
        """
        Fetches the latest market data from the exchange.
        Adjust this method based on the specifics of what data your strategy requires.
        """
        return self.client.get_recent_trades()  # Simplified example; customize as needed.

    def execute_trade(self, decision, market_data):
        """
        Executes trades based on the decision from the strategy.
        """
        if decision == 'buy':
            # Implement buy logic
            print("Buying at market price")
            self.client.place_order('buy', market_data['price'], market_data['quantity'])
        elif decision == 'sell':
            # Implement sell logic
            print("Selling at market price")
            self.client.place_order('sell', market_data['price'], market_data['quantity'])

    def run(self):
        """
        Main trading loop that fetches data, makes decisions, and executes trades.
        """
        while True:
            market_data = self.fetch_market_data()
            buy_signal = self.strategy.should_buy(market_data)
            sell_signal = self.strategy.should_sell(market_data)

            if buy_signal:
                self.execute_trade('buy', market_data)
            elif sell_signal:
                self.execute_trade('sell', market_data)

            time.sleep(60)  # Sleep for a minute before the next cycle. Customize as per requirement.

# Example usage
if __name__ == "__main__":
    client = BinanceClient(api_key='your_api_key', secret_key='your_secret_key')
    strategy = AdvancedStrategy(client)
    trader = Trader(client, strategy)
    trader.run()
