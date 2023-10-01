import json
import os

def diary(path):
    pathdotjson = path + ".json"
    
    if not os.path.exists(pathdotjson):
        print('plik jeszcze nie istniał')
        with open(pathdotjson, "w") as diary:
            json.dump([], diary)
            
    with open(pathdotjson, "r") as diary:
        entries = json.load(diary)
    entries.append(input("podaj treść nowego wpisu: \n"))
    
    print("poprzednie wpisy (od najnowszego do najstarszego): \n")
    for index, entry in enumerate(entries[::-1]):
        print(index+1, entry)
    
    with open(pathdotjson, "w") as diary:
        json.dump(entries, diary)
        
diary("moj_pamietnik")