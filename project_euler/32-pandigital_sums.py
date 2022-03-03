# Problem 32 - Pandigital products
# https://projecteuler.net/problem=32
import string

def is_pandigital(num):
    'Return True if num is pandigital. E.g. 1, 12, 21, 3124, 612345 return True'
    num = str(num)
    digits = list(string.digits[1:len(num) + 1])
    for digit in num:
        try:
            digits.remove(digit)
        except ValueError:
            return False
    if not digits:
        return True

@time_this
def collect_pandigitals():
    '''Find sum of all products whose factors and products are pandigital, 1 to 9.

    E.g. For 39 × 186 = 7254, the factors and products are 1 to 9 pandigital.'''
    previous_products = []
    product_sum = 0
    
    # Equation 2345 * 6 = 14070 has 10 total digits, outside the problem space.
    # So the relevant upper bound for factors is less than 2345.
    
    # Only one upper bound has to be high because two high factors will produce a
    #    product with more than 9 digits.
    
    # 100 * 100 = 10000 has 11 digits, so many factor pairs will likely have a
    #    two-digit factor and a three-digit factor.
    # So 1000, exclusive, is a conservative second upper bound.
    for i in range(1, 1000):
        j_maxes = ['type_error', 2345, 999, 99]
        j_max = j_maxes[len(str(i))]
        
        for j in range(1, j_max):
            if (len(str(i)) + len(str(j)) + len(str(i * j))) == 9:
                nums = [str(i), str(j), str(i * j)]
                nums = ''.join(nums)
                if is_pandigital(nums):
                    product = i * j
                    if product not in previous_products:
                        previous_products.append(product)
                        product_sum += i * j
    
    return product_sum

collect_pandigitals()
