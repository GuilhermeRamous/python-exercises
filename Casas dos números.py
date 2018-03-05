def desinencia(x, y, z):
    if int(str(x)[y:z]) > 1:
        return "s"
    else:
        return ""
        
n = int(input("Digite um número natural menor que 1000: "))

if n >= 1000:
    print("O número digitado não é válido!")
else:
    if len(str(n)) == 1:
        print(n, "=", n, "unidade" + desinencia(n, 0, 1))
    elif len(str(n)) == 2:
        print(n, "=", str(n)[0:1], "dezena" + desinencia(n, 0, 1) + " e", str(n)[1:2], "unidade" + desinencia(n, 1, 2))
    elif len(str(n)) == 3:
        print(n, "=", str(n)[0:1], "centena" + desinencia(n, 0, 1) + ",", str(n)[1:2], "dezena" + desinencia(n, 1, 2) + " e", str(n)[2:3], "unidade" + desinencia(n, 2, 3))
        
    
