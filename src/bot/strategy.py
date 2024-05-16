import numpy as np

class BaseStrategy:
    """
    A base trading strategy class from which all trading strategies should inherit.
    """
    def __init__(self, client):
        self.client = client

    def should_buy(self, market_data):
        raise NotImplementedError

    def should_sell(self, market_data):
        raise NotImplementedError

class AdvancedStrategy(BaseStrategy):
    """
    An advanced strategy that uses both SMA and EMA to determine buy and sell signals based on crossover.
    """
    def __init__(self, client, short_window=40, long_window=100):
        super().__init__(client)
        self.short_window = short_window
        self.long_window = long_window

    def _moving_average(self, prices, window, type='sma'):
        """
        Calculate moving averages including SMA and EMA.
        """
        if type == 'sma':
            return np.convolve(prices, np.ones(window), 'valid') / window
        elif type == 'ema':
            weights = np.exp(np.linspace(-1., 0., window))
            weights /= weights.sum()
            a =  np.convolve(prices, weights, 'valid')[:len(prices)]
            return np.concatenate((prices[:window-1], a))
        else:
            raise ValueError("Unsupported MA type")

    def should_buy(self, market_data):
        """
        Generates a buy signal when the short EMA crosses above the long SMA.
        """
        prices = market_data['prices']
        sma = self._moving_average(prices, self.long_window, 'sma')
        ema = self._moving_average(prices, self.short_window, 'ema')

        # Check for the last available complete MA
        if ema[-1] > sma[-1] and ema[-2] < sma[-2]:
            return True
        return False

    def should_sell(self, market_data):
        """
        Generates a sell signal when the short EMA crosses below the long SMA.
        """
        prices = market_data['prices']
        sma = self._moving_average(prices, self.long_window, 'sma')
        ema = self._moving_average(prices, self.short_window, 'ema')

        # Check for the last available complete MA
        if ema[-1] < sma[-1] and ema[-2] > sma[-2]:
            return True
        return False
