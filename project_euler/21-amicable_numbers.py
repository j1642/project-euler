# Problem 21 - Amicable numbers
# https://projecteuler.net/problem=21
@time_this
def sum_all_amicables(less_than_this: int):
    amicables = []
    for i in range(2, less_than_this):
        # if i has part of an amiacable pair, is_amicable returns (True, other_num)
        counterpart = is_amicable(i)
        if isinstance(counterpart, int):
            amicables.append(i)
            amicables.append(counterpart)
    
    return sum(set(amicables))

def is_amicable(num: int):
    counterpart = sum_divisors(num)
    if sum_divisors(counterpart) == num and counterpart != num:
        return counterpart

def sum_divisors(num: int):
    # num itself is not included as a "proper divisor"
    low_divisors = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            low_divisors.append(i)
            
    high_divisors = []
    for divisor in low_divisors:
        high_divisors.append(num // divisor)
    # Remove num b/c it is not a "proper divisor"
    high_divisors.remove(num)
    
    all_divisors = list(set(low_divisors + high_divisors))
        
    return sum(all_divisors)

sum_all_amicables(10000)
