import turtle

def desenhabarra(t, h):
    t.left(90)
    t.forward(h)
    t.right(90)
    t.forward(20)
    t.write(str(h))
    t.forward(20)
    t.right(90)
    t.forward(h)
    t.left(90)

pen = turtle.Pen()
pen.color("red")
wn = turtle.Screen()
wn.bgcolor("black")

for i in [-10, 117, 200, 240, 160, 260, 220]:
    if i >= 200: pen.fillcolor("red")
    elif i >= 100 and i < 200: pen.fillcolor("yellow")
    else: pen.fillcolor("lightgreen")

    pen.begin_fill()
    desenhabarra(pen, i)
    pen.end_fill()

wn.exitonclick()
