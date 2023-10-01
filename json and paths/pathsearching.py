import os


def searchpath(path):
    result = []
    for root, catalogs, files in os.walk(path):
        for file in files:
            if file.lower().endswith('.pdf') and "praca" in file.lower():
                result.append(os.path.join(root, file))
    return result


print(searchpath("test"))
