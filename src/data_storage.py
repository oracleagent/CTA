from db.database import Database
import logging

class DataStorage:
    """
    Manages the storage and retrieval of trading-related data.
    """

    def __init__(self, db: Database):
        """
        Initializes the DataStorage with a database connection.
        Args:
        db (Database): The database connection instance.
        """
        self.db = db

    def store_trade_data(self, trade_data):
        """
        Stores trade data in the database.
        Args:
        trade_data (dict): A dictionary containing trade information.
        """
        try:
            self.db.insert_trade(trade_data)
            logging.info("Trade data stored successfully.")
        except Exception as e:
            logging.error(f"Failed to store trade data: {str(e)}")

    def retrieve_trade_data(self, query):
        """
        Retrieves trade data from the database based on a query.
        Args:
        query (dict): A dictionary specifying query parameters.
        Returns:
        list: A list of trade records matching the query.
        """
        try:
            data = self.db.get_trades(query)
            logging.info("Trade data retrieved successfully.")
            return data
        except Exception as e:
            logging.error(f"Failed to retrieve trade data: {str(e)}")
            return []

    def update_trade_data(self, trade_id, update_fields):
        """
        Updates specific fields of a trade record.
        Args:
        trade_id (str): The unique identifier of the trade to update.
        update_fields (dict): A dictionary of the fields to update.
        """
        try:
            self.db.update_trade(trade_id, update_fields)
            logging.info("Trade data updated successfully.")
        except Exception as e:
            logging.error(f"Failed to update trade data: {str(e)}")

# Example usage:
if __name__ == "__main__":
    db = Database(uri="mongodb://localhost:27017", dbname="trading_bot")
    data_storage = DataStorage(db)
    trade_data = {'trade_id': '1', 'symbol': 'BTC-USD', 'price': 50000, 'quantity': 0.1, 'type': 'buy'}
    data_storage.store_trade_data(trade_data)
    print(data_storage.retrieve_trade_data({'trade_id': '1'}))
    data_storage.update_trade_data('1', {'price': 51000})
