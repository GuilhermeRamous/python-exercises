def bissexto(x):
    if x % 100 > 0: return x % 4 == 0
    else: return x % 400 == 0

ano = int(input("Digite um ano: "))

if bissexto(ano) == True:
    print(ano, "é bissexto")
else:
    print(ano, "não é bissexto")
    
