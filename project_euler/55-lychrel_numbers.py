# Problem 55 - Lychrel Numbers
# https://projecteuler.net/problem=55

#At the time of writing, it seems that no Lychrel numbers have been proven
#    to exist.

@time_this
def lychrel_nums_search(max_range: int):
    '''Many numbers can form palindromes through a reverse-and-add procedure.
    Lychrel numbers are theorized to never form palindromes in this way.
    
    E.g. For 47, 47 + 74 = 121. 121 is a palindromic number, so 47 is not a
    Lychrel number. 74 is the reverse of 47.
    
    E.g. For 349, 349 + 943 = 1292, 1292 + 2921 = 4213, and 4213 + 3124 = 7337.
    7337 is palindromic, so 349 is not a Lychrel number.
    
    This search for potential Lychrel numbers only performs up to 50
    iterations per number to search for a palindromic sum.
    '''
    potential_lychrel_count = 0
    
    for num in range(1, max_range):
        orig_num = num
        for _ in range(50):
            digits = list(str(num))
            reversed_digits = reversed(digits)
            reversed_num = int(''.join(reversed_digits))
            new_num = num + reversed_num
            new_digits = list(str(new_num))
            
            if is_palindrome(new_digits):
                #print('is_pal')
                break
            else:
                # Redefine num for next reverse-and-add iteration
                num = new_num
        # If not break:
        else:
            potential_lychrel_count += 1
            
    return potential_lychrel_count


def is_palindrome(digits: list):
    '''Palindrome check for list of digits strings. E.g. ['1', '0', '1']'''
    for ind, digit in enumerate(digits):
        while ind <= len(digits)//2:
            if digit == digits[-1 * ind - 1]:
                break
            else:
                return False
    return True
    
    
lychrel_nums_search(10000)

