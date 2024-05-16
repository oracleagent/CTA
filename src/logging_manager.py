import logging
from logging.handlers import RotatingFileHandler

class LoggingManager:
    """
    Manages logging for the trading bot, setting up both console and file-based logs.
    """

    def __init__(self, name, file_name='trading_bot.log'):
        """
        Initializes the logging manager with a name and optionally a file name for logs.
        Args:
        name (str): The name of the logger.
        file_name (str): The filename for storing logs.
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)  # Set to debug to capture all levels of logs

        # Create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # Create file handler which logs even debug messages
        fh = RotatingFileHandler(file_name, maxBytes=10485760, backupCount=5)
        fh.setLevel(logging.DEBUG)

        # Create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        # Add the handlers to the logger
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

    def get_logger(self):
        """
        Returns the configured logger.
        Returns:
        logging.Logger: The configured logger.
        """
        return self.logger

# Example usage:
if __name__ == "__main__":
    log_manager = LoggingManager('trading_bot')
    logger = log_manager.get_logger()
    logger.info('Starting the trading bot...')
