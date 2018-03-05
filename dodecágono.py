import turtle
wn = turtle.Screen()
wn.bgcolor("black")
t = turtle.Turtle()
t.left(30)
t.color("white")

for i in range(12):
    t.forward(30)
    t.left(30)

wn.exitonclick()
    
