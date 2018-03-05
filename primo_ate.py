# Programa que retorna os números primos até

def primo(num):
    for i in range(1, num + 1):
        if i != 1 and i != num and num % i == 0 or num == 1:
            return False
        elif i == num:
            return True

valor = int(input("Valor: "))
print()
print([i for i in range(2, valor) if primo(i)])
