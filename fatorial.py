def fatorial(numero):
	resultado = 1
	for i in range(numero):
		resultado *= numero
		numero -= 1
	
	return resultado


valor = int(input("Valor: "))
print()	
print(str(valor) + "! =", fatorial(valor))
	
		
