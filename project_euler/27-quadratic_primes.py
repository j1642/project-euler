# Problem 27 - Quadratic primes
# https://projecteuler.net/problem=27
# Originally, takes >3 sec to test two n values
# Optimization 1 - b must be prime (therefor b must be >= 2)
#    when n = 0, n^2 + an + b = b, so b must be prime for search to continue
# Optimiz. 1 brings speed to ~1 sec for 3 n values, ~1.11 sec for 100 n

@time_this
def quad_primes(max_n: int):
    primes_neg999_pos1000 = []
    for b in range(2, 1000):
        if is_prime(b):
            primes_neg999_pos1000.append(b)
    
    max_num_primes = 0
    consecutive_primes = {}
    for a in range(-999, 1000):
        for b in primes_neg999_pos1000:
            for n in range(0, max_n):
                test_num = n * n + a * n + b
                # Avoid taking square root of negative numbers
                if test_num < 0:
                    break
                elif is_prime(n * n + a * n + b):
                    if (a, b) in consecutive_primes.keys():
                        consecutive_primes[(a, b)] += 1
                    else:
                        consecutive_primes[(a, b)] = 1
                else:
                    break
    longest_consec_primes = max(consecutive_primes, key=consecutive_primes.get)
    
    print(f' a * b = {longest_consec_primes[0] * longest_consec_primes[1]}')
    return f'For (a, b) = {longest_consec_primes}: longest consecutive primes =\
    {consecutive_primes[longest_consec_primes]}'
    
    
def is_prime(num: int):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
    

quad_primes(100)
