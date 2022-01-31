# Problem 14 - Longest Collatz Sequence
# https://projecteuler.net/problem=14
def collatz(initial: int):
    seq_length = 0
    current_num = initial
    while current_num > 1:
        if current_num % 2 == 0:
            current_num /= 2
            seq_length += 1
        else:
            current_num = current_num * 3 + 1
            seq_length += 1
    if current_num == 1:
        seq_length += 1
        
    return seq_length

@time_this
def longest_collatz(max_range):
    longest_seq = (0,)
    for i in range(max_range):
        seq_length = collatz(i)
        if seq_length > longest_seq[0]:
            longest_seq = (seq_length, i)
            
    return longest_seq

longest_collatz(1000000)
