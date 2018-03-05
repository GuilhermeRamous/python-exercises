# Retorna a index de um substring que se encontra no string principal. Caso não se encontre retorna -1

def find(s, l):
	cont = 0

	while cont < len(s):
		if s[cont] == l:
			return cont
		elif cont == len(s) -1:
			return -1

		cont += 1


string = input("String: ")
letter = input("Letter: ")
print()
print("Retorno", find(string, letter))
