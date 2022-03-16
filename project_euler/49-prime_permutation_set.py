# Problem 49 - Prime Permutations
# https://projecteuler.net/problem=49

from collections import defaultdict

def is_prime(n: int):
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True

@time_this
def prime_sieve(max_range: int):
    '''This is the sieve of Eratosthnes. Othere sieves exist, and Wikipedia
    states that the sieve of Atkin is faster than this one.
    '''
    primes = []
    is_prime = [True] * (max_range)
    
    for num in range(2, int(max_range ** 0.5) + 1):
        if is_prime[num] is True:
            multiple = num * num
            while multiple < max_range:
                is_prime[multiple] = False
                multiple += num
                
    for ind, val in enumerate(is_prime):
        if val is True and ind != 0 and ind != 1:
            primes.append(ind)
    
    return primes

@time_this
def prime_perms():
    '''Find set of the three four-digit numbers which are all prime,
    permutations of one another, and are offset from each other by 3330.
    
    Two such sets exist. One is: 1487, 4817, 8147.
    '''
    primes = prime_sieve(10000)
    primes = [prime for prime in primes if prime > 999]
    
    for prime in primes:
        # Skip 1487. We are looking for the other set of primes.
        if prime == 1487:
            continue
        permutation_count = defaultdict(int)
        
        if is_prime(prime + 3330):
            if is_prime(prime + 2 * 3330):
                
                for num in [prime, prime + 3330, prime + 2 * 3330]:
                    digits = list(str(num))
                    sorted_digits = sorted(digits)
                    sorted_digits = ''.join(sorted_digits)
                    permutation_count[sorted_digits] += 1
                    
                    if permutation_count[sorted_digits] == 3:
                        for_concat = [str(prime), \
                                     str(prime + 3330), \
                                     str(prime + 2 * 3330)]
                        
    return ''.join(for_concat)
        
            
prime_perms()

