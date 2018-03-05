def list_to_stack(lista):
    stack = []

    while len(lista) > 0:
        topo = lista.pop()
        stack.append(topo)

    return stack

print(list_to_stack([1, 2, 3]))


