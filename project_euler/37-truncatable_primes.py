# Problem 37 - Truncatable Primes
# https://projecteuler.net/problem=37

# Searching list of primes is ~180x slower than calculatng whether truncated
#    numbers are each prime for max_range of 1 million.

@time_this
def find_primes(max_range: int):
    
    primes = []
    for num in range(2, max_range):
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                break
        else:
            primes.append(num)
    return primes

@time_this
def is_truncatable(primes: list):
    '''Given list of primes, Return sum of truncatable primes.
    
    Single digit primes are not considered truncatable.
    E.g. 3797 -> 797 -> 97 -> 7 are all prime (remove left-most digit).
    Also, 3797 -> 379 -> 37 -> 3 are primes (remove right-most digit).
    Therefore, 3797 is considered a trunctable prime.
    
    Problem states that there are 11 truncatable primes from both left
    and right.'''
    # Alternatively, a "while len(truncatable_primes) < 11" loop would work.
    truncatable_primes = []
    
    # Exclude single digit primes from truncatable checks
    for prime in primes[4:]:
        truncs = []
        prime = str(prime)
        
        for i in range(1, len(prime)):
            # Progressively strip off right-most digit, working to the left.
            truncs.append(int(prime[:-i]))
            # Progressively strip off left-most digit, working to the right.
            truncs.append(int(prime[i:]))
        
        # Check whether all truncated numbers are also prime.
        if is_prime(truncs):
            truncatable_primes.append(int(prime))
    
    return sum(truncatable_primes)

def is_prime(truncs: list):
    for num in truncs:
        if num < 2:
            return False
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                return False
    return True
    
# is_trunc() searching primes list approach takes 77 sec for 1 mil
# is_trunc() is_prime() approach takes 0.43 sec for 1 mil
is_truncatable(find_primes(1000000))

