import logging
from src.bot.logging import setup_logging

# Setup logger for error handling
logger = setup_logging()

class ErrorHandling:
    """A class to handle exceptions and errors in the trading bot."""

    @staticmethod
    def handle_exception(exc, message="An error occurred"):
        """Log the exception and its message."""
        logger.error(f"{message}: {str(exc)}")

    @staticmethod
    def critical_error_handler(exc):
        """Handle critical errors that may require stopping the bot."""
        ErrorHandling.handle_exception(exc, "Critical error encountered")
        # Additional logic to perform cleanup and safely stop the bot
        # Consider sending notification to the administrator if required

# Example of using the error handling in practice
def risky_operation():
    try:
        # Potentially risky code goes here
        pass
    except Exception as exc:
        ErrorHandling.critical_error_handler(exc)

if __name__ == "__main__":
    risky_operation()
