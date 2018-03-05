ganho_por_hora = float(input("Valor ganhado por hora em seu trabalho: "))
horas = int(input("Horas trabalhadas: "))

print("Valor mensal recebido: R$", ganho_por_hora * horas)
print("Valor semestral recebido: R$", 6 * (ganho_por_hora * horas))
print("Valor anual recebido: R$", 12 * (ganho_por_hora * horas))
