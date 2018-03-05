""" Pedro e Paulo sempre costumam correr de manhã cedo e eles sempre correm no mesmo circuito. Hoje eles decidiram marcar o tempo que cada um conseguia completar o circuito, enquanto um corria o outro marcava o tempo.

Pedro está aprendendo a programar no colégio e sempre que possível ele gosta de colocar suas habilidades à prova.

Ajude Pedro a fazer um programa simples, onde tendo o tempo de cada um diga qual dos dois completou o circuito em menos tempo, como Pedro que teve a ideia do programa ele se considera ganhador em caso de empate"""

pedro_time = float(input("Pedro: "))
paulo_time = float(input("Paulo: "))
print("")
'
if pedro_time < paulo_time or pedro_time == paulo_time:
	print("Pedro")
else:
	print("Paulo")
