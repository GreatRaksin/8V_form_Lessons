from turtle import *

t = Turtle()
t.shape('turtle')


def circles(turtle, radius, length):
    turtle.goto(0, 0)
    turtle.clear()
    turtle.down()

    for i in range(length):
        turtle.circle(radius)
        turtle.rt(360 / length)

    turtle.up()

circles(t, 50, 10)

done()