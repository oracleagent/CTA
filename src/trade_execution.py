from api.api_manager import APIManager
from utils.notifications import NotificationManager
import logging

class TradeExecutor:
    """
    Manages the execution of trades on cryptocurrency exchanges.
    """

    def __init__(self, api_manager: APIManager, notification_manager: NotificationManager):
        """
        Initializes the TradeExecutor with API and notification managers.
        Args:
        api_manager (APIManager): The manager responsible for API calls to exchanges.
        notification_manager (NotificationManager): The manager responsible for sending notifications.
        """
        self.api_manager = api_manager
        self.notification_manager = notification_manager

    def execute_trade(self, exchange, symbol, trade_type, quantity):
        """
        Executes a trade on the specified exchange.
        Args:
        exchange (str): The name of the exchange to execute the trade on.
        symbol (str): The trading symbol (e.g., 'BTC-USD').
        trade_type (str): Type of trade, 'buy' or 'sell'.
        quantity (float): Amount of the asset to trade.
        """
        result = self.api_manager.execute_trade(exchange, trade_type, symbol, quantity)
        if result:
            logging.info(f"Executed {trade_type} order for {quantity} of {symbol} on {exchange}")
            self.notification_manager.send_email(
                subject="Trade Execution Notification",
                message=f"Executed {trade_type} order for {quantity} of {symbol} on {exchange}",
                recipient="trader@example.com"
            )
        else:
            logging.error(f"Failed to execute {trade_type} order for {symbol} on {exchange}")
            self.notification_manager.send_email(
                subject="Trade Execution Failure",
                message=f"Failed to execute {trade_type} order for {symbol} on {exchange}",
                recipient="trader@example.com"
            )

# Example usage:
if __name__ == "__main__":
    api_manager = APIManager(api_config={"api_key": "your_key", "api_secret": "your_secret"})
    notification_manager = NotificationManager(email_host="smtp.example.com", email_port=587,
                                               email_user="your-email@example.com", email_password="your-email-password")
    trade_executor = TradeExecutor(api_manager, notification_manager)
    trade_executor.execute_trade("binance", "BTC-USD", "buy", 1.0)
