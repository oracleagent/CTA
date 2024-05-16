import numpy as np
import pandas as pd

class MarketAnalysis:
    """
    Provides tools for analyzing cryptocurrency market data.
    """

    @staticmethod
    def calculate_moving_average(data, window=14):
        """
        Calculates the moving average of the given data over the specified window size.
        Args:
        data (list): A list of prices.
        window (int): The number of periods over which to calculate the moving average.
        Returns:
        numpy.array: An array containing the moving averages.
        """
        return np.convolve(data, np.ones(window), 'valid') / window

    @staticmethod
    def calculate_rsi(data, periods=14):
        """
        Calculates the Relative Strength Index (RSI) for the given data.
        Args:
        data (list): A list of prices.
        periods (int): The number of periods to use in calculation.
        Returns:
        numpy.array: An array containing the RSI values.
        """
        delta = np.diff(data)
        gain = (delta > 0) * delta
        loss = (delta < 0) * -delta
        avg_gain = np.convolve(gain, np.ones(periods), 'valid') / periods
        avg_loss = np.convolve(loss, np.ones(periods), 'valid') / periods
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

# Example usage:
if __name__ == "__main__":
    data = [45, 46, 47, 48, 45, 43, 44, 46, 47, 48, 49, 50, 51, 52, 53]
    analysis = MarketAnalysis()
    print("Moving Average:", analysis.calculate_moving_average(data, window=3))
    print("RSI:", analysis.calculate_rsi(data))
