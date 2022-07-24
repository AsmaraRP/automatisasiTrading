import pandas as pd
import numpy as np
import pandas as pd
import sqlalchemy
from binance.client import Client
from binance import BinanceSocketManager
# %run ./binance_apiKey.ipynb
# Get data BTC dari Big Data

# Get BTC dari Binance
# client = Client(api_key, api_secret)
# bsm = BinanceSocketManager(client)
# socket = bsm.trade_socket('BTCUSDT')

# while True:
#     await socket._aenter_()
#     msg = await socket.recv()
#     frame = createframe(msg)
#     frame.to_sql('BTCUSDT', engine, if_exists='append', index=False)
#     print frame

# def createframe(msg):
#     df = pd.DataFrame([msg])
#     df = df.loc[:,['s','E','p']]
#     df.columns = ['symbol','Time', 'Price']
#     df.Price = df.Price.astype(float)
#     df.Time - pd.to_datetime(df.Time, unit='ms')
#     return df

# VWAP
# Moving Average
# Moving Average 30, 90, 200
# MA cross
# golden cros dan death cross
# RSI
# RSI BTC
# MACD

# Strategy Trend Following
# def strategy(entry, lookback, open_position=False):
#     while True:
#         df = pd.read.sql('BTCUSDT', engine)
#         lookbackperiod = df.iloc[-lookback:]
#         cumret = (lookbackperiod.Price.pct_change() + 1).cumprod()-1
#         if not open_position:
#             if cumret[cumret.last_valid_index()] > entry:
#                 order = client.create_order(
#                     symbol='BTCUSDT', side='BUY', type='MARKET', quantity=qty)
#                 print(order)
#                 open_position = True
#                 break
#     if open_position:
#         while True:
#             df = pd.read.sql('BTCUSDT', engine)
#             sincebuy = df.loc[df.Time > pd.to_datetime(
#                 order['transactTime'], unit='ms')]
#             if len(sincebuy) > 1:
#                 sincebuyret = (sincebuy.Price.pct_change()+1).cumprod() - 1
#                 last_entry = sincebuyret[sincebuyret.last_valid_index()]
#                 if last_entry > 0.0015 or last entry < -0.0015:
#                     order = client.create_order(
#                         symbol='BTCUSDT', side='SELL', type='MARKET', quantity=qty)
#                     print(order)
#                     break
# Strategy Trailling Stop Los
# def strategy(entry, loockback, qty, open_position=False):
#     while True:
#         df = pd.read_sql(pair,engine)
#         lookbackperiod = df.iloc[-lookback:]
#         cumret = (lookbackperiod.Price.pct_change() +1).cumprod() - 1
#         if cumret[cumret.last_valid_index() < entry]:
#             order = client.create.order(symbol=pair,side='BUY',
#                                         type='MARKET',quantity=qty)
#             print(order)
#             open_position = True
#         #STOP LOSS PART
#     if open_position:
#         while True:
#             df = pd.read_sql(f"""SELECT * FROM {pair} WHERE \
#             Time >= '{pd.to_datetime(order['transactTime'], unit='ms')}'""", engine)
#             df['Benchmark'] = df.Price.cummax()
#             df['TSL'] = df.Benchmark * 0.995
#             if df[df.Price < df.TSL].first_valid_index():
#                 order = client.create.order(symbol=pair,side='SELL',
#                                         type='MARKET',quantity=qty)

#                 print(order)
#                 break
