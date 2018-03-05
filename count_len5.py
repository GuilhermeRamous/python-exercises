def count_len5(lista):
    count = 0

    for i in lista:
        if len(i) == 5:
            count += 1

    return count

num_elementos = int(input("Número de elementos da lista: "))
print()
lista = []

for i in range(num_elementos):
    valor = input("Elemento " + str(i + 1) + ": ")
    lista.append(valor)

print()
print("Número de strings na lista com len 5:", count_len5(lista))
