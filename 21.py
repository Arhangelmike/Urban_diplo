from settins1 import *


# обрезать даты
# df=df.set_index(pd.to_datetime(df['date'])).loc['2020-01-01':'2020-07-30'].reset_index(drop=True)
# df.reset_index(drop=True, inplace=True)
# #_------------------------------------------------
# fig = px.box(df, x="letter_code", y="rate", color='letter_code',
#              color_discrete_sequence= px.colors.sequential.matter,)
# fig.show()

# #_------------------------------------------------
# df_1 = df[df['letter_code'].isin(df[df['rate'] > 30]['letter_code'])]
# fig = px.pie(df_1, values=df_1.rate, names="letter_code",
#              title='Количество проданной валюты')
# fig.update_traces(textposition='inside', textinfo='percent+label')
# fig.show()
# #_------------------------------------------------stacked bar carts

# colorlist=['aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure',
#             'beige', 'bisque', 'black', 'blanchedalmond', 'blue',
#             'blueviolet', 'brown', 'burlywood', 'cadetblue',
#             'chartreuse', 'chocolate', 'coral', 'cornflowerblue',
#             'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan',
#             'darkgoldenrod', 'darkgray', 'darkgrey', 'darkgreen',
#             'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange',
#             'darkorchid', 'darkred', 'darksalmon', 'darkseagreen',
#             'darkslateblue', 'darkslategray', 'darkslategrey',
#             'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue',
#             'dimgray', 'dimgrey', 'dodgerblue', 'firebrick',
#             'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro',
#             'ghostwhite', 'gold', 'goldenrod', 'gray', 'grey', 'green',
#             'greenyellow', 'honeydew', 'hotpink', 'indianred', 'indigo',
#             'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen',
#             'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan']
#
#
# fig=px.bar(df, x='date', y='rate',  title="Курсы валют", color = 'letter_code', hover_name='letter_code')
# fig.update_layout(bargroupgap=False, barmode="stack" )
# # show the figure
# fig.show()

# #_------------------------------------------------3dSurface
# обрезать даты
df=df.set_index(pd.to_datetime(df['date'])).loc['2018-01-01':'2018-04-28'].reset_index(drop=True)
print(len(df['letter_code'].unique())) # проверить сколько переменных попадает в построение графика
# обрезать число валют
currency_list_s = random.sample(list(df['letter_code'].unique()), 10)
# отобрать для работы в новый датафрейм те строки где есть отобранная валюта
df=df[df['letter_code'].isin(currency_list_s)]
print(len(df['letter_code'].unique()))



# corrmat = df2.corr(numeric_only=True)
z_data = df2.date
x_data = df2.close
y_data = df2.open
print(z_data.head(3))
print(x_data.head(3))
print(y_data.head(3))

# Создание теплокарты
heatmap  = go.Heatmap(z=['z_data','x_data'], colorscale='Blues')
# Создание макета
layout = go.Layout(title='Heatmap Example')

# Создание фигуры
fig = go.Figure(data=[heatmap], layout=layout)
# plot_data = [trace]
# offl.plot(plot_data, filename='Heatmap.html')

# fig = go.Figure(data=[go.Surface(z=z_data, x=x_data, y=y_data)])
# fig.update_layout(
#     title='3D Surface Plot',
#     scene=dict(
#         xaxis_title='Date',
#         yaxis_title='Open price',
#         zaxis_title='Max price'
#     )
# )
# fig.update_layout(autosize=True)

fig.show()