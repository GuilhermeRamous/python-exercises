numero = int(input("Digite o número principal de sua tabuada: "))

for i in range(11):
	print(str(numero) + " X " + str(i) + " = ", numero * i)
