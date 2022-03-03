# Problem 36 - Double-based palindromes
# https://projecteuler.net/problem=36
# Could break into more functions.
# Unsure if it is appropriate to strip leading and trailing zeros from binary
#   numbers. This code does not strip.

@time_this
def is_pal_bases_10_2(max_range: int):
    '''Check if a number base 10 if palindromic, then pass num to base 2
    converter and palindrome check function.'''
    palindromes = []
    
    for num in range(max_range):
        num_split = list(str(num))
        reversed_num = list(reversed(num_split))
        if num_split == reversed_num:
            if is_pal_base_2_convert(num):
                palindromes.append(num)
                
    return sum(palindromes)
    
def is_pal_base_2_convert(num):
    '''Convert number to binary and return True if it is binary palindrome.
    Can also use format(<number>, 'b') to convert to binary.'''
    # Use list as stack
    binary_stack = []
    num_orig = num
    while num > 0:
        binary_stack.append(str(num % 2))
        num = num // 2
    # Reverse binary stack to gt binary num
    binary_num = list(reversed(binary_stack))
    if binary_num == binary_stack:
        return True
    return False
    
is_pal_bases_10_2(1000000)

