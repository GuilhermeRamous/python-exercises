print("Candidatos: ")
print("")
print("a. Matheus Pinto")
print("b. Michel Não Tema")
print("c. Tirirola")
print("")

votos1 = 0
votos2 = 0
votos3 = 0
votos_nulos = 0
quantidade_eleitores = int(input("Quantidade de eleitores: "))

for i in range(quantidade_eleitores):
	voto = input(str(i + 1) + "° eleitor: ")
	
	if voto == "a" :
		votos1 += 1
	elif voto == "b":
		votos2 += 1
	elif voto == "c":
		votos3 += 1
	else:
		votos_nulos += 1

print("")
print("Votos para Matheus Pinto:", votos1)
print("Votos para Michel Não Tema:", votos2)
print("Votos para Tirirola:", votos3)
print("Votos nulos:", votos_nulos)
