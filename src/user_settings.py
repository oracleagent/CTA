import json
from db.database import Database

class UserSettings:
    """
    Manages user settings for the trading bot.
    """
    
    def __init__(self, db: Database):
        self.db = db

    def update_settings(self, user_id, settings):
        """
        Updates the user's settings in the database.
        Args:
        user_id (str): The unique identifier for the user.
        settings (dict): A dictionary of settings to update.
        """
        result = self.db.update_user_settings(user_id, settings)
        if result:
            print(f"Settings updated for user {user_id}")
        else:
            print(f"Failed to update settings for user {user_id}")

    def load_settings(self, user_id):
        """
        Loads the user's settings from the database.
        Args:
        user_id (str): The unique identifier for the user.
        Returns:
        dict: The user's settings.
        """
        settings = self.db.get_user_settings(user_id)
        if settings:
            print(f"Loaded settings for user {user_id}: {settings}")
        else:
            print(f"No settings found for user {user_id}")
        return settings

# Example usage
if __name__ == "__main__":
    db = Database(uri="mongodb://localhost:27017", dbname="trading_bot")
    user_settings_manager = UserSettings(db)
    user_id = "user123"
    new_settings = {
        'risk_level': 'moderate',
        'api_key': 'new_api_key_here',
        'notification_preferences': {
            'email': 'user@example.com',
            'sms': '1234567890'
        }
    }
    user_settings_manager.update_settings(user_id, new_settings)
    settings = user_settings_manager.load_settings(user_id)
