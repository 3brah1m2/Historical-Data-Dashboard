from data_related.finance_data_extractor import FinanceDataExtractor  
import pandas as pd

class DataProcessor:
    def __init__(self, ticker):
        self.extractor = FinanceDataExtractor(ticker)
        self.df = self.extractor.get_history()
    def process_data(self):
        self.new_df = self.df[['Close', 'Volume']]
        return self.new_df