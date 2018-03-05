def reverse_list(lista):

    if len(lista) == 1:
        return [lista[0]]
    else:
        topo = lista.pop()
        return [topo] + reverse_list(lista) 


print(reverse_list([1, 2, 3]))
