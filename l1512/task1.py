def bin_sum(a, b):
    return bin(a + b)[2:]


def calculate(n1, n2, o):
    if o in 'add':
        return bin(n1 + n2)[2:]
    if o in 'multiply':
        return bin(n1 * n2)[2:]
    if o in 'subtract':
        return bin(n1 - n2)[2:]



'''


add  +
multiply  *
subtract  -
division   /

bin_sum(1, 5, 'multiply') -> '101'
'''


print(bin_sum(5, 6))

assert bin_sum(1, 1) == '10', 'should be 10'
assert bin_sum(0, 1) == '1', 'should be 1'
assert bin_sum(2, 2) == '100', 'should be 100'
assert bin_sum(51, 12) == '111111', 'should be 111111'