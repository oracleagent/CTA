import json
import logging
from pathlib import Path

class Config:
    """
    Handles loading and accessing configuration settings for the trading bot.
    """

    def __init__(self, config_file='config/default.json'):
        """
        Initializes the Config class and loads settings from a JSON file.
        Args:
        config_file (str): Path to the configuration file.
        """
        self.config_file = Path(config_file)
        self.config = self.load_config()

    def load_config(self):
        """
        Loads the configuration settings from a JSON file.
        Returns:
        dict: The configuration settings.
        """
        if not self.config_file.exists():
            logging.error(f"Config file not found: {self.config_file}")
            return {}

        with open(self.config_file, 'r') as file:
            try:
                config = json.load(file)
                logging.info(f"Loaded config from {self.config_file}")
                return config
            except json.JSONDecodeError as e:
                logging.error(f"Error parsing config file: {e}")
                return {}

    def get(self, key, default=None):
        """
        Retrieves a configuration value.
        Args:
        key (str): The key of the configuration value.
        default: The default value to return if the key is not found.
        Returns:
        The configuration value or the default value.
        """
        return self.config.get(key, default)

# Example usage:
if __name__ == "__main__":
    config = Config('config/default.json')
    api_key = config.get('api_key', 'default_key')
    print(f"API Key: {api_key}")
