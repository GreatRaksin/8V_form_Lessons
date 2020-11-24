'''Task 1. Нарисовать звездочки линиями'''
from turtle import *

t = Turtle()


def stars(turtle, size, lines):
    """Получаем черепашку, размер линии и количчество линий"""
    turtle.goto(0, 0)
    turtle.clear()
    turtle.lt(90)
    turtle.down()

    for line in range(lines):
        turtle.fd(size)
        turtle.bk(size)
        turtle.rt(360 / lines)

    turtle.up()

stars(t, 100, 255)


done()
