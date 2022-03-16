# Problem 46 - Goldbach/s Other Conjecture
# https://projecteuler.net/problem=46

@time_this
def prime_sieve_and_odd_composites(max_range: int):
    '''Sieve of Eratosthenes with added functionality to gather odd composite
    numbers.
    
    Returns a list of primes, a list of odd composite numbers, and an
    integer for disprove_goldbach() to use in generating a list of doubled squares..
    '''
    primes = []
    odd_composites = []
    is_prime = [True] * max_range
    
    for n in range(2, int(max_range ** 0.5) + 1):
        if is_prime[n] is True:
            composite = n * n
            while composite < max_range:
                is_prime[composite] = False
                composite += n
                
    for index, value in enumerate(is_prime):
        if value is True and index != 0 and index != 1:
            primes.append(index)
        if value is False and index % 2 == 1:
            odd_composites.append(index)
    
    return primes, odd_composites, max_range
        

@time_this
def disprove_goldbach(primes_composites_range: tuple):
    '''Find smallest odd composite number which cannot be expressed as the
    sum of a prime and a doubled square.
    '''
    primes = primes_composites_range[0]
    odd_composites = primes_composites_range[1]
    max_range = primes_composites_range[2]
    
    squares_2x = [2 * n ** 2 for n in range(1, max_range)]
    
    for composite in odd_composites:
        possible_primes = [prime for prime in primes if prime < composite]
        possible_squares_2x = \
                    [square_2 for square_2 in squares_2x if square_2 < composite]
        
        result = test_goldbach(composite, possible_primes, possible_squares_2x)
        if result:
            pass
        else:
            return composite
        
                            
def test_goldbach(composite: int, possible_primes, possible_squares_2x):
    for prime in possible_primes:
        for square_2x in possible_squares_2x:
            test_sum = square_2x + prime
            if test_sum == composite:
                #print(f'{composite} = {prime} + {square_2x}')
                return True
    return False
    
disprove_goldbach(prime_sieve_and_odd_composites(10000))

