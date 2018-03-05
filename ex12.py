def index(lista, palavra):
    for i in range(len(lista)):
        if palavra == lista[i]:
            return i

def ex12(lista):
    if "sam" not in lista:
        return len(lista)
    else:
        return index(lista, "sam") + 1
            

print(ex12(["jdjd", "djdjdj"]))
print(ex12(["djjf", "djjfjf", "ndjd", "sam", "sam", "sam"]))
