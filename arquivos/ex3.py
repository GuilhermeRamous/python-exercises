
arquivo = open("notas_estudantes.dat", "r")

for x in arquivo:
    lista = x.split(" ") 
    notas = []

    for y in lista:
        try: 
            int(y)
            notas.append(int(y))
        except:
            pass
    print("Nota máxima de " + lista[0] + ":", max(notas))
    print("Nota mínima de " + lista[0] + ":", min(notas))
    print()
