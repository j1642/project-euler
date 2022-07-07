# Problem 14 - Longest Collatz Sequence
# https://projecteuler.net/problem=14
from time_this import time_this


def calculate_collatz_length(initial: int) -> int:
    '''Return the length of the Collatz sequence for a given number.'''
    # Initial number counts as the first step in the sequence.
    seq_length = 1
    current_num = initial
    while True:
        if current_num in sequence_length_cache:
            # Don't include the initial seq_length more than once.
            seq_length += sequence_length_cache[current_num] - 1
            sequence_length_cache[initial] = seq_length
            break
        elif current_num % 2 == 0:
            current_num = current_num // 2
            seq_length += 1
        else:
            current_num = current_num * 3 + 1
            seq_length += 1

    return seq_length


@time_this
def longest_collatz(max_range: int) -> int:
    '''Return the length of the longest Collatz sequence that starts with an
    integer less than 1 million.
    '''
    longest_seq = 0
    for n in range(1, max_range):
        seq_length = calculate_collatz_length(n)
        if seq_length > longest_seq:
            longest_seq = seq_length

    return longest_seq


sequence_length_cache = {1: 1}
print(longest_collatz(1000000))
