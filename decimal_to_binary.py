decimal = int(input("Decimal: ")) 
resultado = ""

while decimal != 0:
    resto = decimal % 2
    resultado = str(resto) + resultado
    decimal = decimal // 2

print()
print(resultado)
