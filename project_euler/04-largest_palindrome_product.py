# Problem 4 - Largest palindrome product
# https://projecteuler.net/problem=4

'''
Find the largest palindrome made from the product of two 3-digit numbers.
'''

from time_this import time_this


def is_pal(num: int) -> bool:
    '''Determine if num argument is a pallindrome.'''
    num_is_pal = True
    str_num = str(num)
    for i in range(len(str_num) // 2):
        # compare index 0 vs index -1, etc.
        if str_num[i] != str_num[-1 * (i + 1)]:
            num_is_pal = False
            break
    return num_is_pal


@time_this
def palindrome_pdts(minimum: int, maximum: int) -> int:
    '''Return largest palindromic number which is a product of two three-digit
    numbers.
    '''
    #palindromes = []
    max_product = 0
    for i in range(minimum, maximum):
        for j in  range(minimum, maximum):
            product = i * j
            if is_pal(product):
                #palindromes.append((i, j, product))
                if product > max_product:
                    max_product = product
    return max_product

print(palindrome_pdts(100, 1000))
