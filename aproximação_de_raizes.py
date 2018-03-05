def aprox_de_raiz(n):
	aprox = 0.5 * n
	betteraprox = 0.5 * (aprox + n / aprox)
	
	while aprox != betteraprox:
		aprox = betteraprox
		betteraprox = 0.5 * (aprox + n / aprox)
	
	return betteraprox

numero = int(input("Digite um número natural para aproximação de raiz: "))
print("Raiz quadrada de", numero,"=",  aprox_de_raiz(numero))

