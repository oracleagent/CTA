import logging
from logging.handlers import RotatingFileHandler

def setup_logging(log_file='trading.log', level=logging.INFO):
    """
    Sets up the logging configuration.
    """
    logger = logging.getLogger('trading_bot')
    logger.setLevel(level)

    # Create handlers
    c_handler = logging.StreamHandler()
    f_handler = RotatingFileHandler(log_file, maxBytes=1000000, backupCount=5)

    # Create formatters and add it to handlers
    c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger

# Usage
logger = setup_logging()
logger.info('Logger setup complete - ready to start trading operations')
