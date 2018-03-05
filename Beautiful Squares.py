import turtle

def desenhaquadrado(t, tam):
    for i in range(4):
        t.forward(tam)
        t.left(90)

t = turtle.Turtle()
t.color("hotpink")
t.pensize(5)
wn = turtle.Screen()
wn.bgcolor("lightgreen")

for i in range(5):
    desenhaquadrado(t, 20)
    t.penup()
    t.forward(50)
    t.pendown()

wn.exitonclick()


