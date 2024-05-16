import pytest

def test_trade_execution(test_trader, test_db, mocker):
    """Test that a trade execution results in logging the trade."""
    mocker.patch('trader.Trader.fetch_market_data', return_value={'price': 100, 'quantity': 1})
    mocker.patch('db.Database.insert_trade', return_value=True)
    test_trader.execute_trade('buy', {'price': 100, 'quantity': 1})
    test_db.insert_trade.assert_called_once_with({'type': 'buy', 'price': 100, 'quantity': 1})
