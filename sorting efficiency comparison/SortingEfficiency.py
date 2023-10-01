import random
import time
import plotly.express as px
import pandas as pd
import math as m


def bubble_basic(data):
    for i in range(len(data)):
        for j in range(0, len(data) - i - 1):
            if data[j] > data[j + 1]:
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp
    return data


def bubble_better(data):
    for i in range(len(data)):
        change = True
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp
                change = False
            if change:
                break
    return data


def bubble_worst(data):
    for i in range(len(data)):
        for j in range(0, len(data) - 1):
            if data[j] > data[j + 1]:
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp
    return data


def insert(data):
    for i in range(len(data)):
        for j in range(0, i):
            if data[i] < data[j]:
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
    return data


def select(data):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
    return data


def avg_max_time(execs, length, function):
    exec_times = []
    for i in range(execs):
        to_sort = [random.randint(0, 1000) for i in range(length)]
        start = time.time()
        function(to_sort)
        end = time.time()
        result = end - start
        exec_times.append(result)

    avg_exec = sum(exec_times) / len(exec_times)
    max_exec = max(exec_times)

    return avg_exec, max_exec


def efficiency_test(length, function):
    to_sort = [random.randint(0, 1000) for i in range(length)]
    start = time.time()
    function(to_sort)
    end = time.time()
    worktime = end - start
    return worktime


lengths = (10, 20, 50, 100, 200, 500, 1000)

avgs = {"bubble": [], "select": [], "insert": []}
maxs = {"bubble": [], "select": [], "insert": []}
for n in lengths:
    temp_avg, temp_max = avg_max_time(10, n, bubble_basic)
    avgs["bubble"].append(round(temp_avg, 5))
    maxs["bubble"].append(round(temp_max, 5))

    temp_avg, temp_max = avg_max_time(10, n, insert)
    avgs["insert"].append(round(temp_avg, 5))
    maxs["insert"].append(round(temp_max, 5))

    temp_avg, temp_max = avg_max_time(10, n, select)
    avgs["select"].append(round(temp_avg, 5))
    maxs["select"].append(round(temp_max, 5))

avgs_dataframe = pd.DataFrame.from_dict(avgs).set_axis(lengths, axis="index")
maxs_dataframe = pd.DataFrame.from_dict(maxs).set_axis(lengths, axis="index")

avgs_wykres = px.line(avgs_dataframe, template="plotly_dark", markers=True,
                      title="Srednie czasy dzialania algorytmow sortujacych",
                      labels={"value": "Czas", "index": "Ilosc danych", "variable": "Algorytm"})
maxs_wykres = px.line(maxs_dataframe, template="plotly_dark", markers=True,
                      title="Maxymalne czasy dzialania algorytmow sortujacych",
                      labels={"value": "Czas", "index": "Ilosc danych", "variable": "Algorytm"})
with open("plots.html", "w") as f:
    f.write(avgs_wykres.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(maxs_wykres.to_html(full_html=False, include_plotlyjs='cdn'))

basic_bubble_eff = []
worse_bubble_eff = []
better_bubble_eff = []

n_list = (10, 100, 1000)

for n in n_list:
    temp_time = efficiency_test(n, bubble_basic)
    try:
        log_eff = (n * m.log10(n)) / temp_time
    except ZeroDivisionError:
        log_eff = "Zbyt krotki czas by policzyc"
    basic_bubble_eff.append((n, temp_time, log_eff))

    temp_time = efficiency_test(n, bubble_better)
    try:
        log_eff = (n * m.log10(n)) / temp_time
    except ZeroDivisionError:
        log_eff = "Zbyt krotki czas by policzyc"
    better_bubble_eff.append((n, temp_time, log_eff))

    temp_time = efficiency_test(n, bubble_worst)
    try:
        log_eff = (n * m.log10(n)) / temp_time
    except ZeroDivisionError:
        log_eff = "Zbyt krotki czas by policzyc"
    worse_bubble_eff.append((n, temp_time, log_eff))

print("Testy wydajnościowe: n | t(n) | (n*log(n))/t(n)")
for i in range(len(basic_bubble_eff)):
    print(f"basic: {basic_bubble_eff[i][0]} | {basic_bubble_eff[i][1]}s | {basic_bubble_eff[i][2]}")
    print(f"better: {better_bubble_eff[i][0]} | {better_bubble_eff[i][1]}s | {better_bubble_eff[i][2]}")
    print(f"worse: {worse_bubble_eff[i][0]} | {worse_bubble_eff[i][1]}s | {worse_bubble_eff[i][2]}")
