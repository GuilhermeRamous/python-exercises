nome = input("Nome do arquivo: ")
extensao = input("Extensão do arquivo: ")
destino = input("Destino do arquivo: ")

arquivo = open("/" + destino + "/" + nome + "." + extensao, "w")
print()
print("Arquivo criado com sucesso!")
print()
question = input("Deseja escrever algo em seu arquivo? ")

if question == "S" or question == "s":
    cont = input("Digite o que deseja escrever: ")
    arquivo.write(cont)
