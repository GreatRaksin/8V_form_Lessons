from turtle import *

t = Turtle()
t.lt(90)
x_cor = 0  # сохраняю ее положение по иксу

for line in range(8):
    t.goto(x_cor, 0)  # переместилась в координаты

    t.down()
    t.fd(150)
    t.bk(150)  # нарисовала линию (одну)
    t.up()

    x_cor += 20


done()