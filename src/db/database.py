from pymongo import MongoClient

class Database:
    def __init__(self, uri, dbname):
        self.client = MongoClient(uri)
        self.db = self.client[dbname]

    def insert_trade(self, trade_data):
        """
        Inserts a trade record into the database.
        """
        trades_collection = self.db.trades
        result = trades_collection.insert_one(trade_data)
        return result.inserted_id

    def get_recent_trades(self, limit=10):
        """
        Retrieves recent trade records from the database.
        """
        trades_collection = self.db.trades
        recent_trades = trades_collection.find().sort('_id', -1).limit(limit)
        return list(recent_trades)

    def update_user_settings(self, user_id, settings):
        """
        Updates user settings in the database.
        """
        users_collection = self.db.users
        result = users_collection.update_one({'user_id': user_id}, {'$set': settings}, upsert=True)
        return result.modified_count
