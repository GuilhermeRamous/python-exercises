i = int(input())
resultado = ""

for t in range(i):
    value = int(input())
    summ = 1

    for div in range(2, value):
        if value % div == 0:
            summ += div

    resultado += str(summ) + "\n"  

print(resultado)

    
