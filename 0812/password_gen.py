from tkinter import *
from random import *
from string import *
from pyperclip import *

app = Tk()  # инициализируем окно программы
app.geometry('400x400')  # устанавливаем размеры окна
app.resizable(0, 0)  # делаем окно фиксированным по размеру
app.title('Генератор паролей | PG')

Label(app, text='PASSWORD GENERATOR', font='arial 15 bold').pack()
pass_label = Label(app, text='PASSWORD LENGTH', font='arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(app, from_=8, to_=32, textvariable=pass_len, width=15).pack()

pass_str = StringVar()


def Generator():
    password = ''
    for i in range(4):
        password = choice(ascii_lowercase) + \
                   choice(ascii_uppercase) + \
                   choice(digits) + \
                   choice(punctuation)
    for j in range(pass_len.get() - 4):
        password = choice(ascii_lowercase) + \
                   choice(ascii_uppercase) + \
                   choice(digits) + \
                   choice(punctuation)
    pass_str.set(password)


Button(app, text='Generate!', command=Generator).pack()
Entry(app, textvariable=pass_str).pack()

app.mainloop()