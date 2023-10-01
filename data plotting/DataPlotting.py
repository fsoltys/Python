import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "wyniki-pm10-bap-24h.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, pm10, bap = [], [], []
    for row in reader:
        dateI = datetime.strptime(row[0], '%Y-%m-%d')
        try:
            tempPm10 = float(row[1])
            tempBap = float(row[2])
        except ValueError:
            print(f"No data for {dateI}")
        else:
            dates.append(dateI)
            pm10.append(tempPm10)
            bap.append(tempBap)

filename = "pojazdy.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    gminy, ilosci = [], []
    for row in reader:
        gmina = str(row[2])
        ilosc = int(row[3])

        gminy.append(gmina)
        ilosci.append(ilosc)

# sorting data into a pie chart to extract the top10
for n in range(len(ilosci) - 1, 0, -1):
    for i in range(n):
        if ilosci[i] < ilosci[i + 1]:
            # swapping data if the element is less than next element in the array
            ilosci[i], ilosci[i + 1] = ilosci[i + 1], ilosci[i]
            gminy[i], gminy[i + 1] = gminy[i + 1], gminy[i]

fig, axs = plt.subplots(2, 2, figsize=(16, 18))

axs[0, 0].plot(dates, pm10, dates, bap, linewidth=1)
axs[0, 0].set_title("Pomiary Pm10[µg/m3] i BaP[ng/m3]", fontsize=12)
axs[0, 0].set_xlabel("Data pomiaru", fontsize=8)
axs[0, 0].set_ylabel("Wartosc pomiaru [µg/m3]", fontsize=8)
axs[0, 0].tick_params(axis='y', labelsize=14)
axs[0, 0].tick_params(axis='x', labelsize=10)

axs[1, 0].set_title("Czestotliwosc wartosci pomiarow pm10", fontsize=12)
axs[1, 0].hist(pm10, bins=20, edgecolor='black')
axs[1, 0].set_ylabel("Czestotliwosc wystapien", fontsize=8)
axs[1, 0].set_xlabel("Wartosc pomiaru", fontsize=8)

axs[0, 1].pie(ilosci[:10], autopct='%1.1f%%', pctdistance=1.2)
axs[0, 1].set_title("Pojazdy wjezdzajace do wroclawia z wybranych regionow")
axs[0, 1].legend(gminy[:10], bbox_to_anchor=(1, 1), frameon=True)

axs[1, 1].scatter(dates, pm10, alpha=0.4)
axs[1, 1].set_title("Zanieczyszczenie Pm10 we Wroclawiu")
axs[1, 1].set_xlabel("Data")
axs[1, 1].set_ylabel("Pomar Pm10")

plt.show()
