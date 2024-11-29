from settins1 import *


#подготовка области для вывода графика
sns.set(rc={'figure.figsize':(18, 12)}, style='whitegrid')
def seaborn_lineplot():
    sns.lineplot(
        x="date",
        y="rate",
        hue='letter_code',
        legend = 'full',
        data=df)
    # вывести график на экран
    plt.show()
    # подсказка legend = “auto”, “brief”, “full”, or False
#_------------------------------------------------
def seaborn_scatterplot():
    # извлекаем 5 случайных имен валют
    currency_list = random.sample(letter, 5)
    # получаем облегченный датафрейм только с нужными валютами
    filtered_df = df[df['letter_code'].isin(currency_list)]
    #  Готовим данные для осей
    x1 = filtered_df[filtered_df['letter_code'].isin(currency_list)]['date']
    y1 = filtered_df[filtered_df['letter_code'].isin(currency_list)]['rate']
    # готовим график для визуализации
    sns.scatterplot(x=x1, y=y1, hue=df['letter_code'], marker="x", s=3, legend =False)
    # вывести график на экран
    plt.show()
#_------------------------------------------------
def seaborn_facegridGR():
    # формируем отдельный датафрейм с отобранными валютами
    df1=df[df['letter_code'].isin(currency_list)]
    # обрезать даты
    df1=df1.set_index(pd.to_datetime(df1['date'])).loc['2018-01-01':'2018-05-31'].reset_index(drop=True)
    # обозначить количество столцов на вывод
    g = sns.FacetGrid(df1, col='letter_code',  col_wrap=6, height=2.0)
    # подготовить к выводу сам график
    g.map_dataframe(sns.lineplot, "date", "rate", marker=".", color="red")
    # вывести готовый график
    plt.show()
#
def seaborn_heatmap():
    # обрезать даты
    df1=df.set_index(pd.to_datetime(df['date'])).loc['2018-01-01':'2018-04-28'].reset_index(drop=True)
    # обрезать число валют
    currency_list_s = random.sample(list(df['letter_code'].unique()), 10)
    # отобрать для работы в новый датафрейм те строки где есть отобранная валюта
    df2=df1[df1['letter_code'].isin(currency_list_s)]

    glue = df2.pivot(index="date", columns="letter_code", values="rate")
    sns.heatmap(glue.corr(), square=True, annot=True, fmt='.2g', vmin=0, vmax=1,
                center=0, cmap='viridis',  cbar_kws={'orientation': 'horizontal'})
    plt.show()

# _------------------------------------------------
def seaborn_boxplot():
    # прочесть файл и создать датафрейм из csv указав какие  столбцы нужны (данных много,для ускорения работы программы)
    df_test = pd.read_csv('csv/data_182small.csv', usecols=['letter_code', 'date', 'rate'], sep=';')
    # собрать данные в серию каждой валюте соответствует среднее значение за весь период
    mean_rate = df_test.groupby('letter_code').agg({'rate': 'mean'}).reset_index()
    # собрать данные в серию для валют со значением  больше среднего значения
    mean_rate_1 = mean_rate[
        mean_rate['letter_code'].isin(mean_rate[mean_rate['rate'] > mean_rate['rate'].mean()]['letter_code'])]
    # собрать данные в серию для валют со значением  меньше среднего значения
    mean_rate_2 = mean_rate[
        mean_rate['letter_code'].isin(mean_rate[mean_rate['rate'] <= mean_rate['rate'].mean()]['letter_code'])]
    # выделить из основного датафрейма строки которые собержат имя валюты со значением больше среднего
    df_test_1 = df_test[df_test['letter_code'].isin(mean_rate_1['letter_code'])]
    # Подготовить область под отрисовку графика размером 20 на 15
    plt.figure(figsize=(20, 15))
    # отрисовать графмк
    sns.boxplot(x='letter_code', y='rate', data=df_test_1, hue='letter_code', legend=False)
    # Вывести график
    plt.show()

    plt.figure(figsize=(20, 15))
    # выделить из основного датафрейма строки которые собержат имя валюты со значением меньше среднего
    df_test_2 = df_test[df_test['letter_code'].isin(mean_rate_2['letter_code'])]
    # Подготовить область под отрисовку графика размером 20 на 15
    # отрисовать графмк
    sns.boxplot(x='letter_code', y='rate', data=df_test_2, hue='letter_code', legend=False)
    # Вывести график
    plt.show()

# seaborn_boxplot()
# seaborn_facegridGR()
# seaborn_heatmap()
# seaborn_lineplot()
# seaborn_scatterplot()

