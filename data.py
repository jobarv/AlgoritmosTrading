import yfinance as yf

ticker='MSFT'
df_MSFT = yf.download(tickers=ticker, period="5d")
print(df_MSFT)
