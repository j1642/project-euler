# Problem 6 - Sum square difference
# https://projecteuler.net/problem=6
from time_this import time_this


@time_this
def sums_squares_difference(start: int, end: int) -> int:
    '''For integers 1 to 100, find the difference between the sum of their
    squares and the square of their sum.
    '''
    sum_of_squares = 0
    for i in range(start, end):
        # i * i seems faster than i ** 2
        sum_of_squares += i * i

    # Could include progressive summation in the for loop.
    square_of_sums = sum(range(start, end)) ** 2

    return square_of_sums - sum_of_squares


print(sums_squares_difference(1, 101))
