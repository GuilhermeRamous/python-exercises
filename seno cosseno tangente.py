from math import sin, cos, tan, radians
print("1. Seno")
print("2. Cosseno")
print("3. Tangente")
op = int(input("Digite a operação que deseja fazer: "))
print("")

if op == 1:
    grau = int(input("Grau: "))
    print("Seno de", grau, "° =", sin(radians(grau)))

if op == 2:
    grau = int(input("Grau: "))
    print("Cosseno de", grau, "° =", cos(radians(grau)))

if op == 3:
    grau = int(input("Grau: "))
    print("Tangente de", grau, "° =", tan(radians(grau)))
    
        
