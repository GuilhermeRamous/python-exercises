from math import ceil

def par_ou_impar(x):
    if x % 2 == 0:
        return "par"
    else:
        return "ímpar"

def positivo_ou_negativo(y):
    if y > 0:
        return "positivo"
    else:
        return "negativo"

def int_ou_dec(z):
    if ceil(z) == z:
        return "inteiro"
    else:
        return "decimal"
    
print("1. adição")
print("2. subtração")
print("3. multiplicação")
print("4. divisão")
print("5. exponenciação")
print("")
n1 = float(input("1° número: "))
n2 = float(input("2° número: "))
op = int(input("Digite qual operação deseja fazer: "))

if op == 1:
    resultado = n1 + n2
    print("Resultado:", resultado)
    print("Informações sobre o resultado:")
    print(resultado, "é", par_ou_impar(resultado))
    print(resultado, "é", positivo_ou_negativo(resultado))
    print(resultado, "é", int_ou_dec(resultado))
elif op == 2:
    resultado = n1 - n2
    print("Resultado:", resultado)
    print("Informações sobre o resultado:")
    print(resultado, "é", par_ou_impar(resultado))
    print(resultado, "é", positivo_ou_negativo(resultado))
    print(resultado, "é", int_ou_dec(resultado))
elif op == 3:
    resultado = n1 * n2
    print("Resultado:", resultado)
    print("Informações sobre o resultado:")
    print(resultado, "é", par_ou_impar(resultado))
    print(resultado, "é", positivo_ou_negativo(resultado))
    print(resultado, "é", int_ou_dec(resultado))
elif op == 4:
    resultado = n1 / n2
    print("Resultado:", resultado)
    print("Informações sobre o resultado:")
    print(resultado, "é", par_ou_impar(resultado))
    print(resultado, "é", positivo_ou_negativo(resultado))
    print(resultado, "é", int_ou_dec(resultado))
else:
    resultado = n1 ** n2
    print("Resultado:", resultado)
    print("Informações sobre o resultado:")
    print(resultado, "é", par_ou_impar(resultado))
    print(resultado, "é", positivo_ou_negativo(resultado))
    print(resultado, "é", int_ou_dec(resultado))
    
    
    
