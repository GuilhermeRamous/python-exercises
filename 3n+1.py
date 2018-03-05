def cjc(n):
	resultado = str(n)

	if n == 1:
		return n
	elif n <= 0 or n > 10 ** 6 or int(n) != n:
		return "O valor de entrada deve ser inteiro, diferente de zero e menor que 1 milhão."
	else:
		while n != 1:
			if n % 2 == 0:
				n /= 2
				resultado += " " + str(n)
			else:
				
				n = 3 * n + 1

				resultado += " " + str(n)

	return resultado


numero = int(input("Número: "))
print()
print(cjc(numero))
