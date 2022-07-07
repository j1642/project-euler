# Problem 10 - Summation of primes
# https://projecteuler.net/problem=10
from time_this import time_this


@time_this
def find_primes(max_num):
    '''Return the sum of all primes less than 2 million.'''
    # Searching for primes using trial division in slow. Using a prime sieve
    # like in later problems would be much faster.
    primes = []
    for test_num in range(2, max_num):
        for divisor in range(2, int(test_num ** 0.5) + 1):
            if test_num % divisor == 0:
                break
        else:
            primes.append(test_num)
    return sum(primes)

print(find_primes(2000000))
