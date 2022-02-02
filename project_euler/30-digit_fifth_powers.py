# Problem 30 - Digit fifth powers
# https://projecteuler.net/problem=30

# Tested up to 10 mil, same as 1 mil
# Actual upper bound is probably closer to 6 * 9^5 = 354294 (six digits)

@time_this
def digit_5th_powers(max_range: int):
    '''Return sum of numbers which equal the sum of 5th power of their digits
    
    Similar to 1634 = 1^4 + 6^4 + 3^4 + 4^4, except using 5th power.'''
    nums = []
    for num in range(2, max_range):
        # Get sum of 5th power of digits
        digit_sum = 0
        for digit in str(num):
            digit_sum += int(digit) ** 5
            
        if num == digit_sum:
            nums.append(num)
    
    return sum(nums)

digit_5th_powers(1000000)
