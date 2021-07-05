import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import seaborn as sns
yf.pdr_override()


tickers = [ "^BVSP", "USDBRL=X"]
# grnd = [ "^BVSP", "USDBRL=X"]
carteira = web.get_data_yahoo(tickers, start="2007-01-01")["Close"]
carteira = carteira.dropna()
carteira.columns = [ "DOLAR", "IBOV" ]

# Dolar Today
print('-=' * 20)
print(f'DOLAR: {carteira["DOLAR"][-1]:.2f}')
print(f'IBOV: {carteira["IBOV"][-1]:.2f}')
print('-=' * 20)