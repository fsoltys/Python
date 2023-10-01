# zad 1 i 2
a = 6
a += 12
b = 7
b += 16
b -= 9
print("a + b = %d" % (a + b))
print("a * b = %d" % (a * b))
print("a / b = %0.2f" % (a / b))
print("a mod b = %d" % (a % b))
print("b - a = %d" % (b - a))
print("a ^ b = %e" % (a ** b))
# zad 3
x = 7
StringX = str(x)
FloatX = int(StringX)
print(x)
print(StringX)
print(FloatX)

# zad 4
inicjaly = "fs"
imie = "filip"
nazwisko = "soltysiak"

imie_nazwisko = f"{imie} {nazwisko}"
dane_osobowe = f"Inicjały: {inicjaly.upper()}\nImie: {imie.capitalize()}\nNazwisko: {nazwisko.capitalize()}"

print(dane_osobowe)
