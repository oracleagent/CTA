import time
import logging
from api.binance.client import BinanceClient
from bot.strategy import AdvancedStrategy

class Trader:
    def __init__(self, client, strategy):
        self.client = client
        self.strategy = strategy
        self.logger = logging.getLogger(__name__)

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
            self.logger.info("Buying at market price")
            self.client.place_order('buy', market_data['price'], market_data['quantity'])
        elif decision == 'sell':
            # Implement sell logic
            self.logger.info("Selling at market price")
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
    logging.basicConfig(level=logging.INFO)
    client = BinanceClient(api_key=os.getenv("BINANCE_API_KEY"), secret_key=os.getenv("BINANCE_SECRET_KEY"))
    strategy = AdvancedStrategy(client)
    trader = Trader(client, strategy)
    trader.run()
