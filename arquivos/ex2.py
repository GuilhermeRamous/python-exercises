# Nesse programa calcula-se a media de cada aluno que se encontra no arquivo

arquivo = open("notas_estudantes.dat", "r")

for x in arquivo:
    lista = x.split(" ")
    divisor = 0
    dividendo = 0
    
    for y in lista:
        try:
            dividendo += int(y)
            divisor += 1
        except:
            divisor += 0

    print("Media de " + lista[0] + ":", dividendo / divisor)

