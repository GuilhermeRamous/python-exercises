print("MAIOR, MENOR OU IGUAL?")
print("")

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))

if n1 > n2:
    print(n1 , "é maior que", n2)
else:
    if n1 < n2:
        print(n1, "é menor que", n2)
    else:
        print(n1, "é igual a", n2)
