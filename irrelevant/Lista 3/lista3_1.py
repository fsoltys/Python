def bilet(wiek):
    if wiek <= 18 | wiek >= 65:
        print("Cena biletu ulgowego wynosi 15zl")
    elif wiek <= 0:
        print("Podano nieprawidłowy wiek")
    else:
        print("Cena biletu wynosi 30zl")


bilet(int(input("Podaj swoj wiek:")))