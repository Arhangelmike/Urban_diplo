from settins1 import *
from csvread import *
from csvread2 import *
from csvread3 import *



while True:
    choise = int(input(
        f'Приветствую!. Выберите вид диаграммы рассеяния: \n'
        f'1 - Библиотека Matplotlib.\n'
        f'2 - Библиотека Seaborn\n'
        f'3 - Библиотека Plotly\n'
        f'Для выхода из внутреннего меню, набрать число больше, чем максимальное, в меню\n'))
    if choise == 1:
        # -------- Библиотека Matplotlib
        while True:
            choise = int(input(
                f'Выберите: \n1 - scetterGR.\n2 - pieGR\n3 - candleGR\n4 - plotGR\n5 - barGR'))
            if choise == 1:
                # --------
                mat_scetterGR()
                # --------
                continue
            if choise == 2:
                # --------
                mat_pieGR()
                # --------
                continue

            if choise == 3:
                # --------
                mat_candleGR()
                # --------
                continue
            if choise == 4:
                # --------
                mat_plotGR()
                # --------
                continue
            if choise == 5:
                # --------
                mat_barGR()
                # --------
                continue
            else:
                break
        # --------
        continue
    if choise == 2:
        # -------- Библиотека Seaborn
        while True:
            choise = int(input(
                f'Выберите: \n1 - boxplot\n2 - facegridGR\n3 - heatmap\n4 - lineplot\n5 - scatterplot'))
            if choise == 1:
                # --------
                seaborn_boxplot()
                # --------
                continue
            if choise == 2:
                # --------
                seaborn_facegridGR()
                # --------
                continue

            if choise == 3:
                # --------
                seaborn_heatmap()
                # --------
                continue
            if choise == 4:
                # --------
                seaborn_lineplot()
                # --------
                continue
            if choise == 5:
                # --------
                seaborn_scatterplot()
                # --------
                continue
            else:
                break
        # --------
        continue
    if choise == 3:
        # --------Библиотека Plotly
        while True:
            choise = int(input(
                f'Выберите:  \n1 - ScatterGR\n2 - boxGR\n3 - pieGR\n4 - barGR\n5 - candleGR\n6 - scetter3dGR'))
            if choise == 1:
                # --------
                plotly_ScatterGR()
                # --------
                continue
            if choise == 2:
                # --------
                plotly_boxGR()
                # --------
                continue
            if choise == 3:
                # --------
                plotly_pieGR()
                # --------
                continue
            if choise == 4:
                # --------
                plotly_barGR()
                # --------
                continue
            if choise == 5:
                # --------
                plotly_candleGR()
                # --------
                continue
            if choise == 6:
                # --------
                plotly_scetter3dGR()
                # --------
                continue
            else:
                break
        # --------
        continue
    else:
        break