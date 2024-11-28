from settins1 import *


fig = go.Figure(data=[go.Candlestick(x=df2['date'],
                open=df2['open'], high=df2['high'],
                low=df2['low'], close=df2['close'])
                     ])

fig.update_layout(xaxis_rangeslider_visible=False)
fig.show()