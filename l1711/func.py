def chooseCave():
    cave = ''
    while cave != '1' or cave != '2':
        cave = input('Выберите пещеру (1 или 2): ')
        return cave


def checkCave(choosenCave):
    from random import randint
    from time import sleep

    print('Вы приближаетесь к пещере...')
    sleep(2)
    print('Ее темнота заставляет вас дрожать от страха...')
    sleep(2)
    print('Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...')
    sleep(2)

    friendlyCave = randint(1, 2)

    if choosenCave == str(friendlyCave):
        print('...и делится с вами сокровищами.')
    else:
        print('...моментально вас съедает!')


def displayIntro():
    print('''
    Вы находитесь в землях, заселенных драконами.
    Перед собой вы видите две пещеры. В одной из них — дружелюбный дракон, который 
    готов поделиться с вами своими сокровищами. Во второй — жадный и голодный дракон,
    который мигом вас съест. В какую пещеру вы войдете? 
    (нажмите клавишу 1 или 2)
    ''')