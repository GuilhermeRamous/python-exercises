def grau_da_nota(nota):
    if nota >= 90:
        return "A"
    elif nota >= 80 and nota < 90:
        return "B"
    elif nota >= 70 and nota < 80:
        return "C"
    elif nota >= 60 and nota < 70:
        return "D"
    else:
        return "F"

for i in [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]:
    print("Grau de", i, ":", grau_da_nota(i))

    
