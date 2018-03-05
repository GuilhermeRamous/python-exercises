import string

arquivo = open("28885.txt", "r")
lista = arquivo.readlines()
lista_nova = []
caracteres = []
caracteres_indesejados = []
palavras = []
alice = 0

for linha in lista:
    for letra in linha:
        if letra not in caracteres:
            caracteres.append(letra)

for char in caracteres:
    if char not in string.ascii_letters:
        caracteres_indesejados.append(char)

for linha in lista:
    for char in caracteres_indesejados:
        if char in linha:
            linha = linha.replace(char, " ")
    
    lista_nova.append(linha.lower())

for linha in lista_nova:
    palavras += linha.split()

for i in palavras:
    if i == "alice":
        alice += 1

print("O termo alice aparece no livro", alice, "vezes")
    









