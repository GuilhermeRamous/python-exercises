def fib(n):
    print(str(n))

    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

termo = int(input("Termo: "))
print()
print(fib(termo))
