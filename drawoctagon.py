import turtle
def drawoctagon(t, tam):
    for i in range(8):
        t.forward(tam)
        t.left(45)

t = turtle.Pen()
wn = turtle.Screen()

drawoctagon(t, 80)

wn.exitonclick()
        
