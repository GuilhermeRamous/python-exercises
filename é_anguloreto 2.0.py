def é_anguloreto(x, y, z):
    if x > y and x > z:
        hipot = x
        catetos = (y ** 2 + z ** 2) ** 0.5
    elif y > x and y > z:
        hipot = y
        catetos = (x ** 2 + z ** 2) ** 0.5
    elif z > x and z > y:
        hipot = z
        catetos = (x ** 2 + y ** 2) ** 0.5
    else:
        return False
    if (hipot - catetos) < 0.000001:
        return True
    else:
        return False

print(é_anguloreto(15, 12, 9))
