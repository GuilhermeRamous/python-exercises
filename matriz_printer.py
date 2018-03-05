num_linhas = int(input("Número de linhas: "))
num_colunas = int(input("Número de colunas: "))
resultado = "" 

for v1 in range(num_linhas):
    print(str(v1 + 1) + "° linha: ")
    print("")

    for v2 in range(num_colunas):
        valor = input(str(v2 + 1) + "° coluna: ")

        resultado += valor + " "

        if v2 == num_colunas - 1:
            resultado += "\n"
            print()

print()
print(resultado)


        

        
