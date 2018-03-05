print("Todas as resposta devem ser respondidas com 0 (não) ou 1 (sim)")
print("")
a = int(input("Telefonou para vítima? "))
b = int(input("Esteve no local do crime? "))
c = int(input("Mora perto da vítima? "))
d = int(input("Devia para vítima? "))
e = int(input("Já trabalhou com a vítima? "))
resultado = a + b + c + d + e

if resultado == 2:
    print("Clasificação: suspeita")
elif resultado == 3 or resultado == 4:
    print("Clasificação: cúmplice")
elif resultado == 5:
    print("Clasificação: assassina")
else:
    print("Clasificação: inocente")
