import logging
from alerts import Alerts
from order_manager import OrderManager

class EventHandler:
    """
    Handles various events in the trading bot such as price changes, order updates, and other significant events.
    """

    def __init__(self, alerts: Alerts, order_manager: OrderManager):
        """
        Initializes the EventHandler with alerts and order manager instances.
        Args:
        alerts (Alerts): The alerts manager to send notifications.
        order_manager (OrderManager): The order manager to handle order-related events.
        """
        self.alerts = alerts
        self.order_manager = order_manager

    def handle_price_change(self, symbol, price):
        """
        Handles a price change event.
        Args:
        symbol (str): The trading pair symbol (e.g., 'BTC-USD').
        price (float): The new price of the symbol.
        """
        logging.info(f"Price change detected for {symbol}: {price}")
        # Add your price change handling logic here
        # For example, check if the price exceeds a threshold and trigger an alert
        threshold = 45000  # Example threshold
        self.alerts.send_price_alert(symbol, price, threshold)

    def handle_order_update(self, order_id, status):
        """
        Handles an order update event.
        Args:
        order_id (str): The unique identifier of the order.
        status (str): The new status of the order (e.g., 'filled', 'cancelled').
        """
        logging.info(f"Order update detected for order ID {order_id}: {status}")
        # Add your order update handling logic here
        # For example, send an alert when an order is filled or cancelled
        if status == 'filled':
            order_details = self.order_manager.get_order_status('exchange_name', order_id)
            self.alerts.send_trade_execution_alert(order_details)
        elif status == 'cancelled':
            self.alerts.send_error_alert(f"Order {order_id} was cancelled")

    def handle_error(self, error_message):
        """
        Handles an error event.
        Args:
        error_message (str): The error message to handle.
        """
        logging.error(f"Error detected: {error_message}")
        # Add your error handling logic here
        self.alerts.send_error_alert(error_message)

# Example usage:
if __name__ == "__main__":
    from notification_service import NotificationService
    from api.api_manager import APIManager

    email_host = 'smtp.example.com'
    email_port = 587
    email_user = 'your-email@example.com'
    email_password = 'your-email-password'
    notification_service = NotificationService(email_host, email_port, email_user, email_password)

    alerts = Alerts(notification_service)
    api_manager = APIManager(api_config={"api_key": "your_key", "api_secret": "your_secret"})
    order_manager = OrderManager(api_manager)

    event_handler = EventHandler(alerts, order_manager)
    event_handler.handle_price_change('BTC-USD', 50000)
    event_handler.handle_order_update('order_id_12345', 'filled')
    event_handler.handle_error('An unexpected error occurred')
