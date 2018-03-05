quantidade_cd = int(input("Quantidade de cds: "))
valor = 0
print("")

for i in range(quantidade_cd):
	valor += float(input("preço do " + str(i + 1) + "° cd: "))

print("")
print("Valor gasto em todos os cds:", valor)
print("Média de preço dos cds:", valor / quantidade_cd)

