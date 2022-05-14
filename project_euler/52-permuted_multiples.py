# Problem 52 - Permuted Multiples
# https://projecteuler.net/problem=52
@time_this
def find_permuted_mults(max_range: int):
    '''Return smallest positive int x where x, 2x, 3x, 4x, 5x, and 6x all
    contain the same digits.
    '''
    for num in range(1, max_range):
        num_digits = list(str(num))
        # Following check is a big time-saver
        len_num_times_six = len(str(num * 6))
        if len(num_digits) != len_num_times_six:
            continue
            
        for factor in range(2, 7):
            multiple = num * factor
            multiple_digits = list(str(multiple))
            
            if check_digits(multiple_digits, num_digits):
                if factor == 6:
                    return num
            else:
                break
            
def check_digits(multiple_digits: list, num_digits: list):
    digits = num_digits.copy()
    for digit in multiple_digits:
            if digit in digits:
                digits.remove(digit)
            else:
                return False
    if digits == []:
        return True

print(find_permuted_mults(1000000))

