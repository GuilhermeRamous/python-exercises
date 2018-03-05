def count_list(valor, lista):
    count = 0

    for i in lista:
        if i == valor:
            count += 1

    return count

lista = ["hello world", 1, 2]
print(count_list("hello world", lista))

