import unittest
from unittest.mock import patch, Mock
from bot.trader import Trader
from bot.strategy import Strategy
from bot.scheduler import Scheduler
from db.models import Trade, Order, session

class TestTrader(unittest.TestCase):

    @patch('bot.trader.Trader.execute_trade')
    def test_run(self, mock_execute_trade):
        # Mock execute_trade method
        mock_execute_trade.return_value = True

        # Create a mock client and strategy
        mock_client = Mock()
        mock_strategy = Mock()
        mock_strategy.generate_signal.return_value = 'buy'

        trader = Trader(mock_client, mock_strategy)
        trader.run()

        # Verify execute_trade was called
        mock_execute_trade.assert_called_once()

class TestStrategy(unittest.TestCase):

    def test_generate_signal(self):
        # Create an instance of Strategy
        strategy = Strategy()
        
        # Mock market data
        market_data = {'price': 50000.0}
        
        # Generate a trading signal
        signal = strategy.generate_signal(market_data)
        
        # Verify the signal is correct
        self.assertIn(signal, ['buy', 'sell', 'hold'])

class TestScheduler(unittest.TestCase):

    @patch('bot.scheduler.BackgroundScheduler.start')
    @patch('bot.scheduler.BackgroundScheduler.shutdown')
    def test_scheduler(self, mock_start, mock_shutdown):
        # Create a mock trader
        mock_trader = Mock()
        
        # Initialize the scheduler with the mock trader
        scheduler = Scheduler(mock_trader)
        
        # Start the scheduler
        scheduler.start()
        mock_start.assert_called_once()
        
        # Shutdown the scheduler
        scheduler.shutdown()
        mock_shutdown.assert_called_once()

class TestDatabaseModels(unittest.TestCase):

    def test_trade_model(self):
        # Create a new trade instance
        new_trade = Trade(symbol="BTC-USD", trade_type="buy", price=50000.0, quantity=0.1)
        
        # Add to the session and commit
        session.add(new_trade)
        session.commit()
        
        # Retrieve the trade from the database
        retrieved_trade = session.query(Trade).filter_by(symbol="BTC-USD").first()
        
        # Verify the trade details
        self.assertEqual(retrieved_trade.symbol, "BTC-USD")
        self.assertEqual(retrieved_trade.trade_type, "buy")
        self.assertEqual(retrieved_trade.price, 50000.0)
        self.assertEqual(retrieved_trade.quantity, 0.1)

    def test_order_model(self):
        # Create a new order instance
        new_order = Order(order_id="12345", symbol="BTC-USD", order_type="limit", price=51000.0, quantity=0.1, status="open")
        
        # Add to the session and commit
        session.add(new_order)
        session.commit()
        
        # Retrieve the order from the database
        retrieved_order = session.query(Order).filter_by(order_id="12345").first()
        
        # Verify the order details
        self.assertEqual(retrieved_order.order_id, "12345")
        self.assertEqual(retrieved_order.symbol, "BTC-USD")
        self.assertEqual(retrieved_order.order_type, "limit")
        self.assertEqual(retrieved_order.price, 51000.0)
        self.assertEqual(retrieved_order.quantity, 0.1)
        self.assertEqual(retrieved_order.status, "open")

if __name__ == '__main__':
    unittest.main()
