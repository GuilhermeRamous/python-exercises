def numero_de_digitos(numero):
	if type(numero) == type(1):
		return len(str(numero))
	else:
		return None

try:
	valor = int(input("Valor: "))
	print(numero_de_digitos(valor))
except:
	print("O valor deve ser inteiro")








