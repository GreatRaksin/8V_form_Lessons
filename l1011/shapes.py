def draw_square(turtle, color, size, x, y):
    '''Рисует квадрат по параметрам'''
    turtle.up()
    turtle.color(color)
    turtle.goto(x, y)
    turtle.down()

    for i in range(4):
        turtle.fd(size)
        turtle.rt(90)


def draw_filled_square(turtle, color, size, x, y):
    '''Рисует закрашенный квадрат по параметрам'''
    turtle.up()
    turtle.color(color)
    turtle.fillcolor(color)  # добавили цвет заливки
    turtle.goto(x, y)
    turtle.down()

    turtle.begin_fill()  # начать заливку
    for i in range(4):
        turtle.fd(size)
        turtle.rt(90)
    turtle.end_fill()  # закончить заливку


def draw_filled_triangle(turtle, color, size, x, y):
    '''Рисует закрашенный треугольник по параметрам'''
    turtle.up()
    turtle.color(color)
    turtle.fillcolor(color)  # добавили цвет заливки
    turtle.goto(x, y)
    turtle.down()

    turtle.begin_fill()  # начать заливку
    for i in range(3):
        turtle.fd(size)
        turtle.lt(120)
    turtle.end_fill()  # закончить заливку


