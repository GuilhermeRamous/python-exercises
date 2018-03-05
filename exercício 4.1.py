import turtle
wn = turtle.Screen()
t = turtle.Turtle()
wn.bgcolor("black")

for color in ["red", "yellow", "hotpink"]:
    t.color(color)
    t.forward(150)
    t.left(120)

wn.exitonclick()
