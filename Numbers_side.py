primeiro_numero = int(input("Primeiro número: "))
segundo_numero = int(input("Segundo número: "))
resultado = ""

if primeiro_numero == segundo_numero:
	resultado = primeiro_numero
elif primeiro_numero < segundo_numero:
	
	for i in range(primeiro_numero, segundo_numero + 1):
		resultado += str(i) + " "
else:
	for i in range(primeiro_numero, segundo_numero - 1, -1):
		resultado += str(i) + " "

print(resultado)
