def bissexto(x):
    """Retorna se o ano da string que representa uma data é bisexto ou não"""
    
    if int(x[6:10]) % 400 == 0:
        return True
    elif int(x[6:10]) % 4 == 0 and int(x[6:10]) % 100 > 0:
        return True
    else:
        return False

def função_dia(y):
    """retorna se o dia da string que representa uma data é possível, tomando como referência o mês
       nota: não checa o mês de fevereiro pois ele é um excessão aos outros meses, ele será checado no final"""
    
    if int(y[3:5]) == 1 or int(y[3:5]) == 3 or int(y[3:5]) == 5 or int(y[3:5]) == 7 or int(y[3:5]) == 8 or int(y[3:5]) == 10 or int(y[3:5]) == 12:
        return int(y[0:2]) <= 31
    elif int(y[3:5]) == 4 or int(y[3:5]) == 6 or int(y[3:5]) == 9 or int(y[3:5]) == 11:
        return int(y[0:2]) <= 30  

    
data = input("Digite uma data no formato dd/mm/aaaa: ")
mes = int(data[3:5])
dia = int(data[0:2])

if len(data) == 10:
    if bissexto(data) == False:
        if mes == 2:
            if dia <= 28 and mes <= 12:
                print("Data válida")
            else:
                print("Data inválida")
        else:
            if função_dia(data) == True and mes <= 12:
                print("Data válida")
            else:
                print("Data inválida")
    if bissexto(data):
        if mes == 2:
            if dia <= 29 and mes <= 12:
                print("Data válida")
            else:
                print("Data inválida")
        else:
            if função_dia(data) == True and mes <= 12:
                print("Data válida")
            else:
                print("Data inválida")
else:
    print("O data digitada não está no formato requerido")
