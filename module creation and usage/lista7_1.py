from moj_modul import Admin
# from moj modul import *
# import moj_modul as ...

uz1 = Admin("Janusz", "Kowalski", "kowal", (11, 12, 1997), "kowaljan@admin.pl", ["zablokuj", "usun komentarz"])

uz1.pozdrow_uzytkownika()
uz1.dodaj_probe_logowania()
uz1.dodaj_probe_logowania()
uz1.wyswietl_przywileje()
uz1.resetuj_proby_logowania()