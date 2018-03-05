primeiro_numero = int(input("Primeiro número: "))
segundo_numero = int(input("Segundo número: "))
soma = 0

if primeiro_numero == segundo_numero or primeiro_numero > segundo_numero:
	print("Lista vazia")
else:
	for i in range(primeiro_numero + 1, segundo_numero):
		print(i)
		soma += i

print("Soma:", soma)
