import turtle
wn = turtle.Screen()
wn.bgcolor("black")
t = turtle.Turtle()
t.color("darkblue")
t.shape("circle")  
t.penup()
t.speed(0)

for i in range(5, 100, 2):
    t.stamp()
    t.forward(i)
    t.left(-24)

wn.exitonclick()
    
