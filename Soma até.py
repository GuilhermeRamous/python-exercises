n = int(input("Digite um número natural: "))
resultado = 0

for i in range(n):
    resultado += n
    n -= 1

print(resultado)
