from .binance.client import BinanceClient
from .coinbase.client import CoinbaseClient
import logging

class APIManager:
    """
    Manages API interactions for different cryptocurrency exchanges.
    """

    def __init__(self, api_config):
        """
        Initializes API clients for supported exchanges.
        Args:
        api_config (dict): Contains API configurations for each supported exchange.
        """
        self.clients = {
            'binance': BinanceClient(api_key=api_config['binance']['api_key'],
                                     secret_key=api_config['binance']['secret_key']),
            'coinbase': CoinbaseClient(api_key=api_config['coinbase']['api_key'],
                                       secret_key=api_config['coinbase']['secret_key'])
        }

    def fetch_market_data(self, exchange, symbol):
        """
        Fetches market data for a specified symbol from a specified exchange.
        Args:
        exchange (str): The name of the exchange ('binance', 'coinbase', etc.).
        symbol (str): The symbol to fetch data for (e.g., 'BTC-USD').
        Returns:
        dict: Market data.
        """
        client = self.clients.get(exchange)
        if not client:
            logging.error(f"Exchange {exchange} is not supported.")
            return None
        return client.get_market_data(symbol)

    def execute_trade(self, exchange, trade_type, symbol, quantity):
        """
        Executes a trade on a specified exchange.
        Args:
        exchange (str): The name of the exchange.
        trade_type (str): 'buy' or 'sell'.
        symbol (str): The symbol to trade.
        quantity (float): The quantity to trade.
        """
        client = self.clients.get(exchange)
        if not client:
            logging.error(f"Exchange {exchange} is not supported.")
            return None
        return client.place_order(trade_type, symbol, quantity)

# Example usage:
if __name__ == "__main__":
    config = {
        'binance': {'api_key': 'your_binance_api_key', 'secret_key': 'your_binance_secret_key'},
        'coinbase': {'api_key': 'your_coinbase_api_key', 'secret_key': 'your_coinbase_secret_key'}
    }
    api_manager = APIManager(api_config=config)
    market_data = api_manager.fetch_market_data('binance', 'BTC-USD')
    print(market_data)
    api_manager.execute_trade('binance', 'buy', 'BTC-USD', 0.1)
