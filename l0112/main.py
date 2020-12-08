def mult_3_or_5(number):
    sum = 0  # количество всех чисел
    sum_1 = 0  # сумма всех чисел
    for num in range(1, number):  # строим последовательность
        if (num % 3) == 0 or (num % 5) == 0:
            sum = sum + 1
            sum_1 += num
    return sum, sum_1


print(mult_3_or_5(0))

"""Task 2. Посчитать гласные буквы в строке/строках"""


def vowel_count(string):
    vowel = 'aeiouаеиоуюя'
    end = []
    for letter in string:
        if letter in vowel:
            end.append(letter)
    return end, len(end)


print(vowel_count('hello guys у меня все найс'))

'''Task 3. Определить пиковые числа. Число называется пиковым,
если в нем количество десятков больше количества единиц и сотен'''
# bit.ly/ConsPro <- Конспект 2\3


def fade_number(number):
    n1 = number // 100  # сотни
    n2 = number % 100
    n3 = n2 % 10  # единицы
    n4 = n2 // 10  # десятки

    return n3 < n4 > n1


print(fade_number(282))

