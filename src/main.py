import os
import sys
import signal
from api.binance.client import BinanceClient
from bot.trader import Trader
from bot.strategy import AdvancedStrategy
from bot.scheduler import Scheduler
from db.database import Database
import logging
from bot.logging import setup_logging
from api.metamask import MetaMask  # Import MetaMask

def load_configuration():
    # Placeholder for configuration loading logic
    return {
        "db_uri": os.getenv("DB_URI", "mongodb://localhost:27017"),
        "db_name": os.getenv("DB_NAME", "crypto_trading"),
        "api_key": os.getenv("BINANCE_API_KEY"),
        "api_secret": os.getenv("BINANCE_SECRET_KEY"),
        "infura_url": os.getenv("INFURA_URL"),
        "metamask_private_key": os.getenv("METAMASK_PRIVATE_KEY")
    }

def handle_shutdown(signum, frame):
    logging.info("Shutdown signal received")
    scheduler.shutdown()
    sys.exit(0)

if __name__ == "__main__":
    logging = setup_logging()

    # Load configuration
    config = load_configuration()

    # Setup signal handling
    signal.signal(signal.SIGINT, handle_shutdown)
    signal.signal(signal.SIGTERM, handle_shutdown)

    # Initialize database
    db = Database(uri=config["db_uri"], dbname=config["db_name"])

    # Initialize API client
    client = BinanceClient(api_key=config["api_key"], secret_key=config["api_secret"])

    # Initialize trading strategy
    strategy = AdvancedStrategy(client)

    # Initialize trader
    trader = Trader(client, strategy)

    # Initialize and start scheduler
    scheduler = Scheduler(trader)
    scheduler.start()

    # MetaMask Integration
    metamask = MetaMask()
    balance = metamask.get_balance()
    logging.info(f"MetaMask Account Balance: {balance} ETH")

    # Send a transaction (for demonstration purposes, adjust accordingly)
    to_address = '0xRecipientAddressHere'  # Replace with actual recipient address
    amount = 0.01  # Amount in ETH
    tx_hash = metamask.send_transaction(to_address, amount)
    logging.info(f"Transaction sent with hash: {tx_hash}")

    logging.info("Trading bot started successfully.")
