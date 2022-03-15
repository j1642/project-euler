# Problem 43 - Sub-string Divisibility
# https://projecteuler.net/problem=43

import itertools

@time_this
def generate_pandigitals():
    'Return list of 0 to 9 pandigital numbers. E.g. 123456789.'
    digits = list(range(10))
    # itertools.permutations deals with items based on position, not values.
    #   If there are repeated elements in the iterable, there will be repeated
    #   permutations in the function output.
    pandigitals = list(itertools.permutations(digits))
    
    return pandigitals

@time_this
def test_pandigital_slices(pandigitals: list):
    '''From list of 0 to 9 pandigital numbers, find numbers in which the
    following conditions are all true:
    1. The concatenation of digits 2 through 4 is divisible by 2
    2. The concatenation of digits 3 through 5 is divisible by 3
    3. The concatenation of digits 4 through 6 is divisible by 5
    4. The concatenation of digits 5 through 7 is divisible by 7
    5. The concatenation of digits 6 through 8 is divisible by 11
    6. The concatenation of digits 7 through 9 is divisible by 13
    7. The concatenation of digits 8 through 10 is divisible by 17
    
    The first digit is digit 1, the second digit is digit 2, etc.
    '''
    slice_start = tuple(range(1, 8))
    divisors = (2, 3, 5, 7, 11, 13, 17)
    passed_tests = []
    
    for tup in pandigitals:
        for ind, start in enumerate(slice_start):
            concat_number = tup[start] * 100 + tup[start + 1] * 10 \
                + tup[start + 2]
            
            if concat_number % divisors[ind] == 0:
                continue
            else:
                break
        
        else:
            digits = []
            for digit in tup:
                digits.append(str(digit))
            digits = ''.join(digits)
            passed_tests.append(int(digits))
    
    return sum(passed_tests)
    
    
test_pandigital_slices(generate_pandigitals())

