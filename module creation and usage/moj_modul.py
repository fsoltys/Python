class Uzytkownik:
    def __init__(self, imie, nazwisko, nick, data_urodzenia, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nick = nick
        self.data_urodzenia = data_urodzenia
        self.email = email
        self.proby = 0

    def opisz_uzytkownika(self):
        print(f"Uzytkownik {self.nick} nazywa sie {self.imie} {self.nazwisko}, urodzil sie {self.data_urodzenia}, "
              f"jego adres email to {self.email}, proby logowania do konta: {self.proby}")

    def pozdrow_uzytkownika(self):
        print(f"Witaj {self.nick}, milego korzystania z serwisu")

    def resetuj_proby_logowania(self):
        self.proby = 0

    def dodaj_probe_logowania(self):
        self.proby += 1


class Admin(Uzytkownik):
    def __init__(self, imie, nazwisko, nick, data_urodzenia, email, przywileje):
        super().__init__(imie, nazwisko, nick, data_urodzenia, email)
        self.przywileje = Przywileje(przywileje)

    def wyswietl_przywileje(self):
        print("Administrator ma nastepujace przywileje:")
        if self.przywileje.lista_p:
            for przywilej in self.przywileje.lista_p:
                print(przywilej)
        else:
            print("Nie ustawiono zadnych specjalnych przywilejow dla administratora")


class Przywileje:
    def __init__(self, przywileje):
        self.lista_p = przywileje