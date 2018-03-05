""" O programa serve para calcular quanto tempo demorará para que a população A supere numericamente a população B"""

a = int(input("População A: "))
taxa_a = float(input("Taxa de crescimento: "))
print("")
b = int(input("População B: "))
taxa_b = float(input("Taxa de crescimento: "))

if a > b:
	print("A população A já é superior numericamente à população B.")
elif taxa_a < taxa_b:
	print("A população A nunca será superior numericamente à população B, a não ser que a sua taxa de crescimento mude.")
else:
	anos = 0
	while a < b:
		a += a * taxa_a / 100
		b += b * taxa_b / 100
		anos += 1
	
	print("Resultado:", anos)
	

