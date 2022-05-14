# Problem 56 - 
# https://projecteuler.net/problem=56

@time_this
def max_digit_sum():
    '''Find largest sum of the digits of a number a^b, where a and b are less
    than 100.
    '''
    largest_digit_sum = 0
    for a in range(1, 100):
        for b in range(1, 100):
            digits = list(str(a ** b))
            digits = [int(num) for num in digits]
            digit_sum = sum(digits)
            if digit_sum > largest_digit_sum:
                largest_digit_sum = digit_sum
    return largest_digit_sum

max_digit_sum()

