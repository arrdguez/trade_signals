import pandas as pd

from finta import TA


class Strategies:

  @staticmethod
  def marginTrade(df, step:int = 0):

    if  df['4_ema'][step] > df['9_ema'][step] and  df['9_ema'][step] > df['18_ema'][step]:
      if df['SIGNAL'][step] < df['MACD'][step] and df['open'][step] < df['close'][step]:
        return {"signal"   : "BUY"}
      return {"signal"   : "Red candle or the signal is over MACD"}


    elif df['4_ema'][step]< df['9_ema'][step]:
      if df['SIGNAL'][step] > df['MACD'][step]:
        return {"signal"   : "SELL"}
      return {"signal"    : "SELL"}

    else:
      return {"signal"   : "No sell, no buy, just wait!"}
