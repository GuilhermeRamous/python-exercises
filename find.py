def find(string,substring):
	i = 0
	for i in range(len(string)):
		if string[i] == substring:
			return i

palavra = input("Palavra: ")
letra = input("Letra: ")

if find(palavra, letra) != None:
	print(find(palavra, letra))
else:
	print(-1)

 
