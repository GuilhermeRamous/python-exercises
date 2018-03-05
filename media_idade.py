quantidade_pessoas = int(input("Quantidade de pessoas: "))
n = 0

for i in range(quantidade_pessoas):
	n += int(input(str(i + 1) + "° idade: ")) / quantidade_pessoas

if 0 <= n <= 25:
	print("Turma jovem")
elif 26 <= n <= 60:
	print("Turma adulta")
else:
	print("Turma idosa")

print("Média:", n)

