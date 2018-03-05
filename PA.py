def PA(r, vi, i):
	resultado = str(vi) + " "
	for i in range(i):
		resultado += str(vi + r) + " "
		vi += r
	return resultado

razão = int(input("Razão: "))
valor_inicial = int(input("Valor inicial: "))
iteracao = int(input("Iterações: "))
print()
print(PA(razão, valor_inicial, iteracao))
	
