def fatorial(n):
    if n < 0:
        return "Números negativos não possuem fatorial"
    elif n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

num = int(input("Número: "))
print()
print(fatorial(num))

