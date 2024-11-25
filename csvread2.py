import seaborn as sns
import pandas as pd
import random
import matplotlib.pyplot as plt


df = pd.read_csv('csv/data_182small.csv', sep=';', parse_dates=['date'], dayfirst=True)
unique_codes = df['letter_code'].unique()
# для разных графиков нужны данные в формате списка, а некоторым не нужны
currency_list = list(unique_codes)
df['rate'] = round(df['rate'], 2)
df = df.dropna()
# размер выводимого графика
sns.set(rc={'figure.figsize':(18, 12)}, style='whitegrid')
sns.set_theme(style="whitegrid")

# sns.lineplot(
#     x="date",
#     y="rate",
#     hue='letter_code',
#     legend = 'brief',
#     data=df)
# plt.show()
# legend = “auto”, “brief”, “full”, or False
#_------------------------------------------------
# currency_list = random.sample(unique_codes, 5)
# currency_list = list(unique_codes)
# filtered_df = df[df['letter_code'].isin(currency_list)]
# x1 = filtered_df[filtered_df['letter_code'].isin(currency_list)]['date']
# y1 = filtered_df[filtered_df['letter_code'].isin(currency_list)]['rate']
#
#
# sns.scatterplot(x=x1, y=y1, hue=df['letter_code'], marker="x", s=3, legend =False)
#_------------------------------------------------
# currency_list = list(unique_codes)
# df1=df[df['letter_code'].isin(currency_list)]
# # обрезать даты
# df1=df1.set_index(pd.to_datetime(df1['date'])).loc['2018-01-01':'2018-01-31'].reset_index(drop=True)
# g = sns.FacetGrid(df1, col='letter_code',  col_wrap=10, height=2.0)
# g.map_dataframe(sns.lineplot, "date", "rate", marker=".")
# plt.show()
#_------------------------------------------------
# currency_list = list(unique_codes)
# # обрезать число валют
# df1=df[df['letter_code'].isin(currency_list)]
# # обрезать даты
# df1=df1.set_index(pd.to_datetime(df1['date'])).loc['2018-01-01':'2018-01-31'].reset_index(drop=True)
# sns.pairplot(df1)
# plt.show()
#_------------------------------------------------
# currency_list = list(unique_codes)
# # обрезать число валют
# df1=df[df['letter_code'].isin(currency_list)]
# # обрезать даты
# df1=df1.set_index(pd.to_datetime(df1['date'])).loc['2018-01-01':'2018-01-31'].reset_index(drop=True)
# sns.histplot(x='rate', kde=True, data=df1)
# plt.show()
#_------------------------------------------------
# currency_list = list(unique_codes)
# currency_list = random.sample(currency_list, 8)
# # обрезать число валют
# df1=df[df['letter_code'].isin(currency_list)]
# # обрезать даты
# df1=df1.set_index(pd.to_datetime(df1['date'])).loc['2018-01-01':'2018-03-28'].reset_index(drop=True)
# #  отображения сгруппированных скрипичных диаграмм
# sns.violinplot(data=df1, x='letter_code', y="date", hue ="rate")
# plt.show()
#_------------------------------------------------
def raaa():
    r = random.random()
    return r
# обрезать даты
df=df.set_index(pd.to_datetime(df['date'])).loc['2020-01-01':'2020-07-30'].reset_index(drop=True)
# обрезать число валют
df1 = df[df['letter_code'] == 'JPY']
# print(df1.head(10))

df_temp = pd.DataFrame(columns=['open'])
for i in range(len(df1)):
    r=raaa()
    # print(r)
    df_temp.loc[i] = [round(r, 2)]

    # print(type(df_temp))
df1.reset_index(drop=True, inplace=True)
m_df = pd.concat([df1, df_temp], axis=1)
m_df['min'] =  round(m_df['rate']*m_df['open'], 2)
m_df['max'] =  round(m_df['rate']/m_df['open'], 2)
m_df.to_csv( 'csv/m_df.csv', sep=';', encoding='utf-8', index=False, header=True)
# print(df1.head(10))
print(m_df.head(10))
sns.boxplot(x='letter_code', y='date', data=m_df, hue='rate', palette='Set2')
plt.show()
#_------------------------------------------------
# # обрезать даты
# df=df.set_index(pd.to_datetime(df['date'])).loc['2018-01-01':'2018-04-28'].reset_index(drop=True)
# print(len(df['letter_code'].unique())) # проверить сколько переменных попадает в построение графика
# # обрезать число валют
# currency_list_s = random.sample(list(df['letter_code'].unique()), 10)
# # отобрать для работы в новый датафрейм те строки где есть отобранная валюта
# df1=df[df['letter_code'].isin(currency_list_s)]
# print(len(df1['letter_code'].unique()))
#
#
# glue = df1.pivot(index="date", columns="letter_code", values="rate")
# sns.heatmap(glue.corr(), square=True, annot=True, fmt='.2g',vmin=0, vmax=1,
#             center=0, cmap='viridis',  cbar_kws={'orientation': 'horizontal'})
# plt.show()