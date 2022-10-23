# Problem 63 - Powerful Digit Sums
# https://projecteuler.net/problem=63

# The square of any two digit number will have more than two digits, etc.
# Therefore all bases to these exponents must be single digits.

from time_this import time_this

@time_this
def count_n_powers_with_n_digits():
    count = 0
    base = 0
    len_digits = 0
    # Any two digit base will not yield a two digit square, cube, etc.
    # Base loop ends at 8 + 1 = 9. Going to 10 will cause infinite loop.
    # Exclude 0 as base b/c question specifies positive integers.
    while base < 9:
        exponent = 0
        base += 1
        # Skip 0 as exponent because it will not lead to a 0 digit num.
        while exponent <= len_digits:
            exponent += 1
            num = base ** exponent
            len_digits = len(str(num))
            if exponent == len_digits:
                count += 1
                # Only print 1 once. Avoids 1^1, 1^2, 1^3, etc.
                if num == 1:
                    break
    return count


print(count_n_powers_with_n_digits())

