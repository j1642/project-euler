# Problem 16 - Power digit sum
# https://projecteuler.net/problem=16
from time_this import time_this


@time_this
def power_digit_sum(base: int, exponent: int) -> int:
    '''Find sum of digits of base^exponent.'''
    power = base ** exponent
    digits = []
    # Extract sum of digits of power. Could use str indexing instead.
    while power > 0:
        digits.append(power % 10)
        power = power // 10

    return sum(digits)


print(power_digit_sum(2, 1000))
