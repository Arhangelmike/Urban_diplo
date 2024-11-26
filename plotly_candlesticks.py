import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('csv/candle_sample.csv', sep=',' )
df = df[['date', 'open', 'high', 'low', 'close']]

fig = go.Figure(data=[go.Candlestick(x=df['date'],
                open=df['open'], high=df['high'],
                low=df['low'], close=df['close'])
                     ])

fig.update_layout(xaxis_rangeslider_visible=False)
fig.show()