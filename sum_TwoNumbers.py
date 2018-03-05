t = int(input())
lista = []
p1 = 0
p2 = 1

for i in range(t):
    values = input()
    lista += values.split(" ")

for i in range(t):
    print(int(lista[p1]) + int(lista[p2]))
    p1 += 2 
    p2 += 2


