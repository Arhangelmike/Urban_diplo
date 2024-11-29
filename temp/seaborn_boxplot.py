from settins1 import *

# прочесть файл и создать датафрейм из csv указав какие  столбцы нужны (данных много,для ускорения работы программы)
df_test = pd.read_csv('csv/data_182small.csv', usecols=['letter_code', 'date', 'rate'], sep=';')
# print(df_test.head(5))
# собрать данные в серию каждой валюте соответствует среднее значение за весь период
mean_rate = df_test.groupby('letter_code').agg({'rate':'mean'}).reset_index()
# собрать данные в серию для валют со значением  больше среднего значения
mean_rate_1 = mean_rate[mean_rate['letter_code'].isin(mean_rate[mean_rate['rate'] > mean_rate['rate'].mean()]['letter_code'])]
# собрать данные в серию для валют со значением  меньше среднего значения
mean_rate_2 = mean_rate[mean_rate['letter_code'].isin(mean_rate[mean_rate['rate'] <= mean_rate['rate'].mean()]['letter_code'])]
# выделить из основного датафрейма строки которые собержат имя валюты со значением больше среднего
df_test_1 = df_test[df_test['letter_code'].isin(mean_rate_1['letter_code'])]
# Подготовить область под отрисовку графика размером 20 на 15
plt.figure(figsize=(20,15))
# отрисовать графмк
sns.boxplot(x='letter_code', y='rate', data=df_test_1, hue='letter_code', legend=False)
#
# Вывести график
plt.show()

plt.figure(figsize=(20,15))
# выделить из основного датафрейма строки которые собержат имя валюты со значением меньше среднего
df_test_2 = df_test[df_test['letter_code'].isin(mean_rate_2['letter_code'])]
# Подготовить область под отрисовку графика размером 20 на 15

# отрисовать графмк
sns.boxplot(x='letter_code', y='rate',data=df_test_2, hue='letter_code', legend=False)
# Вывести график
plt.show()
