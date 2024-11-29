from settins1 import *

#_____________________________________________________________matplotlib
#_____________________________________________________________matplotlib -  plot
def mat_plotGR():
    # подготовка слоя для отображения графика
    plt.figure(figsize=(20, 12))
    # подготовка данных для отрисовки графиков
    for code in unique_codes:
        currency_data = df[df['letter_code'] == code]
        # выбор типа графика и передача данных в него
        plt.plot(currency_data['date'], currency_data['rate'], label=code)
    # подпись осей и графика
    plt.xlabel('Дата')
    plt.ylabel('Курс')
    plt.title('Графики курсов валют')
    plt.grid()
    # команда вывода получившегося граика
    plt.show()

#_____________________________________________________________matplotlib
#_____________________________________________________________matplotlib -  bar
def mat_barGR():

    #  подготовка области под график
    plt.figure(figsize=(15, 8))
    #  отбираем данные для построения курсов
    df1 = df.set_index(pd.to_datetime(df['date'])).loc['2010-01-01':'2010-05-31'].reset_index(drop=True)
    #  рисуем график перед выводом
    df1.groupby('letter_code')['date'].nunique().plot(kind='bar', stacked=True, legend=False, color=colorlist)

    #  подписываем
    plt.xlabel('Сокращенное название валюты')
    plt.ylabel('Курс')
    plt.title('Максимальное значение для каждого курс за период 2010-01-01:2010-05-31')
    plt.grid()
    #  отображаем график
    plt.show()

#_____________________________________________________________matplotlib
#_____________________________________________________________matplotlib -  candlestick_ohlc
def mat_candleGR():
    # назначаем цветовую гамму
    plt.style.use('fivethirtyeight')
    # преобразует значения столбца «Дата» в датафрейме df в числовые значение кол-ва дней
    df2['date'] = df2['date'].map(mpdates.date2num)
    # создаем область под график
    fig, ax = plt.subplots(figsize=(20,15))
    # функция candlestick_ohlcv для построения свечного графика,
    # затем наложения данных с использованием встроенных возможностей matplotlib.
    candlestick_ohlc(ax, df2.values, width=0.6,
                     colorup='green', colordown='red',
                     alpha=0.8)
    # показать сетку на графике
    ax.grid(True)
    # подпишем оси
    ax.set_xlabel('Дата')
    ax.set_ylabel('Цена')
    # заголовок графика
    plt.title('Цены за период 2017-08 to 2024-01')
    # правим отображение даты на графике
    date_format = mpdates.DateFormatter('%d-%m-%Y')
    ax.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()
    fig.tight_layout()
    # отобразить график
    plt.show()


#_____________________________________________________________matplotlib
#_____________________________________________________________matplotlib - pie
def mat_pieGR():
    # создаем область под график
    fig, ax = plt.subplots(figsize=(15,10))
    # список расстояний отступа элементов диаграмммы
    explode_val = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
    # подготавливаем данные для построения по ним диаграммы
    #  значение уникальных названий валют
    y = unique_codes
    # сгруппировать суммы по валютам и округлить их
    x = round(df.groupby('letter_code')['rate'].sum(), 2)
    # отсортировать и выбрать первые 10 из получившегося набора
    data_sorted = x.sort_values(ascending=False)
    top_10 = data_sorted[:10]
    # подготовить диаграмму для отображения
    plt.pie(top_10, labels=top_10.index, autopct='%2.2f%%', shadow = True, explode = explode_val)
    #  подписать оси и названияя
    plt.ylabel('Доли сумм объемов купленных  Топ 10')
    plt.title('Графики валют')
    #  вывести данные не в процентах, а в числовом эквиваленте
    plt.legend(top_10, labels=top_10, loc="upper right")
    #  отрисовать диаграмму
    plt.show()


#_____________________________________________________________matplotlib
#_____________________________________________________________matplotlib - scatter
def mat_scetterGR():
    # выбор 10-ти случайных валют из списка, для улучшения читаемости графика
    currency_list = random.sample(letter, 10)
    # делаем выборку из всего набора данных строк содержащих эти валюты
    filtered_df = df[df['letter_code'].isin(currency_list)]
    # из отсортированных данных выбираем два столбца дата и курс для построения графика
    x = filtered_df[filtered_df['letter_code'].isin(currency_list)]['date']
    y = filtered_df[filtered_df['letter_code'].isin(currency_list)]['rate']
    # создаем список цветов для окрашивания графиков разных валюют разными цветами
    colors=["#"+''.join([random.choice('0123456789ABCDEF') for i in range(6)])
           for j in range(10)]
    #создаем словарь цветов для передачи на отрисовку
    color_dic = dict(zip(currency_list, colors))


    # выбираем каокй вариант отрисовать для того чтобы не запускать программу каждый раз когда надо показать
    # как выглядит видоизмененный график
    while True:
        choise = int(input(
            f'Приветствую!. Выберите вид диаграммы рассеяния: \n1 - график с цветом.\n2 - график без цвета\n3 - график без цвета полный\n'))
        if choise == 1:
            # -------- цветной для 10 курсов валют
            '''	это метод создания графика, объединяющий инициализацию области для рисунка (fig) и осей (ax),
                на которых впоследствии будут отображаться данные.'''
            fig, ax = plt.subplots(figsize=(15, 8))
            '''строим график, который соединит точки и окрасит указаным набором цветов для каждой валюты'''
            plt.scatter(x, y, marker=".", s=1, c=filtered_df['letter_code'].map(color_dic))
            # подпишем ось Х
            plt.xlabel('Дата')
            # подпишем ось У
            plt.ylabel('Курс')
            # подпишем название графика
            plt.title('Графики курсов валют')
            plt.grid()
            plt.show()
            # --------
            continue
        if choise == 2:
            # -------- вывод для примера как выглядит график если его не окрашивать
            fig, ax = plt.subplots(figsize=(15, 8))
            plt.scatter(x, y, marker=".", s=1)
            plt.xlabel('Дата')
            plt.ylabel('Курс')
            plt.title('Графики курсов валют 10 без цвета')
            plt.grid()
            plt.show()
            # --------
            continue

        if choise == 3:
            # --------вывод графика для примера насколько не читаемый график если не сортировать его
            #
            fig, ax = plt.subplots(figsize=(15, 8))
            plt.scatter(df['date'], df['rate'], marker=".", s=1)
            plt.xlabel('Дата')
            plt.ylabel('Курс')
            plt.title('Графики курсов валют все без цвета')
            plt.grid()
            plt.show()
            # --------
            continue
        else:
            break

# mat_scetterGR()
# mat_pieGR()
# mat_candleGR()
# mat_plotGR()
# mat_barGR()