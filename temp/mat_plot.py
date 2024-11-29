from settins1 import *


# формируем подложку графика
fig, ax = plt.subplots(figsize=(15,8))
# для каждой валюты создаем график
for code in unique_codes:
    currency_data = df[df['letter_code'] == code]
    plt.plot(currency_data['date'], currency_data['rate'], label=code)

#  подписываем оси и график
plt.xlabel('Дата')
plt.ylabel('Курс')
plt.title('Графики курсов валют')
plt.grid()
# отобразить график
plt.show()
