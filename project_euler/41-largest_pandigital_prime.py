# Problem 41 - Pandigital Prime
# https://projecteuler.net/problem=41

# Largest possible pandigital number has 9 digits and is 1 to 9 pandigital.
#    But this number may or may not be prime.

# Reordered code to build list of pandigitals then check for primes, for speed
#    and for extra practice.
# Also, I read that only length 4 and 7 pandigitals can be primes because of
#    digit sums. The other digit sums are all divisible by 3.
def is_prime(num: int):
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            return False
    return True


@time_this
def test_pandigitals(max_length: int):
    '''Return the largest number which is pandigital and prime.'''
    # Math library has a perm function tha gives amount of permutations
    # And itertools.permutation() exists.
    primes = []
    
    for num_length in range(1, max_length + 1):
        digits = list(range(1, num_length + 1))
        digits = [str(digit) for digit in digits]
        pandigitals = list(lexico_permute_string(digits))
        for pandigital_num in pandigitals:
            if is_prime(int(pandigital_num)):
                primes.append(int(pandigital_num))
                
    return max(primes)
        
        
def lexico_permute_string(s: str):
    '''
    Generate pandigital numbers.
    
    https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
    From StackOverflow.
    
    1. Find largest index j, such that a[j] < a[j + 1]. If no such index exists,
        the perm. is the last perm.
    2. Find largest index, k, greater than j, such that a[j] < a[k].
    3. Swap the value of a[j] with that of a[k].
    4. Reverse the sequence from a[j + 1] up to and including the final
        element a[n].
    '''
    a = sorted(s)
    n = len(a) - 1
    while True:
        yield ''.join(a)
        # 1. Find largest index, j, such that a[j] < a[j + 1]
        for j in range(n - 1, -1, -1):
            if a[j] < a[j + 1]:
                break
        # If not break,
        else:
            return
        # 2. Find largest index, k, greater than j such that a[j] < a[k]
        value = a[j]
        for k in range(n, j, -1):
            if value < a[k]:
                break
        # 3. Swap the value of a[j] with that of a[k]
        a[j], a[k] = a[k], a[j]
        # 4. Reverse the tail of the sequence
        a[j+1:] = a[j+1:][::-1]
        
test_pandigitals(9)

