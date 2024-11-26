import plotly.express as px
import pandas as pd


df = pd.read_csv('csv/data_182small.csv', sep=';', usecols=['letter_code', 'date', 'rate'],
                 parse_dates=['date'], dayfirst=True)
df = df.dropna()
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