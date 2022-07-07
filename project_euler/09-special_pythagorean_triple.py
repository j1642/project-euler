# Problem 9 - Special Pythagorean triplet
# https://projecteuler.net/problem=9
from time_this import time_this


@time_this
def find_pythagorean_triples(maximum_search):
    '''Return the integers and product of the only Pythagorean triplet where
    a + b + c = 1000.
    '''
    squares = []
    for num in range(2, maximum_search):
        squares.append(num * num)

    for a in range(2, maximum_search):
        for b in range(2, maximum_search):
            sum_squares_ab = a * a + b * b
            if a < b and sum_squares_ab in squares:
                c = int(sum_squares_ab ** 0.5)
                if a + b + c == 1000:
                    return f'{a} * {b} * {c} = {a * b * c}'

print(find_pythagorean_triples(450))
