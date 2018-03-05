def par(x):
	if x % 2 == 0:
		return True
	else:
		return False
pares = 0
impares = 0

for i in range(10):
	n = int(input(str(i + 1) + " número: "))
	
	if par(n):
		pares += 1
	else:
		impares += 1

print("")
print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)

	
	
