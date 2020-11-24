from turtle import *
from l1011.shapes import *

tina = Turtle()
tina.shape('turtle')

draw_square(tina, '#fd2a4c', 100, 50, -90)
draw_filled_square(tina, 'violet', 59, -100, -100)
draw_filled_triangle(tina, 'olive', 100, 200, 200)

done()