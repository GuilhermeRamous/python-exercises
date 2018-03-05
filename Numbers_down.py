primeiro_numero = int(input("Primeiro número: "))
segundo_numero = int(input("Segundo número: "))

if primeiro_numero == segundo_numero:
	print(primeiro_numero)
elif primeiro_numero < segundo_numero:
	for i in range(primeiro_numero, segundo_numero + 1):
		print(i)
else:
	for i in range(primeiro_numero, segundo_numero - 1, -1):
		print(i)
