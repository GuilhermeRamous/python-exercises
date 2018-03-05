i = int(input()) # Run time error in spoj, search more about and solve the problem
resultados = [] 

for a in range(i):
    valores = []
    numbers = []
    lista = input().split(" ")

    for b in lista:
        numbers.append(int(b))

    for c in range(2, numbers[0]):
        if c % numbers[1] == 0 and c % numbers[2] != 0:
            valores.append(c)

    resultados.append(valores) 


for d in resultados:
    saida = ""

    for e in d:
        saida +=  str(e) + " "
    
    print(saida)


        

