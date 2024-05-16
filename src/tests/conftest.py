import pytest
from api.binance.client import BinanceClient
from bot.trader import Trader
from bot.strategy import AdvancedStrategy
from db.database import Database

@pytest.fixture(scope='session')
def test_db():
    """Fixture to initialize database connection for testing."""
    return Database(uri="mongodb://test:test@localhost:27017/test_db")

@pytest.fixture(scope='session')
def test_client():
    """Fixture to initialize the API client for testing."""
    return BinanceClient(api_key='test_key', secret_key='test_secret')

@pytest.fixture(scope='session')
def test_strategy(test_client):
    """Fixture to initialize the trading strategy for testing."""
    return AdvancedStrategy(test_client)

@pytest.fixture(scope='session')
def test_trader(test_client, test_strategy):
    """Fixture to initialize the trader for testing."""
    return Trader(test_client, test_strategy)
