tabuada = int(input("Montar a tabuada de: "))
começo = int(input("Começar por: "))
fim = int(input("Terminar em: "))

if começo < fim:
	for i in range(começo, fim + 1):
		print(str(tabuada) + " X " + str(i) + " = ", tabuada * i)
else:
	for i in range(começo, fim - 1, -1):
		print(str(tabuada) + " X " + str(i) + " = ", tabuada * i)
