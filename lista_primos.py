# retorna uma lista vertical dos números primos entre 1 e um número inteiro informado pelo usuário.

def primo(x):
	divisores = []
	
	for i in range(x):
		if x % (i + 1) == 0:
			divisores.append(i + 1)
	
	if len(divisores) == 2:
		return True
	else:
		return False


numero = int(input("Número: "))
print("")

for num in range(2, numero):
	if primo(num):
		print(num)


