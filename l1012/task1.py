def list_com(array):
    new_array = []
    for number in array:
        if number % 2 == 0:
            number = number ** 2
        else:
            number = int(number ** 0.5)
        new_array.append(number)
    return new_array


print(list_com([1, 56, 34, 78, 55, 90, 11, 73]))