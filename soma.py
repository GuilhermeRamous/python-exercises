# Retorna a soma de todos elementos da lista, exclusive o primeiro número par

def soma(lista):
    n = 0
    soma = 0

    for i in lista:
        if i % 2 == 0 and n == 0:
            n += 1
        else:
            soma += i

    return soma

num_elementos = int(input("Número de elementos da lista: "))
print()
lista = []

for i in range(num_elementos):
    valor = int(input("Elemento " + str(i + 1) + ": "))
    lista.append(valor)

print()
print("Soma:", soma(lista))
