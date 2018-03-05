def triangle_check(x, y, z):
    if abs(y - z) < x < y + z and abs(x - z) < y < x + z and abs(x - y) < z < x + y:
        return True
    else:
        return False
    
lado1 = float(input("1° lado: "))
lado2 = float(input("2° lado: "))
lado3 = float(input("3° lado: "))

if triangle_check(lado1, lado2, lado3):
    print("Pode formar um triângulo: sim")

    if lado1 == lado2 and lado2 == lado3:
        print("Tipo de triângulo: equilátero")
    elif lado1 != lado2 and lado1 != lado3 and lado2 != 3:
        print("Tipo de triângulo: escaleno")
    else:
        print("Tipo de triângulo: isósceles")
else:
    print("Pode formar um triangulo: não")

    
