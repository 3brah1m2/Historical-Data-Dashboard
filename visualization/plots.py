from data_related.data_processor import DataProcessor
import plotly.express as px

class Plotter:
    def __init__(self, ticker):
        self.data_processor = DataProcessor(ticker)
        self.df = self.data_processor.process_data()
    
    def plot_close(self):
        fig = px.line(self.df, x=self.df.index, y="Close", title=f'{self.data_processor.extractor.ticker} Stock Price')
        fig.show()
    
    def plot_volume(self):
        fig = px.line(self.df, x=self.df.index, y="Volume", title=f'{self.data_processor.extractor.ticker} Stock Volume')
        fig.show()