# Problem 29 - Distinct powers
# https://projecteuler.net/problem=29
@time_this
def distinct_powers(max_range):
    'Return num. of unique powers a^b, 2 <= a < max_range, 2 <= b < max_range'
    powers = []
    for a in range(2, max_range):
        for b in range(2, max_range):
            powers.append(a ** b)
            
    powers = sorted(set(powers))
    return len(powers)


distinct_powers(101)
