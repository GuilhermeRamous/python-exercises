nota1 = float(input("1° nota: "))
nota2 = float(input("2° nota: "))
media = (nota1 + nota2) / 2

print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Média:", media)

if media > 9 and media <= 10:
    print("Grau: A")
    print("APROVADO!")
elif media > 7.5 and media <= 9:
    print("Grau: B")
    print ("APROVADO!")
elif media > 6 and media <= 7.5:
    print("Grau: C")
    print("APROVADO!")
elif media > 4 and media <= 6:
    print("Grau: D")
    print("REPROVADO!")
else:
    print("Grau: E")
    print("REPROVADO!")
