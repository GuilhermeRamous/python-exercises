def baskara(a, b, c):
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        return "A equação passada não possui raizes reais"
    elif delta == 0:
        return "Raiz da equação:", -b / 2 * a
    else:
        return "Raizes da equação", (-b + delta) / 2 * a, (-b - delta) / 2 * a

a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))
print()
print(baskara(a, b, c))

