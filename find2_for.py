# Análoga a função find comum, porém o usuário pode escolher um index de partida. Caso não escolha o index de partida será zero, que é o padrão.

def find2(stri, l, sta=0):
	if sta >= len(string):
		return -1
	else:
		for i in range(sta, len(stri)):
			if stri[i] == l:
				return i
			elif i == len(stri) - 1:
				return -1

string = input("String: ")
letter = input("Letter: ")
start = int(input("Start: "))
print()
print("Retorno:", find2(string, letter, start))
		
