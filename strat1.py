import pandas as pd
import pandas_ta as ta
import yfinance as yf
import matplotlib.pyplot as plt

ticker = 'AAPL'
data = yf.download(ticker, start="2020-01-01", end="2023-01-01")

data['RSI'] = ta.rsi(data['Close'], length=14)

data['Signal'] = 0
data.loc[data['RSI'] >= 70, 'Signal'] = 1 
data.loc[data['RSI'] <= 30, 'Signal'] = -1 

plt.figure(figsize=(14,7))

plt.subplot(2, 1, 1)
plt.plot(data.index, data['Close'], label='Close Price')
plt.title(f'{ticker} Close Price and RSI Buy/Sell Signals')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(data.index, data['RSI'], label='RSI', color='purple')
plt.axhline(70, color='green', linestyle='--') 
plt.axhline(30, color='red', linestyle='--')
plt.legend()

plt.show()

print(data[['Close', 'RSI', 'Signal']].tail(10))
