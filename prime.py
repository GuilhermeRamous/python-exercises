def prime(num):
    for i in range(num):
        if i + 1 != 1 and i + 1 != num and num % (i + 1) == 0 or num == 1:
            return False
        elif i == num - 1:
            return True

t = int(input())
lista = []
p1 = 0
p2 = 1

for i in range(t):
    lista += input().split(" ")

for i in range(t):
    for i in range(int(lista[p1]), int(lista[p2]) + 1):
        if prime(i):
            print(i)

    p1 += 2
    p2 += 2
    print()
