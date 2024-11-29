from settins1 import *


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

