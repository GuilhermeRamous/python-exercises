import turtle

pen = turtle.Pen()
wn = turtle.Screen()
tam = 20

for i in range(5):
    for v in range(4):
        pen.forward(tam)
        pen.left(90)
    tam += 20
    pen.right(90)
    pen.forward(10)
    pen.left(90)
    
wn.exitonclick()
