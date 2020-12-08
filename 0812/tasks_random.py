from random import *

''' <- randint(a, b) - возвращает случайно сгенерированное число от a до b
string = input('Введите фразу: ')

for i in range(5):
    random_num = randint(0, len(string) - 1)
    print(string[random_num])
'''
string = 'sgskhjf'
print(choice(string))  # <- возвращает случайный символ из строки

for i in range(randrange(1, 10)):  # <- задание случайного количества повторений цикла
    print(i)