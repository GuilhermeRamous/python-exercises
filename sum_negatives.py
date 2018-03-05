def sum_negatives(lista):
    soma = lista [0]

    for i in lista[1:]:
        if i < 0:
            soma += i

    return soma

num_elementos = int(input("Número de elementos da lista: "))
print()
lista = []

for i in range(num_elementos):
    valor = int(input("Elemento " + str(i + 1) + ": "))
    lista.append(valor)

print()
print("Soma dos negativos da lista:", sum_negatives(lista))
