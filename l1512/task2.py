a = [i for i in range(1, 11)]
'''Аналог:
a = []
for i in range(1, 11):
    a.append(i)
'''

a1 = [i ** 2 for i in range(1, 51) if i % 2 == 0]
'''Аналог:
a2 = []
for i in range(1, 51):
    if i % 2 == 0:
        a2.append(i ** 2)
'''

'''Заполнить массив случайными числами (-1000, 1000) в случайном промежутке
(5, 10)'''
from random import randint
b = [randint(-1000, 1000) for i in range(randint(5, 10))]
print(b)


'''Заполнить массив английским алфавитом'''
import string
c = [i for i in string.ascii_uppercase]
print(c)

'''Заполнить массив английскими буквами, с четным индексом'''
alph = string.ascii_letters
d = [alph[i] for i in range(len(alph)) if i % 2 == 0]
print(d)
