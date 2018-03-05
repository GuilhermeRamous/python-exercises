import turtle
def poligono(t, comprimento, numlados):
    for i in range(numlados):
        t.forward(comprimento)
        t.left(360 / numlados)

def circulo(t, raio):
    comprimento = (2 * 3.1415 * raio) / 360
    poligono(t, comprimento, 360)

pen = turtle.Pen()
wn = turtle.Screen()
circulo(pen, 30)

wn.exitonclick()
    
    
