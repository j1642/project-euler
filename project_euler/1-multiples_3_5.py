# Problem 1 - multiples of 3, 5
# https://projecteuler.net/problem=1
def get_multiples():
    multiples_3_5 = []
    for num in range(1000):
        if (num % 3 == 0) or (num % 5 == 0):
            multiples_3_5.append(num)
    return sum(multiples_3_5)

get_multiples()
