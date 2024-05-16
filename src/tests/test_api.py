import unittest
from unittest.mock import patch, Mock
from src.api.binance.client import BinanceClient
from src.api.coinbase.client import CoinbaseClient

class TestBinanceClient(unittest.TestCase):

    @patch('src.api.binance.client.requests.get')
    def test_fetch_market_data(self, mock_get):
        # Mock API response
        mock_response = Mock()
        expected_data = {
            'symbol': 'BTCUSDT',
            'price': '50000.00'
        }
        mock_response.json.return_value = expected_data
        mock_get.return_value = mock_response

        binance_client = BinanceClient(api_key='test', secret_key='test')
        data = binance_client.fetch_market_data('BTCUSDT')
        self.assertEqual(data, expected_data)

    @patch('src.api.binance.client.requests.post')
    def test_place_order(self, mock_post):
        # Mock API response
        mock_response = Mock()
        expected_data = {
            'orderId': 1,
            'symbol': 'BTCUSDT',
            'price': '50000.00',
            'origQty': '0.1',
            'status': 'FILLED'
        }
        mock_response.json.return_value = expected_data
        mock_post.return_value = mock_response

        binance_client = BinanceClient(api_key='test', secret_key='test')
        order = binance_client.place_order('BTCUSDT', 'BUY', 'LIMIT', 0.1, 50000.0)
        self.assertEqual(order, expected_data)

class TestCoinbaseClient(unittest.TestCase):

    @patch('src.api.coinbase.client.requests.get')
    def test_fetch_market_data(self, mock_get):
        # Mock API response
        mock_response = Mock()
        expected_data = [{
            'time': '2021-01-01T00:00:00Z',
            'low': '29000.00',
            'high': '29500.00',
            'open': '29250.00',
            'close': '29350.00',
            'volume': '100.0'
        }]
        mock_response.json.return_value = expected_data
        mock_get.return_value = mock_response

        coinbase_client = CoinbaseClient(api_key='test', secret_key='test')
        data = coinbase_client.fetch_market_data('BTC-USD')
        self.assertEqual(data, expected_data)

    @patch('src.api.coinbase.client.requests.post')
    def test_place_order(self, mock_post):
        # Mock API response
        mock_response = Mock()
        expected_data = {
            'id': 'order_123',
            'product_id': 'BTC-USD',
            'side': 'buy',
            'price': '29250.00',
            'size': '0.1',
            'status': 'done'
        }
        mock_response.json.return_value = expected_data
        mock_post.return_value = mock_response

        coinbase_client = CoinbaseClient(api_key='test', secret_key='test')
        order = coinbase_client.place_order('BTC-USD', 'buy', 0.1, 29250.0)
        self.assertEqual(order, expected_data)

if __name__ == '__main__':
    unittest.main()
