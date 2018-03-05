import turtle

def drawtriangle(t, lado):
    for i in range(3):
        t.forward(lado)
        t.left(120)

t = turtle.Pen()
wn = turtle.Screen()

drawtriangle(t, 150)

wn.exitonclick()
