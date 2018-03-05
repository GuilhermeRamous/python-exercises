quantidade_temperatura = int(input("Quantidade de temperaturas: "))
lista = []
media = 0

for i in range(quantidade_temperatura):
	temp = float(input("Temperatura: "))
	lista.append(temp)
	media += temp / quantidade_temperatura

print()
print("Maior temperatura:", max(lista)) 
print("Menor temperatura:", min(lista))	
print("Média:", media)
