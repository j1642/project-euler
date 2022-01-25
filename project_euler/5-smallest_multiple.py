# Problem 5 - Smallest multiple
# https://projecteuler.net/problem=5
# Optimization 1 - Don't check mod 2-10
@time_this
def smallest_mult(min_num, max_num):
    for test_num in range(min_num, max_num):
        # Can optimize by removing some tests
        # E.g.: a number divisible by 8 is also divisible by 2 and 4
        for i in range(11, 21):
            if test_num % i != 0:
                break
        else:
            return test_num

# Takes ~1 sec to check ~10 million numbers
smallest_mult(230802560, 232802560)
