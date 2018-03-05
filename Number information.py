n = int(input("Digite um número menor que 1000: "))
desinencia = ""

if len(str(n)) == 1:
    if -1 < n > 1:
        desinencia = "s"
    print(n, ":", n, "unidade" + desinencia)
