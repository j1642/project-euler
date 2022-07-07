# Problem 1 - multiples of 3, 5
# https://projecteuler.net/problem=1
def get_multiples():
    '''Find all multiples of 3 and 5 less than 1000.'''
    multiples_3_5 = []
    for num in range(1000):
        if (num % 3 == 0) or (num % 5 == 0):
            multiples_3_5.append(num)
    return sum(multiples_3_5)

print(get_multiples())
