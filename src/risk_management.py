class RiskManager:
    """
    Handles risk management for trading activities.
    """

    def __init__(self, max_risk_per_trade=0.01, max_daily_risk=0.05, volatility_threshold=0.02):
        """
        Initializes the risk manager with basic risk parameters.
        Args:
        max_risk_per_trade (float): Maximum risk percentage per trade.
        max_daily_risk (float): Maximum total risk percentage for all trades per day.
        volatility_threshold (float): Volatility threshold to adjust the risk.
        """
        self.max_risk_per_trade = max_risk_per_trade
        self.max_daily_risk = max_daily_risk
        self.volatility_threshold = volatility_threshold

    def calculate_position_size(self, portfolio_value, entry_price, stop_loss_price):
        """
        Calculates the position size based on the stop-loss price and maximum risk per trade.
        Args:
        portfolio_value (float): Total value of the current portfolio.
        entry_price (float): The price at which the trade would be entered.
        stop_loss_price (float): The stop-loss price.
        Returns:
        float: The maximum position size.
        """
        risk_per_share = entry_price - stop_loss_price
        if risk_per_share <= 0:
            return 0
        position_size = (self.max_risk_per_trade * portfolio_value) / risk_per_share
        return position_size

    def adjust_for_volatility(self, current_volatility):
        """
        Adjusts the trading parameters based on the current market volatility.
        Args:
        current_volatility (float): The current volatility of the market.
        """
        if current_volatility > self.volatility_threshold:
            # Reduce risk parameters in high volatility
            self.max_risk_per_trade *= 0.5
            self.max_daily_risk *= 0.5
        else:
            # Reset risk parameters
            self.max_risk_per_trade = 0.01
            self.max_daily_risk = 0.05

# Example usage:
if __name__ == "__main__":
    rm = RiskManager()
    portfolio_value = 10000
    entry_price = 100
    stop_loss_price = 95
    print("Position Size:", rm.calculate_position_size(portfolio_value, entry_price, stop_loss_price))
    rm.adjust_for_volatility(0.03)
    print("Adjusted Max Risk Per Trade:", rm.max_risk_per_trade)
