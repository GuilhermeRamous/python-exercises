import random

valores = []
media = 0

for i in range(100):
    valores.append(random.randrange(1001))
    media += valores[i] / 100

print("Lista:", valores)
print()
print("Media dos valores da lista:", media)


