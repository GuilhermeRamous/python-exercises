def double_stuff(lista):
    lista_nova = []

    for i in lista:
        lista_nova.append(i * 2)

    return lista_nova

lista = [1, 2, 3, 4]
print(double_stuff(lista))
