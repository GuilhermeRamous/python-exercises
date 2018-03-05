import random
import turtle

def estanatela(tar, tela):
    if tar.xcor() > tela.window_width() / 2 or tar.xcor() < - tela.window_width() / 2:
        return False
    elif tar.ycor() > tela.window_height() / 2 or tar.ycor() < - tela.window_height():
        return False
    else:
        return True

t = turtle.Turtle()
wn = turtle.Screen()

while estanatela(t, wn):
    if random.randrange(2) == 0:
        t.left(90)
    else:
        t.right(90)

    t.forward(50)

wn.exitonclick()
