#!/usr/bin/python3

import pandas as pd



import sys
sys.path.insert(1, '../')
from exchange.binance import Binance
from strategies.strategies import Strategies
from plot.plot import chart
#import exchange


class tradeSigns():
  """
    docstring for tradeSigns

  """
  def __init__(self):
    self.exchange = Binance()
    self.chart = chart()


    self.param = [{"col_name" : "4_ema", 
                   "color"    : 'green', 
                   "name"     : "4_ema"},
                  {"col_name" : "9_ema", 
                   "color"    : 'yellow', 
                   "name"     : "9_ema"},
                  {"col_name" : "18_ema", 
                   "color"    : "red", 
                   "name"     : "18_ema"}]
    self.buy_signals = []
    self.sell_signals = []

  def sign(self, symbol:str, timeframe:str):
    """



    """

    df = self.exchange.GetSymbolKlines(symbol = symbol, interval = timeframe)
    df = self.exchange.technicalA(df)
    df["sign"] = ""
    entrypoint = 'off'
    for i in range(0, len(df['close'])-1):
      strategy_result = Strategies.marginTrade(df = df, step = i)

      if strategy_result['signal'] == 'BUY' and entrypoint == 'off':
        #print('buy: ',i)
        self.buy_signals.append([df['time'][i], df['low'][i]])
        df.loc[i, 'sign'] = 'buy'
        entrypoint = 'on'
      elif strategy_result['signal'] == 'SELL' and entrypoint == 'on':
        #print('sell: ',i)
        df.loc[i, 'sign'] = 'sell'
        self.sell_signals.append([df['time'][i], df['low'][i]])
        
        entrypoint = 'off'

    #print(self.sell_signals)
    self.chart.plotData(df, symbol, timeframe, self.param, self.buy_signals, self.sell_signals)





def Main():

  ts = tradeSigns()
  ts.sign("BTCUSDT", "5m")


if __name__ == '__main__':
  Main()

