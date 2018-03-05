nota1 = float(input("1° nota: "))
nota2 = float(input("2° nota: "))
media = (nota1 + nota2) / 2

if media == 10:
    print("Aprovado com distinção.")
elif media >= 7:
    print("Aprovado.")
else:
    print("Reprovado.")
