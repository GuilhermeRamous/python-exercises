import turtle
wn = turtle.Screen()
wn.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.pensize(10)

for color in ["#B0171F", "#8B1C62", "#9370DB", "#00FF7F"]:
    t.color(color)
    t.forward(150)
    t.right(90)
