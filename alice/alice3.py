import string

arquivo = open("28885.txt", "r")
lista = arquivo.readlines()
caracteres = []
caracteres_indesejados = []
lista_nova = []
palavras = []
maior = ""

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

    lista_nova.append(linha)

for linha in lista_nova:
    novas_palavras = linha.split()

    for i in novas_palavras:
        if i not in palavras:
            palavras.append(i.lower())

for i in palavras:
    if len(i) > len(maior):
        maior = i

print("A palavra mais longa do texto é", maior)

