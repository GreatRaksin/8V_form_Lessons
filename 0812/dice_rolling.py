from random import randint

rolling = 'yes'

while rolling == 'yes' or rolling == 'y':
    res1 = randint(1, 6)
    res = randint(1, 6)
    rolling = input('Хотите бросить еще раз? (yes/y, no/n)\n')