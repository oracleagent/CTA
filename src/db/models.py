from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Trade(Base):
    __tablename__ = 'trades'

    id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String, nullable=False)
    trade_type = Column(String, nullable=False)  # 'buy' or 'sell'
    price = Column(Float, nullable=False)
    quantity = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(String, unique=True, nullable=False)
    symbol = Column(String, nullable=False)
    order_type = Column(String, nullable=False)  # 'limit', 'market', etc.
    price = Column(Float, nullable=True)
    quantity = Column(Float, nullable=False)
    status = Column(String, nullable=False)  # 'open', 'filled', 'cancelled', etc.
    timestamp = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)

class Configuration(Base):
    __tablename__ = 'configuration'

    id = Column(Integer, primary_key=True, autoincrement=True)
    key = Column(String, unique=True, nullable=False)
    value = Column(String, nullable=False)

# Database setup
DATABASE_URL = "sqlite:///trading_bot.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def create_tables():
    Base.metadata.create_all(engine)

# Example usage
if __name__ == "__main__":
    create_tables()

    # Example of adding a new trade
    new_trade = Trade(symbol="BTC-USD", trade_type="buy", price=50000.0, quantity=0.1)
    session.add(new_trade)
    session.commit()

    # Example of adding a new order
    new_order = Order(order_id="12345", symbol="BTC-USD", order_type="limit", price=51000.0, quantity=0.1, status="open")
    session.add(new_order)
    session.commit()

    # Example of adding a configuration setting
    config = Configuration(key="api_key", value="your_api_key")
    session.add(config)
    session.commit()
