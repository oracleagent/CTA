from pydantic import BaseModel
from typing import List

class Kline(BaseModel):
    open_time: int
    open: str
    high: str
    low: str
    close: str
    volume: str
    close_time: int
    quote_asset_volume: str
    number_of_trades: int
    taker_buy_base_asset_volume: str
    taker_buy_quote_asset_volume: str
    ignore: str

class Trade(BaseModel):
    symbol: str
    order_id: int
    order_list_id: int
    client_order_id: str
    transact_time: int
    price: str
    orig_qty: str
    executed_qty: str
    cummulative_quote_qty: str
    status: str
    time_in_force: str
    type: str
    side: str
    fills: List[dict]

class OrderStatus(BaseModel):
    symbol: str
    order_id: int
    order_list_id: int
    client_order_id: str
    price: str
    orig_qty: str
    executed_qty: str
    cummulative_quote_qty: str
    status: str
    time_in_force: str
    type: str
    side: str
    stop_price: str
    iceberg_qty: str
    time: int
    update_time: int
    is_working: bool
    orig_quote_order_qty: str

# Example usage:
if __name__ == "__main__":
    kline_example = {
        "open_time": 1617184800000,
        "open": "56256.97000000",
        "high": "56457.14000000",
        "low": "56177.28000000",
        "close": "56362.17000000",
        "volume": "132.53452000",
        "close_time": 1617184859999,
        "quote_asset_volume": "7463452.82503200",
        "number_of_trades": 4578,
        "taker_buy_base_asset_volume": "67.63649000",
        "taker_buy_quote_asset_volume": "3808534.32323100",
        "ignore": "0"
    }

    trade_example = {
        "symbol": "BTCUSDT",
        "order_id": 28,
        "order_list_id": -1,
        "client_order_id": "6gCrw2kRUAF9CvJDGP16IP",
        "transact_time": 1507725176595,
        "price": "0.078772",
        "orig_qty": "0.001",
        "executed_qty": "0.001",
        "cummulative_quote_qty": "0.00007877",
        "status": "FILLED",
        "time_in_force": "GTC",
        "type": "LIMIT",
        "side": "SELL",
        "fills": []
    }

    kline = Kline(**kline_example)
    trade = Trade(**trade_example)

    print(kline)
    print(trade)
