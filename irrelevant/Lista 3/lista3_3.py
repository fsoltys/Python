def LiczSrednia(*args):
    """funkcja obliczajaca srednia z dowolnej liczby argumentow"""
        #po zadeklarowaniu zmiennej korzystam z try except zeby uniknac bledow w obliczaniu
    try:
        srednia = sum(args)/len(args)
        #obliczam srednia, nastepnie sprawdzam parzystosc i na jej podstawie wypisuje odpowiedni komunikat przy uzyciu fstring
        if srednia % 2 == 0:
            #w kazdym print wypisuje float oraz int, float zaokraglam do 2 miejsc po przecinku
            print(f"Srednia podanych liczb wynosi {srednia: .2f} i jest parzysta,\npo zaokragleniu otrzymujemy srednia = {int(srednia)}\n")
        else:
            print(f"Srednia podanych liczb wynosi {srednia: .2f} i jest nieparzysta,\npo zaokragleniu otrzymujemy srednia = {int(srednia)}\n")
    except TypeError:
        #przypadek w ktorym podano nieprawidlowy typ argumentu
        print(f"Wpisane argumenty, {args} nie sa liczbami\n")

    except ZeroDivisionError:
        #przypadek w ktorym nie podano zadnego argumentu
        print(f"Nie podano zadnych liczb\n")


print(LiczSrednia.__doc__) #wypisuje dokumentacje funkcji
LiczSrednia(1, 15, 45, 120, 0)
LiczSrednia(-3, 5, "slowo", 45)
LiczSrednia()
LiczSrednia(-2, -5, 0, 1)
