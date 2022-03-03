# Problem 35 - Circular Primes
# https://projecteuler.net/problem=35
# Calling is_prime once per num should be more efficient than calling once
#   per each rotated num
# Prime sieve would likely be faster.

@time_this
def circular_primes(max_range: int):
    '''Check if rotated digits of a nummber are all prime.
    E.g. 197 -> 719 -> 971 has three permutations, not 3! permutations.'''
    
    circular_primes = []
    
    for num in range(2, max_range):
        rotations = []
        rotations.append(num)
        digits = list(str(num))
        for i in range(len(digits) - 1):
            digits.insert(0, digits.pop())
            rotations.append(int(''.join(digits)))
        if is_prime(rotations):
            circular_primes.append(num)
    
    return f'No. circular primes below {max_range}: {len(circular_primes)}'
    
def is_prime(rotations: list):
    for num in rotations:
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                return False
    return True

circular_primes(1000000)

