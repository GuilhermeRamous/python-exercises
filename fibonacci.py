qt_digitos = int(input("Digite quantos dígitos terá em sua lista: "))
tipo_lista = input("Digite o tipo de lista que deseja (v -> vertical e h -> horizontal): ")
numero1 = 1
numero2 = 1
novo_numero = 0

if tipo_lista == "v" or tipo_lista == "V":
	print(numero1)
	print(numero2)

	for i in range(qt_digitos - 2):
		numero_novo = numero1 + numero2
		numero1 = numero2
		numero2 = numero_novo	
		print(numero_novo)

elif tipo_lista == "h" or tipo_lista == "H":
	lista_horizontal = str(numero1) + " " + str(numero2)

	for i in range(qt_digitos - 2):
		numero_novo = numero1 + numero2
		numero1 = numero2
		numero2 = numero_novo
		lista_horizontal += " " + str(numero_novo)

	print(lista_horizontal)

else:
	print("O tipo de lista requerido não existe.")
                

		

