import turtle

numlados = int(input("Número de lados de seu polígono: "))
comprimento = float(input("Comprimento dos lados de seu polígono: "))
t = turtle.Pen()
t.color("red")
wn = turtle.Screen()
wn.bgcolor("black")

for i in range(numlados):
    t.forward(comprimento)
    t.right(360 / numlados)

wn.exitonclick()
