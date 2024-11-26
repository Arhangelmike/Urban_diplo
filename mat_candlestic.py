import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import pandas as pd
import matplotlib.dates as mpdates
# назначаем цветовую гамму
plt.style.use('fivethirtyeight')

# читаем из файла данные  и второй строкой обрезаем те серии данных что не нужны
df = pd.read_csv('csv/candle_sample.csv', sep=',' )
df = df[['date', 'open', 'high', 'low', 'close']]

# нормализуем отображение времени
df['date'] = pd.to_datetime(df['date'])

# преобразует значения столбца «Дата» в датафрейме df в числовые значение кол-ва дней
df['date'] = df['date'].map(mpdates.date2num)

# создаем область под график
fig, ax = plt.subplots(figsize=(20,15))

# функция candlestick_ohlcv для построения свечного графика,
# затем наложения данных с использованием встроенных возможностей matplotlib.
candlestick_ohlc(ax, df.values, width=0.6,
                 colorup='green', colordown='red',
                 alpha=0.8)

# показать сетку на графике
ax.grid(True)

# подпишем оси
ax.set_xlabel('Дата')
ax.set_ylabel('Цена')

# заголовок графика
plt.title('Цены за период 2017-08 to 2024-01')

# правим отображение даты на графике
date_format = mpdates.DateFormatter('%d-%m-%Y')
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate()

fig.tight_layout()

# отобразить график
plt.show()
