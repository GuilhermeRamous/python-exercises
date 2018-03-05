def prog_a(r, i, vi):
	resultado = str(vi)

	for i in range(i - 1):
		resultado += " " + str(vi + r)
		vi += r

	return resultado

razão = int(input("Razão: "))
iteração = int(input("Iteração: "))
valor_inicial = int(input("Valor inicial: "))
print()
print("Progressão aritimética:", prog_a(razão, iteração, valor_inicial))
		
