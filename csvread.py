import pandas as pd
import matplotlib.pyplot as plt

# чтение файла с данными
df = pd.read_csv('csv/data_182small.csv', sep=';', parse_dates=['date'], dayfirst=True)
# подготовка данных для их отрисовки с помощью pandas
df['rate'] = round(df['rate'], 2)
df['date'] = pd.to_datetime(df['date'])
unique_codes = df['letter_code'].unique()

# подготовка слоя для отображения графика
plt.figure(figsize=(20, 12))
# подготовка данных для отрисовки графиков
for code in unique_codes:
    currency_data = df[df['letter_code'] == code]
    # выбор типа графика и передача данных в него
    plt.plot(currency_data['date'], currency_data['rate'], label=code)
# подпись осей и графика
plt.xlabel('Дата')
plt.ylabel('Курс')
plt.title('Графики курсов валют')
plt.grid()
# команда вывода получившегося граика
plt.show()
