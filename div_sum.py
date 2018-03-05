def divisors(num):
    result = 0

    for i in range(1, num):
        if num % i == 0:
            result += i

    return result

t = int(input())
lista = []
p = 0

for i in range(t):
    lista.append(int(input()))

for i in range(t):
    print(divisors(lista[p]))
    p += 1

        
