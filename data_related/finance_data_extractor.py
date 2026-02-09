import yfinance as yf
data = yf.Ticker('MSFT') 

class FinanceDataExtractor:
    def __init__(self, ticker):
        self.ticker = ticker
        self.data = yf.Ticker(ticker)

    def get_history(self, period='2mo'):
        return self.data.history(period=period)