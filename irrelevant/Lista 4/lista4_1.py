a = [i for i in range(1, 21)]
b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

def ListReorg(lista, k):
    for i in range(k):
        pom = lista.pop()
        lista.insert(0, pom)

    return lista

print(ListReorg(a, int(input("O jaki krok przesunac liste a (od 1 do 20):"))))
print(ListReorg(b, int(input("O jaki krok przesunac liste b (od 1 do 8):"))))
