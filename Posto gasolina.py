print("1. Álcool:")
print(" Preço por litro: R$ 1,90")
print(" a. Até 20 litros, desconto de 3% por litro")
print(" b. Acima de 20 litros, desconto de 5% por litro")
print("")
print("2. Gasolina:")
print("Preço por litro: R$ 2,50")
print(" a. até 20 litros, desconto de 4% por litro")
print(" b. acima de 20 litros, desconto de 6% por litro")

litros = float(input("Litros: "))
combustivel = int(input("Digite o combustível que deseja colocar em seu veículo: "))

if combustivel == 1:
    if litros <= 20:
        preço = litros * 3/100 * 1.90
    elif litros > 20:
        preço = litros * 5/100 * 1.90
if combustivel == 2:
    if litros <= 20:
        preço = litros * 4/100 * 2.50
    elif litros > 20:
        preço = litros * 6/100 * 2.50

print("Preço: R$", preço)
        
