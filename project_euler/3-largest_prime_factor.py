# Problem 3 - Largest Prime Factor
# https://projecteuler.net/problem=3
@time_this
def get_factors(number: int):
    factors = []
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0: 
            factors.append(i)
    return factors

# Pretty fast
@time_this
def is_prime(factors: list):
    primes = []
    for num in factors:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return max(primes)

factors = get_factors(600851475143)
is_prime(factors)
