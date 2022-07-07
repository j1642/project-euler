# Problem 3 - Largest Prime Factor
# https://projecteuler.net/problem=3
from time_this import time_this

@time_this
def get_factors(number: int):
    '''Find factors of number argument.'''
    found_factors = []
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            found_factors.append(divisor)
            found_factors.append(number // divisor)
    return found_factors


# Pretty fast
@time_this
def max_prime(factors: list):
    '''Return largest prime number in factors argument.'''
    primes = []
    for num in factors:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return max(primes)

factors = get_factors(600851475143)
print(max_prime(factors))
