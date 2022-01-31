# Problem 16 - Power digit sum
# https://projecteuler.net/problem=16
def power_digit_sum(exponent):
    power = 2 ** exponent
    digits = []
    # Extract sum of digits of power. Otherwise, could use str indexing.
    while power > 0:
        digits.append(power % 10)
        power = power // 10
    
    return sum(digits)

power_digit_sum(1000)
