from datetime import date

print("1. Saber data daqui a x dias")
print("2. Saber data há x dias")

dia = date.today()
escolha = int(input("Escolha uma opção: "))

if escolha == 1:
    print("")
    x = int(input("Valor: "))
    futuro = date.fromordinal(dia.toordinal() + x)
    print("Data requerida:", futuro)
elif escolha == 2:
    print("")
    x = int(input("Valor: "))
    passado = date.fromordinal(dia.toordinal() - x)
    print("Data requerida:", passado)
else:
    print("Valor inválido!")
