def primo(numero):
	divisores = 0
	for i in range(numero):
		if numero % (i + 1) == 0:
			divisores += 1

	if divisores == 2:
		return True
	else:
		return False


valor = int(input("Valor: "))
if primo(valor):
	print("O número", valor, "é primo")
else:
	print("O número", valor, "não é primo")
