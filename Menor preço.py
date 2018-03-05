preço1 = float(input("1° preço: R$ "))
preço2 = float(input("2° preço: R$ "))
preço3 = float(input("3° preço: R$ "))

if preço1 < preço2 and preço1 < preço3:
    print("Menor preço: R$", preço1)
elif preço2 < preço1 and preço2 < preço3:
    print("Menor preço: R$", preço2)
else:
    print("Menor preço: R$", preço3)
