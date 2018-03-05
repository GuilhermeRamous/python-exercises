def insert(position, lista, value):
    new_lista = []

    for i in range(len(lista)):
        if  i == position:
            new_lista += [value] + [lista[i]]
        else:
            new_lista.append(lista[i])

    return new_lista


print(insert(2, [1, 2, 3], 999))


