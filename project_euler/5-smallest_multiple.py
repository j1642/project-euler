# Problem 5 - Smallest multiple
# https://projecteuler.net/problem=5
from time_this import time_this


@time_this
def smallest_mult(min_num: int, max_num: int) -> int:
    '''Find smallest number which is divisible by all integers from 1 to 20.
    2520 is given as the smallest num. divisible by all integers 1 to 10.'''
    for test_num in range(min_num, max_num, 2520):
        # Can optimize by removing some tests
        # E.g.: a number divisible by 8 is also divisible by 2 and 4
        # Better optimization from skipping 2520 between tests.
        # Only multiples of 2520 would still be divisible by integers 1 to 10.
        for i in range(11, 21):
            if test_num % i != 0:
                break
        else:
            return test_num

    print('No number found.')


print(smallest_mult(2520, 300100100))
