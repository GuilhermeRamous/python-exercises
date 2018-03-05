import random

valores = []

for x in range(100):
    valores.append(random.randrange(1001))

maior_valor = valores[0]

for y  in valores:
    if y > maior_valor:
        maior_valor = y

print("Lista:", valores)
print()
print("Maior valor da lista:", maior_valor)
