from turtle import *

t = Turtle()

for i in range(4):
    for j in range(3):
        t.fd(100)
        t.rt(90)
    t.lt(180)

done()