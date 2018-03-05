def soma_de_quadrados(lista):
    soma = 0

    for i in lista:
        soma += i ** 2

    return soma

num_elementos = int(input("Número de elementos da lista: "))
print()
lista = []

for i in range(num_elementos):
    valor = int(input("Elemento " + str(i + 1) + ": "))
    lista.append(valor)

print()
print("Resultado:", soma_de_quadrados(lista))



