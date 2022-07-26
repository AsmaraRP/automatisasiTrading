import pandas as pd
import numpy as np
import pandas as pd
import sqlalchemy
from binance.client import Client
from binance import BinanceSocketManager
import api_key from "./binance_apiKey.ipynb"
import api_secret from "./binance_apiKey.ipynb"
# Get data BTC dari Big Data

# Get BTC dari Binance
client = Client(api_key, api_secret)
bsm = BinanceSocketManager(client)
socket = bsm.trade_socket('BTCUSDT')

while True:
    await socket._aenter_()
    msg = await socket.recv()
    frame = createframe(msg)
    frame.to_sql('BTCUSDT', engine, if_exists='append', index=False)
    print frame


def createframe(msg):
    df = pd.DataFrame([msg])
    df = df.loc[:, ['s', 'E', 'p']]
    df.columns = ['symbol', 'Time', 'Price']
    df.Price = df.Price.astype(float)
    df.Time - pd.to_datetime(df.Time, unit='ms')
    return df

# VWAP
# Moving Average
# Moving Average 30, 90, 200
# MA cross
# golden cros dan death cross
# RSI
# RSI BTC
# MACD
