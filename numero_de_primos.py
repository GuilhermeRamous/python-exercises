"""O programa retorna o número de números primos entre 1 e um número informado pelo usuário"""

def primo(valor):
	subtraendo = 0
	divisores = 0
	
	for i in range(valor):
		if valor % (valor - subtraendo) == 0:
			divisores += 1
		subtraendo += 1

	if divisores == 2:
		return True
	else:
		return False

def primo_counter(numero):
	lista = []

	for i in range(abs(numero - 1)):
		if primo(i + 1):
			lista.append(i + 1)

	return lista


limite_aberto = int(input("Limite aberto: "))
print()
print("Quantidade de números primos entre 1 e " + str(limite_aberto) + ":", primo_counter(limite_aberto))
		
	
		
