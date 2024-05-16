import logging
from notification_service import NotificationService

class Alerts:
    """
    Manages alerts for various conditions and triggers in the trading bot.
    """

    def __init__(self, notification_service: NotificationService):
        """
        Initializes the Alerts manager with a notification service.
        Args:
        notification_service (NotificationService): The service responsible for sending notifications.
        """
        self.notification_service = notification_service

    def send_price_alert(self, symbol, price, threshold):
        """
        Sends an alert if the price of a symbol exceeds a threshold.
        Args:
        symbol (str): The trading pair symbol (e.g., 'BTC-USD').
        price (float): The current price of the symbol.
        threshold (float): The price threshold for the alert.
        """
        if price > threshold:
            message = f"Alert: {symbol} price has exceeded the threshold. Current price: {price}, Threshold: {threshold}"
            self.notification_service.send_email(
                subject="Price Alert",
                message=message,
                recipient="trader@example.com"
            )
            logging.info(message)

    def send_trade_execution_alert(self, trade_details):
        """
        Sends an alert with details of a trade execution.
        Args:
        trade_details (dict): A dictionary containing trade details such as symbol, trade_type, quantity, and price.
        """
        message = f"Trade Execution Alert: {trade_details['trade_type']} {trade_details['quantity']} of {trade_details['symbol']} at {trade_details['price']}"
        self.notification_service.send_email(
            subject="Trade Execution Alert",
            message=message,
            recipient="trader@example.com"
        )
        logging.info(message)

    def send_error_alert(self, error_message):
        """
        Sends an alert with an error message.
        Args:
        error_message (str): The error message to be sent in the alert.
        """
        self.notification_service.send_email(
            subject="Error Alert",
            message=error_message,
            recipient="trader@example.com"
        )
        logging.error(error_message)

# Example usage:
if __name__ == "__main__":
    email_host = 'smtp.example.com'
    email_port = 587
    email_user = 'your-email@example.com'
    email_password = 'your-email-password'
    notification_service = NotificationService(email_host, email_port, email_user, email_password)

    alerts = Alerts(notification_service)
    alerts.send_price_alert('BTC-USD', 50000, 45000)
    alerts.send_trade_execution_alert({
        'symbol': 'BTC-USD',
        'trade_type': 'buy',
        'quantity': 0.1,
        'price': 49000
    })
    alerts.send_error_alert("Failed to execute trade due to insufficient funds.")
