# Problem 48 - Self Powers
# https://projecteuler.net/problem=48

@time_this
def big_sum_final_digits(max_exponent: int):
    '''Return last ten digits of the sum of all i**i from 1 to max_exponent,
    inclusive.
    '''
    total_sum = 0
    for n in range(1, max_exponent + 1):
        total_sum += n ** n
        
    return str(total_sum)[-10:]
        
big_sum_final_digits(1000)

