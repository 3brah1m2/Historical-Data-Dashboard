from visualization.plots import Plotter

if __name__ == "__main__":
    ticker = 'MSFT'
    plotter = Plotter(ticker)
    plotter.plot_close()
    plotter.plot_volume()