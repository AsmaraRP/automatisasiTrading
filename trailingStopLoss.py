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

# Strategy Trailling Stop Los


def strategy(entry, loockback, qty, open_position=False):
    while True:
        df = pd.read_sql(pair, engine)
        lookbackperiod = df.iloc[-lookback:]
        cumret = (lookbackperiod.Price.pct_change() + 1).cumprod() - 1
        if cumret[cumret.last_valid_index() < entry]:
            order = client.create.order(symbol=pair, side='BUY',
                                        type='MARKET', quantity=qty)
            print(order)
            open_position = True
        # STOP LOSS PART
    if open_position:
        while True:
            df = pd.read_sql(f"""SELECT * FROM {pair} WHERE \
            Time >= '{pd.to_datetime(order['transactTime'], unit='ms')}'""", engine)
            df['Benchmark'] = df.Price.cummax()
            df['TSL'] = df.Benchmark * 0.995
            if df[df.Price < df.TSL].first_valid_index():
                order = client.create.order(symbol=pair, side='SELL',
                                            type='MARKET', quantity=qty)

                print(order)
                break
