import json
from bot.trader import Trader

class SessionManager:
    """
    Manages trading sessions, including their configuration and lifecycle.
    """

    def __init__(self, trader: Trader):
        self.trader = trader
        self.session_active = False

    def load_session_config(self, config_path):
        """
        Loads session configuration from a JSON file.
        """
        with open(config_path, 'r') as file:
            config = json.load(file)
        self.trader.update_strategy(config['strategy'])
        print(f"Loaded configuration: {config}")

    def start_session(self):
        """
        Starts a new trading session using the loaded configuration.
        """
        if not self.session_active:
            self.session_active = True
            self.trader.run()
            print("Trading session started.")
        else:
            print("A session is already active.")

    def stop_session(self):
        """
        Stops the current trading session.
        """
        if self.session_active:
            self.session_active = False
            print("Trading session stopped.")
        else:
            print("No active session to stop.")

# Example usage
if __name__ == "__main__":
    from api.binance.client import BinanceClient
    from bot.strategy import AdvancedStrategy

    client = BinanceClient(api_key='your_api_key', secret_key='your_secret_key')
    strategy = AdvancedStrategy(client)
    trader = Trader(client, strategy)
    
    session_manager = SessionManager(trader)
    session_manager.load_session_config('config/session_config.json')
    session_manager.start_session()
    # Later you can stop the session
    session_manager.stop_session()
