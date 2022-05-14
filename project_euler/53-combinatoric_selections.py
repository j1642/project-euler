# Problem 53 - Combinatoric Selections
# https://projecteuler.net/problem=53
from math import factorial

@time_this
def combinatoric_selections(max_range: int):
    '''Return amount of non-distinct values greater than 1 million for 
    (n r) = n!/(r!(n-r)!), where r is less than or equal to n and n is
    between or equal to 1 and 100.
    
    (n r) represents the number of ways to select r items from a set of
    n items.
    '''
    count = 0
    for n in range(1, max_range):
        for r in range(0, n + 1):
            value = factorial(n) / (factorial(r) * factorial(n - r))
            if value > 1000000:
                count += 1
    return count
    
    
combinatoric_selections(101)

