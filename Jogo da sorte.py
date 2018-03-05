import random
import math

numero_da_sorte = int(input("Aposte um número que se encaixe no intervalo [0; 10): "))
numero_sorteado = random.random() * 10

print("AGORA CUIDADO! ESCOLHA 1 OU 2! ISSO PODE DETERMINAR SE VC SERÁ UM VENCEDOR OU PERDEDOR!")
um_ou_dois = int(input("Digite aqui a sua escolha: "))

if um_ou_dois == 1:
    numero_sorteado = math.floor(numero_sorteado)

elif um_ou_dois == 2:
    numero_sorteado = math.ceil(numero_sorteado)

else:
    print("O valor que vc digitou não é nem 1 nem 2. Rode o programa novamente e faça de maneira correta o processo.")


print("")
if numero_sorteado == numero_da_sorte:
    print("PARABÉNS VC ACERTOU! VOCÊ É UM VENCEDOR!")

else:
    print("VISH! PARECE QUE VC PERDEU! VOCÊ É UM PERDEDOR!")
    print("Número correto:", numero_sorteado)
    
