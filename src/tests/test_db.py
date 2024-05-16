import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base, Trade, Order, Configuration

class TestDatabaseModels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Set up a temporary database for testing.
        """
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)
    
    def setUp(self):
        """
        Create a new session before each test.
        """
        self.session = self.Session()

    def tearDown(self):
        """
        Rollback any changes after each test.
        """
        self.session.rollback()
        self.session.close()

    def test_trade_model(self):
        # Create a new trade instance
        new_trade = Trade(symbol="BTC-USD", trade_type="buy", price=50000.0, quantity=0.1)
        
        # Add to the session and commit
        self.session.add(new_trade)
        self.session.commit()
        
        # Retrieve the trade from the database
        retrieved_trade = self.session.query(Trade).filter_by(symbol="BTC-USD").first()
        
        # Verify the trade details
        self.assertEqual(retrieved_trade.symbol, "BTC-USD")
        self.assertEqual(retrieved_trade.trade_type, "buy")
        self.assertEqual(retrieved_trade.price, 50000.0)
        self.assertEqual(retrieved_trade.quantity, 0.1)

    def test_order_model(self):
        # Create a new order instance
        new_order = Order(order_id="12345", symbol="BTC-USD", order_type="limit", price=51000.0, quantity=0.1, status="open")
        
        # Add to the session and commit
        self.session.add(new_order)
        self.session.commit()
        
        # Retrieve the order from the database
        retrieved_order = self.session.query(Order).filter_by(order_id="12345").first()
        
        # Verify the order details
        self.assertEqual(retrieved_order.order_id, "12345")
        self.assertEqual(retrieved_order.symbol, "BTC-USD")
        self.assertEqual(retrieved_order.order_type, "limit")
        self.assertEqual(retrieved_order.price, 51000.0)
        self.assertEqual(retrieved_order.quantity, 0.1)
        self.assertEqual(retrieved_order.status, "open")

    def test_configuration_model(self):
        # Create a new configuration instance
        new_config = Configuration(key="api_key", value="your_api_key")
        
        # Add to the session and commit
        self.session.add(new_config)
        self.session.commit()
        
        # Retrieve the configuration from the database
        retrieved_config = self.session.query(Configuration).filter_by(key="api_key").first()
        
        # Verify the configuration details
        self.assertEqual(retrieved_config.key, "api_key")
        self.assertEqual(retrieved_config.value, "your_api_key")

if __name__ == '__main__':
    unittest.main()
