# Problem 57 - Square root convergents (typo?)
# https://projecteuler.net/problem=57

# fractions.Fraction wasn't simplifying well. Not too bad to simplify manually.
# Optimization 1: continue working from previous continued fraction,
# rather than starting from scratch.
# Results in ~10x speed improvement for this problem.
#
# Optimization 2: Use int(math.log(x, 10)) to get number of digits,
# rathern than len(list(str(x))). Results in ~5x speed improvement.

import math
from time_this import time_this

@time_this
def square_root_convergence(max_depth: int):
    '''Return amount of fractions with a longer numerator than denominator
    for the first 1000 expansions of the square root of 2 converging equations.
    
    1 + 1/2 = 3/2 = 1.5 (numerator and denominator have equal lengths)
    1 + 1/(2 + 1/2) = 7/5 = 1.4
    1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
    Etc.
    '''
    longer_numerator_count = 0
    numer, denom = 1, 2
    
    for _ in range(max_depth):
        numer += 2 * denom
        # Simplify inverted fraction. E.g. 1 / (3/2) = 2/3
        numer, denom = denom, numer
        # Convert mixed number to improper fraction. E.g. 1 1/2 -> 3/2
        numer += 1 * denom
        
        #numerator_digits = list(str(numer))
        #denominator_digits = list(str(denom))
        numerator_digit_count = int(math.log(numer, 10))
        denominator_digit_count = int(math.log(denom, 10))
        if numerator_digit_count > denominator_digit_count:
            longer_numerator_count += 1
        
        # Reset for next step of the continued fraction calculation.
        numer -= denom
            
    return longer_numerator_count


print(square_root_convergence(1000))

