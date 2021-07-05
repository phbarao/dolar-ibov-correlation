import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import seaborn as sns
yf.pdr_override()


tickers = [ "^BVSP", "USDBRL=X"]
carteira = web.get_data_yahoo(tickers, start="2007-01-01")["Close"]
carteira = carteira.dropna()
carteira.columns = [ "DOLAR", "IBOV" ]

carteira["DOLAR"].rolling(252).corr(carteira["IBOV"]).plot(figsize=(22,8))
plt.show()
