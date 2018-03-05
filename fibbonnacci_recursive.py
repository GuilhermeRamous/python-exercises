def fib(n, numeros=[0, 1]):
    if len(numeros) == n:
        return numeros
    else:
        soma = [numeros[len(numeros) - 1] + numeros[len(numeros) - 2]]
        return soma + fib(n, numeros + soma)

print(fib(5))

