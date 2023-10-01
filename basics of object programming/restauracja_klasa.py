class Restauracja:
    def __init__(self, nazwa, typ, godz_otw):
        self.nazwa = nazwa
        self.typ = typ
        self.klienci = 0
        self.godz_otw = (min(godz_otw), max(godz_otw))

    def opis_restauracji(self):
        print(f"Nazwa restauracji: '{self.nazwa}'\nTyp kuchni: {self.typ}\nObsluzeni dzisiaj klienci: {self.klienci}")

    def ustaw_liczbe_obsluzonych_klientow(self, nowi_k):
        if isinstance(nowi_k, int) and nowi_k >= 0:
            self.klienci = nowi_k
            print(f"Liczba klientow obsluzonych przez restauracje {self.nazwa} wynosi {self.klienci}")
        else:
            print("Nie podano prawidlowej liczby klientow")

    def dodaj_liczne_obsluzonych_klientow(self, liczba):
        if isinstance(liczba, int) and liczba >= 0:
            print(f"Po dodaniu {liczba} klientow, restauracja obsluzyla {self.klienci + liczba} klientow")
            self.klienci += liczba
        elif isinstance(liczba, int) and liczba < 0 and (self.klienci + liczba) >= 0:
            print(f"Po odjeciu {(-1) * liczba} klientow, restauracja obsluzyla {self.klienci + liczba} klientow")
            self.klienci += liczba
        else:
            print(f"Podano nieprawidlowa liczbe klientow")

    def czy_otwarta(self):
        teraz = int(input("Ktora jest godzina?"))
        if teraz >= self.godz_otw[0] and teraz <= self.godz_otw[1]:
            print(
                f"{self.nazwa} pracuje w godzinach {self.godz_otw[0]} - {self.godz_otw[1]}, "
                f"wiec tak, jest teraz otwarta")
        else:
            print(
                f"{self.nazwa} pracuje w godzinach {self.godz_otw[0]} - {self.godz_otw[1]}, "
                f"wiec niestety, jest teraz zamknieta")


class Lodziarnia(Restauracja):
    def __init__(self, nazwa, godz_otw, smaki):
        super().__init__(nazwa, "Lodziarnia", godz_otw)
        self.smaki = smaki

    def wyswietl_smaki(self):
        if self.smaki:
            print(f"Dostepne smaki w {self.nazwa}:")
            for smak in self.smaki:
                print(smak)

        else:
            print(f"W {self.nazwa} skonczyly sie lody")


mammamia = Restauracja("Mamma mia", "wloska", (10, 22))
mammamia.opis_restauracji()
mammamia.ustaw_liczbe_obsluzonych_klientow(20)
mammamia.dodaj_liczne_obsluzonych_klientow(25)
mammamia.dodaj_liczne_obsluzonych_klientow(-6)
mammamia.dodaj_liczne_obsluzonych_klientow(-70)
mammamia.czy_otwarta()

bar_ml = Restauracja("Jak u mamy", "bar mleczny", (8, 16))
bar_ml.opis_restauracji()
bar_ml.ustaw_liczbe_obsluzonych_klientow(10)
bar_ml.dodaj_liczne_obsluzonych_klientow(15)
bar_ml.czy_otwarta()

lody = Lodziarnia("Dziadek mroz", (12, 20),
                  ["Sorbet cytrynowy", "Sorbet mango", "Wanilia", "Smietankowe", "Czekolada", "Tiramisu"])
lody.wyswietl_smaki()
lody.opis_restauracji()

lody2 = Lodziarnia("Galka smaku", (12, 20), [])
lody2.wyswietl_smaki()
