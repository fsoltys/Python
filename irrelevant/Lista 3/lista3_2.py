from math import sqrt

def trojmian(a, b, c):
    """funkcja do obliczania rzeczywistych miejsc zerowych funkcji kwadratowej"""
        #najpierw sprawdzam czy mamy doczynienia z funkcja kwadratową (a=0 daje nam funkcję liniową)
    if a != 0:
        delta = (pow(b, 2)-4*a*c)
            #obliczam deltę a następnie na jej podstawie dzielę kod na 3 przypadki
        if delta > 0:
            #korzystając z zaimportowanej z modułu math funkcji sqrt obliczam pierwiastki funkcji
            x1 = ((-b - sqrt(delta))/(2*a))
            x2 = ((-b + sqrt(delta))/(2*a))
            #wypisuje wartosci korzystając z fstringa a wartosci zmiennoprzecinkowe formatuje do 2 miejsc po przecinku
            print(f"Funkcja ma dwia pierwiastki:\nx1 = {x1: .2f}\nx2 = {x2: .2f}")
        elif delta == 0:
            #jak wyzej, tym razem jednak pierwiastek jest tylko jeden
            x = (-b/(2*a))
            print(f"Funkcja ma jeden pierwiastek:\nx = {x}")
        else:
            #zostaje nam ostatni przypadek, w ktorym a=0 czyli funkcja nie ma pierwiastkow rzeczywistych
            print("Funkcja nie ma pierwiastkow rzeczywistych")
    else:
        #w tym przypadku a=0 czyli nie mamy funkcji kwadratowej
        print("Podane wspolczynniki nie tworza funkcji kwadratowej")

print(trojmian.__doc__)
trojmian(1, 5, 10)
trojmian(0, 10, 15)
trojmian(1, 4, 4)
trojmian(-1, 0, 5)
