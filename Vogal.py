def vogal(x):
    if x == "a" or x == "A" or x == "e" or x == "E" or x == "o" or x == "O" or x == "i" or x == "I" or x == "u" or x == "U":
        return True
    else:
        return False
    
letra = input("Digite uma letra: ")

if vogal(letra):
    print(letra, "é vogal")
else:
    print(letra, "é consoante")
