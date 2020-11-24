from turtle import *

t = Turtle()

t.pensize(5)

for i in range(2):
    t.begin_fill()

    t.fd(100)
    t.rt(90)
    t.fd(200)
    t.rt(90)

    t.end_fill()


def draw_circle(turtle, color):
    turtle.pencolor(color)
    turtle.fillcolor(color)

    turtle.begin_fill()
    turtle.circle(45)
    turtle.end_fill()

m = int(input('Сколько времени горит светофор? '))

if m % 2 == 0:
    t.up()
    t.goto(50, -190)

    t.down()
    draw_circle(t, 'green')
else:
    t.up()
    t.goto(50, -100)

    t.down()
    draw_circle(t, 'red')

done()