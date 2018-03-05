from math import ceil

n = float(input("Digite um número: "))

if ceil(n) == n:
    print(int(n), "é um número inteiro")
else:
    print(n, "é um número decimal")

