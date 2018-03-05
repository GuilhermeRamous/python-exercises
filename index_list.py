def index_list(valor, lista):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
        elif i == len(lista) - 1:
            return "Valor não encontrado na lista"

print(index_list("oi", ["oi", "ola"]))
print(index_list("oi", [1, 2]))


