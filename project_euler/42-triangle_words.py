# Problem 42 - Coded Triangle Numbers
# https://projecteuler.net/problem=42

# Combining is_triangle_word() functionality into find_triangle_words() did
#    not make things noticably faster.

import string
import urllib.request

@time_this
def find_triangle_words(url: str):
    triangle_nums = []
    # Range up to 50 is somewhat arbitrary. It gives a max triangle number
    #   of 1275, which is equivalent to a word consisting of the letter z
    #   49 times.
    for num in range(1, 50):
        triangle_nums.append(int(0.5 * num * (num + 1)))
    
    alphabet = string.ascii_lowercase
    triangle_word_count = 0
    
    with urllib.request.urlopen(url) as f:
        # Decode external UTF-8 to python internal Unicode
        word_list = (f.read().decode()).split(',')
        for word in word_list:
            letter_vals = []
            word = word.strip('"')
            word = word.lower()
            
            for char in word:
                # Adjust to make value of 'a' equal to 1, not 0
                letter_vals.append(alphabet.index(char) + 1)
            if sum(letter_vals) in triangle_nums:
                triangle_word_count += 1
            
                
    return triangle_word_count
    
find_triangle_words('https://projecteuler.net/project/resources/p042_words.txt')

