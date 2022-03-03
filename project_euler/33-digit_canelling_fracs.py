# Problem 33 - Digit Cancelling Fractions
# https://projecteuler.net/problem=33
import functools, math

@time_this
def find_digit_cancelling_fracs():
    '''
    Find fractions that contain two digit numerators and denominators which
    appear to simplify by cancelling a shared digit, but do not actually
    simplify in that way, for fractions less than 1.
    E.g. 49/98 = 4/8, but cannot be obtained simply by cancelling the nines.
    Fractions like 10/20 are not to be included.
    '''
    numerators = []
    denominators = []
    
    for denominator in range(10, 100):
        for numerator in range(10, denominator):
            numer_digits = list(str(numerator))
            denom_digits = list(str(denominator))
            for digit in numer_digits:
                # Test for equality between original and "simplified" fraction
                if digit in denom_digits and int(digit) != 0:
                    shared_digit = digit
                    numer_over_denom = numerator/denominator

                    numer_digits.remove(shared_digit)
                    denom_digits.remove(shared_digit)

                    try:
                        simplified_numer_over_denom = int(numer_digits[0]) \
                                                    / int(denom_digits[0])
                    except ZeroDivisionError:
                        continue
                    if numer_over_denom == simplified_numer_over_denom:
                        numerators.append(numerator)
                        denominators.append(denominator)
                        
    # Report simplified donominator of product of the four found fractions.
    # Reduce() reduces the iterable into a sigle value.
    #    In this case, it gives the product of numers list.
    #    x is the accumulator value, y is the next value from the iterable.
    pdt_numers = functools.reduce(lambda x, y: x*y, numerators)
    pdt_denoms = functools.reduce(lambda x, y: x*y, denominators)
    grtst_comm_denom = math.gcd(pdt_numers, pdt_denoms)
    return int(pdt_denoms / grtst_comm_denom)
    
find_digit_cancelling_fracs()
