numero = int(input("Número: "))
resultado = 1
string = ""
sinal = ""

for i in range(numero):
	resultado *= numero - i
	
	if i != numero - 1:
		sinal = " . "
	else:
		sinal = " = "

	string += str(numero - i) + sinal

print(str(numero) + "! = " + string, resultado )
	
