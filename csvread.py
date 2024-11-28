from settins1 import *

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
