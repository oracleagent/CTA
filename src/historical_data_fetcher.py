import logging
import requests
import pandas as pd
from datetime import datetime, timedelta
from api.api_manager import APIManager

class HistoricalDataFetcher:
    """
    Fetches historical market data from cryptocurrency exchanges.
    """

    def __init__(self, api_manager: APIManager):
        """
        Initializes the HistoricalDataFetcher with an API manager instance.
        Args:
        api_manager (APIManager): The manager responsible for API calls to exchanges.
        """
        self.api_manager = api_manager

    def fetch_binance_historical_data(self, symbol, interval, start_str, end_str):
        """
        Fetches historical data from Binance exchange.
        Args:
        symbol (str): The trading pair symbol (e.g., 'BTCUSDT').
        interval (str): The interval between data points (e.g., '1d', '1h').
        start_str (str): The start date in 'YYYY-MM-DD' format.
        end_str (str): The end date in 'YYYY-MM-DD' format.
        Returns:
        DataFrame: Pandas DataFrame containing the historical data.
        """
        base_url = 'https://api.binance.com/api/v3/klines'
        params = {
            'symbol': symbol,
            'interval': interval,
            'startTime': int(datetime.strptime(start_str, '%Y-%m-%d').timestamp() * 1000),
            'endTime': int(datetime.strptime(end_str, '%Y-%m-%d').timestamp() * 1000)
        }

        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data, columns=[
                'open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time',
                'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 
                'taker_buy_quote_asset_volume', 'ignore'
            ])
            df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
            df['close_time'] = pd.to_datetime(df['close_time'], unit='ms')
            return df
        else:
            logging.error(f"Failed to fetch historical data from Binance: {response.text}")
            return pd.DataFrame()

    def fetch_coinbase_historical_data(self, symbol, granularity, start, end):
        """
        Fetches historical data from Coinbase exchange.
        Args:
        symbol (str): The trading pair symbol (e.g., 'BTC-USD').
        granularity (int): The granularity of the data in seconds (e.g., 86400 for 1 day).
        start (str): The start date in 'YYYY-MM-DD' format.
        end (str): The end date in 'YYYY-MM-DD' format.
        Returns:
        DataFrame: Pandas DataFrame containing the historical data.
        """
        base_url = f'https://api.pro.coinbase.com/products/{symbol}/candles'
        params = {
            'granularity': granularity,
            'start': start,
            'end': end
        }

        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data, columns=['time', 'low', 'high', 'open', 'close', 'volume'])
            df['time'] = pd.to_datetime(df['time'], unit='s')
            return df
        else:
            logging.error(f"Failed to fetch historical data from Coinbase: {response.text}")
            return pd.DataFrame()

# Example usage:
if __name__ == "__main__":
    api_manager = APIManager(api_config={"api_key": "your_key", "api_secret": "your_secret"})
    data_fetcher = HistoricalDataFetcher(api_manager)
    binance_data = data_fetcher.fetch_binance_historical_data('BTCUSDT', '1d', '2021-01-01', '2021-12-31')
    coinbase_data = data_fetcher.fetch_coinbase_historical_data('BTC-USD', 86400, '2021-01-01T00:00:00', '2021-12-31T00:00:00')
    print(binance_data.head())
    print(coinbase_data.head())
