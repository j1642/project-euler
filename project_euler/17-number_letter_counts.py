# problem 17 - Number letter counts
# https://projecteuler.net/problem=17
from time_this import time_this


@time_this
def count_letters(min_number:int, max_number: int):
    '''If all integers 1 to max_number are written out, find amount of letters.
    '''
    letters = {0: 0, 'and': 3, 'hundred': 7, 'thousand': 8}
    low_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
              'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
              'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen',
              'twenty']
    higher_words = ['thirty', 'forty', 'fifty', 'sixty', 'seventy',
              'eighty', 'ninety']
    # Map integer value to length of integer as a word
    for ind, word in enumerate(low_words):
        letters[ind + 1] = len(word)
    for ind, word in enumerate(higher_words):
        letters[30 + (10 * ind)] = len(word)

    letter_total = 0
    for num in range(min_number, max_number):
        letter_total += get_length_in_letters(num, letters)

    return letter_total


def get_length_in_letters(num: int, letters: dict):
    '''Return the amount of letters if num argument is written out.'''
    if num <= 20:
        return letters[num]
    
    letter_count = 0
    digits = []
    # Extract each digit from num in reverse order (ones place to thousands)
    while num > 0:
        digits.append(num % 10)
        num = num // 10

    for ind, digit in enumerate(digits):
        if ind == 3:
            letter_count += letters['thousand'] + letters[digit]
        elif ind == 2:
            # E.g. 1000 has no contribution from the hundreds place
            if digits[2] == 0 and digits[1] == 0 and digits[0] == 0:
                pass
            # E.g. 900 is 'ninehundred'
            elif digits[1] == 0 and digits[0] == 0:
                letter_count += letters['hundred'] + letters[digit]
            # E.g. 901 is 'ninehundredandone'
            else:
                letter_count += letters['and'] + letters['hundred'] + letters[digit]

        elif ind == 1:
            # If last two digits are in the teens, combine to get num in teens
            if digit == 1:
                tens_and_ones = int(''.join([str(digits[1]), str(digits[0])]))
                letter_count += letters[tens_and_ones]
            else:
                # E.g. 3 as the tens digit becomes 30
                digit *= 10
                letter_count += letters[digit]
                # Included ones digit here
                letter_count += letters[digits[0]]

        # Index 0 is dealt with alongside the tens place (index 1)
        elif ind == 0:
            pass
    return letter_count


print(count_letters(1, 1001))
