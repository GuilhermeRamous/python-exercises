def double_stuff(lista):
    for i in range(len(lista)):
        lista[i] = lista[i] * 2

    return lista


lista = [1, 2, 3]
print(double_stuff(lista))
