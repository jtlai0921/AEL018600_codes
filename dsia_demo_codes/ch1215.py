import requests
import datetime
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

def get_ohlc(twse_ticker):
  """
  Get ohlc data for current month
  """
  today = datetime.datetime.today().strftime('%Y%m%d')
  twse_url = "http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date={}&stockNo={}".format(today, twse_ticker)
  stock = requests.get(twse_url).json()
  trading_dates = []
  opens = []
  highs = []
  lows = []
  closes = []
  for i in range(len(stock["data"])):
    trading_dates.append(stock["data"][i][0])
    opens.append(float(stock["data"][i][3]))
    highs.append(float(stock["data"][i][4]))
    lows.append(float(stock["data"][i][5]))
    closes.append(float(stock["data"][i][6]))

  trading_dates_year = [str(int(td.split("/")[0]) + 1911) for td in trading_dates]
  trading_dates_month = [td.split("/")[1] for td in trading_dates]
  trading_dates_day = [td.split("/")[2] for td in trading_dates]
  trading_dates = ["{}-{}-{}".format(yr, m, d) for yr, m, d in zip(trading_dates_year, trading_dates_month, trading_dates_day)]
  trading_dates = pd.to_datetime(trading_dates)
  df = pd.DataFrame()
  df["trading_date"] = trading_dates
  df["open"] = opens
  df["high"] = highs
  df["low"] = lows
  df["close"] = closes
  df = df.set_index("trading_date")
  return df

tsmc = get_ohlc('2330')
py.sign_in('USERNAME', 'APIKEY') # Use your own plotly Username / API Key
trace = go.Candlestick(x=tsmc.index,
                       open=tsmc["open"],
                       high=tsmc["high"],
                       low=tsmc["low"],
                       close=tsmc["close"])
layout = go.Layout(
    xaxis = dict(
        rangeslider = dict(
            visible = False
        )
    )
)
data = [trace]
fig = go.Figure(data=data,layout=layout)
py.iplot(fig, filename='simple_candlestick')