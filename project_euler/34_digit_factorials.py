# Problem 34 - Digit Factorials
# https://projecteuler.net/problem=34
# Unsure how to find upper bound (tested up to 10 mil)
# For largest possible 8-digit number (all nines),
#    8 * 9! = 2903040, seven digit product.
import math

@time_this
def sum_factorial_digit_nums(max_range: int):
    '''
    145 = 1! + 4! + 5!, the sum of the factorials of each digit. 
    Returns sum of similar numbers. Each num must have >1 digit to form a sum.
    '''
    nums = []
    for num in range(10, max_range):
        digits = list(str(num))
        sum_digit_factorials = sum([math.factorial(int(digit)) for digit in digits])
        if num == sum_digit_factorials:
            nums.append(num)
    return sum(nums)

sum_factorial_digit_nums(100000)
