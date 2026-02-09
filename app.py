import streamlit as st
from visualization.plots import Plotter

st.set_page_config(page_title="Finance Data Extractor", layout="wide")
st.title("Finance Data Extractor", text_alignment="center")
ticker_select = st.selectbox("Ticker Selection", options=["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"], index=1)
ticker = ticker_select
plotter = Plotter(ticker)
st.space(size='medium')
col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("Stock Price")
    st.plotly_chart(plotter.plot_close(), use_container_width=True)
with col2:
    st.subheader("Stock Volume")
    st.plotly_chart(plotter.plot_volume(), use_container_width=True)

st.space(size='medium')

st.dataframe(plotter.uncensored_df, use_container_width=True)