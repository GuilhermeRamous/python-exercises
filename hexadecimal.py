print("1. Hex to Dec")
print("2. Dec to Hex")

op = int(input("Type an option "))
print("")

if op == 1:
    hexadecimal = input("Type your hex: ")
    exp = len(hexadecimal) - 1
    dec = 0

    for i in range(len(hexadecimal)):
        if hexadecimal[i:i + 1] == "a" or "A":
            value = 10
        elif hexadecimal[i:i + 1] == "b" or "B":
            value = 11
        elif hexadecimal[i:i + 1] == "c" or "C":
            value = 12
        elif hexadecimal[i:i + 1] == "d" or "D":
            value = 13
        elif hexadecimal[i:i + 1] == "e" or "E":
            value = 14
        elif hexadecimal[i:i + 1] == "f" or "F":
            value = 15
        else:
            value = int(hexadecimal[i:i + 1])

        dec += value * (16 ** exp)
        exp -= 1
    print(dec)

