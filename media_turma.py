quantidade_turma = int(input("Quantidade de turmas: "))
media = 0
msg = ""
print("")

for i in range(quantidade_turma):
	media += int(input("Quantidade de alunos na " + str(i + 1) + "° turma: ")) / quantidade_turma
	
	if media * quantidade_turma > 40:
		msg = "Há salas com muitos alunos, reportar a direção da escola."
	else:
		msg = "Tudo está correto! Ótimo trabalho!"
print("")
print("Média de alunos por turma:", media)
print(msg)
