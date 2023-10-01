try:
    file = open("testfile.txt", "r")
    flag = 0
    index = 0
    phraseindex = 0
    charamount = 0
    phrase = str(input("Podaj szukana fraze: "))

    for line in file:
        index += 1
        wordlist = line.split()
        charamount += sum(len(word) for word in wordlist)
        if phrase in line:
            flag = 1
            phraseindex = index

    if flag == 1:
        print(f"Fraze {phrase} znaleziono w linijce {phraseindex}")

    else:
        print(f"Frazy {phrase} nie ma w tekscie")

    print(f"W calym pliku jest {charamount} znakow")
    file.close()
except FileNotFoundError:
    print("Nie istnieje taki plik")