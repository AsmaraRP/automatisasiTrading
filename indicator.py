import pandas_datareader.data as reader
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Get BTC
start2 = dt.date(2022, 3, 18)
end2 = dt.date(2022, 4, 20)
crypto = ['BTC-USD']
df_b = reader.get_data_yahoo(crypto, start2, end2)
# df_b.drop('High', inplace=True, axis=1)
# df_b.drop('Open', inplace=True, axis=1)
# df_b.drop('Low', inplace=True, axis=1)
# df_b.drop('Adj Close', inplace=True, axis=1)
# df_b["Harga"] = df_b["Close"].values
df_b

# VWAP

# Moving Average
df_b['MA30'] = df_b['Close'].rolling(30).mean()
df_b['MA90'] = df_b['Close'].rolling(90).mean()
# remove data
df_b = df_b.dropna()
df_b.drop('Regresi', inplace=True, axis=1)
df_b.drop('Regresi-', inplace=True, axis=1)
df_b.drop('Regresi+', inplace=True, axis=1)
df_b.drop('test', inplace=True, axis=1)
df_b

# MA cross
# golden cros dan death cross
# RSI
# RSI BTC
# MACD
