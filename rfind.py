def rfind(string, substring):
	for i in range(len(string)):
		index = -i
	
		if string[index] == substring:
			return index + len(string)

palavra = input("Palavra: ")
letra = input("Letra: ")

if rfind(palavra, letra) == None:
	print(-1)
else:
	print(rfind(palavra, letra))
