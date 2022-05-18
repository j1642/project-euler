# Problem 57 - Square root convergents (typo?)
# https://projecteuler.net/problem=57

# fractions.Fraction wasn't simplifying well. Not too bad to simplify manually.

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
    for depth in range(max_depth):
        numer, denom = 1, 2
        for _ in range(depth):
            numer += 2 * denom
            numer, denom = denom, numer
        numer += 1 * denom
        
        numerator_digits = list(str(numer))
        denominator_digits = list(str(denom))
        
        if len(numerator_digits) > len(denominator_digits):
            longer_numerator_count += 1
            
    return longer_numerator_count
    
square_root_convergence(1000)

