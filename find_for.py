# Retorna o index de um substring que se encontra no string principal. Caso não se encontre retorna -1

def find(s, l):
	for position in range(len(s)):
		if s[position] == l:
			return position
		elif position == len(s) - 1:
			return -1
	
string = input("String: ")
letter = input("Letter: ")
print()
print("Retorno:", find(string, letter))
