# Problem 47 - Distinct Prime Factors
# https://projecteuler.net/problem=47

@time_this
def distinct_prime_factors(num_dist_pr_fctr: int, max_range: int):
    '''Find lowest set of x consecutive integers which each have x distinct prime
    factors, where x is the num_dist_pr_fctr parameter (number of distinct prime
    factors).
    E.g. 14 and 15 are consecutive and have two distinct prime factors (2, 7) and
    (3, 5).
    E.g. 644, 645, 646 each have three distinct prime factors. 644 = 2^2 * 7 * 23.
    Number of digits is irrelevant.
    '''
    consecutive_nums = []
    
    for n in range(2, max_range):
        factors = []
        prime_factors = []
        # Collect factors
        for divisor in range(2, int(n ** 0.5) + 1):
            if n % divisor == 0:
                factors.append(divisor)
                factors.append(n // divisor)
        #Test if factors are prime
        for factor in factors:
            if is_prime(factor):
                prime_factors.append(factor)
        dist_prime_factors = set(prime_factors)
        
        dist_prime_factor_count = len(prime_factors)
    
        if dist_prime_factor_count == num_dist_pr_fctr:
            consecutive_nums.append(n)
            try:
                # If integer at start of consecutive_nums is num_dist_pr_fctr (int)
                #   steps less than n, then they are part of consecutive series.
                if consecutive_nums[-1 * num_dist_pr_fctr] == \
                    n - num_dist_pr_fctr + 1:
                    
                    return consecutive_nums
                else:
                    # If a consecutive set hasn't been found, remove the first value
                    #   from consecutive_nums.
                    del consecutive_nums[-1 * num_dist_pr_fctr]
            except IndexError:
                pass
    return None
            
def is_prime(n: int):
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True


distinct_prime_factors(4, 1000000)

