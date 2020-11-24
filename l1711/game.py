from l1711.func import *


if __name__ == '__main__':
    playAgain = 'y'
    while playAgain == 'yes' or playAgain == 'y':
        displayIntro()  # стартовый текст
        cave = chooseCave()  # выбираем пещеры
        checkCave(cave)  # проверяем пещеру

        playAgain = input('Хотите продолжить? ')