import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
yf.pdr_override()


tickers = ["GRND3.SA"]
carteira = (web.get_data_yahoo(tickers, start="2021-01-01")["Close"])

# Cotações
carteira.plot()
plt.show()