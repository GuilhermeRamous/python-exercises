def cjc(n):
	vezes = 0
	while n != 1:
		if n % 2 == 0:
			n /= 2
			vezes += 1
		else:
			n = 3 * n + 1
			vezes += 1

	return vezes


primeiro_numero = int(input("Primeiro número: "))
segundo_numero = int(input("Segundo número: "))

if cjc(primeiro_numero) > cjc(segundo_numero):
	print("Número com maior operações:", primeiro_numero)
elif cjc(segundo_numero) > cjc(segundo_numero):
	print("Número com maior operações:", segundo_numero)
else:
	print("Os números de ocorrências são iguais")
