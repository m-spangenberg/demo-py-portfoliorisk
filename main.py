import numpy as np
import yfinance as yf
from datetime import datetime


class FinancialDataPipeline:
    """
    Demo pipeline for Value at Risk (VaR) calculation using historical price data from Yahoo Finance.
    """

    def __init__(self, ticker: str, initial_investment: float):
        self.ticker = ticker
        self.investment = initial_investment

    def fetch_data(self, period: str = "1mo", interval: str = "1d") -> np.ndarray:
        """
        Fetching financial data from the source.

        Parameters:
        - period: The time period for which to fetch data (e.g., '1d', '5d', '1mo', '1y').
        - interval: The data interval (e.g., '1m', '1d', '1wk', '1mo').
        """
        data = yf.download(
            self.ticker, period=period, interval=interval, progress=False
        )
        return data["Close"]

    def calculate_metrics(self, prices: np.ndarray) -> dict:
        """
        Transform raw data into insights.

        Parameters:
        - prices: An array of closing prices for the asset.
        """
        returns = prices.pct_change().dropna()
        mu = np.mean(returns)
        sigma = np.std(returns)

        # 95% Confidence Level VaR
        var_95 = self.investment * (1.645 * sigma - mu)

        return {
            "timestamp": datetime.now(),
            "last_price": prices.iloc[-1],
            "daily_return": returns.iloc[-1],
            "var_95": var_95,
        }

    def run_pipeline(self):
        """
        Orchestration of the data pipeline: fetch, transform, and store results.
        """
        print(f"--- Starting Pipeline for {self.ticker} ---")
        raw_data = self.fetch_data()
        metrics = self.calculate_metrics(raw_data)
        print(f"Process Complete at {metrics['timestamp']}")
        print(f"Current Value at Risk (95%): ${metrics['var_95']:.2f}")
        # TODO: Maybe send metrics to a database or a file.


# Application
if __name__ == "__main__":
    # Simulate a $100,000 investment in Nvidia stock (NVDA) for the last month
    pipeline = FinancialDataPipeline("NVDA", 100000)
    pipeline.run_pipeline()
