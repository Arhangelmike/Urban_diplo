from settins1 import *


# #_------------------------------------------------
def plotly_boxGR():
    fig = px.box(df, x="letter_code", y="rate", color='letter_code',
                 color_discrete_sequence= px.colors.sequential.matter,)
    fig.show()

# #_------------------------------------------------
def plotly_pieGR():
    df_1 = df[df['letter_code'].isin(df[df['rate'] > 30]['letter_code'])]
    fig = px.pie(df_1, values=df_1.rate, names="letter_code",
                 title='Количество проданной валюты')
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.show()
# #_------------------------------------------------stacked bar carts
def plotly_barGR():
    # нарисовать график
    fig=px.bar(df, x='date', y='rate',  title="Курсы валют", color = 'letter_code', hover_name='letter_code')
    # наложить на каждый столбец все столбцы других валют другим цветом
    fig.update_layout(bargroupgap=False, barmode="stack" )
    # показать график
    fig.show()
# #_------------------------------------------------candle
def plotly_candleGR():
    fig = go.Figure(data=[go.Candlestick(x=df2['date'],
                    open=df2['open'], high=df2['high'],
                    low=df2['low'], close=df2['close'])
                         ])
    fig.update_layout(xaxis_rangeslider_visible=False)
    fig.show()
# #_------------------------------------------------3dScater
def plotly_scetter3dGR():
    z_data = df2.volume
    x_data = df2.open
    y_data = df2.close

    # # Создание 3D графика
    trace = go.Scatter3d(
        x=x_data,
        y=y_data,
        z=z_data,
        mode='markers',  # Режим отображения: только маркеры
        marker=dict(
            size=5,
            color=z_data,  # Цвет маркеров на основе координаты Z
            colorscale='burg',  # Цветовая шкала
            opacity=0.8
        ),
        name='3D Рассеяние'
    )

    # Создание макета
    layout = go.Layout(
        title='3D рассеивания ',
        scene=dict(
            xaxis=dict(title='Ось X'),
            yaxis=dict(title='Ось Y'),
            zaxis=dict(title='Ось Z')
        )
    )

    # Создание фигуры
    fig = go.Figure(data=[trace], layout=layout)
    fig.show()




plotly_boxGR()
plotly_pieGR()
plotly_barGR()
plotly_candleGR()
plotly_scetter3dGR()