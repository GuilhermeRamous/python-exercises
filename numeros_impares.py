def numero_impar(x):
	if x % 2 > 0:
		return True
	else:
		return False

primeiro_numero = int(input("Primeiro número: "))
segundo_numero = int(input("Segundo número: "))

if primeiro_numero == segundo_numero:
	if numero_impar(primeiro_numero):
		print(primeiro_numero) 
	else:
		print("Não há número ímpares para a lista.")
elif primeiro_numero < segundo_numero:
	for i in range(primeiro_numero, segundo_numero + 1):
		if numero_impar(i):
			print(i)
else:
	for i in range(primeiro_numero, segundo_numero - 1, -1):
		if numero_impar(i):
			print(i) 
