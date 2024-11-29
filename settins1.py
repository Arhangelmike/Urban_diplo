import seaborn as sns
import pandas as pd
import random
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.dates as mpdates

import plotly.graph_objects as go
import plotly.graph_objs as go
import plotly.offline as offl
import plotly.express as px

import cufflinks as cf
from plotly.tools import FigureFactory as FF
from mplfinance.original_flavor import candlestick_ohlc

# читаем из первого файла только нужные столбцы
df = pd.read_csv('csv/data_182small.csv', sep=';', usecols=['letter_code', 'date', 'rate'],
                 parse_dates=['date'], dayfirst=True)
# получаем список уникальных имен валют
unique_codes = df['letter_code'].unique()
# для разных графиков нужен списк имен валют
currency_list = list(unique_codes)
# Округлим до второго знака после запятой значения цены
df['rate'] = round(df['rate'], 2)
df['date'] = pd.to_datetime(df['date'])
# удалить строки с пустыми параметрами
df = df.dropna()



# читаем из второго файла только нужные столбцы
df2 = pd.read_csv('csv/candle_sample.csv', sep=',', usecols=['date', 'open', 'high',  'low',  'close', 'volume'],
                 parse_dates=['date'], dayfirst=True)
df2['date'] = pd.to_datetime(df2['date'])



# готовим лист всех валют, можно и через df['letter_code'].unique()
letter = ['AUD', 'BGN', 'HUF', 'DKK', 'USD', 'INR', 'CAD', 'CNY', 'NOK', 'PLN', 'SGD',
          'TRY', 'FRF', 'GBP', 'SEK', 'CHF', 'JPY', 'XDR', 'DEM', 'ATS', 'BEF', 'GRD', 'IEP',
          'ISK', 'ESP', 'ITL', 'NLG', 'PTE', 'TRL', 'FIM', 'XEU', 'EEK', 'LVL', 'LTL', 'KZT',
          'KGS', 'MDL', 'BYB', 'CZK', 'UZS', 'AZM', 'AMD']
# готовим лист цветов
colorlist=['aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure',
            'beige', 'bisque', 'black', 'blanchedalmond', 'blue',
            'blueviolet', 'brown', 'burlywood', 'cadetblue',
            'chartreuse', 'chocolate', 'coral', 'cornflowerblue',
            'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan',
            'darkgoldenrod', 'darkgray', 'darkgrey', 'darkgreen',
            'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange',
            'darkorchid', 'darkred', 'darksalmon', 'darkseagreen',
            'darkslateblue', 'darkslategray', 'darkslategrey',
            'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue',
            'dimgray', 'dimgrey', 'dodgerblue', 'firebrick',
            'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro',
            'ghostwhite', 'gold', 'goldenrod', 'gray', 'grey', 'green',
            'greenyellow', 'honeydew', 'hotpink', 'indianred', 'indigo',
            'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen',
            'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan']
#


