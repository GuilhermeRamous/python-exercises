# Análogo ao find comum, porém o usuário pode escolher um index inicial. Caso o usuário não escolha o index será zero, que é o padrão.

def find2(stri, l, sta=0):
	if sta >= len(stri):
		return -1
	else:
		counter = sta
		
		while counter < len(stri):
			if stri[counter] == l:
				return counter
			elif counter == len(string) - 1:
				return -1

			counter += 1

string = input("String: ")
letter = input("Letter: ")
start = int(input("Start: "))
print()
print("Retorno:", find2(string, letter, start))
