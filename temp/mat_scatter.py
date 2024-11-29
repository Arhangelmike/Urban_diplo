from settins1 import *

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
        continue
