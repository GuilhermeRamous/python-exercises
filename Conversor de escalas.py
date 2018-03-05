print("1. Celsius - Fahrenheit")
print("2. Fahrenheit - Celsius")

op = int(input("Digite qual operação deseja fazer: "))
print("")

if op == 1:
    tc = int(input("Celsius: "))
    print(tc ,"°C =", tc / 100, "°F")

if op == 2:
    tf = int(input("Fahrenheit: "))
    print(tf, "°F =", (tf - 32) / 180, "°C")
    
