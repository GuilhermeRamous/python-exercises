numero_clientes = int(input("Número de clientes: "))
lista_codigo = []
lista_altura = []
lista_massa = []
maior_altura = 0
menor_altura = 0
maior_massa = 0
menor_massa = 0
MaiorAlturaCode = ""
MenorAlturaCode = ""
MaiorMassaCode = ""
MenorMassaCode = ""
index = -1

for i in range(numero_clientes):
	print(str((i + 1)) + "° cliente:" )
	print()
	codigo = int(input("Código: "))
	altura = float(input("Altura (metros): "))
	massa = float(input("Massa (quilogramas): "))
	lista_codigo = lista_codigo.append(codigo)
	lista_altura = lista_altura.append(altura)
	lista_massa = lista_massa.append(massa)
	maior_altura = max(lista_altura)
	menor_altura = min(lista_altura)
	maior_massa = max(lista_massa)
	menor_massa = min(lista_massa)
	

for y in lista_altura:
	# os codigos da maior e menor altura são obtidos nesse laço
	index += 1
	
	if y == maior_altura:
		if MaiorAlturaCode == "":
			MaiorAlturaCode += str(lista_codigo[index]) 
	else:
			MaiorAlturaCode += ", " + str(lista_codigo[index]) 

	if y == menor_altura:
		if MenorAlturaCode == "":
			MenorAlturaCode += str(lista_codigo[index])	
		else:
			MenorAlturaCode += ", " + str(lista_codigo[index])

index = -1

for z in lista_massa:
	# os códigos da maior e menor massa são obtidos nesse laço
	index += 1

	if z == maior_massa:
		if MaiorMassaCode == "":
			MaiorMassaCode += str(lista_codigo[index])
		else:
			MaiorMassaCode += ", " + str(lista_codigo[index])	

	if z == menor_massa:
		if MenorMassaCode == "":
			MenorMassaCode += str(lista_codigo[index])	
		else:
			MenorMassaCode += ", " + str(lista_codigo[index])


print("Cliente(s) com maior altura:")
print("   Código(s):", MaiorAlturaCode)
print("   Altura:", maior_altura)
print()
print("Cliente(s) com menor altura:")
print("   Código(s):", MenorAlturaCode)
print("   Altura:", menor_altura)
print()
print("Cliente(s) com maior massa:")
print("   Código(s):", MaiorMassaCode)
print("   Massa:", maior_massa)
print()
print("Cliente(s) com menor massa:")
print("   Código(s):", MenorMassaCode)
print("   Massa:", menor_massa)

		
	



