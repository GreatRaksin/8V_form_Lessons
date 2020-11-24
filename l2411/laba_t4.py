from turtle import *

t = Turtle()

t.rt(90)

for i in range(4):
    t.circle(45)  # рисование круга
    t.up()
    t.fd(90)
    t.down()

done()