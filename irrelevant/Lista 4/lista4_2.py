names = []

for i in range(1, 6):
    names.append(input(f"Podaj nazwisko {i}/5: ").title())

namesK = []  # lista na nazwiska zaczynające się od K wzwyż
names5 = []  # lista na nazwiska 5 znakowe i dłuższe
for i in range(len(names)):
    name = names[i]
    if name[0] >= 'K':  # Dopisuje nazwiska zaczynajace sie od K wzwyz do odpowiedniej listy
        namesK.append(name.title())

    if len(name) >= 5:  # Dopisuje nazwiska rowne i dluzsze niz 5 znakow do odpowiedniej listy
        names5.append(name.title())

# wypisuje nazwiska zgodnie z poleceniem, najpierw zaczynajace sie od K wzwyz
# nastepnie rowne i dluzsze 5 znakow, w kolejnosci alfabetycznej
print(f"Nazwiska zaczynające się od litery K i późniejszej w alfabecie: {namesK}")
print(f"Nazwiska równe i dłuższe niż 5 znaków, w kolejności alfabetycznej: {sorted(names5)}")
