def wypisz(karton):  # funkcja wypisujaca wszystkie wartosci w slowniku z wykorzystaniem odpowiednich kluczy
    print(f"Informacje o mleku:\nData waznosci: {karton['data_waznosci']}\nPojemnosc opakowania: {karton['pojemnosc']}l\n"
          f"Cena za 1 op.: {karton['cena']}zl\nProducent: {karton['marka']}")


def zakupy(karton):  # funkcja obliczajaca cene 6 kartonow mleka na podstawie ceny podanej w slowniku
    SumOf6 = 6*karton["cena"]
    return SumOf6


karton_mleka = {}  # pusty słownik

# wypełniam slownik parami klucz - wartosc
karton_mleka["data_waznosci"] = (9, 11, 2021)
karton_mleka["pojemnosc"] = 1.5
karton_mleka["cena"] = 3.99
karton_mleka["marka"] = "Mlekpol"

# wywolanie obu funkcji
wypisz(karton_mleka)
print(f"Za kupno 6 takich kartonow zaplacimy {zakupy(karton_mleka)}zl")
