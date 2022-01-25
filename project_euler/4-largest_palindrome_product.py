# Problem 4 - Largest palindrome product
# https://projecteuler.net/problem=4
def is_pal(num: int):
    is_pal = True
    str_num = str(num)
    for i in range(len(str_num) // 2):
        # compare index 0 vs index -1, etc.
        if str_num[i] != str_num[-1 * (i + 1)]:
            is_pal = False
            break
    return is_pal

@time_this
def palindrome_pdts(minimum, maximum):
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

palindrome_pdts(100, 1000)
