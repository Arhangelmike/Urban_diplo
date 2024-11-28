from settins1 import *


dfA = pd.DataFrame({
    "Price": df['rate'],
    "Years": df['date'],
    "Currency": df['letter_code']
})

currencies = dfA['Currency'].unique()

fig = go.Figure()
for idx, currency in enumerate(currencies):
    filtered_data = dfA[dfA['Currency'] == currency]
    fig.add_trace(
        go.Scatter(x=filtered_data["Years"], y=filtered_data["Price"], name=currency),
    )

fig.update_layout(
    # height=400 * n_rows,
    title="Мультиграфики по валютам",
    showlegend=True  # Скрыть легенду, если она не нужна
)
fig.show()
