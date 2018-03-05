ganho_por_hora = float(input("Ganho por hora: R$ "))
horas = float(input("Horas trabalhadas mensalmente: "))
salario = horas * ganho_por_hora
imposto = salario * (1 - 0.11)
inss = salario * (1 - 0.08)
sindicato = salario * (1 - 0.05)

print("Salário bruto: R$", salario)
print("Imposto de renda: R$", imposto)
print("INSS: R$", inss)
print("Sindicato: R$", sindicato)

if salario - (imposto + inss + sindicato) > 0:
    print("Salário líquido: R$", salario - (imposto + inss + sindicato))

else:
    print("Salário bruto: R$ 0.0")
