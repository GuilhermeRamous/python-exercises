print("           Até 5 kg           Acima de 5 kg")
print("         ______________       ______________")
print("Morango  R$ 2.50 por kg       R$2.20 por kg")
print("Maçã     R$ 1.80 por kg       1.50 por kg")
print("")
print("Se comprar mais de 8 kg ou ustrapassar R$ 25,00 o preço, receberá desconto de 10%")

morango_kg = float(input("Quilograma de morangos: "))
maçã_kg = float(input("Quilograma de maçãs: "))

if morango_kg < 0 or maçã_kg < 0:
    print("Valores negativos não são aceitos para representação de quilogramas")
else:
    if morango_kg <= 5:
            preço_morango = morango_kg * 2.50
    else:
            preço_morango = morango_kg * 2.20

    if maçã_kg <= 5:
            preço_maçã = maçã_kg * 1.80
    else:
            preço_maçã = maçã_kg * 1.50

    preço_total = preço_morango + preço_maçã

    if preço_total > 25 or morango_kg + maçã_kg > 8:
        preço_total = preço_total*(1 - 10/100)

    print("Preço total:", preço_total)
            



