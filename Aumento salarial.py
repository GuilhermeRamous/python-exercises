salario = float(input("Salário: R$ "))

if salario <= 280:
    percentual = "20%"
    aumento = salario * 20/100
    novo_salario = salario + aumento
elif salario > 280 and salario < 700:
    percentual = "15%"
    aumento = salario * 15/100
    novo_salario = salario + aumento
elif salario > 700 and salario < 1500:
    percentual = "10%"
    aumento = salario * 10/100
    novo_salario = salario + aumento
else:
    percentual = "5%"
    aumento = salario * 5/100
    novo_salario = salario + aumento

print("Salário antes do rajuste: R$", salario)
print("Percentual aplicado:", percentual)
print("Valor do aumento: R$", aumento)
print("Novo salário: R$", novo_salario)
