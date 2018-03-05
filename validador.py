def validador(nome, idade, sexo, salario, estado_civil):
	if len(nome) > 3 and 0 < idade < 150 and salario > 0 and sexo == "m" or sexo == "f" and estado_civil == "s" or estado_civil == "c" or estado_civil == "v" or estado_civil == "d":
		return True
	else:
		return False

nome = ""
idade = 0
sexo = ""
salario = 0
estado_civil = ""

while validador(nome, idade, sexo, salario, estado_civil) == False:
	nome = input("Nome: ")
	idade = int(input("Idade: "))
	sexo = input("Sexo: ")
	salario = float(input("Salário: "))
	estado_civil = input("Estado Civil: ")
	print("")

print("Correto!")

		
