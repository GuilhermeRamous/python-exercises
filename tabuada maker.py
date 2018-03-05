tabuada = int(input("Tabuada: "))
numero_final = int(input("Número final: "))

for i in range(numero_final):
    print(tabuada , "X", i, "=", i * tabuada)

print(tabuada, "X", i + 1, "=", (i + 1) * tabuada)
