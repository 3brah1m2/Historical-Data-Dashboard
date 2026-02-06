import yfinance as yf
data = yf.Ticker('MSFT') 

class FinanceDataExtractor:
    def __init__(self, ticker):
        self.ticker = ticker
        self.data = yf.Ticker(ticker)

    def get_history(self, period='7d'):
        return self.data.history(period=period)
    
if __name__ == "__main__":  
    extractor = FinanceDataExtractor('MSFT')
    history_data = extractor.get_history()
    print(history_data)