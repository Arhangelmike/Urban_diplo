import seaborn as sns
import pandas as pd
import random
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.dates as mpdates

import plotly.graph_objects as go
import plotly.graph_objs as go
import plotly.offline as offl

import cufflinks as cf
from plotly.tools import FigureFactory as FF
from mplfinance.original_flavor import candlestick_ohlc

# читаем из первого файла только нужные столбцы
df = pd.read_csv('csv/data_182small.csv', sep=';', usecols=['letter_code', 'date', 'rate'],
                 parse_dates=['date'], dayfirst=True)
# получаем список уникальных имен валют
unique_codes = df['letter_code'].unique()
# для разных графиков нужны данные в формате списка
currency_list = list(unique_codes)
df['rate'] = round(df['rate'], 2)
df['date'] = pd.to_datetime(df['date'])
df = df.dropna()
# читаем из второго файла только нужные столбцы
df2 = pd.read_csv('csv/candle_sample.csv', sep=',', usecols=['date', 'open', 'high',  'low',  'close', 'volume'],
                 parse_dates=['date'], dayfirst=True)
df2['date'] = pd.to_datetime(df2['date'])