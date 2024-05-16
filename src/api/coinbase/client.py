import json
import time
from .common import APIBase

class CoinbaseClient(APIBase):
    def __init__(self, api_key, api_secret):
        super().__init__("https://api.pro.coinbase.com")
        self.api_key = api_key
        self.api_secret = api_secret

    def get_account_info(self):
        """Fetch account information."""
        endpoint = "/accounts"
        return self.get(endpoint, headers=self._create_headers(endpoint))

    def place_order(self, product_id, side, size, price=None, order_type="limit"):
        """Place an order."""
        endpoint = "/orders"
        data = {
            "type": order_type,
            "side": side,
            "product_id": product_id,
            "size": size
        }
        if price:
            data["price"] = price
        return self.post(endpoint, json=data, headers=self._create_headers(endpoint, body=json.dumps(data)))

    def _create_headers(self, request_path, body=""):
        timestamp = str(time.time())
        message = timestamp + 'GET' + request_path + body
        signature = hmac.new(self.api_secret.encode(), message.encode(), hashlib.sha256).hexdigest()
        return {
            "CB-ACCESS-SIGN": signature,
            "CB-ACCESS-TIMESTAMP": timestamp,
            "CB-ACCESS-KEY": self.api_key,
            "Content-Type": "application/json"
        }
