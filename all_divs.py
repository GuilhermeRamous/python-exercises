def divisors(num):
    resultado = ""

    for i in range(1, num + 1):
        if num % i == 0:
            resultado += " " + str(i)

    return resultado

n = int(input("Number: "))
print()
print("All divisors of " + str(n) + ":", divisors(n))
