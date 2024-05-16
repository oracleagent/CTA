import hashlib
import hmac
import time
from .common import APIBase

class BinanceClient(APIBase):
    def __init__(self, api_key, secret_key):
        super().__init__("https://api.binance.com")
        self.api_key = api_key
        self.secret_key = secret_key

    def _create_signature(self, query_string):
        return hmac.new(self.secret_key.encode(), query_string.encode(), hashlib.sha256).hexdigest()

    def get_account_info(self):
        """Fetch account information."""
        endpoint = "/api/v3/account"
        timestamp = int(time.time() * 1000)
        query_string = f"timestamp={timestamp}"
        signature = self._create_signature(query_string)
        params = f"{query_string}&signature={signature}"
        return self.get(endpoint, params=params, headers={"X-MBX-APIKEY": self.api_key})

    def place_order(self, symbol, side, quantity, price=None, order_type="LIMIT"):
        """Place an order."""
        endpoint = "/api/v3/order"
        timestamp = int(time.time() * 1000)
        query_string = f"symbol={symbol}&side={side}&type={order_type}&timeInForce=GTC&quantity={quantity}&timestamp={timestamp}"
        if price:
            query_string += f"&price={price}"
        signature = self._create_signature(query_string)
        params = f"{query_string}&signature={signature}"
        return self.post(endpoint, params=params, headers={"X-MBX-APIKEY": self.api_key})
