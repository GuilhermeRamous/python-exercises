import random

numero_certo = random.randrange(11)
numero_chute = ""

while numero_certo != numero_chute:
	print("")
	numero_chute = int(input("Digite um número de 0 a 10:"))
	if numero_chute == numero_certo:
		print("Você acertou!")
	else:
		print("Você errou. Tente novamente")
