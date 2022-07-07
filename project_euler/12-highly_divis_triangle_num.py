# Problem 12 - Highly divisible triangular number
# https://projecteuler.net/problem=12

'''
Find the first triangular number which has more than 500 divisors.
'''

from time_this import time_this


def find_divisors(number: int) -> set:
    '''Return set of divisors of a number, including 1 and the number itself'''
    divisors = []

    for divisor in range(1, int(number ** 0.5) + 1):
        if number % divisor == 0:
            # Low divisors
            divisors.append(divisor)
            # High divisors
            divisors.append(number // divisor)
    divisor_count = len(set(divisors))

    return divisor_count


@time_this
def highly_divis_tri_num() -> int:
    '''Generate triangular numbers and call find_divisors() for each.
    Return the first triangular number with more than 500 divisors.'''
    # Initialize triangle_nums with the first triangular number.
    triangle_nums = [1]
    # Initialize i as 2 because second triangluar number is 3 = 1 + 2.
    i = 2
    while True:
        # Do-it-yourself generator of sorts by using a stack.
        triangle_nums.append(triangle_nums.pop() + i)
        divisor_count = find_divisors(triangle_nums[0])
        if divisor_count > 500:
            return triangle_nums[0]
        i += 1


print(highly_divis_tri_num())
