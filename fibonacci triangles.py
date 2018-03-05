import turtle

def desenhatriangulocolorido(t, tam):

    for i in ["pink", "red", "blue"]:
        t.color(i)
        t.forward(tam)
        t.left(120)

pen = turtle.Pen()
pen.pensize(3)
wn = turtle.Screen()
wn.bgcolor("black")

pen.speed(0)
tamanho = 20
for i in range(40):
    desenhatriangulocolorido(pen, tamanho)
    tamanho += 10
    pen.right(18)

wn.exitonclick()
