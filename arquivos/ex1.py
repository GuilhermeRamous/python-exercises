# Nesse programa retorna-se o número de notas que cada aluno possui

arquivo = open("notas_estudantes.dat", "r")


for x in arquivo:
    lista = x.split(" ")
    cont = 0

    for y in range(len(lista)):
        try:
            int(lista[y])
            cont += 1
        except:
            cont += 0

    if cont > 6:
        print(lista[0])
        

