import yfinance as yf
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime

ticker='MSFT'
df_MSFT = yf.download(tickers=ticker, period="5d")
print(df_MSFT)


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])])

fig.show()