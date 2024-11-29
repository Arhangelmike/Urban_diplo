                                                                          **Дипломная работа**
                   *Сравнение различных библиотек для визуализации данных: Matplotlib, Seaborn и Plotly: Создать набор визуализаций 
                        с использованием Matplotlib, Seaborn и Plotly, сравнить их функциональность и удобство использования.*

                                                                             **Введение**

Сегодня самым ценным ресурсом в мире является уже не нефть, а данные. Визуализация становится все более важным инструментом для понимания миллиардов строк данных. Преобразуя данные в графическое представление, которое легко интерпретировать, визуализация данных помогает излагать историю данных, выделяя соответствующую информацию, закономерности и выбросы. Однако данные и графика должны работать вместе: это искусство объединения качественного анализа с отличным повествованием. 

Визуализация данных — это важный инструмент для анализа и представления информации. Python предлагает множество библиотек для создания разнообразных графиков, диаграмм и других визуализаций. 
Язык программирования Python часто используют аналитики данных. Для этого в нем существуют расширения — библиотеки, наборы готовых инструментов для более эффективной работы.
Визуализация данных, неотъемлемая часть науки о данных, представляет собой визуальное представление данных. Преобразовывая сложные наборы данных в более понятный графический формат, мы можем эффективно передавать идеи. Войдите в Python, мощный язык программирования, широко известный своим применением в науке о данных, благодаря своей простоте и широкому набору библиотек, предназначенных для обработки и визуализации данных.
Важность визуализации данных
Визуализация данных — это не модное дополнение, а необходимость. Это позволяет нам быстро интерпретировать данные и корректировать различные переменные, чтобы увидеть их влияние. Диаграммы и графики облегчают передачу данных, поскольку они могут эффективно рассказать историю. Python играет здесь решающую роль; его разнообразные библиотеки визуализации предоставляют инструменты для создания сложных и информативных изображений, помогая лучше анализировать данные и принимать решения.



Обоснование выбора темы.

В текущее время все больше и больше данных накапливает человечество, что порождает спрос на обработку, накопленной информации. Исходя из особенности человеческого восприятия и перефразируя поговорку: «Большое видится на расстоянии», другими словами большие объемы данных человек воспринимает лучше в графическом виде, давайте рассмотрим, как это реализуется на Python. 
И для начала приведем наиболее популярные инструменты для этого.  Так как данный вопрос очень интересен было принято решение выбрать данную тему диплома «Сравнение различных библиотек для визуализации данных: Matplotlib, Seaborn и Plotly».


Введение в библиотеки для визуализации на Python.
Python библиотеки для визуализации данных: Matplotlib, Seaborn и Plotly.
Python обладает большим числом библиотек для визуализации данных, предлагая инструменты для любых нужд. Эти библиотеки похожи на разные кисти, каждая со своим уникальным стилем и силой, готовые воплотить ваши данные в жизнь. Здесь мы обсудим три популярных:

1.	Matplotlib. Matplotlib часто считается основой визуализации данных в Python. Это универсальная библиотека. Несмотря на то, что это одна из старейших библиотек Python для этой цели, ее сила заключается в ее гибкости. Это позволяет вам полностью контролировать внешний вид ваших графиков, от простых линейных графиков до сложных трехмерных графиков. Matplotlib предлагает широкий спектр параметров настройки, что дает вам возможность создавать практически любую визуализацию.
2.	Seaborn: если Matplotlib — это огромный, красивый, но несколько пугающий лес, то Seaborn — это дружелюбный проводник, который проведет вас через него. Seaborn построен на основе Matplotlib, предлагая более удобный интерфейс и эстетическое улучшение. Он специализируется на статистической визуализации, что позволяет легко создавать привлекательные и информативные статистические графики. От простых точечных диаграмм до сложных тепловых карт Seaborn предлагает упрощенный подход к сложной визуализации.
3.	Plotly. В эпоху интерактивности Plotly сияет. Он позволяет создавать динамические и интерактивные визуальные эффекты, которые можно встраивать в веб-приложения или в отдельный HTML-код. Эта интерактивность предлагает новый уровень взаимодействия, позволяя пользователям масштабировать, панорамировать, наводить курсор и нажимать на графики для получения дополнительной информации. Plotly позволяет не только увидеть, но и испытать ваши данные.

   Дополнительно для упрощения работы с большими объемами данных применяют библиотеку Pandas, перед тем как отправить эти данные на визуализацию, формируя понятные и информативные графики и диаграммы. Pandas — популярная библиотека в Python для работы с данными. Её активно используют аналитики данных и ученые. 
Библиотека была создана в 2008 году компанией AQR Capital, а в 2009 году она стала проектом с открытым исходным кодом с поддержкой большого комьюнити, что и обеспечило ее популярность и дальнейшее развитие.

Данную библиотеку используют в таких областях как:
Аналитика данных: продуктовая, маркетинговая и другая. Работа с любыми данными требует анализа и подготовки: необходимо удалить или заполнить пропуски, отфильтровать, отсортировать или каким-то образом изменить данные. Pandas в Python позволяет быстро выполнить все эти действия, а в большинстве случаев ещё и автоматизировать их.
Data science и работа с большими данными. Pandas помогает подготовить и провести первичный анализ данных, чтобы потом использовать их в машинном или глубоком обучении.
Статистика. Библиотека поддерживает основные статистические методы, которые необходимы для работы с данными. Например, расчёт средних значений, их распределение по квантилям и другие.

И получившиеся результаты в дальнейшем проще визуализировать.


Возможно вы часто в последнее время слышите слова: котировки, биржа, фьючерсы и т. п., но если присмотреться, то с точки зрения программиста это будут наборы переменных числа, и строки. Причем эти данные могут как изменяться в реальном времени так и накапливаться где либо для дальнейшего анализа. Беря для примера график курса RUB-EUR мы получаем в случае упрощения набор на единичный график где у вас две координаты стоимость и дата, и он достаточно прост. Но что будет если взать более 30 пар валют и период времени не один два месяца, где количество данных будет небольшим. А период в несколько десятилетий, и при этом у нас возможны в данном наборе вариант, когда данные не полные на каком-то периоде, при недостатке данных и их переизбытке как поведут себя библиотеки для визуализации.
Возьмем наборы данных и проведём для него  набор визуализаций с использованием разных библиотек Matplotlib, Seaborn и Plotly, чтобы сравнить их функциональность и удобство использования. Возьмем набор из 320 тысяч строк и  более 30 валют их стоимость относительно рубля.
данные взяты с источника: https://data.rcsi.science/data-catalog/datasets/182/   (Инфраструктура научно-исследовательских данных - ИНИД - данные для всех)

Структура программы

![struckure](https://github.com/user-attachments/assets/8cff41b3-428e-48e5-b68b-f100f67b5a39)


Библиотека Matplotlib

Первое, что замечаешь при работе с таким объемом данных это требуемое время для обработки всех строк и при использовании данной библиотеки оно ощутимо, а второе - возникающие артефакты, связанные с неполнотой данных по отдельным валютам.

![image](https://github.com/user-attachments/assets/72028cb0-390f-4392-b1ee-2b99f3c3c64d)

Далее при попытке понять с чем связаны артефакты проводил эксперименты по изменению количества отображаемых данных. Например единичный график.


![image](https://github.com/user-attachments/assets/13b47dd3-06e5-4897-aea5-95f177d41c38)

Как видим отрисовывается без проблем что говорит, о том, что артефакты возникают не по причине отдельных данных
Вернув количество графиков, но оставив ограничение по времени отображения получили:


![image](https://github.com/user-attachments/assets/fdffef12-70e3-485c-88ac-d279c355003f)

Проведя анализ исходных данных получил результат: что качество исходных данных также требуется корректировать, отсеивать неполные данные, введя ограничение по периоду когда были данные по всем валютам 

![image](https://github.com/user-attachments/assets/74be3d8c-db9c-44fe-9628-11d8b874fda1)

Так же для ускорения работы с построением такого объема данных в виде графика в программу импортируем не всю библиотеку а только часть ее

import matplotlib.pyplot as plt

Так же при просмотре построенных данных мы моем получить более детальную информацию просто увеличив график не закрываю программу

![image](https://github.com/user-attachments/assets/e81efe85-fdda-4bce-b899-4c9c7f112de4)


Как видим мы наблюдаем по всем валютам рост стоимости валют в период с 2014-09 месяца по примерно 2016-03 месяц. Скорее всего в данный период возникли мировые события повлиявшие на стоимость валют, но скорее всего даже ранее, так как рынок имеет инерцию реагирования.

Далее мы рассмотрим другие типы гарфиков
Cоздание бар-график с использованием pandas чтением из csv файла, гистограмму не будем рассматривать, так как на наборе данных по валютным курсам она не совсем информационно обоснована (нам нет необходимости видеть частоту появления того или иного параметра). Хотя по большому счету визуально они очень похожи.


![bar carts restricted matplotlib](https://github.com/user-attachments/assets/47b2214c-09e5-441f-af9c-fd0c28ad0fc5)
На данном графике суммарное колебание более 30 пар валют, как видим не совсем информативно, поэтому введем ограничение на число пар и раскрасим. После длительных экспериментов с использованием данной библиотеки пришел к выводу что оптимальное число выводимых курсов колеблется от 3х до 5ти в зависимости от величины курса (должны быть сопоставимы в по размеру значений), а так же при попытке испольовать стакование "Баров" с данной библиотекой выяснено, что занимает формирование графика неоправданно много времени, так как временной период более 20 лет с данными по каждому дню.
Ниже приведен вариант графика 3х валют:
![matplotlib bar2](https://github.com/user-attachments/assets/1a941e5d-201c-4ba7-b712-45d412c43de3)


Так же достаточно информативно выглядит круговая диограмма:
![matplotlib circle diogramm 2](https://github.com/user-attachments/assets/8a4009c4-b471-441a-aac7-81bad8856659)

Также можно нарисовать график типа scatter без обработки и введения ограничений также не информативен
![matplotlib scatter2](https://github.com/user-attachments/assets/18f15854-23c1-4ec2-a9bf-92c0332d582d)


после ограничения до 10 пар валют


![matplotlib scatter3](https://github.com/user-attachments/assets/0034e7b6-ab92-44dc-889b-134ba2269538)

Так же довольно популярный график для биржевых сводок, когда он строиться по данным курса открытия закрытия максимума и минимума. (использовался набор данных для  1INCH — это агрегатор ликвидности криптовалюты,


![matplotlib_candlestick](https://github.com/user-attachments/assets/e9c165c6-3c49-49c2-ace2-3d34c03e100f)

![matplotlib_candlestick2](https://github.com/user-attachments/assets/650e32d9-7db4-4491-b257-8513d8002cc2)


Библиотека  Seaborn.

Начнем знакомство с библиотекой  Seaborn с предыдущего типа графиков. Посмотрим, как измениться отображение данных на графике диаграммы рассеяния (scatterplot), с использованием библиотеки более высокого уровня, но основанная на matplotlib в варианте все пары валют. 

![image](https://github.com/user-attachments/assets/b4c5cba9-0062-4237-b640-c3e345ae6932)

Как видим достаточно похоже выглядят графики в том числе и в увеличении

![image](https://github.com/user-attachments/assets/53dd9898-f387-484c-a36a-c8c41700a0f9)

Но как можно видеть при подкладывании полного объема данных с пробелами в данных артефактов стало меньше


![image](https://github.com/user-attachments/assets/7145f9ef-678d-48b1-bc2a-7abe0853668f)

Так же заметно что график отрисовывается быстрее, кода в программе меньше 16 строк против 23 строк с базовой библиотекой и он более читабельный.

Возьммем другой тип графика диаграмму рассеивания scatter. Сначала для всего набора данных.

![seab_scaterplot1](https://github.com/user-attachments/assets/52363465-53ba-4994-9eff-03213c6dd1e3)


А теперь более читаемого вида графика внесем изменения - уменьшим размер точки, сократим число пар до 10, поменяем вид маркера (что при маленьком значении размера добавит насыщенности графику)


![seab_scaterplot1 colored](https://github.com/user-attachments/assets/d9a91d0f-def4-4610-8df2-521c437ba53b)


Но для данного типа графика, все же многовато пар, в случае когда разница колебаний курсов валют сильно различаются то такие пары видны отчетливо а те что достаточно близки по значению начинают сливаться.


![seab_scaterplot1 colored_restrict](https://github.com/user-attachments/assets/e6ccad46-9600-4cc2-b0ce-b930a357a609)


Так же можно вывести групповой график Facegrid, но для данного набора данных несет не так много информации.


![seab_FacetGrid](https://github.com/user-attachments/assets/5991bd9a-53fe-462f-9f56-f5d700387be9)




Достаточно информативно смотриться построенный по текущему набору данных график типа heatmap, приведен график с корреляцией:


![seab_heatmap3](https://github.com/user-attachments/assets/85fdaef7-9fb3-48a6-b4b1-8becd1a86766)



Также можно привести достаточно непростой boxplot на двух картинках выведены графика для пар валют высокой стоимости и низкой стоимости.

![seab_boxplot_r1](https://github.com/user-attachments/assets/56890618-9163-4929-8ecd-b83b44f10476)

![seab_boxplot_r2](https://github.com/user-attachments/assets/a1a5a7f6-44fe-4621-98b0-24f8e14d0a64)







Библиотека Plotly

Работа с данной библиотекой сразу отличается от предыдущих библиотек, начиная, с того что формирует сразу из «коробки» график, не как окно, а как html документ, открывая в браузере как новую страницу с локальным адресом. А так же, всплывающими аннотациями при наведении курсора на точку графика. Plotly - это javascript -библиотека (plotly.js), построенная поверх D3.js - тоже javascript-библиотеки, которая заточена на отрисовку визуализаций в HTML-документах (читай web-страницах). А уже plotly.py - это python-библиотека,  которая взаимодействует с plotly.js и позволяет задавать различные параметры для наших чартов, что и делает  возможности визуализации гораздо более широкими и гибкими.
Есть два основных преимущества использования Plotly по сравнению с другими библиотеками Python, способными создавать графики, такими как Matplotlib и Seaborn. Это:


Простота использования - создание интерактивных графиков, 3D-графиков и другой сложной графики уместится всего в несколько строк кода. Сделать то же самое в других библиотеках потребует гораздо больше работы.

Больше возможностей - поскольку Plotly построен на основе D3.js, его возможности построения графиков намного больше, чем у аналогов. Финансовые, статистические, научные чарты, свечные диаграммы, гео-карты. На момент написания поста около 40 типов графиков доступно в Plotly

![image](https://github.com/user-attachments/assets/84bedb53-ea0e-424e-84a6-ab00b6014331)


Например при включении “легенды” можно управлять отображаем ли какой то из графиков нажатием на нужную легенду.



![image](https://github.com/user-attachments/assets/30e58e30-cbb9-498c-84f6-369eb1a7a68f)


При просмотре сырых данных видим, что данная библиотека, так же требует контроля изначальных данных, если данных на каком-то участке не хватает или есть где-то неупорядоченность данных.


![image](https://github.com/user-attachments/assets/3c47bb89-5d18-4c7c-98dd-7b09e8271c43)


Но что достаточно удобно в отличии от двух предыдущих библиотек мы наблюдаем результат выполнения и после закрытия программы


![image](https://github.com/user-attachments/assets/b6fd31bf-9532-423b-b31e-adfe3dc3a5ce)

В отличии от двух предыдущих библиотек, результат выполнения, с помощью которых, возможен, лишь при запущенной программе.

![image](https://github.com/user-attachments/assets/f8d7ff96-e7f5-4220-a030-df67e1617cc3)

Приведем еще варианты графиков - начнем со свечного графика

![plotly_candlestick](https://github.com/user-attachments/assets/f11fc1c4-d7b9-4750-b0cc-46fa893ffdab)

Увеличим его:

![plotly_candlesticks2](https://github.com/user-attachments/assets/1a09ae9b-e27e-4740-82f9-b787c389ee83)

Вариант boxplot 

![plotly_boxplot](https://github.com/user-attachments/assets/17f7be14-988b-4a83-82d3-c1f919fdb8de)

Гистограмма со стакующимся столбцами не требует на построение так много времени как другими библиотеками расммотренными здесь, и не потребовалоь ограничивать количество пар валют.

![plotly_bar_3](https://github.com/user-attachments/assets/97aafc70-ff89-49c7-ba10-9de38fd79f85)

Круговая диограмма так же не потребовала много сил на настройку
Варианты с разными выводами labels

![plotly_pie](https://github.com/user-attachments/assets/ce005ba1-9275-422a-b407-15b201ffdeca)

![plotly_pie2](https://github.com/user-attachments/assets/8a9d593c-a2ba-49b3-9023-a471c94fa639)

Также легко удалось отобразить диаграмму рассеивания в 3D


![plotly_scatter3D](https://github.com/user-attachments/assets/6c6059b4-0dcd-4f14-ad5e-f1850ae16fd6)





Анализ и интерпретация результатов.

Не смотря на то что для получения аналогичного графика для экспериментального сравнения удобства библиотек потребовалось 27 строк, время обработки данных близко к библиотеке Seaborn, и также быстрее обработала массив данных, чем matplotlib. Так же ощутимо отзывчивее при большом количестве данных на графике работает Plotly, увеличение и уменьшение маштаба графиков происходит ощутимо быстрее. Но при уменьшении количества визуализируемых данных ситуация выравнивается и скорость работы становиться не отличной друг от друга. 



Преимущества Matplotlib
Гибкость, можно настроить буквально всё, даже то, о чем вы не подозревали.
Мощность, если это можно нарисовать, Matplotlib это сделает.
Совместимость, работает везде, где есть Python.
Обширная, документация.
Большое сообщество, всегда найдется кто-то, кто уже решил вашу проблему.

Недостатки Matplotlib
Высокий порог вхожденения, требуется много знать и еще больше читать.
Многословность, для создания простого графика нужно написать много кода.
Устаревший дизайн по умолчанию, графики выглядят так, будто их создали в 90-х.
Необходимость ручной настройки, хотите красивый график? Готовьтесь потратить больше времени на стилизацию, чем на анализ данных.
Отсутствие встроенных статистических функций, для статистики придется привлекать дополнительные библиотеки.


Преимущества Seaborn
Эстетика, графики выглядят прилично даже без дополнительных настроек.
Простота использования, можно создать сложный график парой строк кода.
Статистические функции из коробки, встроенные возможности для визуализации статистических моделей.
Интеграция с pandas, работает с DataFrame без дополнительных настроек.
Автоматический выбор палитры, больше никаких споров о том, какой оттенок синего лучше подходит для вашего графика.

Недостатки Seaborn
Ограниченная кастомизация, хотите что-то сильно нестандартное? Готовьтесь к борьбе с библиотекой.
Зависимость от Matplotlib, под капотом всё равно старый добрый Matplotlib, со всеми его причудами.
Ограниченный набор графиков, для некоторых специфических типов визуализации придется возвращаться к Matplotlib.
Может быть медленнее на больших объемах данных, красота требует жертв, в данном случае — производительности.
Переусложненность для простых задач: использовать Seaborn для создания простого линейного графика не просто.


Преимущества Plotly:

Интерактивность. Plotly позволяет создавать графики с возможностью интерактивного взаимодействия, такого как увеличение, выбор данных по клику и прокрутка.
Широкие возможности. Plotly предлагает множество типов графиков и диаграмм для визуализации различных типов данных.
Хорошую документацию. У Plotly хорошо структурированная и подробная документация, что упрощает процесс изучения и использования библиотеки.
Поддержку различных платформ. Plotly может использоваться как в Jupyter Notebook, так и в веб-приложениях, что делает его удобным для разных сценариев использования.

Недостатки Plotly::

Иногда требуется дополнительное время на настройку, высокий порог вхождения. Настройка определенных аспектов графиков в Plotly может потребовать дополнительных усилий и времени для достижения желаемого результата.
Стоимость. Некоторые функции Plotly недоступны без платной версии.




















