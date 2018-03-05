quantidade_notas = int(input("Quantidade de notas: "))
n = 0

for i in range(quantidade_notas):
	n += float(input(str(i + 1) + "° número: ")) / quantidade_notas

	
print("Média aritimética:", n)
