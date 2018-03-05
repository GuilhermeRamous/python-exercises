print("1. File duplo:")
print(" Até 5 kg: R$ 4.90/kg")
print(" Acima de 5 kg: R$ 5.80/kg")
print("")
print("2. Alcatra:")
print(" Até 5 kg: R$ 5.90/kg")
print(" Acima de 5 kg: R$ 6.80/kg")
print("")
print("3. Picanha:")
print(" Até 5 kg: R$ 6.90/kg")
print(" Acima de 5 kg: 7.80/kg")

tipo_de_carne = int(input("Digite qual tipo de carne deseja comprar: "))
quantidade = float(input("Quantidade (kg): "))
pagamento = input("Pagamento (c ou d): ")

if quantidade < 0 or tipo_de_carne > 3 and tipo_de_carne < 0:
    print("ERRO! Leia novamente o manual e execute o programa novamenete")
else:
    if tipo_de_carne == 1:
        string_carne = "File duplo"
        if quantidade <= 5:
            preço = quantidade * 4.90
        else:
            preço = quantidade * 5.80
    elif tipo_de_carne == 2:
        string_carne = "Alcatra"
        if quantidade <= 5:
            preço = quantidade * 5.90
        else:
            preço = quantidade * 6.80
    elif tipo_de_carne == 3:
        string_carne = "Picanha"
        if quantidade <= 5:
            preço = quantidade * 6.90
        else:
            preço = quantidade * 7.80

    if pagamento == "c" or pagamento == "C":
        desconto = "5%"
        preço = preço*(1 - 5/100)
        pagamento = "cartão de crédito Hipermercado Tabajara"
    else:
        desconto = "0%"
        pagamento = "dinheiro"

    print("Tipo de carne:", string_carne)
    print("Preço:", preço)
    print("Desconto:", desconto)
    print("Pagamento:", pagamento)        
    
