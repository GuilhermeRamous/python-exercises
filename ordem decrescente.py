print("Digite números diferentes!")
n1 = float(input("1° número: "))
n2 = float(input("2° número: "))
n3 = float(input("3° número: "))

if n1 == n2 or n1 == n3 or n2 == n3:
    print("Você digitou números iguais")
else:
# Decisão do menor número:
    if n1 < n2 and n1 < n3:
        menor = n1
    elif n2 < n1 and n2 < n3:
        menor = n2
    else:
        menor = n3

# Desição do número do meio:
    if n1 > menor and (n1 < n2 or n1 < n3):
        meio = n1
    elif n2 > menor and (n2 < n1 or n2 < n3):
        meio = n2
    else:
        meio = n3

# Desição do maior número:
    if n1 > n2 and n1 > n3:
        maior = n1
    elif n2 > n1 and n2 > n3:
        maior = n2
    else:
        maior = n3

print(menor)
print(meio)
print(maior)
    


