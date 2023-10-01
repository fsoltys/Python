file = open("testfile.txt", 'a')

while x:=input("Wpisz tekst:"):
    file.write(f"{x}\n")
file.close()