import string

livro = open("28885.txt", "r")
lista = livro.readlines() 
caracteres = []
caracteres_indesejados = []
lista_nova = []
palavras = []
dic = {} 
arquivo = open("output.txt", "w")

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
palavras.sort()

for i1 in palavras:
    if i1 not in dic:
        dic[str(i1)] = 1
    else:
        dic[str(i1)] += 1

for a, b in dic.items():
    arquivo.write(a + " " + str(b) + "\n")




    



