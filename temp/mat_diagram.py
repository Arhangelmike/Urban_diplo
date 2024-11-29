from settins1 import *


# создаем область под график
fig, ax = plt.subplots(figsize=(15,10))
# список расстояний отступа элементов диаграмммы
explode_val = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
# подготавливаем данные для построения по ним диаграммы
#  значение уникальных названий валют
y = unique_codes
# сгруппировать суммы по валютам и округлить их
x = round(df.groupby('letter_code')['rate'].sum(), 2)
# отсортировать и выбрать первые 10 из получившегося набора
data_sorted = x.sort_values(ascending=False)
top_10 = data_sorted[:10]
# подготовить диаграмму для отображения
plt.pie(top_10, labels=top_10.index, autopct='%2.2f%%', shadow = True, explode = explode_val)
#  подписать оси и названияя
plt.ylabel('Доли сумм объемов купленных  Топ 10')
plt.title('Графики валют')
#  вывести данные не в процентах, а в числовом эквиваленте
plt.legend(top_10, labels=top_10, loc="upper right")
#  отрисовать диаграмму
plt.show()


