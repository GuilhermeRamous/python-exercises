def count_impar(lista):
    resultado = 0

    for i in lista:
        if i % 2 > 0:
            resultado += 1

    return resultado

num_elementos = int(input("Número de elemetos: "))
print()
lista = []

for i in range(num_elementos):
    valor = int(input("Elementos " + str(i + 1) + ": "))
    lista.append(valor)

print()
print("Números ímpares da lista:", count_impar(lista))



            
            
