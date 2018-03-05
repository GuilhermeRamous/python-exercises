def troca(string, velho, novo):
    if velho not in string:
        return string
    else:
        new_string = ""

        for i in string:
            if i != velho:
                new_string += i
            else:
                new_string += novo
        return new_string

string = input("String: ")
velho = input("Velho: ")
novo = input("Novo: ")
print()
print("Resultado:", troca(string, velho, novo))
            
