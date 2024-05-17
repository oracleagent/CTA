import os
import sys
import signal
import json
from dotenv import load_dotenv
from api.binance.client import BinanceClient
from api.coinbase.client import CoinbaseClient
from api.metamask.client import MetaMaskClient
from bot.trader import Trader
from bot.strategy import AdvancedStrategy
from bot.scheduler import Scheduler
from db.database import Database
import logging
from bot.logging import setup_logging

# Load environment variables from .env file
load_dotenv()

def load_configuration():
    with open("config/default.json") as config_file:
        config = json.load(config_file)
    return config

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
    db = Database(uri=f"mongodb://{config['database']['user']}:{config['database']['password']}@{config['database']['host']}:{config['database']['port']}", dbname=config["database"]["dbName"])

    # Initialize API clients
    binance_client = BinanceClient(api_key=os.getenv("BINANCE_API_KEY"), secret_key=os.getenv("BINANCE_SECRET_KEY"))
    coinbase_client = CoinbaseClient(api_key=os.getenv("COINBASE_API_KEY"), secret_key=os.getenv("COINBASE_SECRET_KEY"))
    metamask_client = MetaMaskClient(os.getenv("METAMASK_PRIVATE_KEY"), os.getenv("INFURA_URL"))

    # Initialize trading strategy
    strategy = AdvancedStrategy(binance_client)

    # Initialize trader
    trader = Trader(binance_client, strategy)

    # Initialize and start scheduler
    scheduler = Scheduler(trader)
    scheduler.start()

    logging.info("Trading bot started successfully.")

    # Example MetaMask transaction
    tx_hash = metamask_client.send_transaction("recipient_address", 0.01, 21000, 50)
    logging.info(f"MetaMask transaction sent with hash: {tx_hash}")
