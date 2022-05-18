# Problem 59 - XOR Decryption
# https://projecteuler.net/problem=59
import urllib.request
from collections import Counter

@time_this
def xor_find_key_decrypt():
    '''Prints 6 possible plaintext solutions and their plaintext ASCII character
    sums. The user must notice if any solutions are correct.
    
    The algorithm can be made more robust by including an English language
    detction function and by permuting the most common character search.
    Check comments above "for most_common_plaintext_char in ' etaoi'" loop
    for more context.
    
    Assume the encryption method is XOR and the key is "three lowercase
    [ASCII] characters."
    
    Encryption method for this specific problem:
    
    With variables key: str, plaintext: str, ciphertext: empty list
    
    for ind, plain_char in enumerate(plaintext):
        cipher_char = ord(plain_char) ^ ord(key[ind % len(key)])
        ciphertext.append(cipher_char)
    ','.join(ciphertext)
    '''
    len_key = 3
    url = 'https://projecteuler.net/project/resources/p059_cipher.txt'
    with urllib.request.urlopen(url) as f:
        for ciphertext in f:
            ciphertext = ciphertext.decode()
    ciphertext = ciphertext.split(',')
    ciphertext = [int(num) for num in ciphertext]
    # Split ciphertext letters into three lists, one for each char. in the key.
    ciphertext_by_index = [[], [], []]
    for ind, letter in enumerate(ciphertext):
        ciphertext_by_index[ind % len_key].append(letter)
    assert ciphertext[:3] == [ciphertext_by_index[0][0],
                              ciphertext_by_index[1][0],
                              ciphertext_by_index[2][0]]
    # Frequency analysis to find key (etaoi most common english letters)
    # This algorithm is not exceptionally robust. It assumes all lists in
    #    ciphertext_by_index have the same most common plaintext character.
    for most_common_plaintext_char in ' etaoi':
        key_guesses = []
        # sublists 0, 1 have ~ 20% diff b/w two most freq. chars, could be
        #    ciphertext letters.
        # sublist 2 has huge 60% diff b/w two most freq. chars, so most freq
        #    ciphertext char is unlikely to be a letter.
        for sublist in ciphertext_by_index:
            char_counter = Counter(sublist)
            most_frequent_cipher_char = max(char_counter, key=char_counter.get)
            # 255 is ASCII max value for possible keys, so use range(256)
            for key_guess in range(256):
                if (ord(most_common_plaintext_char) ^ key_guess) == \
                    most_frequent_cipher_char:
                        
                    key_guesses.append(key_guess)
    
        potential_key = ''.join([chr(key_char) for key_char in key_guesses])
        print('Potential ASCII key:', key_guesses, '\n',
              'Potential plain text key:', potential_key)
        plaintext = []
        for ind, letter in enumerate(ciphertext):
            plaintext.append(str(chr(letter ^ key_guesses[ind % len_key])))
        
        print(''.join(plaintext))
        
        # Display sum of ASCII values of plain text message.
        plaintext_ascii_sum = 0
        for char in plaintext:
            plaintext_ascii_sum += ord(char)
            
        print('Plain text sum of character ASCII values:', plaintext_ascii_sum, '\n')
        

xor_find_key_decrypt()

