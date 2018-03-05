def para_segundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos

horas = float(input("Horas: "))
minutos = float(input("Minutos: "))
segundos = float(input("Segundos: "))
print(horas, "hora(s),", minutos, "minutos(s) e", segundos, "segundo(s) =", int(para_segundos(horas, minutos, segundos)), "segundo(s)")
